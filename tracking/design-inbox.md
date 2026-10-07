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

### 2026-10-07: Claude's own gap sweep (Aksan asked "did we miss anything?")

Proposed verdicts; nothing changes in `SYLLABUS` until Aksan decides.

| # | Gap | Proposed verdict | Placement and reason |
|---|---|---|---|
| 1 | Using a debugger on our own code: breakpoints, stepping, reading a stack trace (pdb, Node inspector, gdb, VS Code) | New chapter | Part III, after Node.js. Every later part assumes we can debug; no course teaches it. |
| 2 | The editor as a client: VS Code, language servers, and which interpreter it picked | New chapter | Part VI, after the conda and uv chapters. Directly Aksan's two-Pythons, four-kernels situation. |
| 3 | Regular expressions in practice | New chapter | Part II, after globbing (the contrast is the point; CSE331 refresher). |
| 4 | Text and JSON at the command line: grep, sed, awk, jq | New chapter | Part II, right after regex. |
| 5 | Config formats: JSON, YAML, TOML, and their traps | New chapter | Part II, after dotfiles; every manifest from Part VI on is one of these. |
| 6 | Long jobs on a remote machine: tmux, nohup, surviving a dropped SSH connection | New chapter | Part II, after SSH. Essential for GPU training runs. |
| 7 | Scheduled work and time: cron, systemd timers, UTC, time zones | New chapter | Part XIV, after systemd. |
| 8 | The cloud as someone else's computer: VMs, object storage, paying by the hour | New chapter | Part XIV, after the first deploy. Mental model only, no provider certification. |
| 9 | AI coding assistants as tools: what they run, what they see, how we review it | New chapter | Part XIII, after pre-commit and linters: permissions, review, and trust, using the tools Aksan already uses. |
| 10 | Shared GPU machines and job schedulers: Slurm in practice | New chapter (specialized) | Part XVI, after CUDA. Research clusters run on it. |
| 11 | Documents as code: Markdown, LaTeX, BibTeX, reproducible papers | Consider (specialized) | Part XIII. Thesis and this book both live here; optional. |
| 12 | Tags and releases; CMake; NAT and tunnels (why a friend cannot reach our localhost); winget and Chocolatey; structured logging in our own code | Fold-ins | Into Semantic versioning; Makefiles; localhost and private vs. public addresses; apt; Reading logs. |

Net effect if all accepted: 153 to 163 or 164 chapters.

## Triaged

| Date | Source | Confusion | Verdict | Where |
|---|---|---|---|---|
| 2026-10-07 | React work; four-module proposal from another agent | Terminal anatomy, compilers vs. interpreters vs. JIT, shell environment and scripted CLIs, dependency topography | Mixed: some covered, rest new chapters | Recorded retroactively. New Part III (From Source Code to Running Process), new Part VII (JavaScript and Node Tooling), four Part II chapters, Part VI opener. Full reasoning in the 2026-10-07 design-review session log entry. |
| 2026-10-07 | ChatGPT review of the 126-page skeleton | Twenty structural suggestions | Triaged by Claude on Aksan's instruction ("adopt what you agree with"), under the new audience rule (CS graduates who know the academic concepts) | **Adopted as new chapters**: Part V split and expanded (ports and sockets, localhost, DNS, TCP/UDP in practice, network tools); new Part VIII APIs (7 ch.), Part IX Databases in Practice (9 ch., practice not SQL theory), Part X Security in Practice (6 ch., placed by dependency: before CI and deployment, after APIs and databases); Part XIV expanded to 10 ch. (systemd, reverse proxies, domain to HTTPS, process inspection with strace, profiling, monitoring, rollback); a namespaces-and-cgroups chapter in Containers; Part XVI Capstone (2 ch.). **Dependency fix**: Semantic versioning moved from automation into Part VI before lockfiles. **Adopted as features**: per-part "Trace it", per-chapter depth tags, "How to use this book" in the preface, broken/fixed starting states in the exercise template. **Folded / covered**: Python packaging history (history-first rule), debugging as a cross-cutting habit. **Rejected**: CPU/registers chapter (course knowledge for this audience; syscalls get their practical face via strace in Part XIV), twenty networking chapters (MAC, DHCP, subnetting are CSE421 theory), the layer re-ordering (breaks dependencies), the fixed eight-step chapter loop (contradicts adaptive chapters), "do not cover everything" (contradicts Aksan's stated goal), the ratings table (no basis). Result: 103 to 139 chapters, 12 to 16 parts. |
| 2026-10-07 | Second ChatGPT review (151-chapter skeleton) | Ten suggestions | Applied as proposed, Aksan: "go" | New chapters: What the CPU actually executes (Part III), SQL at the prompt (Part IX). Retitles: HTTP anatomy, testing levels, race conditions with deadlocks. Fold-ins: TLS distinction table, deadlocks, concurrency scope guard (see Chapter Plan Notes). Jupyter stays; the do-not-add list agreed. 151 to 153 chapters. |
