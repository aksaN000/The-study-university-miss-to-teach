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
| 2026-10-07 | ChatGPT review of the 126-page skeleton | Twenty structural suggestions | Triaged by Claude on Aksan's instruction ("adopt what you agree with"), under the new audience rule (CS graduates who know the academic concepts) | **Adopted as new chapters**: Part V split and expanded (ports and sockets, localhost, DNS, TCP/UDP in practice, network tools); new Part VIII APIs (7 ch.), Part IX Databases in Practice (9 ch., practice not SQL theory), Part X Security in Practice (6 ch., placed by dependency: before CI and deployment, after APIs and databases); Part XIV expanded to 10 ch. (systemd, reverse proxies, domain to HTTPS, process inspection with strace, profiling, monitoring, rollback); a namespaces-and-cgroups chapter in Containers; Part XVI Capstone (2 ch.). **Dependency fix**: Semantic versioning moved from automation into Part VI before lockfiles. **Adopted as features**: per-part "Trace it", per-chapter depth tags, "How to use this book" in the preface, broken/fixed starting states in the exercise template. **Folded / covered**: Python packaging history (history-first rule), debugging as a cross-cutting habit. **Rejected**: CPU/registers chapter (course knowledge for this audience; syscalls get their practical face via strace in Part XIV), twenty networking chapters (MAC, DHCP, subnetting are CSE421 theory), the layer re-ordering (breaks dependencies), the fixed eight-step chapter loop (contradicts adaptive chapters), "do not cover everything" (contradicts Aksan's stated goal), the ratings table (no basis). Result: 103 to 139 chapters, 12 to 16 parts. |
| 2026-10-07 | Second ChatGPT review (151-chapter skeleton) | Ten suggestions | Applied as proposed, Aksan: "go" | New chapters: What the CPU actually executes (Part III), SQL at the prompt (Part IX). Retitles: HTTP anatomy, testing levels, race conditions with deadlocks. Fold-ins: TLS distinction table, deadlocks, concurrency scope guard (see Chapter Plan Notes). Jupyter stays; the do-not-add list agreed. 151 to 153 chapters. |
| 2026-10-07 | Claude's gap sweep, then a second sweep at Aksan's request ("add all, find more") | 32 chapters, 12 fold-ins | All adopted; boundary kept: practical layer as chapters, course theory as refreshers | All eleven first-sweep items, plus getting help, links, signals, VMs, disks, archives, hashes, WebAssembly, memory and sanitizers, Git LFS/submodules, DevTools, streaming/WebSockets/gRPC, application servers, HTTP caching/CDNs, infrastructure as code, orchestration, multi-GPU, data formats, HF cache, local models, LLM serving. Fold-ins in Chapter Plan Notes. 153 to 185 chapters. |
| 2026-10-07 | Aksan: should the book cover how languages, libraries, and frameworks are built? | 12 chapters | New part, placed by dependency | Part IX, Under the Hood, after APIs: tiny language (3 ch.), library internals, FFI, inversion of control, tiny web framework, tiny React, tiny autograd, plugins, language/runtime/stdlib, language evolution. 185 to 197 chapters. |
| 2026-10-07 | Gemini review (of the older 185-chapter PDF) | Remote compute, model weights, dev vs. prod, venv escape, Security placement, CUDA collision, OOM killer | Mostly adopted; one rejected | New: Moving files and ports over SSH, From dev server to production build, Resource limits and the OOM killer. Fold-ins in Chapter Plan Notes. Already covered: tmux, HF cache, Git LFS. Rejected: Security directly after APIs, because injection needs the databases part first. 197 to 200 chapters. |
