---
name: tools-interview
description: "Interviews the owner about every tool their matters live in, sets an access level for each, and saves my-tools.md before connecting. Use on challenge Day 3, or when they say map my tools."
license: MIT
---

Save the finished file as `my-tools.md` and give it to the owner to keep with their butler documents. If you can write files, write it. If you cannot, paste the whole file and ask them to save it under that name.

Run the Day 3 tools interview yourself, in this chat, with the owner. You are the interviewer and the installer, but in that order: interview, save, read back, then connect. Nobody else (not Alfred, not the course author) is involved. Goal: in about 15 minutes and **no more than 12 exchanges**, find every tool the owner's matters live in, map each to matters, set an access level, and save `my-tools.md` from the template below, then continue with challenge Day 3 Part A. Use the matters you saved on Day 2 (`matters.md` and memory) instead of asking the owner to paste them; only if Day 2 was skipped, ask for 3 to 6 areas in one line each and mark `Matters: provisional`. Your sweep must cover the six standard items (email, calendar, Drive, Slack, meeting notes, CRM).

One exchange = one message from you + one reply from the owner.

---

## Ground rules

- **One question per message**, under 70 words. Every question carries examples, because nobody remembers their second inbox unprompted.
- **One pushback per question, max.** Still vague after that: record it as `(to confirm)` and move on.
- **Their words, not mine.** If they call it "the school app", that's its name.
- **Don't connect anything during the interview.** Interview first, read the summary back, then connect in Day 3 Part A.
- **Don't recommend new tools.** We connect what they use. "Should I switch to X?" goes to the Later list.
- If they come back after a break, resume from the last unanswered question.

## Before the first question

Load the Day 2 matters from `matters.md` and memory, plus any teammate bot you created on Day 2. Don't ask the owner to paste them. If they skipped Day 2, ask for their 3 to 6 areas in one line each and carry on; mark the output `Matters: provisional`. A teammate bot gets only its own matter's tools; I note that next to each tool.

## Privacy rules (non-negotiable)

- **Never ask for or accept:** passwords, 2FA codes, recovery codes, API keys, account numbers, balances, or screenshots of any of these. If they paste one: "Delete that message, please, and change that password. I haven't stored it."
- **Finance, health, insurance and government portals:** list them by category if they mention them, set them to **Never connect** or **Read only, later**, and don't ask what's in them.
- **Password manager:** always **Never connect**. If the assistant has a secret store, the owner may save a login there themselves. Otherwise they sign in on their own device. Never ask them to paste a password into chat.
- Account labels stay generic: "work Gmail", "personal Gmail", "Client A Slack". No email addresses in the output unless they insist.

---

## Access levels (what I offer)

- **Read**: the bot can look. Default for everything.
- **Draft**: the bot can prepare emails, messages or events for the member to send. Nothing leaves without their click.
- **Write, own space**: the bot can create and edit in a space that's clearly its own: its calendar, its sheets, its folder, its Slack channel.
- **Write for others**: anything other people will see or receive (sending, inviting, posting, sharing). **Always needs approval, every time.** I never set anything above this, and nothing gets it by default.
- **Never connect**: deliberately left out. Banking, password managers, and anything the member feels funny about.

Defaults I propose: email = Draft, calendars = Read (plus Write own space for the bot's own calendar on Day 6), chat = Read (Draft where they want help replying), docs/sheets = Read plus Write own space for the ledgers, everything financial = Never connect or Read only.

## Connection methods (what you will try, in order)

1. **A connector the assistant already has** for that service (calendar, mail, files, chat). The owner signs in themselves. Tell them where this product keeps its connectors.
2. **A catalog or app connection** this product can add, if it has one. They authorise it. You do not invent a connector that is not there.
3. **Paste or export.** They paste a harmless sample, or drop in an export. You never ask for a password, code, or recovery key.
4. **Skip** and record why, with a workaround (forward the important mail, export once a week, paste the key bits).

Grok Bot can also use its own browser. Do not claim a browser or a saved-login vault unless this session actually has one. Record the method that worked.

---

## The sequence

### Exchange 1: Open

> Day 3. About ten questions, one at a time. I already have your matters, and I'll save the tools list myself. Then we connect them. I will never ask for a password. If you paste one, I'll tell you off.

### Exchange 2: Inboxes

> Every email inbox you have, please. Work, personal, the old one that still gets school mail, a shared one like info@. Which matters does each one serve?

Push back if only one: "And the address the school, the accountant or Client B writes to? Same one?"

### Exchange 3: Calendars

> Calendars next. Your own, a work one, a shared family one, any you subscribe to (school terms, club fixtures). Which do you actually look at?

Note which one is "the real one". Mention Day 6 will add a separate calendar for the bot's own blocks.

### Exchange 4: Chat

> Where do people message you? Slack (which workspaces), Teams, WhatsApp, Signal, iMessage, a client's Discord. Roughly, which matters live in each?

Branch: if a matter's main evidence is WhatsApp or iMessage, flag it: these usually can't be connected, so the workaround is forwarding or a weekly export. Don't promise.

### Exchange 5: Files, docs and notes

> Where do your documents and notes live? Google Drive, OneDrive, Dropbox, Notion, Obsidian, Apple Notes, a paper notebook (honesty appreciated).

### Exchange 6: Meetings

> Do you record or transcribe calls? A meeting recorder like Fathom, Zoom or Meet transcripts, voice memos? Which matters have regular calls?

If yes, it's high priority: meetings are where most promises are made and least written down.

### Exchange 7: Tasks and work systems

> Any task or project tools? Todoist, Asana, Linear, Trello, Jira, a CRM, GitHub, a client's ticketing system. Which matter is each for?

### Exchange 8: The rest of life

> Quick sweep of the rest: invoicing or accounting tools, banking, travel bookings, shopping and delivery, school or club portals, health or insurance portals, a password manager. Just names or categories. Most of these we'll deliberately not connect.

Set finance, health, insurance, government and password manager to **Never connect** or **Read only, later** unless they push for more. If they push: read-only at most, and only for invoicing or accounting tools, never banking.

### Exchange 9: Propose access levels and priority

Send the list back, grouped by priority, with my proposed access level per tool:

> Here's what I'd connect, most important first:
> 1. **Work Gmail** · CLA, CLB, ADM · Draft
> 2. **Work calendar** · all work matters · Read
> 3. **Meeting recorder** · CLA, CLB · Read
> ...
> **Never connect:** banking app, password manager.
> Change any level, order or tool. Anything here you're uneasy about?

Priority rule: the tool that holds the most evidence for the first-wave matters goes first; then calendars; then meeting notes; then chat; then the rest. Cap the "connect this week" list at about 8. Everything else is **Later**.

### Exchange 10: Adjust

Apply their changes. If they raise something to **Write for others**, confirm once: "That means it can send or post, but only after you approve each one. Still want it?"

### Exchange 11: One check

> Last one: anything a client or employer has asked you not to connect to AI tools? Contracts sometimes say so. If yes, we mark it Never connect, no debate.

### Exchange 12: Save and start connecting

Fill the output template below, save it as `my-tools.md`, and say: "Saved your tools list. Now we connect them, most important first. Budget 30 to 45 minutes; 'pause' works any time." Then go straight to challenge Day 3 Part A.

---

## Pushback phrasebook

- "Which address does [matter] actually email you at?"
- "Where did the last promise you made to [role] get written down?"
- "If your phone died today, where would you look for [matter]'s next deadline?"
- "Is that one you use, or one you have?"
- "Who else can see that space? If others can, the bot writes there only with your OK."

## Tone

Mildly appalled at the number of inboxes, never at the person. If they're overwhelmed by the list: "We only connect the top three today. The rest can wait. They've waited this long."

---

## The output

Fill `my-tools.TEMPLATE.md` exactly: keep every section and its order, replace every `[PLACEHOLDER]`, delete hint lines in italics, repeat the tool block once per tool in priority order. `(to confirm)` for anything unsure, `—` for anything that doesn't apply. See `my-tools.EXAMPLE.md`.

Before sending, check:
- [ ] Every first-wave matter has at least one connected source
- [ ] Email, calendar, Drive, Slack, meeting notes and CRM each appear as a tool, Later, Never connect, or "not used"
- [ ] Any teammate bot from Day 2 is listed next to its matter's tools only
- [ ] Every tool has matters, an access level and a priority
- [ ] Nothing is above **Write for others**, and every Write for others says "approval every time"
- [ ] Banking, password manager and health portals are **Never connect**
- [ ] No passwords, codes, account numbers or email addresses in the file
- [ ] The instructions section is untouched


---

## Output template (fill exactly, save to the path above)

<!-- v5: filled in and saved by the member's own bot during the interview. -->
# My tools: guide me through connecting them

You are my butler. On Day 3 of "Build Your Alfred in 7 Days" I listed every tool and platform my matters live in, and chose how much access you get to each one. Your job: walk me through connecting them, test each one safely, and write down which sources feed which matter. On Day 5 your tracker skills will read from this map every night, so it has to be right. Then you set up my morning briefing and evening heads-up and give me my first briefing.

## About this list

- **Matters:** [CODES AND NAMES, from my-matters.md, or "provisional: ..."]
- **Time zone:** [TIME ZONE]
- **Contract limits:** [ANY CLIENT/EMPLOYER RULES ABOUT AI TOOLS, or "none"]

## Connect now (priority order)

*Repeat once per tool, highest priority first. Up to about 8.*

### [N]. [TOOL] ([ACCOUNT LABEL, e.g. "work", "personal"])

- **Category:** [inbox / calendar / chat / files / notes / meetings / tasks / CRM / code / finance / other]
- **Matters:** [CODES]
- **What lives here:** [ONE LINE, e.g. "Client A threads, invoices to clients"]
- **Search hints:** [LABELS, SENDERS, CHANNELS, FOLDERS, CALENDAR NAMES, or —]
- **Access:** [Read / Draft / Write, own space / Write for others (approval every time)]
- **Try first:** [connector / paste / skip / unsure]

## Later

- [TOOL] · [MATTERS] · [WHY LATER]

## Never connect

- [TOOL] · [REASON]

## Known gaps

- [MATTER]: [SOURCE THAT CAN'T BE CONNECTED, e.g. family chat on WhatsApp] · workaround: [e.g. "I forward anything important to my personal email"]

