#!/usr/bin/env python3
"""Conservatively inspect and remove completed-PR Git worktrees."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Sequence


@dataclass
class Worktree:
    path: str
    oid: str = ""
    branch: str | None = None
    primary: bool = False


@dataclass
class Result:
    worktree: Worktree
    category: str
    reason: str
    pr_number: int | None = None
    pr_state: str | None = None


class CommandError(RuntimeError):
    pass


def run(args: Sequence[str], cwd: str, check: bool = True) -> subprocess.CompletedProcess[str]:
    proc = subprocess.run(args, cwd=cwd, text=True, capture_output=True)
    if check and proc.returncode:
        detail = proc.stderr.strip() or proc.stdout.strip() or f"exit {proc.returncode}"
        raise CommandError(f"{' '.join(args)}: {detail}")
    return proc


def parse_worktrees(text: str) -> list[Worktree]:
    records: list[dict[str, str]] = []
    current: dict[str, str] = {}
    for line in text.splitlines() + [""]:
        if not line:
            if current:
                records.append(current)
                current = {}
            continue
        key, _, value = line.partition(" ")
        current[key] = value

    worktrees: list[Worktree] = []
    for index, record in enumerate(records):
        branch_ref = record.get("branch")
        branch = branch_ref.removeprefix("refs/heads/") if branch_ref else None
        worktrees.append(
            Worktree(
                path=record["worktree"],
                oid=record.get("HEAD", ""),
                branch=branch,
                primary=index == 0,
            )
        )
    return worktrees


def find_pr(repo: str, branch: str) -> tuple[dict | None, str | None]:
    fields = "number,state,headRefOid,url,updatedAt"
    proc = run(
        ["gh", "pr", "list", "--head", branch, "--state", "all", "--limit", "100", "--json", fields],
        cwd=repo,
        check=False,
    )
    if proc.returncode:
        return None, proc.stderr.strip() or proc.stdout.strip() or "GitHub lookup failed"
    try:
        prs = json.loads(proc.stdout)
    except json.JSONDecodeError as exc:
        return None, f"invalid GitHub response: {exc}"
    if not prs:
        return None, None
    open_prs = [pr for pr in prs if pr.get("state") == "OPEN"]
    candidates = open_prs or prs
    candidates.sort(key=lambda pr: pr.get("updatedAt", ""), reverse=True)
    if len(candidates) > 1 and candidates[0].get("updatedAt") == candidates[1].get("updatedAt"):
        return None, "multiple ambiguous PRs found"
    return candidates[0], None


def classify(repo: str, worktree: Worktree) -> Result:
    if worktree.primary:
        return Result(worktree, "KEEP", "primary worktree")
    if not worktree.branch:
        return Result(worktree, "REVIEW", "detached HEAD or no local branch")

    status = run(["git", "status", "--porcelain", "--untracked-files=all"], worktree.path, check=False)
    if status.returncode:
        return Result(worktree, "REVIEW", "cannot inspect worktree status")
    if status.stdout:
        return Result(worktree, "REVIEW", "uncommitted, staged, or untracked changes")

    pr, error = find_pr(repo, worktree.branch)
    if error:
        return Result(worktree, "REVIEW", error)
    if pr is None:
        return Result(worktree, "REVIEW", "no associated PR found")

    number = pr.get("number")
    state = pr.get("state")
    if state == "OPEN":
        return Result(worktree, "KEEP", "PR is open", number, state)
    if state not in {"MERGED", "CLOSED"}:
        return Result(worktree, "REVIEW", f"unknown PR state: {state}", number, state)

    pr_head = pr.get("headRefOid")
    if not pr_head:
        return Result(worktree, "REVIEW", "PR head OID is unavailable", number, state)
    if worktree.oid != pr_head:
        return Result(worktree, "REVIEW", "local branch tip differs from PR head", number, state)
    return Result(worktree, "SAFE", "clean and local tip matches completed PR head", number, state)


def scan(repo: str) -> list[Result]:
    listing = run(["git", "worktree", "list", "--porcelain"], repo).stdout
    return [classify(repo, wt) for wt in parse_worktrees(listing)]


def print_report(results: Sequence[Result]) -> None:
    print("Worktree cleanup\n")
    for category in ("SAFE", "KEEP", "REVIEW"):
        print(category)
        grouped = [result for result in results if result.category == category]
        if not grouped:
            print("  (none)")
        for result in grouped:
            wt = result.worktree
            pr = f"PR #{result.pr_number} {result.pr_state}" if result.pr_number else "no PR"
            branch = wt.branch or "(detached)"
            print(f"  {branch}  {pr}  {wt.path}  — {result.reason}")
        print()


def remove_selected(repo: str, results: Sequence[Result], selected: Sequence[str], assume_yes: bool) -> int:
    normalized = {str(Path(path).resolve()) for path in selected}
    by_path = {str(Path(result.worktree.path).resolve()): result for result in results}
    missing = sorted(normalized - by_path.keys())
    unsafe = [by_path[path] for path in normalized & by_path.keys() if by_path[path].category != "SAFE"]
    if missing or unsafe:
        for path in missing:
            print(f"Refusing unknown worktree: {path}", file=sys.stderr)
        for result in unsafe:
            print(f"Refusing {result.worktree.path}: now {result.category} ({result.reason})", file=sys.stderr)
        return 2

    targets = [by_path[path] for path in normalized]
    if not targets:
        print("No worktrees selected; nothing to remove.", file=sys.stderr)
        return 2

    print("Selected for removal:")
    for result in targets:
        print(f"  {result.worktree.path} ({result.worktree.branch}, PR #{result.pr_number} {result.pr_state})")
    print("Local branch deletion may use git branch -D after the safety checks above.")
    if not assume_yes:
        answer = input("Type 'remove' to continue: ").strip()
        if answer != "remove":
            print("Cancelled.")
            return 1

    # Re-scan immediately before deletion to revalidate safety.
    refreshed_results = scan(repo)
    refreshed_by_path = {str(Path(result.worktree.path).resolve()): result for result in refreshed_results}
    refreshed_missing = sorted(normalized - refreshed_by_path.keys())
    refreshed_unsafe = [
        refreshed_by_path[path]
        for path in normalized & refreshed_by_path.keys()
        if refreshed_by_path[path].category != "SAFE"
    ]
    if refreshed_missing or refreshed_unsafe:
        for path in refreshed_missing:
            print(f"Refusing unknown worktree: {path}", file=sys.stderr)
        for result in refreshed_unsafe:
            print(
                f"Refusing {result.worktree.path}: now {result.category} ({result.reason})",
                file=sys.stderr,
            )
        return 2

    targets = [refreshed_by_path[path] for path in normalized]
    removed = 0
    for result in targets:
        wt = result.worktree
        run(["git", "worktree", "remove", "--", wt.path], repo)
        deleted = run(["git", "branch", "-d", "--", wt.branch], repo, check=False)
        if deleted.returncode:
            run(["git", "branch", "-D", "--", wt.branch], repo)
        removed += 1
        print(f"Removed {wt.path} and local branch {wt.branch}")
    if removed:
        run(["git", "worktree", "prune"], repo)
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fetch", action="store_true", help="run git fetch --prune before inspection")
    parser.add_argument("--apply", action="store_true", help="remove explicitly selected SAFE worktrees")
    parser.add_argument("--worktree", action="append", default=[], help="absolute worktree path; repeat as needed")
    parser.add_argument("--yes", action="store_true", help="skip the final typed confirmation")
    args = parser.parse_args()

    try:
        repo = run(["git", "rev-parse", "--show-toplevel"], ".").stdout.strip()
        if args.fetch:
            run(["git", "fetch", "--prune"], repo)
        results = scan(repo)
        print_report(results)
        if not args.apply:
            if args.worktree or args.yes:
                print("Note: --worktree/--yes have no effect without --apply.", file=sys.stderr)
            return 0
        if not args.worktree:
            print("Refusing --apply without at least one --worktree path.", file=sys.stderr)
            return 2
        return remove_selected(repo, results, args.worktree, args.yes)
    except (CommandError, OSError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
