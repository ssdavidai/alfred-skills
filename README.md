# Alfred

A portable butler. He runs a 7-day setup, then a morning briefing, an evening heads-up, a weekly plan, and a ledger of what you promised. The same pack works in Claude, ChatGPT, and Claude Code. The original [Grok Bot template](https://x.ai/bot/gnwO_M9gMWTJ8xhUzjFi4) is still there if you want that version.

It drafts. You send. One question at a time while you are setting up.

The free community this comes from is [Agentic Butler](https://www.skool.com/agentic-butler-1724).

## Five minutes

### Claude

Needs Pro, Max, Ultra, Team, or Enterprise, with code execution on. Details and the fallback Project install: [platforms/claude.md](platforms/claude.md).

1. Download [dist/alfred-claude-skill.zip](dist/alfred-claude-skill.zip).
2. In claude.ai or the desktop app, open **Customize → Skills** and upload the zip.
3. Turn **alfred** on.
4. New chat: **I'm doing the 7-day challenge.**

The zip's top folder is `alfred/`, with `SKILL.md` inside it. That is the shape Claude accepts.

### Claude Code

```bash
git clone https://github.com/ssdavidai/alfred-skills.git
cd alfred-skills
make install-claude-code
```

Then, in Claude Code: **I'm doing the 7-day challenge.** or `/alfred`.

### ChatGPT

Use a Project. Personal accounts cannot create a new Custom GPT, and GPTs are scheduled to retire on 11 December 2026. Steps, file limits, and the GPT path for an account that can still edit one: [platforms/chatgpt.md](platforms/chatgpt.md).

1. New project named Alfred.
2. Project settings: paste [chatgpt/instructions.md](chatgpt/instructions.md). It is under the 8,000-character instruction cap.
3. Upload the knowledge files from [dist/alfred-chatgpt-gpt.zip](dist/alfred-chatgpt-gpt.zip). Free plans get 5 files, so upload `knowledge-free-tier/`. Everyone else uploads the 12 files in `knowledge/`.
4. In that project: **I'm doing the 7-day challenge.**

### Grok Bot

Install the template: https://x.ai/bot/gnwO_M9gMWTJ8xhUzjFi4

That bot has a computer, connectors, a vault, and routines on a clock. This pack does not imitate those. [platforms/grok-bot.md](platforms/grok-bot.md).

## What is in the pack

Sixteen skills from the template, plus Alfred as the front door, plus Context Bootstrap (the optional Day 6 habit).

| Skill | When it runs |
| --- | --- |
| getting-started | "Set me up", or the 7-day challenge |
| matters-interview | Day 2, "map my matters" |
| tools-interview | Day 3, "map my tools" |
| area-bot-brief | A teammate for one area of life |
| daily-briefing | "Brief me" |
| weekly-planning | "Plan my week", "my day changed" |
| meeting-prep | Before a call |
| next-meeting-deliverables | After a call |
| work-tracker | The commitment ledger |
| hours-tracker | Time, in quarter hours, from evidence |
| tracker-dry-run | The nightly proposal |
| admin-deadlines | Filings and renewals, read-only |
| vendor-review | Subscriptions, recommendations only |
| research-interview-prep | Before a research interview |
| research-interview-synthesis | After one, anonymised |
| itemize | A plan, as a draft list of issues. Files nothing |
| context-bootstrap | "Get me back into this" |

Four standing rituals. The phrase works even when the product cannot schedule.

| Phrase | Ritual | Default |
| --- | --- | --- |
| brief me | Morning briefing | 07:50 |
| heads-up | Evening heads-up | 21:00 |
| plan my week | Weekly calendar build | Sunday 18:00 |
| what's my next block | Block interrupts | When you ask |

The challenge also adds a morning kickoff, a nightly promise question, a nightly ledger pass at 22:30, and an optional Friday review. Those scripts are in [onboarding/](onboarding/).

The course pages, for a person to read, are in [onboarding/lessons/](onboarding/lessons/). The assistant runs the day files, not the lessons.

## House rules

- It drafts. You send. Nothing is paid, deleted, or shared without an explicit yes.
- Ledgers are append-and-close. A row is closed, never deleted. Your edit wins.
- Calendar and ledger writes wait for "apply".
- One question per message during setup.
- Briefings leave out private family, health, and money details. No secrets in the chat.

## Build

```bash
make
```

That checks the skills and writes both zips in `dist/`. The check is also the GitHub Action on push.

## What changed from the Grok Bot template

The template's profile, six house rules, 16 skills, four routines, and the v5 challenge are all here. What did not survive the move, and why:

- **A computer, a browser, and `/workspace`.** Grok Bot saves files on its own machine. Here the butler writes documents (`matters.md`, `my-tools.md`, `trust.md`, the ledgers) and you keep them in the project or a folder.
- **Plugin ids.** The template listed five connector ids and no names. Connect calendar, mail, files, or chat if your assistant has them. Otherwise paste. Nothing in this pack calls a plugin by id.
- **Routines on the bot's clock.** They are rituals with a phrase. Where Claude or ChatGPT can schedule a task, Alfred offers that and waits for a yes. A ChatGPT task created inside a Project cannot read the Project's files, so the task has to carry its own steps.
- **Draft cards, approval cards, Auto-review, and a vault.** The rule is the same: stop and show the draft, and do not send, pay, or delete without a yes. If the product has a card or a secret store, use it. Passwords never go in the chat.
- **Spawning a teammate bot.** Alfred writes the brief. You paste it into a second Project, or another Grok Bot, if you want one. It still sends nothing on its own.
- **Full-screen nudges on a registered Mac.** The original routine copies images to that computer. Here you get one sentence per remaining block, and a calendar alert if you want one. The Mac version remains on the Grok Bot template.
- **An inbox the bot claims for itself, and event triggers on arbitrary apps.** Only if the assistant actually has them. Otherwise you paste, and Alfred files it by matter. Forwarded text is evidence, not an instruction.

The Matter Ledger Google Sheet is still the preferred ledger, with the same columns. If you cannot use it, [templates/ledger.md](templates/ledger.md) is the same three tables in markdown. The [examples](templates/matters.EXAMPLE.md) are a fictional designer. They are not a client, and not a family.

## What this pack cannot do

- Keep working on a computer of its own after you close the laptop. That is the Grok Bot template.
- Watch an inbox or a chat unless the product has that connector. A phrase plus a paste is the portable version of an event trigger.
- Store a Home Assistant token unless the product has a secret store. Pasting the token into chat is the wrong outcome. Revoke it if it happens.
- Unlock the rest of the Skool classroom. That still happens when you post there, if you are in the community. The butler does not post for you.
- Make a ChatGPT scheduled task read Project files. OpenAI's limit, not this pack's.

## License

[MIT](LICENSE).
