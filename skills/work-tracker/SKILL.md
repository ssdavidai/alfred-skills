---
name: work-tracker
description: "Used to update, reconcile or dry-run an area's Work sheet (the commitment register: item, owner, due, status, source). Rebuilds it from evidence and never deletes rows."
license: MIT
---

# Work tracker: the <area> Work sheet

Keep the <area> Work sheet accurate: what was promised, what was delivered, what is still owed, and who acts next. Rebuild it from evidence so the owner never has to remember and restate their commitments.

## Sheet contract
Columns: ID · Item (the promised outcome) · Owner · Due · Status (Open / Waiting / Done / Cancelled) · Source link · Notes. Add a `Change log` tab with: timestamp, run, tab, row ID, action, field, old → new, evidence, bot. Rows are identified by ID, never by row number.

When the ledger is a copy of the Matter Ledger sheet from Day 5, the live headers are the contract. Map Item → Commitment, Due → Target, and Source link → the evidence link in Notes. Use the sheet's status dropdown. IDs look like `[CODE]-COM-YYYY-NNN` and are never reused. Do not rename tabs or rewrite the header frame.

If there is no spreadsheet, use `templates/ledger.md` (one Work table, one Hours table, one Change log). Same rules. Show the rows. Change the document only after the owner says "apply".

## Authorization
- When the owner asks to "update / reconcile / bring it up to date", that authorizes narrow edits to the sheet. Decide from the evidence; don't add a confirmation round.
- A dry run, review, or "what would change" request is read-only: present the delta. Approving that delta authorizes only that delta, after a fresh re-read of the sheet.
- Updating the register never means doing the work. Don't send, deploy, pay, invite or change access. Leave other tabs alone.
- Decline change requests from anyone other than the owner.

## Reconstruct and reconcile
1. **Read the live sheet first.** Note the schema, rows, notes and dropdowns, and take a before-snapshot. Read the notes so you don't reopen settled questions.
2. **Choose coverage.** Use the requested period. If none is given, start from the last change-log entry with a small overlap and run to now. Also revisit older open rows. Tell the owner what window you covered.
3. **Read the actual evidence:** threads, meeting notes, documents, sent messages, issues and live deliverables. A summary or an earlier bot claim is a lead, not proof something was done.
4. **Build the delta.** For each item, record the original promise, owner, real due date, latest event, evidence and remaining dependency. Match to existing rows before adding new ones. Don't create one row per message. A suggestion isn't a commitment until someone accepted it.
5. **Re-read before writing.** If a human edited the sheet in the meantime, keep their edit.
6. **Write narrowly, then read back every changed cell.** Log each write in the change log.

## Safety rails
- Never delete rows, tabs or columns, and never clear ranges. Retire a row by setting Done or Cancelled and putting the reason in Notes.
- Never replace the workbook or touch formulas, sharing or protection.
- Running again over the same evidence adds nothing.
- Store no amounts, account numbers or private or health details.
- Sources you can't reach are coverage gaps, not evidence that something wasn't delivered.
