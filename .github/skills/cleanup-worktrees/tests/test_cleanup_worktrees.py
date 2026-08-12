import importlib.util
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


SCRIPT = Path(__file__).parents[1] / "scripts" / "cleanup_worktrees.py"
SPEC = importlib.util.spec_from_file_location("cleanup_worktrees", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


def git(cwd: Path, *args: str) -> str:
    return subprocess.run(
        ["git", *args], cwd=cwd, check=True, text=True, capture_output=True
    ).stdout.strip()


class CleanupWorktreesTest(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.repo = self.root / "repo"
        self.repo.mkdir()
        git(self.repo, "init", "-b", "main")
        git(self.repo, "config", "user.name", "Skill Test")
        git(self.repo, "config", "user.email", "skill-test@example.invalid")
        (self.repo / "base.txt").write_text("base\n")
        git(self.repo, "add", "base.txt")
        git(self.repo, "commit", "-m", "base")

    def tearDown(self) -> None:
        self.temp.cleanup()

    def add_worktree(self, branch: str, dirty: bool = False) -> tuple[Path, str]:
        path = self.root / branch
        git(self.repo, "worktree", "add", "-b", branch, str(path))
        (path / f"{branch}.txt").write_text(f"{branch}\n")
        git(path, "add", f"{branch}.txt")
        git(path, "commit", "-m", branch)
        oid = git(path, "rev-parse", "HEAD")
        if dirty:
            (path / "untracked.txt").write_text("preserve me\n")
        return path, oid

    def test_classification_matrix(self) -> None:
        merged_path, merged_oid = self.add_worktree("merged")
        closed_path, closed_oid = self.add_worktree("closed")
        open_path, open_oid = self.add_worktree("open")
        dirty_path, dirty_oid = self.add_worktree("dirty", dirty=True)
        no_pr_path, _ = self.add_worktree("no-pr")
        squash_path, squash_oid = self.add_worktree("squash")

        prs = {
            "merged": ({"number": 1, "state": "MERGED", "headRefOid": merged_oid}, None),
            "closed": ({"number": 2, "state": "CLOSED", "headRefOid": closed_oid}, None),
            "open": ({"number": 3, "state": "OPEN", "headRefOid": open_oid}, None),
            "dirty": ({"number": 4, "state": "MERGED", "headRefOid": dirty_oid}, None),
            "no-pr": (None, None),
            # This commit is deliberately not merged into main; PR evidence is sufficient.
            "squash": ({"number": 5, "state": "MERGED", "headRefOid": squash_oid}, None),
        }
        with patch.object(MODULE, "find_pr", side_effect=lambda _repo, branch: prs[branch]):
            results = MODULE.scan(str(self.repo))

        by_branch = {result.worktree.branch: result for result in results}
        self.assertEqual("KEEP", by_branch["main"].category)
        self.assertEqual("primary worktree", by_branch["main"].reason)
        self.assertEqual("SAFE", by_branch["merged"].category)
        self.assertEqual("SAFE", by_branch["closed"].category)
        self.assertEqual("KEEP", by_branch["open"].category)
        self.assertEqual("REVIEW", by_branch["dirty"].category)
        self.assertEqual("REVIEW", by_branch["no-pr"].category)
        self.assertEqual("SAFE", by_branch["squash"].category)
        self.assertFalse(
            subprocess.run(
                ["git", "merge-base", "--is-ancestor", squash_oid, "main"], cwd=self.repo
            ).returncode
            == 0
        )
        self.assertTrue(dirty_path.exists())
        self.assertTrue(no_pr_path.exists())
        self.assertTrue(open_path.exists())
        self.assertTrue(merged_path.exists())
        self.assertTrue(closed_path.exists())
        self.assertTrue(squash_path.exists())

    def test_apply_removes_only_explicit_safe_worktree(self) -> None:
        safe_path, safe_oid = self.add_worktree("safe")
        dirty_path, dirty_oid = self.add_worktree("dirty", dirty=True)
        prs = {
            "safe": ({"number": 10, "state": "MERGED", "headRefOid": safe_oid}, None),
            "dirty": ({"number": 11, "state": "MERGED", "headRefOid": dirty_oid}, None),
        }
        with patch.object(MODULE, "find_pr", side_effect=lambda _repo, branch: prs[branch]):
            results = MODULE.scan(str(self.repo))
            code = MODULE.remove_selected(str(self.repo), results, [str(safe_path)], True)

        self.assertEqual(0, code)
        self.assertFalse(safe_path.exists())
        self.assertNotIn("safe", git(self.repo, "branch", "--format=%(refname:short)").splitlines())
        self.assertTrue(dirty_path.exists())
        self.assertIn("dirty", git(self.repo, "branch", "--format=%(refname:short)").splitlines())

    def test_apply_refuses_review_worktree(self) -> None:
        dirty_path, dirty_oid = self.add_worktree("dirty", dirty=True)
        with patch.object(
            MODULE,
            "find_pr",
            return_value=({"number": 12, "state": "MERGED", "headRefOid": dirty_oid}, None),
        ):
            results = MODULE.scan(str(self.repo))
            code = MODULE.remove_selected(str(self.repo), results, [str(dirty_path)], True)

        self.assertEqual(2, code)
        self.assertTrue(dirty_path.exists())


if __name__ == "__main__":
    unittest.main()
