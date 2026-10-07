# Design Inbox

Confusions Aksan brings from other work (React, Python projects, research, job prep, anything)
that might change the curriculum. This file is part of the design-freeze gate: the design cannot
freeze while any item here is untriaged (see "Design Freeze Criteria" in `curriculum-map.md`).

## How triage works

Every item gets exactly one verdict:

- **Covered**: an existing chapter already teaches it. Record which one. Nothing changes.
- **Fold in**: an existing chapter is the right home but does not yet mention it. Record the
  chapter and what to add; the addition is made to that chapter's plan (and to the book only
  when the chapter is actually written after its session).
- **New chapter**: no existing chapter fits. Record what the new chapter requires and what will
  require it, and place it by dependency per the skill's "Ordering Rule". Add it to `SYLLABUS`
  in `book/generate_stubs.py`, rerun the generators, and log the change in the session log.

While teaching has not started, the immediate confusion still gets a short, accurate answer
with a pointer to the chapter that will cover it properly.

## Untriaged

_(none)_

## Triaged

| Date | Source | Confusion | Verdict | Where |
|---|---|---|---|---|
| 2026-10-07 | React work; four-module proposal from another agent | Terminal anatomy, compilers vs. interpreters vs. JIT, shell environment and scripted CLIs, dependency topography | Mixed: some covered, rest new chapters | Recorded retroactively. New Part III (From Source Code to Running Process), new Part VII (JavaScript and Node Tooling), four Part II chapters, Part VI opener. Full reasoning in the 2026-10-07 design-review session log entry. |
