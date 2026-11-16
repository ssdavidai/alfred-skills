---
name: research-interview-synthesis
description: "Used after a research interview transcript or recap is available to map it to the study's questions (themes, quotes, surprises, follow-ups), or to roll several interviews into emerging findings. Anonymized."
license: MIT
---

# Research interview synthesis

Turn interviews into evidence the report can stand on.

## Inputs
- A transcript or recap the assistant is allowed to read (pasted, linked doc, or an allowed recording source). If none exists, report "no transcript" and stop for that interview.
- The study's research questions.
- For cumulative mode: earlier syntheses (in a synthesis doc).

## Per-interview mode
1. **Participant profile** (anonymized): role, practice size, number of clients, tool stack.
2. **Answers by research question**: for each question that came up, 1–3 bullets with a short supporting quote and timestamp if available. Mark unanswered questions.
3. **Themes**: workflows, pain points, workarounds, what they built themselves, what they pay for, what they wish existed.
4. **Surprises / contradictions** with earlier interviews.
5. **Follow-ups**: anything promised to the participant (e.g. the report), referrals offered, questions to add to the guide.
6. Leave out personal asides entirely.

## Cumulative mode
1. Count interviews covered and list them anonymized (P1, P2 …).
2. **Emerging findings**: each finding with how many participants support it and the best quote; separate strong (3+), emerging (2) and single signals.
3. **Thin questions**: research questions with little evidence so far, and which upcoming interviewees could fill them.
4. **Report outline progress**: sections that now have enough evidence.

## Output
```
Synthesis: <P# · role> — <date>   (or: Cumulative — <n> interviews)
By question: …
Themes: …
Surprises: …
Follow-ups: …
```

## Rules
- Quote participants by name only if the owner confirms they agreed; otherwise anonymize.
- Never invent quotes; paraphrase is marked as paraphrase.
- Work content only.
