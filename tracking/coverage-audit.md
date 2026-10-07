# Coverage Audit: CS2023 Knowledge Areas

Part of the design-freeze gate (see "Design Freeze Criteria" in `curriculum-map.md`). The
question for each ACM/IEEE CS2023 knowledge area: is it covered by Aksan's degree, covered by
this project, or out of scope, and if out of scope, why?

**Status: started 2026-10-07, provisional.** Aksan's full BRAC course list has not yet been
recorded in the repo. The degree column below uses only the courses already on record in
`curriculum-map.md`: STA 301, ECO101, ECO102, CSE321 (Operating Systems), CSE420 (Compiler
Design), Computer Architecture, plus the self-reported and unverified DSA, OOP, databases,
software engineering, Computer Networks, Computer Graphics, and "several AI/ML courses" (no
course codes). Every row marked *pending* needs the real list (codes and titles) to close.
The audit is complete only when no row is pending.

Source: the 17 knowledge areas of CS2023 (csed.acm.org/knowledge-areas). Labels apply at the
area level; where an area splits (theory in the degree, practice here), both are named.

## Labels

- **Degree**: the theory is taught by a BRAC course. This project does not re-teach it.
- **Project**: this project owns it (some or all of the area's practical side).
- **Out of scope**: neither, deliberately. A reason is required.
- **Pending**: cannot be labelled until the course list is in.

## The audit

| KA | Area | Label | Degree side | Project side, or reason for exclusion |
|---|---|---|---|---|
| AL | Algorithmic Foundations | Degree (pending code) | DSA (self-reported); a separate algorithms course not yet confirmed | None needed. Graph intuition reused for Git's DAG (Part IV) and build graphs (Part X). |
| AR | Architecture and Organization | Degree + Project | Computer Architecture | Practical face only: ISAs and calling conventions as they show up in ABIs, executable formats, loaders (Part III); CUDA/driver stack (Part XII). |
| AI | Artificial Intelligence | Degree (pending codes) | "Several AI/ML courses" | Infrastructure only, not the models: Part XII (environments, CUDA, DVC, tracking, serving). |
| DM | Data Management | Degree (pending code) + gap | Databases (self-reported) | **Open question**: the practical side of running a database (installing a server, connecting over a port, connection strings, migrations, backups, a database in a container) has no chapter. Candidate for a new chapter after Part V networking and before or inside Part IX containers. |
| FPL | Foundations of Programming Languages | Degree + Project | CSE420 Compiler Design (front end, parsing, IR) | Runtime half: linking, loaders, interpreters, bytecode VMs, JIT, module systems (Part III, ch70). Type systems and PL semantics stay with the degree; confirm whether a separate PL course exists. |
| GIT | Graphics and Interactive Techniques | Degree | Computer Graphics (self-reported) | Out of scope for this project beyond GPU drivers in Part XII: graphics theory is not tooling. |
| HCI | Human-Computer Interaction | Pending | Unknown | If no course: likely out of scope (design discipline, not the layer around code), but recorded for Aksan's decision rather than assumed. |
| MSF | Mathematical and Statistical Foundations | Degree (pending codes) | STA 301; discrete math and linear algebra not yet confirmed | None needed. |
| NC | Networking and Communication | Degree + Project | Computer Networks (self-reported) | Practical face: ports, localhost, DNS, HTTP, TLS, SSH keys, servers (Part V); container networking (ch82). |
| OS | Operating Systems | Degree + Project | CSE321 (processes, threads, scheduling, sync, memory, file systems; see "What NOT to Re-Teach") | Practical face: Part I, Part II, isolation in Part IX, ops in Part XI. |
| PDC | Parallel and Distributed Computing | Pending + gap | Concurrency and synchronization via CSE321; distributed systems course unknown | **Open question**: no chapter covers practical concurrency tooling (async in Python, worker processes, queues) or distributed-systems basics (more than one machine, partial failure, consistency) beyond Node's event loop (ch38). Needs the course list first: if no distributed systems course, decide project vs. out of scope. |
| SDF | Software Development Fundamentals | Degree | OOP, DSA, early programming courses | Project supplies the environment around it: editors, terminals, running and debugging programs. |
| SE | Software Engineering | Degree + Project | Software Engineering (self-reported) | Practical tooling: Git (Part IV), testing, CI, linters, semver, reproducible builds (Part X), code review (ch46). |
| SEC | Security | Partial + gap | CSE321's final topic was protection and security (not confirmed landed); dedicated security course unknown | Project covers permissions (ch05), TLS (ch51), SSH keys (ch52), supply chain (ch72). **Open question**: secrets management (env files, never committing keys, CI secrets), basic threat modelling, and authentication for a deployed service have no home. Likely a fold-in to ch45/ch87/ch94, possibly a new chapter. |
| SEP | Society, Ethics, and the Profession | Pending | Unknown (BRAC may require an ethics course) | Licensing of what we publish (the book, OFL fonts, open-source licences on dependencies) has no chapter. Candidate fold-in to ch63 or ch72. Broader ethics: out of scope here, belongs to the degree. |
| SF | Systems Fundamentals | Project (mostly) | Pieces via CSE321 and Computer Architecture | This is the area the project most directly serves: layering, state, resource allocation, performance, reliability as practised. **Open question**: performance measurement and profiling (timing, profilers, reading resource usage) has no dedicated chapter; Missing Semester's profiling lecture is already the anchor for Part XI. |
| SPD | Specialized Platform Development | Project (web) + Out of scope (others) | Unknown | Web platform tooling is in scope (Part VII, React/Vite). Mobile, embedded, game, robotics and quantum platforms: out of scope, because each is a specialism Aksan has not chosen, and the transferable tooling questions are already taught via the cross-ecosystem capstones (ch73, ch93). Revisit if his job search points at one. |

## Open questions this audit has raised so far

These are not yet inbox items or syllabus changes. Each becomes one once Aksan decides.

1. Databases in practice (DM).
2. Practical concurrency and distributed-systems basics (PDC), after the course list is in.
3. Secrets and service security (SEC).
4. Licensing what we use and publish (SEP).
5. Measuring performance and profiling (SF).
6. HCI: degree, out of scope, or something else.

## To close the audit

- [ ] Aksan's full course list (codes and titles) recorded, and every *pending* row resolved
- [ ] Each open question above decided: new chapter, fold-in, or out of scope with a reason
- [ ] Any resulting syllabus changes made via `SYLLABUS` and the generators
