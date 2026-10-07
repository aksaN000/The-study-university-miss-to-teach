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

### 2026-10-07: external review of the 126-page skeleton (from ChatGPT)

Reviewed the stub PDF (structure only; no chapter has content yet). Claude's proposed verdicts
below; nothing moves into `SYLLABUS` until Aksan decides each one.

| # | Suggestion | Proposed verdict | Notes |
|---|---|---|---|
| 1 | Databases as a pillar | New chapters | Same as audit open question 1. Operating a database (server process, connecting, pooling, migrations, ORM vs. SQL, transactions and indexes in practice, EXPLAIN, backups, caching), not SQL from zero (CSE370 theory). After Part V, before Part IX. |
| 2 | Sockets, TCP vs. UDP, DNS depth, network tools (curl, dig, ss), reverse proxies | New chapters in Part V | ch49 already bundles three ideas (ports, localhost, IP vs. DNS) and breaks the one-concept rule; split it. About five chapters, not the twenty proposed: MAC, DHCP, subnetting are CSE421 theory. |
| 3 | APIs: REST, JSON, sessions, cookies, JWT, CORS, webhooks | New chapters after HTTP | CORS is exactly the confusion React work produces. |
| 4 | Security foundations | New chapters, placed by dependency | Same as audit open question 3. Reject the proposed late "Part XII Security": secrets are needed before CI (ch87) and deployment, web vulnerabilities right after APIs. |
| 5 | Debugging as a cross-book skill; process inspection tools (ps, lsof, ss, strace, DevTools) | Fold in + one new chapter | Debugging is already a cross-cutting habit in the curriculum map; add one chapter on inspecting a running process. |
| 6 | Profiling | New chapter | Same as audit open question 5. |
| 7 | Production fundamentals (systemd, reverse proxy, domain to HTTPS, health checks, restarts, rollback, observability, backups) | Expand Part XI | Three chapters is thin for the stated goal. |
| 8 | CPU, registers, stack/heap, syscalls, user vs. kernel mode | New chapter early in Part I | Aksan has CSE340/CSE321, but the book assumes nothing, and Part III's ABI chapter needs it. |
| 9 | "Containers are not VMs"; namespaces and cgroups | Fold into ch80 | Already the chapter's natural content. |
| 10 | Python packaging history (distutils to pyproject) | Covered | The history-first rule already requires it in ch54/ch58/ch60. |
| 11 | Semantic versioning earlier | Dependency bug: move | ch65 (npm semver ranges) depends on ch91 (Semantic versioning), which comes 26 chapters later. Move semver into Part VI before the lockfile chapters. |
| 12 | Recurring "Trace it" exercise (what happens when we type `python train.py`, `git push`, ...) | Adopt | Fits the mental-model goal; part-end feature, no new chapters needed. |
| 13 | Final integrated capstone (app, API, database, CI, Docker, deploy, break and recover) | Adopt as a closing part | |
| 14 | "How to use this book" | Fold into preface | |
| 15 | Core / practical / deep-dive / specialized markers | Adopt (cheap) | A margin tag per chapter; helps readers, does not cut content. |
| 16 | Fixed eight-step loop for every chapter | Reject | Contradicts the adaptive-chapter decision; the live session already runs the Ladder. |
| 17 | Re-layer the parts (machine, talking, running, ... security, ML) | Reject the order, borrow the framing | Its order breaks dependencies (security last; venv after databases). Layer-style part names could still be used. |
| 18 | 103 chapters is a risk; "do not cover everything" | Aksan decides | Chapters are only written after sessions, so the book cannot outrun the learning. Scope is a brief question: his stated goal is the opposite of "do not cover everything". |
| 19 | Lab folder per chapter (broken/, fixed/) | Fold into practice templates | `practice/` already exists; add broken/fixed starting states to the exercise template. |
| 20 | Ratings table | No action | Numbers without a stated basis. |

Missed by the review: practical concurrency and distributed basics (audit open question 2).

## Triaged

| Date | Source | Confusion | Verdict | Where |
|---|---|---|---|---|
| 2026-10-07 | React work; four-module proposal from another agent | Terminal anatomy, compilers vs. interpreters vs. JIT, shell environment and scripted CLIs, dependency topography | Mixed: some covered, rest new chapters | Recorded retroactively. New Part III (From Source Code to Running Process), new Part VII (JavaScript and Node Tooling), four Part II chapters, Part VI opener. Full reasoning in the 2026-10-07 design-review session log entry. |
