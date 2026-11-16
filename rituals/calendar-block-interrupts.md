# Calendar block interrupts

One of the four standing rituals from the Agentic Butler template.

The template version runs on a computer the Grok Bot has registered. It makes a full-screen image for each remaining block and shows it when the block starts. This pack does not do that. Claude and ChatGPT have no registered computer to copy images to, and you must not claim they do.

- **Trigger phrases:** "what's my next block", "set today's nudges", "block interrupts"
- **Default times, if a product can schedule two weekday runs:** 07:30 and 12:30 in the time zone in `profile.md`.
- **Writes:** nothing, unless they ask for calendar alerts on the Butler calendar and you can add those. Alerts are a proposal until they say yes.

## What to do here

1. List today's remaining timed blocks that start before the end of day in `profile.md` or `calendar.md`. Skip all-day events.
2. For each block, one plain sentence: what to do now, and the block's name. Dark, quiet, no lecture.
3. If they use the Butler calendar and want alerts, tell them how to add a notification at the start of each block, or add it yourself only on the Butler calendar after they say yes.
4. On Grok Bot, with a computer actually registered to that bot, the original full-screen nudge is available. Set it up only when that capability is really there, and test once. Otherwise do not schedule a job on their machine.

Message them only if they asked, or if a scheduled nudge they already approved could not be set.
