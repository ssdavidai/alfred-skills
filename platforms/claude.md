# Claude

Two installs. The skill is the one that matches this pack: Claude reads the description and loads Alfred when the request fits. A Project is the fallback when a skill upload is not available on the account.

Docs checked 16 November 2026: [Create custom skills](https://claude.com/docs/skills/how-to), [Agent Skills](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview), [scheduled tasks](https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-claude-cowork).

## Skill upload (about five minutes)

Custom skills are on Pro, Max, Ultra, Team, and Enterprise, with [code execution enabled](https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude). Skills uploaded to claude.ai stay on that account. Claude Code uses files on the machine instead. They do not sync by themselves.

1. Download `dist/alfred-claude-skill.zip` from this repository.
2. In claude.ai or the desktop app, open **Customize → Skills** and upload the zip.
3. Turn **alfred** on.
4. Start a new chat. Say: **I'm doing the 7-day challenge.**

The zip has one skill at the top, which is what Claude looks for:

```text
alfred-claude-skill.zip
└── alfred/
    ├── SKILL.md
    └── references/
        ├── skills/        the 16 template skills, plus Context Bootstrap
        ├── onboarding/    the day scripts and the course pages
        ├── templates/
        └── rituals/
```

If upload complains that it cannot find a skill, the zip was repacked without the `alfred/` folder. Use this zip as it is.

## Claude Code

From a checkout of this repo:

```bash
make install-claude-code
```

That copies each skill into `~/.claude/skills/` and puts the onboarding, templates and rituals next to `alfred` and `getting-started`, so a day file is on disk. Open Claude Code in any project and say **I'm doing the 7-day challenge**, or type `/alfred`.

To share it with a repository instead of your home folder, copy the same `skills/` tree into that repo's `.claude/skills/` and commit it. The install script only writes under `~/.claude/skills/`.

## A Claude Project, if skills are not available

1. Create a Project.
2. Paste `chatgpt/instructions.md` into the project instructions. It is under 8,000 characters and states the house rules.
3. Upload the files in `dist/alfred-chatgpt-gpt.zip` under `knowledge/`. The same texts are the day scripts and the skills.

Use the skill upload when the account allows it. A Project holds the files, but it does not load a skill by description the way Customize → Skills does.

## Morning, evening, Sunday

On a paid plan, Claude can run scheduled tasks in Cowork and in the current Claude experience, including when the computer is off. Ask: **Schedule my morning briefing at 07:50 on weekdays.** Review the name, the clock time and the instructions, then confirm. Manage them under **Scheduled**.

Enterprise may need an owner to turn scheduled tasks on. If the account cannot schedule, the phrases still work: "brief me", "heads-up", "plan my week".

Alfred will not claim a schedule it did not set up.
