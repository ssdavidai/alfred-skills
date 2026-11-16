---
name: admin-deadlines
description: "Used for a weekly or on-demand check of company admin and tax deadlines: recurring filings and payments, bookkeeper requests, contract renewals and open admin items, overdue first. Read-only."
license: MIT
---

# Company admin deadlines

Keep the recurring admin calendar of small companies visible so nothing lapses (filings, contributions, bookkeeping hand-ins).

## Inputs
- The recurring calendar from the assistant's brief (per entity: what, when, who acts).
- Open admin items in memory or a tracker (failed payments, signatures pending, notices).
- Contracts with renewal or notice dates.
- Only the sources the brief allows. If notices arrive in a mailbox the assistant cannot read, say so and rely on what the owner forwards.

## Steps
1. **Window:** today through the next 21 days (owner timezone). Include anything overdue.
2. **Expand recurring items** into concrete dates for the window. Shift weekend dates the way the authority does (usually to the next working day) and mark that as an assumption.
3. **Merge** open items and contract dates. For each: entity, what, due date, who acts (owner, assistant/admin person, bookkeeper, provider), status, evidence.
4. **Rank:** overdue → due within 7 days → due within 21 days. Mark items where a lapse has consequences (penalties, loss of a service or registration) as **urgent**.
5. **Draft** the next action where useful (an email to the bookkeeper in their language, a checklist). Drafts only.
6. **Post:**
   ```
   Admin & tax — week of <date>
   Overdue: …
   Next 7 days: …
   Next 21 days: …
   Unknown dates to confirm: …
   STATUS | <green/yellow/red> | top 3 open: … | blocked on: … | next deadline: …
   ```

## Rules
- No amounts, tax numbers, registration numbers or account numbers in posts or memory.
- Personal or family items that appear in the same notices (individual payroll, benefits, household payments) are out of scope: omit them.
- If a date is not established, list it under "Unknown dates to confirm"; never guess a statutory deadline.
