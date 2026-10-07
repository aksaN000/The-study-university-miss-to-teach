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

### 2026-10-07: second external review (ChatGPT, of the 151-chapter skeleton)

Claude's proposed verdicts; nothing changes in `SYLLABUS` until Aksan decides.

| # | Suggestion | Proposed verdict | Notes |
|---|---|---|---|
| 1 | "What the CPU actually executes" chapter (instructions, registers, stack, heap, x86-64 vs. ARM64, user vs. kernel mode) | New chapter, Part III, after "The C pipeline" and before "Linking and loading" | Reverses the earlier rejection: under the "studied, not mastered" audience rule this has a real practical face (disassemble our own compiled C with objdump, watch registers in gdb). Needs WSL's gcc, so Part III, not Part I. ABIs and multi-architecture Docker images build on it. |
| 2 | SQL fundamentals before ORMs | New chapter after "SQLite" | "SQL at the prompt: psql, sqlite3, and the queries we actually write": a CSE370 refresher done hands-on, so the ORM chapter has something to compare against. |
| 3 | HTTP request/response anatomy explicit | Retitle | "HTTP basics" becomes "HTTP: the anatomy of a request and a response". |
| 4 | Keep concurrency practical, not a distributed-systems course | Covered, plus one fold-in | The six titles are already practical; add deadlocks to the race-conditions chapter. |
| 5 | Testing levels (unit, integration, end-to-end) and what a test proves | Retitle and fold in | "Automated testing: what a test proves, from unit to end-to-end". |
| 6 | Trace it, break it, diagnose it as a consistent method | Covered | Already built: `traceit` and `breakage` boxes, and the session's breakage step. |
| 7 | Encryption vs. authentication vs. integrity vs. trust | Fold into the TLS chapter | A distinction table there; revisited by the security part. |
| 8 | Move Jupyter later | Reject (the review itself says leave it) | Its dependencies (Python environments, networking) are already met. |
| 9 | Do not add Kubernetes, Terraform, cloud certs, framework tutorials, system design, DSA | Agree | None are in the syllabus; this matches the project's identity. |
| 10 | Scores | No action | |

Net effect if accepted: 151 to 153 chapters, two retitles, three fold-ins.

## Triaged

| Date | Source | Confusion | Verdict | Where |
|---|---|---|---|---|
| 2026-10-07 | React work; four-module proposal from another agent | Terminal anatomy, compilers vs. interpreters vs. JIT, shell environment and scripted CLIs, dependency topography | Mixed: some covered, rest new chapters | Recorded retroactively. New Part III (From Source Code to Running Process), new Part VII (JavaScript and Node Tooling), four Part II chapters, Part VI opener. Full reasoning in the 2026-10-07 design-review session log entry. |
| 2026-10-07 | ChatGPT review of the 126-page skeleton | Twenty structural suggestions | Triaged by Claude on Aksan's instruction ("adopt what you agree with"), under the new audience rule (CS graduates who know the academic concepts) | **Adopted as new chapters**: Part V split and expanded (ports and sockets, localhost, DNS, TCP/UDP in practice, network tools); new Part VIII APIs (7 ch.), Part IX Databases in Practice (9 ch., practice not SQL theory), Part X Security in Practice (6 ch., placed by dependency: before CI and deployment, after APIs and databases); Part XIV expanded to 10 ch. (systemd, reverse proxies, domain to HTTPS, process inspection with strace, profiling, monitoring, rollback); a namespaces-and-cgroups chapter in Containers; Part XVI Capstone (2 ch.). **Dependency fix**: Semantic versioning moved from automation into Part VI before lockfiles. **Adopted as features**: per-part "Trace it", per-chapter depth tags, "How to use this book" in the preface, broken/fixed starting states in the exercise template. **Folded / covered**: Python packaging history (history-first rule), debugging as a cross-cutting habit. **Rejected**: CPU/registers chapter (course knowledge for this audience; syscalls get their practical face via strace in Part XIV), twenty networking chapters (MAC, DHCP, subnetting are CSE421 theory), the layer re-ordering (breaks dependencies), the fixed eight-step chapter loop (contradicts adaptive chapters), "do not cover everything" (contradicts Aksan's stated goal), the ratings table (no basis). Result: 103 to 139 chapters, 12 to 16 parts. |
