---
name: cleanup-worktrees
description: Safely inspect and clean up linked Git worktrees and local branches after GitHub pull requests are merged or closed. Use when parallel Codex or developer tasks have left stale worktrees, when the user asks to audit or prune completed-PR branches, or when cleanup must account for dirty worktrees and squash/rebase merges. Do not use for general repository maintenance or to delete worktrees that are unrelated to completed GitHub pull requests.
---

# Clean Up Git Worktrees

Use the bundled `scripts/cleanup_worktrees.py` helper. Keep inspection and deletion separate; always inspect first.

## Preconditions

1. Run from any worktree belonging to the target repository.
2. Require `git` and `gh`; verify `gh auth status` before querying GitHub.
3. Prefer fresh remote state. Run `git fetch --prune` only after confirming the repository's remote is the intended one, or pass `--fetch` to the helper.
4. Do not use this skill while another process is creating, moving, or removing worktrees.

## Inspect

Run:

```bash
python3 .github/skills/cleanup-worktrees/scripts/cleanup_worktrees.py
```

The helper defaults to dry-run reporting and makes no deletions. It parses `git worktree list --porcelain`, checks every linked worktree with `git status --porcelain`, looks up PRs with `gh pr list --head <branch> --state all`, and prints `SAFE`, `KEEP`, and `REVIEW` groups.

Interpret the groups as follows:

- `SAFE`: the linked worktree is clean, its PR is `MERGED` or `CLOSED`, and the local branch tip exactly matches the PR's recorded `headRefOid`.
- `KEEP`: the primary worktree or a worktree whose associated PR is `OPEN`.
- `REVIEW`: any dirty worktree, detached HEAD, missing PR, failed GitHub lookup, missing PR head evidence, multiple ambiguous PRs, or local tip that differs from the PR head.

Never promote `KEEP` or `REVIEW` to `SAFE` merely because the remote branch is missing or `git branch --merged` reports the branch as merged.

## Confirm and remove

Show the complete dry-run report to the user. Obtain explicit confirmation naming the `SAFE` paths to remove. Then run one apply command with only those exact paths:

```bash
python3 .github/skills/cleanup-worktrees/scripts/cleanup_worktrees.py \
  --apply \
  --worktree /absolute/path/to/task-a \
  --worktree /absolute/path/to/task-b
```

The helper rescans immediately before deletion and refuses any selected path that is no longer `SAFE`. It prompts once more unless `--yes` is passed. Use `--yes` only when the user already explicitly approved the exact paths in the same interaction.

For each still-safe selection, the helper runs `git worktree remove`, then deletes the local branch. It first tries `git branch -d`. If Git rejects that command after a squash or rebase merge, it may use `git branch -D` because the completed PR, clean worktree, and exact PR-head match were revalidated. Finally it runs `git worktree prune` if at least one worktree was removed.

## Safety model

- Always preserve the primary worktree, regardless of its branch or PR state.
- Treat staged, unstaged, and untracked files as dirty and classify the worktree as `REVIEW`.
- Treat an `OPEN` PR as `KEEP`.
- Treat `MERGED` and `CLOSED` PRs only as candidates; require a clean worktree and exact local-tip/PR-head equality.
- Treat no PR or an unavailable GitHub state as `REVIEW`.
- Use the PR head OID as evidence that the branch commits are represented by the PR. This supports squash and rebase merges without requiring the original commits to be ancestors of the base branch.
- Never manually delete `.git/worktrees` metadata.
- Never pass `--force` to `git worktree remove`.

## Examples

Audit all worktrees without fetching or deleting:

```bash
python3 .github/skills/cleanup-worktrees/scripts/cleanup_worktrees.py
```

Refresh remote refs, then audit:

```bash
python3 .github/skills/cleanup-worktrees/scripts/cleanup_worktrees.py --fetch
```

Remove one previously reported safe worktree after confirmation:

```bash
python3 .github/skills/cleanup-worktrees/scripts/cleanup_worktrees.py \
  --apply --worktree /private/tmp/project-task
```

Do not use this workflow to recover corrupted worktree metadata, delete arbitrary directories, clean untracked files, or decide whether unpublished work is disposable. Handle those as separate, explicitly authorized tasks.
