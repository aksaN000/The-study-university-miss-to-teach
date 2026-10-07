# Curriculum Map — Systems & Developer Tooling, From Zero

This file is the persistent memory for a project with no fixed end date. Read it at the start of
every session. Update it at the end of every session — the status table, the relevant checklist, and
the session log at minimum. Do not rely on conversation recall alone to know where things stand.

---

## Phase Status

Generated from `book/generate_stubs.py` (the single syllabus source). Phase N = Part N+1.

| Phase | Part | Topic | Status |
|---|---|---|---|
| 0 | I | Mental Foundations (9 ch.) | 🔄 Diagnostic sent, awaiting answers |
| 1 | II | The Command Line (19 ch.) | ⏳ Not started |
| 2 | III | From Source Code to Running Process (11 ch.) | ⏳ Not started |
| 3 | IV | Version Control, Properly (9 ch.) | ⏳ Not started |
| 4 | V | Networking Essentials (5 ch.) | ⏳ Not started |
| 5 | VI | Python Environments and Packaging (10 ch.) | ⏳ Not started |
| 6 | VII | JavaScript and Node Tooling (10 ch.) | ⏳ Not started |
| 7 | VIII | Jupyter and the Notebook Stack (6 ch.) | ⏳ Not started |
| 8 | IX | Containers (6 ch.) | ⏳ Not started |
| 9 | X | Automation and Build Tooling (8 ch.) | ⏳ Not started |
| 10 | XI | Deployment and Operations (3 ch.) | ⏳ Not started |
| 11 | XII | Machine Learning Infrastructure (7 ch.) | ⏳ Not started |

---

## Detailed Phase Breakdown

Check items off only once taught AND confirmed by a recall check. Chapter numbers are
book chapter numbers; they shift automatically whenever the syllabus changes, so refer to
chapters by title in conversation and by number only when reading the compiled book.

### Phase 0: Mental Foundations (Part I)
- [ ] ch01 What does an operating system actually do
- [ ] ch02 Processes: the unit of a running program
- [ ] ch03 Memory: what is actually there
- [ ] ch04 The filesystem: how storage becomes files and folders
- [ ] ch05 File permissions: who is allowed to do what
- [ ] ch06 Running a program: fork, exec, and CreateProcess
- [ ] ch07 Environment variables: the machine's sticky notes
- [ ] ch08 Paths: absolute, relative, and relative to what
- [ ] ch09 Text encodings and line endings: why files disagree

### Phase 1: The Command Line (Part II)
- [ ] ch10 Terminal, console, shell: three things we call by one name
- [ ] ch11 What a shell is and why it exists
- [ ] ch12 PowerShell vs. bash/zsh: different languages, not different skins
- [ ] ch13 Navigating, creating, moving, deleting
- [ ] ch14 Standard input, output, and error
- [ ] ch15 Pipes and redirection
- [ ] ch16 Exit codes: how a program reports back
- [ ] ch17 Globbing and quoting
- [ ] ch18 Anatomy of a command line: argv, flags, options, and the double dash
- [ ] ch19 PATH: how a name becomes a program
- [ ] ch20 Environment variables in practice
- [ ] ch21 Session versus persistent configuration: dotfiles, profiles, and the registry
- [ ] ch22 Installing WSL2
- [ ] ch23 Doing it all again in Ubuntu
- [ ] ch24 apt, the Linux filesystem hierarchy, and sudo
- [ ] ch25 SSH
- [ ] ch26 Writing real shell scripts
- [ ] ch27 Living comfortably in the terminal
- [ ] ch28 A third machine: where macOS agrees with Linux, and where it quietly doesn't

### Phase 2: From Source Code to Running Process (Part III)
- [ ] ch29 Three kinds of things on PATH: native binaries, language engines, and scripted tools
- [ ] ch30 Executable files: ELF, PE, Mach-O, magic numbers, and shebangs
- [ ] ch31 The C pipeline: preprocess, compile, assemble, link
- [ ] ch32 Linking and loading: static, dynamic, and the loader that runs first
- [ ] ch33 ABIs: why a binary built here refuses to run there
- [ ] ch34 Interpreters, honestly: line by line, tree walking, and bytecode
- [ ] ch35 Inside CPython: from source to .pyc to the evaluation loop
- [ ] ch36 Bytecode virtual machines: the JVM and .NET
- [ ] ch37 JIT compilation through V8: Ignition, Sparkplug, Maglev, TurboFan
- [ ] ch38 Node.js: a JavaScript engine plus an operating system API
- [ ] ch39 Scripted CLIs: shebangs, launcher shims, and why python -m pip exists

### Phase 3: Version Control, Properly (Part IV)
- [ ] ch40 The object model: blobs, trees, and commits
- [ ] ch41 Refs, and what a branch actually is
- [ ] ch42 HEAD
- [ ] ch43 Merge vs. rebase, and when each is correct
- [ ] ch44 Resolving conflicts without panic
- [ ] ch45 .gitignore: what belongs in a repo
- [ ] ch46 Remotes, pull requests, and code review
- [ ] ch47 Recovering from disasters with reflog
- [ ] ch48 Reading someone else's history

### Phase 4: Networking Essentials (Part V)
- [ ] ch49 Ports, localhost, and IP vs. DNS
- [ ] ch50 HTTP basics
- [ ] ch51 TLS and certificates
- [ ] ch52 SSH keys
- [ ] ch53 What a server actually is

### Phase 5: Python Environments and Packaging (Part VI)
- [ ] ch54 What a package manager actually automates
- [ ] ch55 How the interpreter finds code: sys.path and site-packages
- [ ] ch56 Why global installs cause problems: a tour of our own machine
- [ ] ch57 venv: what it actually does, mechanically
- [ ] ch58 pip, PyPI, sdists, and wheels
- [ ] ch59 Why compiled packages make Python versions matter
- [ ] ch60 requirements.txt, lockfiles, and pyproject.toml
- [ ] ch61 conda: what problem it solved that pip could not
- [ ] ch62 Modern tooling: uv and poetry
- [ ] ch63 Packaging and publishing something of our own

### Phase 6: JavaScript and Node Tooling (Part VII)
- [ ] ch64 npm, global installs, and project scope
- [ ] ch65 package.json and semver ranges: declaring what we need
- [ ] ch66 node_modules: nested, flattened, hoisted, and linked
- [ ] ch67 Lockfiles and npm ci: making installs repeatable
- [ ] ch68 npm configuration: .npmrc, npm_config variables, and stricter validation
- [ ] ch69 npx, npm create, and scaffolding CLIs
- [ ] ch70 CommonJS and ES modules: two module systems in one ecosystem
- [ ] ch71 Transpilers, bundlers, and dev servers: what Vite does with our React code
- [ ] ch72 Supply-chain security: every dependency is code we chose to run
- [ ] ch73 Packaging elsewhere: Cargo, Maven, Go modules, and what every ecosystem shares

### Phase 7: Jupyter and the Notebook Stack (Part VIII)
- [ ] ch74 The frontend/kernel split, and why it exists
- [ ] ch75 The kernel protocol
- [ ] ch76 Kernel specs: where they live, how discovery works
- [ ] ch77 Why notebooks break in ways scripts do not
- [ ] ch78 Notebooks and version control
- [ ] ch79 When a notebook is the wrong tool

### Phase 8: Containers (Part IX)
- [ ] ch80 The isolation idea, generalized from environments to the whole OS
- [ ] ch81 Images, layers, and Dockerfiles
- [ ] ch82 Volumes, ports, and networking
- [ ] ch83 docker-compose
- [ ] ch84 GPU containers
- [ ] ch85 Why "works on my machine" stops being necessary

### Phase 9: Automation and Build Tooling (Part X)
- [ ] ch86 Makefiles
- [ ] ch87 GitHub Actions and CI/CD
- [ ] ch88 Automated testing as a habit, not a chore
- [ ] ch89 Pre-commit hooks
- [ ] ch90 Linters and formatters
- [ ] ch91 Semantic versioning
- [ ] ch92 Reproducible builds
- [ ] ch93 The same pipeline, five languages: CI beyond Python

### Phase 10: Deployment and Operations (Part XI)
- [ ] ch94 Deploying something small to a real machine
- [ ] ch95 Reading logs
- [ ] ch96 Debugging a process that will not start

### Phase 11: Machine Learning Infrastructure (Part XII)
- [ ] ch97 Reproducible ML environments
- [ ] ch98 CUDA and driver versions
- [ ] ch99 Data versioning with DVC
- [ ] ch100 Experiment tracking: MLflow and W&B
- [ ] ch101 Configuration management
- [ ] ch102 Serving a model
- [ ] ch103 Why almost every ML project fails to be reproducible

### Cross-Cutting — Professional Habits (reinforce throughout, not a single session)
- [ ] Reading documentation and source instead of guessing
- [ ] Reading error messages carefully and completely
- [ ] Writing a README a stranger can follow
- [ ] Debugging methodically instead of by trial and error
- [ ] Knowing when to ask, and how to ask well

---

## Book Companion

Full LaTeX skeleton lives at `book/` at the repo root: one chapter stub per syllabus entry,
generated by `book/generate_stubs.py`, whose `SYLLABUS` list is the single source of truth for
chapter titles and order (the tables above and the practice repo are generated from it too).
Rules for writing into the book (voice, audience, what "fully completed" gates, adaptive
chapter design) are in SKILL.md, not repeated here.

---

## Anchor Resource Map

Which canonical source to point to for each phase, per the project's own instruction to read
alongside the taught material rather than relying only on Claude's explanations.

| Phase | Primary canonical source |
|---|---|
| 0 | *Computer Systems: A Programmer's Perspective* (Bryant & O'Hallaron), "the layer beneath"; OSTEP for processes and virtualization |
| 1 | *The Linux Command Line* (Shotts, linuxcommand.org); Missing Semester: Shell, Shell Tools & Scripting, Command-line Environment (dotfiles); POSIX Utility Syntax Guidelines (the `--` convention); OverTheWire: Bandit |
| 2 | CS:APP ch. 7 (Linking) and ch. 8 (Exceptional Control Flow: fork/exec); `man 5 elf`, `man 8 ld.so`; *Crafting Interpreters* (Nystrom, free at craftinginterpreters.com) for tree-walking vs. bytecode; the CPython devguide's compiler/interpreter internals; v8.dev blog posts on Ignition, Sparkplug, Maglev; nodejs.org "The Node.js Event Loop" guide |
| 3 | *Pro Git* (Chacon & Straub), especially Git Internals; Missing Semester: Version Control; Learn Git Branching |
| 4 | Julia Evans' networking zines; MDN "An overview of HTTP"; Missing Semester: Security & Cryptography for the TLS/SSH trust model |
| 5 | The Python Packaging User Guide (packaging.python.org) and the relevant PEPs (427 wheels, 517/518 build systems, 621 pyproject metadata, 668 externally managed environments) |
| 6 | docs.npmjs.com (package.json, npmrc, config, scripts, folders); nodejs.org module docs (CommonJS vs. ESM); vite.dev guide ("Why Vite"); pnpm.io "Motivation" |
| 7 | Jupyter client docs: the kernel messaging protocol |
| 8 | Docker's official documentation; docker-curriculum.com |
| 9 | Missing Semester: Metaprogramming (build systems, CI, dependency management); GitHub Actions docs; semver.org |
| 10 | Missing Semester: Debugging and Profiling; `journalctl`/`systemd` man pages |
| 11 | Full Stack Deep Learning (fullstackdeeplearning.com) |
| Cross-cutting | wizardzines.com (Julia Evans) — short, sharp treatments of almost everything above; good as reinforcement after a concept is first taught here, not as the first exposure |

State the specific chapter/lecture at the start of each session, per the project's own instruction —
this map is the starting point, not a substitute for citing the exact section that session covers.

---

## Learner's Machine (use as the running example, not hypotheticals)

- **OS**: Windows 11 Pro, primary daily driver
- **Editor**: VS Code, with the Python and Jupyter extensions
- **Python install #1**: `C:\Users\aksan\AppData\Local\Programs\Python\Python313\python.exe`
  (3.13.1) — roughly 300 packages installed globally into one `site-packages`: torch, tensorflow,
  django, flask, spacy, geopandas, opencv, and years of accumulated project dependencies
- **Python install #2**: Miniconda at `C:\Users\aksan\miniconda3` (3.13.12), with conda envs
  `cv_lab`, `gensim_env`, `sam2-sar`, and four registered Jupyter kernels
- **Git**: installed, used only as memorized `add` / `commit` / `push` — no model of the object model
  underneath
- **Never used**: WSL, Docker, shell scripting, CI

---

## Additional Background (Self-Reported, 2026-07-30 Follow-Up)

Before answering the Phase 0 diagnostic, Aksan volunteered more context. Recorded here, but
deliberately flagged as **self-reported and not yet verified** — the project's own instructions are
explicit that confidence and correctness aren't the same signal, so none of this should be treated as
confirmed until it shows up correctly in an actual answer or a running command.

- **More coursework**: Computer Networks, Computer Graphics, and — in his words — "so many other CS
  and AI, ML courses." OS was reconfirmed as Linux-based.
- **Self-assessed comfort**: "basic Linux shell things," "Linux filesystems," and GitHub at the level
  of commit/push/pull (pull, beyond the add/commit/push named in the original project brief).
- **Practical implication**: treat this as a hypothesis to test, not a fact to build on. Phase 1
  especially should still open by testing this directly rather than skipping ahead on the strength of
  the claim — this is precisely the "sounded confident right up until—" pattern the project exists to
  catch. Computer Networks is a genuinely useful connection for Phase 4 (networking essentials) when we get there.

---

## Degree Course List (Aksan, 2026-10-07)

Stated by Aksan directly; supersedes the partial, self-reported list above. BRAC University.

- **Programming and foundations**: CSE110 Programming Language I, CSE111 Programming Language
  II, CSE220 Data Structures, CSE221 Algorithms, CSE230 Discrete Mathematics, CSE331 Automata
  and Computability, CSE330 Numerical Methods
- **Systems**: CSE260 Digital Logic Design, CSE321 Operating Systems, CSE340 Computer
  Architecture, CSE420 Compiler Design, CSE421 Computer Networks
- **Data and software**: CSE370 Database Systems, CSE470 Software Engineering, web development
  (MERN)
- **AI and ML**: CSE422 Artificial Intelligence, CSE427 Machine Learning, CSE425 Neural
  Networks, CSE440 Natural Language Processing, CSE428 Image Processing
- **Other**: CSE423 Computer Graphics, STA301 Advanced Statistics, ECO101 and ECO102
  (micro and macroeconomics fundamentals)
- **Not on the list**: any security, parallel/distributed systems, HCI, or ethics course; any
  MAT course (to confirm). These shape the coverage audit's open questions.

Courses taken are not the same as material that landed: per the "What NOT to Re-Teach" rule,
verify with one light question before building on any of them.

---

## What NOT to Re-Teach From Scratch

Cross-referenced from the `os-tutor` skill's course map (CSE321, Spring 2026, BRAC University — that
semester has since ended as of this project starting). Use this to calibrate depth in Phase 0 and
wherever OS theory resurfaces later — the goal is to connect this theory to practice, not re-derive
it.

**Confirmed solid** (explicitly marked done mid-semester in the OS course map):
- Process states (new → ready → running → waiting → terminated), PCB structure, `fork()` semantics,
  IPC basics, race conditions between processes
- Thread model: shared code/data/heap, private stack and registers; pthreads API; why concurrent
  thread creation (vs. sequential create-then-join) enables races
- CPU scheduling: FCFS, SJF/SRTF, Priority (preemptive), Round Robin, MLQ, MLFQ; preemption;
  waiting/turnaround time; starvation and aging

**Very likely solid, per the syllabus, but not independently confirmed in this project** (the
Spring 2026 semester ran through these after the OS course map was last updated, so treat as
probably covered and verify with one light question rather than assuming either zero or full
mastery):
- Synchronization: critical-section problem, mutex locks, semaphores, deadlock, classic problems
  (Bounded Buffer, Readers-Writers, Dining Philosophers)
- File systems — the syllabus listed Silberschatz Ch. 11/13/14 *and* OSTEP Ch. 40/42, which means
  crash consistency and journaling were in scope, not just directory structures — this is real
  depth if it landed
- Memory management — paging and segmentation (Silberschatz Ch. 9/10)
- Protection and security (final syllabus topic)

**Practical implication for this project**: when Phase 0's process/memory/filesystem sections come
up, don't open with "here's what a process is." Open with the applied question — how does the
theoretical model show up in what Aksan can actually observe and manipulate on his own Windows
machine and, later, in WSL2/Ubuntu. That gap — theory solid, application untested — is the specific
thing this project exists to close.

---

## Cross-Course Connection Map

| New concept (this project) | Connects back to |
|---|---|
| Process creation (`fork`/`exec` on Linux, `CreateProcess` on Windows) | PCB and process states, OS CSE321 Ch. 3 |
| Why a shell needs `fork`+`exec` to run anything | Same process-creation model, now seen from the caller's side |
| Virtual memory as the reason containers/VMs can isolate | Paging/segmentation, OS CSE321 Ch. 9–10 |
| File permissions (`rwx`, inodes on Linux) | File system internals, OSTEP 40/42, OS CSE321 |
| Why Docker needs namespaces + cgroups | Process isolation and resource limits, OS CSE321 |
| PATH lookup / symbol resolution intuition | Symbol tables and scoping, Compiler Design CSE420 |
| A Makefile's dependency graph | Compiler driver stages — CSE420's lexer→parser→codegen pipeline is itself a build pipeline |
| The gcc driver's stages (cpp, cc1, as, ld) | CSE420's front end/back end split: cc1 *is* the compiler from the course; the other stages are what the course stopped short of |
| Calling conventions and ABIs | Computer Architecture: registers, stack frames, instruction sets |
| Dynamic loading and shared libraries | OS CSE321 memory management: shared pages, mmap, address spaces |
| V8 deoptimization, CPython bytecode | CSE420 intermediate representations and code generation |
| Event loop in Node.js | OS CSE321 I/O and threads: one thread plus non-blocking I/O vs. thread-per-request |
| Git's commit graph (DAG) | Graph theory from DSA |
| Deadlock in a dependency-ordered build or containers waiting on each other | Deadlock conditions, OS CSE321 Ch. 6.8 |
| Cache/registers/memory hierarchy intuition for why Docker layers are fast to reuse | Computer Architecture |
| Globbing vs. regular expressions (two different pattern languages) | Regular languages and finite automata, CSE331 |
| Bits on disk, character encodings, two's complement in file formats | Digital Logic Design, CSE260 |
| Floating-point surprises across machines and GPU reproducibility | Numerical Methods, CSE330 |
| Running a database server, connection strings, migrations | Database Systems, CSE370 (theory side) |
| npm, Vite, and the React toolchain | Web development (MERN): the apps were built; the tooling under them was not taught |

---

## Design Freeze Criteria (2026-10-07)

The project is in its design phase. Teaching (starting with the Phase 0 diagnostic) begins only
once the design freezes, and it freezes only when all three hold at the same time:

- [ ] **The coverage audit is complete**: every CS2023 knowledge area in
  `tracking/coverage-audit.md` is labelled degree, project, or out of scope with a reason; no
  row is pending; every open question the audit raised is decided.
- [ ] **The design inbox is empty of untriaged items**: every entry in
  `tracking/design-inbox.md` has a verdict (covered, fold in, new chapter).
- [ ] **Aksan signs off**, explicitly, in a session, recorded in the session log with the date.

After the freeze, new confusions still go through the inbox, but a new chapter then needs
Aksan's explicit approval because it moves a frozen plan.

---

## Tracking and Infrastructure Decision (2026-10-07, supersedes the 2026-07-30 one below)

Everything lives in one GitHub repository, `aksaN000/The-study-university-miss-to-teach`, which
Aksan will publish together with the finished book. Sessions run in Claude Code (on the web or
the Claude mobile app's Code tab while travelling, or locally), connected to GitHub once through
Anthropic's GitHub app, so Claude commits and pushes all tracking itself. GitHub Actions builds
the PDF on every push and publishes it as the `book-latest` release. Pasted credentials are never
used (Aksan offered; declined). The claude.ai Project remains usable for design discussion but
cannot push. Layout is documented in the skill's "Home of Everything" section.

## Tracking & Tooling Infrastructure Decision (2026-07-30) (historical)

Aksan asked how to keep this durable across sessions and across tools (claude.ai, Cowork, Claude
Code). Decision, recorded here so it doesn't need re-deriving later:

- **Custom Skills don't sync across Claude surfaces** (confirmed against Anthropic's docs, not
  assumed). This skill, built in claude.ai, is also visible in **Cowork** — Cowork loads the skills
  enabled on the claude.ai account at session start. It is **not** automatically visible in **Claude
  Code**, which reads its own local `~/.claude/skills/` on Aksan's machine instead.
- This folder (`/mnt/skills/user/systems-tooling-tutor/`) is now itself a local git repository —
  initialized directly inside the already-persistent skill directory, so real commit history survives
  across sessions with zero external setup or credentials required. Commit here at the end of every
  session, alongside updating this file.
- **Not yet done, Aksan's call whenever he wants it**: pointing this local repo at a real GitHub
  remote, for off-platform backup, human browsing, and use from Claude Code. Recommended path when
  ready: do it from a Claude Code session on his own machine, since Claude Code already has his real
  git/GitHub identity configured locally — that avoids ever pasting a credential into a web chat.
  Once a remote exists, `git pull` at the start of a session and `git push` at the end works cleanly
  from whichever surface is in use that day.

---

## Session Log

Append an entry after every session — date, what was actually covered (and confirmed via recall
check, not just mentioned), any gap that needs revisiting, and what's next.

- **Session 1 (2026-07-30)**: Project kickoff. Reviewed os-tutor / compiler-tutor / sta-tutor to build
  this skill consistently with established patterns. Cross-referenced the OS course map. Sent the
  Phase 0 diagnostic (mental-foundations self-assessment). Before answering, Aksan asked about durable
  cross-tool tracking — set up local git history inside this skill folder (see Tracking & Tooling
  Infrastructure Decision above) and logged additional self-reported background, unverified (see
  Additional Background above). Still awaiting the actual Phase 0 diagnostic answers before starting
  real teaching.
- **Same session, continued**: Aksan asked a genuine syllabus-scoping question before answering the
  diagnostic — why `node file.js` looks different from how he presses "Run" on Python, and why other
  languages seem to need different ceremony. Answered conceptually (compiled vs. interpreted vs.
  bytecode-VM hybrid; the OS-level reason an interpreter binary has to exist at all; JS/Node history;
  connected to CSE420 compiler front-end/back-end split) without the full hands-on ritual, since this
  was scoping rather than a designated session. **Useful signal surfaced**: he believed Python's
  "press run" was simpler/different in kind from `node file.js` — it isn't, they're structurally
  identical (`interpreter filename`); the perceived difference was entirely Colab/VS Code's Run button
  hiding the same command for every language, Python included. This is a clean, concrete instance of
  the exact Colab-blind-spot the whole project exists to close — worth referencing directly when we
  reach Phase 0's "what running a program means" and Phase 1's PATH/invocation content for real.
- **Same session, continued further**: Aksan asked for a companion book — one chapter written
  per fully-completed session, "we" voice, self-contained for a reader who knows nothing (this
  book is meant to be shareable with other students later, unlike the live sessions which build
  on Aksan's specific coursework) — plus a formal full syllabus and an updated skill to make
  this a standing workflow rather than a one-off. Built and verified: a 76-chapter LaTeX
  skeleton across all 9 parts (compiles cleanly with pdflatex/latexmk, confirmed by an actual
  build), custom box environments matching the teaching skill's flag system, a fully-written
  preface, and the book-writing workflow now documented in SKILL.md. Setup is now complete on
  all three fronts Aksan asked for (syllabus, skill, book). Phase 0 diagnostic answers are still
  the one open item before real teaching — everything since the diagnostic was sent has been
  scoping and infrastructure, not yet a taught session.
- **Same session, continued further still**: Aksan created a real GitHub repo (public,
  confirmed reachable) at `github.com/aksaN000/The-study-university-miss-to-teach` for
  chapter-wise exercises, part-wise assignments, and part-wise exams. Cloned it to check state
  (was genuinely empty, not just newly created — worth him double-checking his push actually
  went through, since the pasted commands implied it had). Built the full skeleton: 76 exercise
  placeholders, 9 assignment placeholders, 9 exam placeholders, three format-defining
  TEMPLATE.md files, and a real README — same numbering as the book, generated from the same
  syllabus data so nothing can drift out of sync. No content written yet, same "only after a
  fully completed session" gate as the book. Cannot push directly (no credentials in the
  sandbox, and wouldn't want to route around Aksan's own auth even if it were technically
  possible) — handed over as a zip for him to push himself. Phase 0 diagnostic answers remain
  the single open item before any real teaching or real content begins anywhere.
- **Same session, one more round**: Aksan flagged that examples so far leaned on Python/C/Node
  and asked for genuine multi-language coverage so he can switch languages any time, not a
  Python-only education. Real design decision, not a token addition — see "Multi-Language
  Coverage" in SKILL.md for the full reasoning. Concretely: Phase 3 renamed to "Language
  Environments and Packaging," kept Python as the deep anchor (his real machine, real mess),
  added a closing comparison chapter mapping every Python-specific concept onto npm/Cargo/
  Maven/Go modules. Phase 6 got an equivalent closing comparison chapter for CI/build tooling.
  Phase 0/1 stay language-agnostic as designed, with an explicit standing rule that worked
  examples rotate across languages rather than defaulting to Python. Book regenerated (78
  chapters now, up from 76) and recompiled clean — 130 pages, zero overfull/underfull warnings.
  Practice repo skeleton regenerated to match. Everything renumbers automatically from one
  syllabus source (`book/generate_stubs.py`); nothing hand-maintained in two places. Still
  nothing but the Phase 0 diagnostic standing between all of this and real content.
- **Same session, one more round still**: Aksan extended the same request to operating systems
  — "all os systems," not just Windows and Linux. Real, honest constraint this time that didn't
  apply to languages: he has no Mac and there's no legal way to virtualize macOS on his hardware,
  so unlike the language capstones, this can't be hands-on the same way. Handled it directly
  rather than glossing over it — see "Multi-OS Coverage" in SKILL.md. Windows and Linux/WSL2 stay
  the two hands-on OSes; macOS gets a real comparative chapter (closing Phase 1: "A third machine
  — where macOS agrees with Linux, and where it quietly doesn't," covering BSD-vs-GNU tooling,
  Homebrew, launchd, APFS) without pretending hands-on sessions are possible without hardware.
  Noted one genuine exception worth using later: GitHub Actions' free macOS runners give a real
  hands-on touchpoint when Phase 6 (CI) arrives. Did not add a general OS-history survey chapter
  — that belongs in Chapter 1's own history box, not a separate chapter, same reasoning as
  declining literal all-languages coverage earlier. Book now 79 chapters, recompiled clean (132
  pages, zero warnings). Practice repo regenerated to match. Still nothing but the Phase 0
  diagnostic standing between all of this and real content.
- **Same session, final round**: Aksan asked for a visually distinctive book, no em dashes,
  colon-style headings, and chapter design adaptive to content rather than a fixed template.
  This was a genuine rebuild, not a patch. New typography (Lora, bundled locally in
  `book/fonts/` since it's OFL-licensed, loaded by explicit path after discovering and fixing
  a real xdvipdfmx variable-font embedding bug), new page geometry with a sidenote margin
  column, three-color palette replacing the old five-box system, and XeLaTeX replacing
  pdflatex as the build engine. Removed the rigid mandatory six-box chapter template entirely;
  replaced with an adaptive toolkit (colon headings via `\theading`, sidenotes, optional
  epigraphs, terminal blocks, a lighter breakage callout, booktabs comparison tables, FAQ
  boxes) that chapters use only as their actual content calls for. Rewrote the preface from
  scratch: zero em dashes, and its own claims updated to match ("no two chapters look quite
  alike" instead of the old fixed-shape description). Swept the entire book directory and the
  practice repo for em dashes and removed all of them; in the process found and fixed a real
  bug from earlier regeneration passes that had deleted two of the practice repo's TEMPLATE.md
  files. Added `book/frontmatter/design-reference.tex`, clearly marked as not a real chapter,
  demonstrating every toolkit element with placeholder content so the design could be verified
  visually without inventing content for any of the 79 real chapters. SKILL.md's old
  box-by-name chapter-structure description (referencing boxes that no longer exist) is fixed
  to point at this adaptive system instead, so it doesn't silently drift back. Compiles clean
  with `latexmk -xelatex`, 97 pages, overfull-hbox warnings down to sub-9pt (one TOC entry
  fixed outright by setting the contents listing in `\small`). Practice repo regenerated to
  match. Still nothing but the Phase 0 diagnostic standing between all of this and real
  content, and it is genuinely the only thing left now.
- **2026-10-07, design review (no teaching yet)**: Aksan, while learning React, brought a
  four-module proposal from another agent (terminal anatomy, compilers vs. interpreters vs.
  JIT, shell environment and scripted CLIs, dependency topography). Audit result: Module A
  partly covered (PATH, env vars, process creation existed; terminal-vs-shell split and the
  binary/engine/script classification did not), Module B entirely missing as chapters (it had
  only come up as a scoping tangent), Module C partly covered (dotfiles, argv conventions, the
  `--` separator, npm config validation, and script launchers missing), Module D thin (npm had
  one comparison chapter). Corrected the proposal where it was wrong or dated: shell and
  terminal emulator are peer processes joined by a kernel pty, not a stack; Windows has no
  fork; "line-by-line with an AST" conflates two different interpreter designs; V8 has four
  tiers (Sparkplug 2021, Maglev 2023), not two; `--` is the POSIX end-of-options convention,
  not an npm feature; npm 12 is already out and errors on some unknown configs. Restructure:
  new Part III "From Source Code to Running Process" (11 ch.) placed right after the command
  line because it needs the shell and WSL's gcc, and Part VI's wheel/ABI chapters need it; new
  Part VII "JavaScript and Node Tooling" (10 ch.); four chapters added to Part II; a general
  package-manager opener for Part VI. Also fixed a dependency bug the review exposed: networking
  (ports, localhost, HTTP) was taught after Jupyter and Docker even though both depend on it,
  and Vite's dev server now does too, so networking essentials moved up to Part V and the
  deployment/logs/debugging chapters split into their own late Part XI. Now 103 chapters, 12
  parts, 126 pages, compiles clean. Practice repo skeleton regenerated; its generator and
  templates now live inside this skill under `tools/` so they can't be lost again. The GitHub
  practice repo did not clone anonymously on this date (private now, or never pushed).
- **2026-10-07, infrastructure**: Aksan asked Claude to take over all tracking and GitHub
  management, and offered credentials (declined: Claude never uses pasted credentials). He
  needs GitHub because the book and the full repo will be published publicly, and wants to
  learn while travelling without his home PC. Verified Claude Code on the web runs in Anthropic's
  cloud from browser or mobile and authorizes GitHub through the official app. Consolidated
  everything into one repo: skill under `.claude/skills/`, `CLAUDE.md`, `tracking/`, `book/`
  (PDF built by CI, not committed), `practice/`, `notes/`, `tools/`, and a build-and-release
  workflow. Also decided: no Part VI/VII swap. The project stays in its design phase, fed by
  questions from whatever Aksan is exploring (Python, React, others), until the design covers
  what a complete CS engineer and researcher needs; only then does teaching begin, starting
  with the Phase 0 diagnostic. Proposed next design step: a systematic coverage audit against
  ACM/IEEE CS2023 knowledge areas and his BRAC course list.
- **2026-10-07, design process (no teaching yet)**: Aksan set up the machinery for ending the
  design phase deliberately. Added `tracking/design-inbox.md` (confusions from other work, each
  triaged as covered, fold into an existing chapter, or new chapter placed by dependency; the
  React four-module review is recorded there retroactively as the first triaged item). Recorded
  the Design Freeze Criteria above: audit complete, inbox has no untriaged items, Aksan signs
  off. Started `tracking/coverage-audit.md` against the 17 CS2023 knowledge areas; it is
  provisional because the course list on record is partial and partly self-reported. It raised
  six open questions for Aksan (databases in practice, practical concurrency and distributed
  basics, secrets and service security, licensing, profiling, HCI). **Not done**: saving his
  founding brief as `tracking/project-brief.md`, because the brief and his course list were
  referenced in his message but not included; nothing was reconstructed from memory. Next: Aksan
  pastes the brief verbatim and his full course list, then the audit's pending rows get closed.
- **2026-10-07, coverage audit pass 2**: Aksan gave his full course list (recorded under
  "Degree Course List"). Every CS2023 area in `tracking/coverage-audit.md` is now labelled.
  Degree covers AL, MSF, SDF and GIT outright; AR, AI, FPL, NC, OS, SE and web-SPD split
  between degree theory and project practice; SF is the project's own. No security, parallel/
  distributed, HCI, or ethics course exists, so SEC, PDC, HCI and SEP are open. Seven open
  questions now await Aksan's decisions (databases in practice, practical concurrency and
  distributed basics, secrets and service security, licensing, profiling, HCI, PL theory),
  plus confirming whether any MAT courses were taken. Added five cross-course connections
  (CSE331, CSE260, CSE330, CSE370, MERN). Founding brief still not received; `project-brief.md`
  still not created. Next: brief pasted verbatim, then decisions on the open questions.
- **2026-10-07, branch convention**: the two commits above were first pushed to a
  session-assigned branch (`claude/brave-feynman-eeu2b0`). Aksan asked for all work to go to
  `main`; new branches only when he asks. Main fast-forwarded to include them, and the
  convention is now in SKILL.md under "Home of Everything".
