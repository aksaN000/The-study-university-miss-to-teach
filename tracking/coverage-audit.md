# Coverage Audit: CS2023 Knowledge Areas

Part of the design-freeze gate (see "Design Freeze Criteria" in `curriculum-map.md`). The
question for each ACM/IEEE CS2023 knowledge area: is it covered by Aksan's degree, covered by
this project, or out of scope, and if out of scope, why?

**Status (2026-10-07): every area labelled against Aksan's full course list; open questions
below await his decisions.** The course list itself is recorded in `curriculum-map.md` under
"Degree Course List". The audit is complete when every open question is decided.

Source: the 17 knowledge areas of CS2023 (csed.acm.org/knowledge-areas). Labels apply at the
area level; where an area splits (theory in the degree, practice here), both are named.

## Labels

- **Degree**: the theory is taught by a BRAC course. This project does not re-teach it.
- **Project**: this project owns it (some or all of the area's practical side).
- **Out of scope**: neither, deliberately. A reason is required.
- **Open**: a real gap that neither covers yet; Aksan decides (see "Open questions").

## The audit

| KA | Area | Label | Degree side | Project side, or reason for exclusion |
|---|---|---|---|---|
| AL | Algorithmic Foundations | Degree | CSE220 Data Structures, CSE221 Algorithms, CSE331 Automata and Computability (models of computation, formal languages) | None needed. Reused: Git's DAG (Part IV), build graphs (Part X), regular languages behind globbing and regex (ch17). |
| AR | Architecture and Organization | Degree + Project | CSE260 Digital Logic Design, CSE340 Computer Architecture | Practical face: ISAs and calling conventions as they appear in ABIs, executable formats, loaders (Part III); CUDA and drivers (Part XII). |
| AI | Artificial Intelligence | Degree + Project | CSE422 AI, CSE427 Machine Learning, CSE425 Neural Networks, CSE440 NLP, CSE428 Image Processing | Infrastructure only, never the models: Part XII (environments, CUDA, DVC, experiment tracking, config, serving). |
| DM | Data Management | Degree + Open | CSE370 Database Systems | **Open question 1**: operating a database (installing a server, connecting over a port, connection strings, migrations, backups, a database in a container) has no chapter. |
| FPL | Foundations of Programming Languages | Degree + Project | CSE110 and CSE111 Programming Language I and II, CSE420 Compiler Design (front end, parsing, IR), CSE331 (formal languages) | Runtime half: linking, loaders, interpreters, bytecode VMs, JIT, module systems (Part III, ch70). **Open question 7**: no course covers type systems, semantics, or functional programming. |
| GIT | Graphics and Interactive Techniques | Degree | CSE423 Computer Graphics, CSE428 Image Processing | Out of scope here beyond GPU drivers (Part XII): graphics is a subject, not the layer around code. |
| HCI | Human-Computer Interaction | Open | No course | **Open question 6**. Recommendation: out of scope, because HCI is a design and research discipline rather than tooling; accessibility checks could fold into Part VII's tooling chapters. |
| MSF | Mathematical and Statistical Foundations | Degree | CSE230 Discrete Mathematics, CSE330 Numerical Methods, STA301 Advanced Statistics | None needed. **To confirm**: no MAT courses (calculus, linear algebra) were listed; record them if taken. |
| NC | Networking and Communication | Degree + Project | CSE421 Computer Networks | Practical face: ports, localhost, DNS, HTTP, TLS, SSH keys, servers (Part V); container networking (ch82). |
| OS | Operating Systems | Degree + Project | CSE321 Operating Systems (see "What NOT to Re-Teach") | Practical face: Parts I and II, isolation in Part IX, operations in Part XI. |
| PDC | Parallel and Distributed Computing | Degree (concurrency) + Open | CSE321 covers threads, synchronization, deadlock; no parallel or distributed systems course | **Open question 2**: practical concurrency (async, worker processes, multiprocessing, queues) and distributed basics (several machines, partial failure, retries, consistency) have no chapter beyond Node's event loop (ch38). |
| SDF | Software Development Fundamentals | Degree | CSE110, CSE111, CSE220 | Project supplies the environment around it: terminals, editors, running and debugging programs. |
| SE | Software Engineering | Degree + Project | CSE470 Software Engineering | Practical tooling: Git (Part IV), testing, CI, linters, semver, reproducible builds (Part X), code review (ch46). |
| SEC | Security | Open | No security course; CSE321's final topic was protection and security | Project covers permissions (ch05), TLS (ch51), SSH keys (ch52), supply chain (ch72). **Open question 3**: secrets management (env files, never committing keys, CI secrets), basic threat modelling, and authentication for a deployed service have no home. With no security course, this gap is now firmly ours to decide. |
| SEP | Society, Ethics, and the Profession | Open | No course (ECO101/102 cover economics, not professional ethics) | **Open question 4**: licensing of what we publish and depend on has no chapter. Recommendation: fold into ch63 or ch72; broader ethics out of scope because it is a different kind of study from tooling. |
| SF | Systems Fundamentals | Project | Pieces via CSE321, CSE340, CSE260 | The area this project most directly serves: layering, state, resources, reliability as practised. **Open question 5**: measuring performance and profiling has no dedicated chapter. |
| SPD | Specialized Platform Development | Degree + Project (web); Out of scope (others) | Web development (MERN), as listed | Web tooling is in scope (Part VII: npm, modules, Vite, React's toolchain). Mobile, embedded, game, robotics, quantum: out of scope, because each is a specialism not yet chosen and the transferable questions are taught by the capstones (ch73, ch93). Revisit if the job search points at one. |

## Open questions (Aksan decides each: new chapter, fold in, or out of scope with a reason)

1. **Databases in practice (DM).** Suggested placement if a chapter: after Part V networking
   (needs ports and localhost) and before Part IX containers (which will run one).
2. **Practical concurrency and distributed basics (PDC).**
3. **Secrets and service security (SEC).**
4. **Licensing (SEP).**
5. **Measuring performance and profiling (SF).**
6. **HCI.** Recommendation above: out of scope.
7. **PL theory gap (FPL)**: type systems, semantics, functional programming. Likely out of scope
   for this project (theory, not the layer around code) but a real gap for the "debate as an
   equal" goal; Aksan may want it as separate study.

## To close the audit

- [x] Aksan's full course list recorded and every area labelled (2026-10-07)
- [ ] MAT courses confirmed (taken or not)
- [ ] Each open question decided
- [ ] Any resulting syllabus changes made via `SYLLABUS` and the generators, each logged
