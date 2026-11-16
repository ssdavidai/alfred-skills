---
name: next-meeting-deliverables
description: "Used after a call to turn its recap or notes into a plain list of what each side owes before the next meeting, matched against the commitment tracker. A proposal only."
license: MIT
---

# Next-meeting deliverables

Turn a finished call into a clear, plain-English list of what is owed before the next meeting.

## Inputs
- The call: attendee(s) and date, or "the latest call with X", or "any new calls since the last run".
- Allowed evidence for the assistant (as set in its brief): e.g. a recap email in the mailbox, a summary pasted or posted in Slack, notes docs, the project commitment tracker. Do not use sources the brief excludes.

## Steps
1. **Find the call evidence.** Prefer the most complete allowed record (recap with action items, then posted summary, then the owner's own notes). If none exists, report "no call record found" and stop; never reconstruct a call from a calendar slot alone.
2. **Extract commitments.** For each action item capture: owner, the concrete deliverable, the due point ("before next meeting", a date, or none stated), and the evidence (link or quoted line; timestamp if the record has one).
3. **Separate** accepted commitments from suggestions or open questions. A suggestion is not a commitment until someone accepted it.
4. **Match to the register.** Compare with open rows in the project commitment tracker by outcome and owner. Mark each item as: matches existing row <ID> (status change?), new candidate commitment, or not register-worthy.
5. **Find the next meeting** if an allowed source shows it; otherwise say "next meeting not scheduled".
6. **Output**, in the project's working language:
   ```
   After <call> (<date>): before the next meeting (<date or "not scheduled">)
   Owner owes:
   - <deliverable> — due <…> — evidence <link/timestamp>
   Others owe:
   - <owner>: <deliverable> — evidence
   Register impact (proposal only): <row ID → change> / <new candidate>
   Open questions: <…>
   ```

## Rules
- This is a proposal. Do not write to the tracker; apply register changes only when the owner explicitly asks to apply them.
- Work content only: drop personal asides completely.
- Keep it short; plain English, no jargon padding.
