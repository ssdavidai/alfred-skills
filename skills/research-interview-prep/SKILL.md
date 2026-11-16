---
name: research-interview-prep
description: "Used before a research or customer-discovery interview to build a one-screen brief from the candidate's notes, the outreach thread and the study's research questions. Read-only; research, not sales."
license: MIT
---

# Research interview prep

A brief the interviewer can read in two minutes before a short research call.

## Inputs
- The interview (name, date/time with time zone) from the tracker or the outreach reports.
- The candidate's research row (role, practice, AI or tool evidence, why interview, screening gaps, public sources) and the personalization hook used in outreach.
- The study's research questions and promises (e.g. "research only, no pitch", "participants get the report").

## Steps
1. **Confirm the slot**: date and time in the owner's timezone and the interviewee's local time if known. If the time is uncertain, say so.
2. **Profile** in 3–4 bullets from the row only: role, practice and size, client model, notable workflow or tool evidence. Mark anything not in the sources as unknown.
3. **Pick 5 questions** from the research questions that this person is best placed to answer, ordered for a 15-minute call, plus one opener based on the hook and one closer (referral ask, report promise).
4. **Gaps to probe:** the row's screening gaps phrased as quick checks.
5. **Reminders:** research only; don't pitch; promised the report; ask permission before quoting by name.
6. **Output:**
   ```
   Interview prep: <Name> — <date time, owner tz> (<local>)
   Who: …
   Why them: …
   Opener: …
   Questions (15 min): 1… 5…
   Probe: …
   Close: referral? · report promised ✔
   ```

## Never
- Contact the interviewee or change the calendar.
- Add facts that are not in the sources; never invent achievements.
