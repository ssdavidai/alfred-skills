---
name: itemize
description: "Turns a plan into an epic and child-issue draft, one atomic issue per phase, sequenced and cross-referenced. Use when the owner says itemize this or asks to break a plan into issues. Files nothing."
license: MIT
---

# Itemize — plan → atomic, sequenced units

Turns a plan into a **draft** that the owner (or their coding agent) files. The bot files nothing itself.

## What "atomic" means
- Every single unit of work is one item, not bundled.
- Properly cross-referenced: each item links to its parent, dependencies and related items.
- Labeled: type (feat/fix/chore/docs), area (package/lane), size (S/M/L) if useful.
- Dependencies marked: which items block which; ordered, it looks like a waterfall.
- Properly sequenced: phase 0 / phase 1 / phase 2, explicit ordering.
- Planned for maximum parallelism: parallel-safe items flagged; items that must sequence say why.

## Steps
1. **Read the plan** from wherever it lives: the conversation, a linked doc, an issue body (read-only), a previous list. Don't decompose blind; ask if the plan is unclear.
2. **Decompose** into units that are each: one discrete piece of work (typically ≤200 LOC or one written artifact), independently verifiable (a concrete done test), owned by one lane/package, and small enough for one agent session. Split big units; merge trivia into an adjacent unit.
3. **Sequence:** Phase 0 = shared foundations (migrations, contracts, schemas, gates); Phase 1+ consumes earlier phases. Within a phase mark parallel-safe vs must-sequence (provider → consumer). For each unit: blocks / blocked by.
4. **Labels:** if a target repo is named, read its existing labels and reuse them; don't invent new ones unless the owner asked.
5. **Produce the draft**:
   ```
   EPIC: <name>   (target repo: <owner/repo or "local task list">)
   Phases: 0 → N

   [P0-1] <title>  labels: <…>  size: S
     Done when: <test>
     Blocks: P1-2, P1-3   Blocked by: —   Parallel-safe: yes
   …
   ```
   Then a filing checklist the owner can hand to their coding agent: create the epic, create children in order with "Part of #<epic>", then back-fill blocks/blocked-by numbers and tick-boxes in the epic.
6. **Confirm:**
   ```
   Itemized into N units across M phases.
   - Phase 0: <n> units (foundations, sequenced)
   - Phase 1: <n> units, <k> parallel-safe
   Draft ready to file in <repo>; nothing was created.
   ```
   Then stop. Do not start executing.

## Pitfalls
- Never create issues, labels or epics yourself from a cloud/team assistant.
- Don't bundle small units into "misc fixes". Don't write "and other tasks": every child is explicit.
