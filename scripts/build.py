#!/usr/bin/env python3
"""Build and check the Alfred skill pack.

Produces two deterministic zips:

- dist/alfred-claude-skill.zip
  One Claude skill. Top level is alfred/SKILL.md, which is what Claude looks
  for when a skill zip is uploaded (Customize > Skills).

- dist/alfred-chatgpt-gpt.zip
  instructions.md (under the 8,000-character Custom GPT cap) plus knowledge
  files for a ChatGPT Project or an existing Custom GPT.
"""

from __future__ import annotations

import re
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
STAGING = DIST / "staging"

SKILL_NAMES = [
    "admin-deadlines",
    "area-bot-brief",
    "daily-briefing",
    "getting-started",
    "hours-tracker",
    "itemize",
    "matters-interview",
    "meeting-prep",
    "next-meeting-deliverables",
    "research-interview-prep",
    "research-interview-synthesis",
    "tools-interview",
    "tracker-dry-run",
    "vendor-review",
    "weekly-planning",
    "work-tracker",
]

TEMPLATE_RITUALS = [
    "morning-briefing",
    "evening-heads-up",
    "weekly-calendar-build",
    "calendar-block-interrupts",
]

ONBOARDING_DAYS = [
    "guided-setup.md",
    "challenge.md",
    "day-1.md",
    "day-2.md",
    "day-3.md",
    "day-4.md",
    "day-5.md",
    "day-6.md",
    "day-7.md",
]

LESSONS = [
    "00-before-we-begin.md",
    "day-1.md",
    "day-2.md",
    "day-3.md",
    "day-4.md",
    "day-5.md",
    "day-6.md",
    "day-7.md",
    "finish.md",
]

NAME_RE = re.compile(r"^[a-z0-9-]{1,64}$")
FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
EMAIL_RE = re.compile(r"[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}", re.I)
SECRET_RE = re.compile(
    r"(sk-[A-Za-z0-9]{10,}|xai-[A-Za-z0-9]{10,}|AKIA[0-9A-Z]{16}|ghp_[A-Za-z0-9]{20,}|BEGIN (RSA |OPENSSH )?PRIVATE KEY)"
)

GPT_INSTRUCTION_LIMIT = 8000
ZIP_EPOCH = (2026, 11, 16, 0, 0, 0)


def fail(msg: str) -> None:
    print(f"error: {msg}", file=sys.stderr)
    sys.exit(1)


def parse_frontmatter(text: str, path: Path) -> dict[str, str]:
    match = FRONTMATTER_RE.match(text)
    if not match:
        fail(f"{path}: missing YAML frontmatter")
    data: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if not line.strip():
            continue
        if ":" not in line:
            fail(f"{path}: bad frontmatter line {line!r}")
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"')
    return data


def check_skill(path: Path, expected_name: str) -> None:
    text = path.read_text(encoding="utf-8")
    meta = parse_frontmatter(text, path)
    name = meta.get("name", "")
    description = meta.get("description", "")
    if name != expected_name:
        fail(f"{path}: name {name!r} does not match directory {expected_name!r}")
    if not NAME_RE.match(name):
        fail(f"{path}: name {name!r} is not a lowercase skill name")
    if name in {"anthropic", "claude"} or "anthropic" in name or "claude" in name:
        fail(f"{path}: reserved word in name")
    if not description or len(description) > 1024:
        fail(f"{path}: description length {len(description)} (must be 1..1024)")
    if "<" in description or ">" in description:
        fail(f"{path}: description contains an angle bracket")
    body = text[text.index("---", 3) + 3 :]
    if len(body.splitlines()) > 500 and expected_name == "alfred":
        fail(f"{path}: SKILL.md body is over 500 lines")


def check_sources() -> None:
    for name in ["alfred", *SKILL_NAMES, "context-bootstrap"]:
        path = ROOT / "skills" / name / "SKILL.md"
        if not path.is_file():
            fail(f"missing skill {path}")
        check_skill(path, name)
    for name in TEMPLATE_RITUALS:
        path = ROOT / "rituals" / f"{name}.md"
        if not path.is_file():
            fail(f"missing ritual {path}")
    for name in ONBOARDING_DAYS:
        path = ROOT / "onboarding" / name
        if not path.is_file():
            fail(f"missing onboarding file {path}")
    for name in LESSONS:
        path = ROOT / "onboarding" / "lessons" / name
        if not path.is_file():
            fail(f"missing lesson {path}")
    for required in [
        "templates/matters.md",
        "templates/matters.EXAMPLE.md",
        "templates/tools.md",
        "templates/tools.EXAMPLE.md",
        "templates/trust.md",
        "templates/ledger.md",
        "templates/charter.md",
        "platforms/claude.md",
        "platforms/chatgpt.md",
        "chatgpt/instructions.md",
        "LICENSE",
        "README.md",
    ]:
        if not (ROOT / required).is_file():
            fail(f"missing {required}")
    instructions = (ROOT / "chatgpt" / "instructions.md").read_text(encoding="utf-8")
    if len(instructions) > GPT_INSTRUCTION_LIMIT:
        fail(
            f"chatgpt/instructions.md is {len(instructions)} characters "
            f"(Custom GPT cap is {GPT_INSTRUCTION_LIMIT})"
        )
    if len(instructions) < 1500:
        fail("chatgpt/instructions.md looks too short to carry the house rules")
    content_roots = [
        ROOT / "skills",
        ROOT / "onboarding",
        ROOT / "templates",
        ROOT / "rituals",
        ROOT / "platforms",
        ROOT / "chatgpt",
        ROOT / "README.md",
    ]
    files: list[Path] = []
    for root in content_roots:
        if root.is_file():
            files.append(root)
        else:
            files.extend(p for p in root.rglob("*") if p.is_file() and p.suffix in {".md", ".txt"})
    blob = "\n".join(p.read_text(encoding="utf-8", errors="replace") for p in files)
    if "/workspace/butler" in blob or "CallDynamicTool" in blob or "grokbot://" in blob:
        fail("portable pack still contains a Grok Bot path or tool call")
    if "pluginId" in blob:
        fail("portable pack still contains a Grok plugin id")
    emails = sorted(set(EMAIL_RE.findall(blob)))
    if emails:
        fail(f"unexpected email addresses: {emails}")
    if SECRET_RE.search(blob):
        fail("unexpected secret-like token")
    print(
        f"checked {1 + len(SKILL_NAMES) + 1} skills, "
        f"{len(TEMPLATE_RITUALS)} template rituals, "
        f"{len(ONBOARDING_DAYS)} onboarding files, "
        f"instructions {len(instructions)}/{GPT_INSTRUCTION_LIMIT} chars"
    )


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def skill_reference(name: str) -> str:
    """Specialist procedure stored beside the uploaded skill, not as a nested skill."""
    text = read(f"skills/{name}/SKILL.md")
    return text


def write_file(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not content.endswith("\n"):
        content += "\n"
    path.write_text(content, encoding="utf-8")


def stage_claude(stage: Path) -> None:
    skill = stage / "alfred"
    write_file(skill / "SKILL.md", read("skills/alfred/SKILL.md"))
    for name in [*SKILL_NAMES, "context-bootstrap"]:
        write_file(skill / "references" / "skills" / f"{name}.md", skill_reference(name))
    for path in (ROOT / "onboarding").rglob("*"):
        if not path.is_file():
            continue
        rel = path.relative_to(ROOT / "onboarding")
        dest = skill / "references" / "onboarding" / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        if path.suffix == ".md":
            write_file(dest, path.read_text(encoding="utf-8"))
        else:
            dest.write_bytes(path.read_bytes())
    for path in (ROOT / "templates").glob("*.md"):
        write_file(
            skill / "references" / "templates" / path.name,
            path.read_text(encoding="utf-8"),
        )
    for path in (ROOT / "rituals").glob("*.md"):
        write_file(
            skill / "references" / "rituals" / path.name,
            path.read_text(encoding="utf-8"),
        )
    write_file(
        skill / "references" / "WHERE.md",
        """# Where these files live

This folder is the portable pack, copied next to `SKILL.md` for the uploaded Claude skill.

- `skills/` — the 16 template skills, plus the optional Day 6 Context Bootstrap skill
- `onboarding/` — guided setup, challenge rules, and one file per day
- `onboarding/lessons/` — the course pages, for the owner
- `templates/` — blank documents and the fictional examples
- `rituals/` — the four standing rituals, plus the ones the challenge adds

Installed as separate Claude Code skills, the same texts live in each skill's own `SKILL.md`. Read those when the owner invokes them.
""",
    )


def chatgpt_knowledge_files() -> dict[str, str]:
    """Fine-grained knowledge files. Custom GPTs take at most 20."""
    files: dict[str, str] = {}
    files["00-how-to-run.md"] = read("chatgpt/knowledge-how-to-run.md")
    files["01-persona-and-house-rules.md"] = read("skills/alfred/SKILL.md")
    files["02-rituals.md"] = "\n\n".join(
        read(f"rituals/{name}.md") for name in sorted(p.stem for p in (ROOT / "rituals").glob("*.md"))
    )
    groups = {
        "03-skills-setup.md": ["getting-started", "matters-interview", "tools-interview", "area-bot-brief"],
        "04-skills-trackers.md": ["work-tracker", "hours-tracker", "tracker-dry-run", "admin-deadlines", "vendor-review"],
        "05-skills-planning.md": [
            "daily-briefing",
            "weekly-planning",
            "meeting-prep",
            "next-meeting-deliverables",
            "context-bootstrap",
        ],
        "06-skills-research.md": [
            "research-interview-prep",
            "research-interview-synthesis",
            "itemize",
        ],
    }
    for filename, names in groups.items():
        files[filename] = "\n\n".join(read(f"skills/{name}/SKILL.md") for name in names)
    files["07-onboarding-setup-and-days-1-3.md"] = "\n\n".join(
        read(f"onboarding/{name}") for name in ["guided-setup.md", "challenge.md", "day-1.md", "day-2.md", "day-3.md"]
    )
    files["08-onboarding-days-4-7.md"] = "\n\n".join(
        read(f"onboarding/{name}") for name in ["day-4.md", "day-5.md", "day-6.md", "day-7.md"]
    )
    files["09-lessons.md"] = "\n\n".join(
        read(f"onboarding/lessons/{name}") for name in LESSONS
    )
    files["10-templates.md"] = "\n\n".join(
        read(f"templates/{name}")
        for name in [
            "charter.md",
            "matters.md",
            "tools.md",
            "trust.md",
            "ledger.md",
            "ledgers.md",
            "sources.md",
            "promises.md",
            "extras.md",
            "calendar.md",
            "notes.md",
            "profile.md",
        ]
    )
    files["11-examples-fiction.md"] = "\n\n".join(
        [
            read("templates/matters.EXAMPLE.md"),
            read("templates/tools.EXAMPLE.md"),
        ]
    )
    return files


def stage_chatgpt(stage: Path) -> None:
    pack = stage / "alfred-chatgpt"
    write_file(pack / "instructions.md", read("chatgpt/instructions.md"))
    write_file(pack / "HOW-TO.txt", read("platforms/chatgpt.md"))
    knowledge = chatgpt_knowledge_files()
    if len(knowledge) > 20:
        fail(f"ChatGPT knowledge has {len(knowledge)} files; a Custom GPT allows 20")
    for name, content in knowledge.items():
        write_file(pack / "knowledge" / name, content)
    images = ROOT / "onboarding" / "images"
    for image in sorted(images.glob("*")):
        dest = pack / "images" / image.name
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(image.read_bytes())
    # Free ChatGPT projects hold 5 files. Five bundles cover the same text.
    bundles = {
        "bundle-1-how-to-run-and-rules.md": ["00-how-to-run.md", "01-persona-and-house-rules.md", "02-rituals.md"],
        "bundle-2-skills.md": [
            "03-skills-setup.md",
            "04-skills-trackers.md",
            "05-skills-planning.md",
            "06-skills-research.md",
        ],
        "bundle-3-onboarding.md": ["07-onboarding-setup-and-days-1-3.md", "08-onboarding-days-4-7.md"],
        "bundle-4-lessons.md": ["09-lessons.md"],
        "bundle-5-templates-and-examples.md": ["10-templates.md", "11-examples-fiction.md"],
    }
    for name, parts in bundles.items():
        write_file(
            pack / "knowledge-free-tier" / name,
            "\n\n".join(knowledge[part] for part in parts),
        )


def zip_dir(src: Path, dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.exists():
        dest.unlink()
    with zipfile.ZipFile(dest, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        files = [p for p in src.rglob("*") if p.is_file()]
        for path in sorted(files, key=lambda p: p.relative_to(src).as_posix()):
            rel = path.relative_to(src.parent).as_posix()
            info = zipfile.ZipInfo(rel, date_time=ZIP_EPOCH)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            archive.writestr(info, path.read_bytes())


def check_zips() -> None:
    claude = DIST / "alfred-claude-skill.zip"
    gpt = DIST / "alfred-chatgpt-gpt.zip"
    with zipfile.ZipFile(claude) as archive:
        names = archive.namelist()
        if "alfred/SKILL.md" not in names:
            fail("claude zip is missing alfred/SKILL.md at the skill root")
        if any(not name.startswith("alfred/") for name in names):
            fail("claude zip has an entry outside alfred/")
        if sum(1 for name in names if name.startswith("alfred/references/skills/")) < 16:
            fail("claude zip is missing specialist skills")
        if "alfred/references/onboarding/day-7.md" not in names:
            fail("claude zip is missing day 7")
    with zipfile.ZipFile(gpt) as archive:
        names = archive.namelist()
        if "alfred-chatgpt/instructions.md" not in names:
            fail("chatgpt zip is missing instructions.md")
        text = archive.read("alfred-chatgpt/instructions.md").decode("utf-8")
        if len(text) > GPT_INSTRUCTION_LIMIT:
            fail("zipped instructions exceed 8000 characters")
        knowledge = [n for n in names if "/knowledge/" in n and n.endswith(".md")]
        bundles = [n for n in names if "/knowledge-free-tier/" in n and n.endswith(".md")]
        if not 1 <= len(knowledge) <= 20:
            fail(f"chatgpt knowledge file count {len(knowledge)}")
        if len(bundles) != 5:
            fail(f"expected 5 free-tier bundles, found {len(bundles)}")
    print(f"zips ok: {claude.name} ({claude.stat().st_size} bytes), {gpt.name} ({gpt.stat().st_size} bytes)")


def build() -> None:
    if STAGING.exists():
        for path in sorted(STAGING.rglob("*"), reverse=True):
            if path.is_file():
                path.unlink()
            elif path.is_dir():
                path.rmdir()
    stage_claude(STAGING / "claude")
    stage_chatgpt(STAGING / "chatgpt")
    zip_dir(STAGING / "claude" / "alfred", DIST / "alfred-claude-skill.zip")
    zip_dir(STAGING / "chatgpt" / "alfred-chatgpt", DIST / "alfred-chatgpt-gpt.zip")
    check_zips()


def main() -> None:
    check_only = "--check" in sys.argv
    check_sources()
    build()
    if check_only:
        print("check passed")


if __name__ == "__main__":
    main()
