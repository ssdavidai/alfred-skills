#!/usr/bin/env python3
"""Copy this pack into ~/.claude/skills for Claude Code.

Override the destination with ALFRED_SKILLS_DIR.
"""

from __future__ import annotations

import os
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEST = Path(os.environ.get("ALFRED_SKILLS_DIR", Path.home() / ".claude" / "skills"))


def copy_tree(src: Path, dest: Path) -> None:
    if dest.exists():
        shutil.rmtree(dest)
    shutil.copytree(src, dest)


def main() -> None:
    skills = ROOT / "skills"
    DEST.mkdir(parents=True, exist_ok=True)
    for skill in sorted(p for p in skills.iterdir() if (p / "SKILL.md").is_file()):
        copy_tree(skill, DEST / skill.name)
        print(f"installed {skill.name}")
    for name in ("alfred", "getting-started"):
        ref = DEST / name / "references"
        ref.mkdir(parents=True, exist_ok=True)
        for folder in ("onboarding", "templates", "rituals"):
            copy_tree(ROOT / folder, ref / folder)
        print(f"attached pack files to {name}")
    print(f"Claude Code skills are in {DEST}")
    print('Open claude and say: I\'m doing the 7-day challenge.')


if __name__ == "__main__":
    main()
