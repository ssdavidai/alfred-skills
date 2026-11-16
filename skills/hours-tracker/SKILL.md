---
name: hours-tracker
description: "Used to catch up or dry-run an area's Hours sheet: reconstruct time per day from calendar and work evidence, in quarter hours, without double-counting."
license: MIT
---

# Hours tracker: time per day per area

Reconstruct how much effort the owner put into <area> and keep the <area> Hours sheet current, without making them run a timer or fill in a questionnaire.

## Sheet contract
Columns: Date · Area · Hours · Description · Status (pending / accepted) · Source / evidence. Plus a `Change log` tab, as in work-tracker.

On a Matter Ledger sheet, map these onto the live Hours headers from Day 5 (Date, Type, Hours, Sub-area, Description, Work ID(s), Status, Source / evidence, Notes). The area is the sheet itself. Status stays `accepted` or `pending`. If there is no spreadsheet, append the same rows to the Hours table in `templates/ledger.md`, and write them only after "apply" unless the owner already asked you to catch the sheet up.

## Standing rules
- **Infer on your own.** When asked to bring the sheet up to date, choose reasonable hours and write them. Don't ask the owner to confirm durations.
- **Count the whole effort:** reading, design, preparation, testing, review, coordination and getting back into context, not only visible keystrokes.
- **Use quarter hours.** Merge fragments of one work block, then round to the nearest 0.25 h, with a minimum of 0.25 h. If no work happened, write no entry.
- **Keep descriptions natural.** Put assumptions, exact source durations and links in Source / evidence.
- **Don't invent measured time.** These are reconstructions, not clock-in records, so say that in the evidence.
- **Don't double-count.** Running again over a covered period adds nothing.

## Reconstruct the work
1. **Read the live sheet.** Note recent entries and gaps, and take a before-snapshot. Pending rows count as coverage too.
2. **Gather evidence for the window.** Use calendar events that actually happened, meeting-note durations, sent email and Slack, document edits, commits and coding sessions.
3. **Group the evidence into work blocks per day.** Add reasonable preparation and wrap-up time. Calls take the recorded duration plus prep.
4. **Re-read the sheet, write narrow appends or updates, and read them back.** Log each write.

## Authorization
"Update / catch up" authorizes writes to this sheet only. A question or review request is read-only. This skill never authorizes invoicing, messages or deployments. Correct a wrong value by revising it with an explanation, never by deleting it.
