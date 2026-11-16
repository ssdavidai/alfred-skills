---
name: meeting-prep
description: "Builds a short read-only brief before a named call: attendees, last time's promises, open commitments, a proposed agenda and questions. Use when the owner asks to prep for a call or for tomorrow's calls."
license: MIT
---

# Meeting prep

Produce a one-screen prep brief so the owner walks into a call knowing what was promised, what is open and what to ask. Read-only: never message attendees, never change the calendar or any tracker.

## Inputs
- The meeting: attendee name(s) and date/time, or "the next call with X", or "tomorrow's calls". Resolve times in the owner's timezone unless told otherwise; note the attendee's local time when it differs.
- The bot's own allowed sources, as defined by the assistant's brief or routine (for example a project mailbox, Slack channels, a tracker sheet, repos). Use only those. If a source is not connected or not allowed, skip it and name the gap; never fall back to a broader personal account.

## Steps
1. **Identify the meeting.** Find the event or request. If there is no calendar access, take the meeting from the request or from scheduling threads in allowed sources. If you cannot identify date and attendees, say so and ask rather than guess.
2. **Pull the history with these attendees** (bounded: last 2–3 conversations or last 30 days, whichever is smaller):
   - prior call recaps or notes that reached an allowed source (recap emails in the mailbox, summaries posted in Slack);
   - recent email threads and Slack messages involving the attendees;
   - open rows in the project commitment tracker owned by the owner or the attendees.
3. **Extract what matters:** decisions made, what the owner promised and by when, what the attendees promised, anything overdue, questions left unanswered, and any scope boundary that still holds.
4. **Draft the brief** in the project's working language:
   ```
   Prep: <meeting> — <date, time, owner tz> (<attendee local time if different>)
   Attendees: <names, roles>
   Last time: <2–4 bullets of decisions/outcomes, with dates and links>
   Owner owes: <items, due dates, status>
   They owe: <items>
   Proposed agenda: <3–5 items, most important first>
   Open questions to ask: <bullets>
   Watch-outs: <scope boundaries, sensitivities, missing evidence>
   ```
5. **Cite sources** inline (thread link, sheet row ID, message permalink). Mark anything inferred as "(inference)".

## Rules
- Summarize work content only. If a source contains a personal aside about anyone (private appointments, wellbeing, home life), leave it out entirely; do not hint at it.
- Do not include rates, balances or invoice amounts unless the request explicitly asks and the conversation is owner-only.
- Missing evidence is a gap to state, not something to fill with invention.
- Multiple meetings: one block per meeting, earliest first.
