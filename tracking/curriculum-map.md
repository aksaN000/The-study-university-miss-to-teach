# Curriculum Map — Systems & Developer Tooling, From Zero

This file is the persistent memory for a project with no fixed end date. Read it at the start of
every session. Update it at the end of every session — the status table, the relevant checklist, and
the session log at minimum. Do not rely on conversation recall alone to know where things stand.

---

## Phase Status

Generated from `book/generate_stubs.py` (the single syllabus source). Phase N = Part N+1.

| Phase | Part | Topic | Status |
|---|---|---|---|
| 0 | I | Mental Foundations (9 ch.) | 🔄 Diagnostic answered (2026-10-07); ch01 next |
| 1 | II | The Command Line (31 ch.) | ⏳ Not started |
| 2 | III | From Source Code to Running Process (16 ch.) | ⏳ Not started |
| 3 | IV | Version Control, Properly (10 ch.) | ⏳ Not started |
| 4 | V | Networking Essentials (9 ch.) | ⏳ Not started |
| 5 | VI | Python Environments and Packaging (12 ch.) | ⏳ Not started |
| 6 | VII | JavaScript and Node Tooling (14 ch.) | ⏳ Not started |
| 7 | VIII | APIs: How Applications Talk (9 ch.) | ⏳ Not started |
| 8 | IX | Under the Hood: How Languages, Libraries, and Frameworks Are Built (13 ch.) | ⏳ Not started |
| 9 | X | Databases in Practice (10 ch.) | ⏳ Not started |
| 10 | XI | Security in Practice (6 ch.) | ⏳ Not started |
| 11 | XII | Concurrency and Distributed Systems in Practice (6 ch.) | ⏳ Not started |
| 12 | XIII | Jupyter and the Notebook Stack (6 ch.) | ⏳ Not started |
| 13 | XIV | Containers (6 ch.) | ⏳ Not started |
| 14 | XV | Automation and Build Tooling (10 ch.) | ⏳ Not started |
| 15 | XVI | Deployment and Operations (17 ch.) | ⏳ Not started |
| 16 | XVII | Machine Learning Infrastructure (12 ch.) | ⏳ Not started |
| 17 | XVIII | Capstone: From Source to Production (2 ch.) | ⏳ Not started |

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
- [ ] ch14 Getting help: man, --help, tldr, and reading documentation properly
- [ ] ch15 Links: symbolic, hard, and Windows junctions
- [ ] ch16 Standard input, output, and error
- [ ] ch17 Pipes and redirection
- [ ] ch18 Exit codes: how a program reports back
- [ ] ch19 Signals and job control: Ctrl+C, kill, and foreground vs. background
- [ ] ch20 Globbing and quoting
- [ ] ch21 Regular expressions: the other pattern language
- [ ] ch22 Structured text: JSON, YAML, TOML, and their traps
- [ ] ch23 Text and JSON at the command line: grep, sed, awk, and jq
- [ ] ch24 Anatomy of a command line: argv, flags, options, and the double dash
- [ ] ch25 PATH: how a name becomes a program
- [ ] ch26 Environment variables in practice
- [ ] ch27 Session versus persistent configuration: dotfiles, profiles, and the registry
- [ ] ch28 Virtual machines and hypervisors: what WSL2 actually is
- [ ] ch29 Installing WSL2
- [ ] ch30 Doing it all again in Ubuntu
- [ ] ch31 apt, the Linux filesystem hierarchy, and sudo
- [ ] ch32 Disks, partitions, and mounts: where storage actually lives
- [ ] ch33 Archives and compression: tar, zip, and gzip
- [ ] ch34 Hashes in practice: checksums, content addressing, and verifying downloads
- [ ] ch35 SSH
- [ ] ch36 Long jobs over SSH: tmux, nohup, and surviving a dropped connection
- [ ] ch37 Moving files and ports over SSH: scp, rsync, sshfs, and port forwarding
- [ ] ch38 Writing real shell scripts
- [ ] ch39 Living comfortably in the terminal
- [ ] ch40 A third machine: where macOS agrees with Linux, and where it quietly doesn't

### Phase 2: From Source Code to Running Process (Part III)
- [ ] ch41 Three kinds of things on PATH: native binaries, language engines, and scripted tools
- [ ] ch42 Executable files: ELF, PE, Mach-O, magic numbers, and shebangs
- [ ] ch43 The C pipeline: preprocess, compile, assemble, link
- [ ] ch44 What the CPU actually executes: instructions, registers, and the stack
- [ ] ch45 Linking and loading: static, dynamic, and the loader that runs first
- [ ] ch46 ABIs: why a binary built here refuses to run there
- [ ] ch47 Interpreters, honestly: line by line, tree walking, and bytecode
- [ ] ch48 Inside CPython: from source to .pyc to the evaluation loop
- [ ] ch49 Bytecode virtual machines: the JVM and .NET
- [ ] ch50 JIT compilation through V8: Ignition, Sparkplug, Maglev, TurboFan
- [ ] ch51 Node.js: a JavaScript engine plus an operating system API
- [ ] ch52 WebAssembly: one portable target for many languages
- [ ] ch53 Memory in practice: garbage collectors, leaks, and sanitizers
- [ ] ch54 Debuggers: breakpoints, stepping, and reading a stack trace
- [ ] ch55 Scripted CLIs: shebangs, launcher shims, and why python -m pip exists
- [ ] ch56 Designing command-line tools for humans: help text, errors, and conventions

### Phase 3: Version Control, Properly (Part IV)
- [ ] ch57 The object model: blobs, trees, and commits
- [ ] ch58 Refs, and what a branch actually is
- [ ] ch59 HEAD
- [ ] ch60 Merge vs. rebase, and when each is correct
- [ ] ch61 Resolving conflicts without panic
- [ ] ch62 .gitignore: what belongs in a repo
- [ ] ch63 Remotes, pull requests, and code review
- [ ] ch64 Large files and many repositories: Git LFS, submodules, and monorepos
- [ ] ch65 Recovering from disasters with reflog
- [ ] ch66 Reading someone else's history

### Phase 4: Networking Essentials (Part V)
- [ ] ch67 Ports and sockets: how a process gets a network address
- [ ] ch68 localhost, loopback, and private vs. public addresses
- [ ] ch69 DNS: from a name to an address
- [ ] ch70 TCP and UDP in practice: connections, handshakes, refusals, and timeouts
- [ ] ch71 HTTP: the anatomy of a request and a response
- [ ] ch72 TLS and certificates
- [ ] ch73 SSH keys
- [ ] ch74 What a server actually is
- [ ] ch75 Network tools as instruments: curl, dig, ss, ping, and traceroute

### Phase 5: Python Environments and Packaging (Part VI)
- [ ] ch76 What a package manager actually automates
- [ ] ch77 How the interpreter finds code: sys.path and site-packages
- [ ] ch78 Why global installs cause problems: a tour of our own machine
- [ ] ch79 venv: what it actually does, mechanically
- [ ] ch80 pip, PyPI, sdists, and wheels
- [ ] ch81 Why compiled packages make Python versions matter
- [ ] ch82 Semantic versioning: what a version number promises
- [ ] ch83 requirements.txt, lockfiles, and pyproject.toml
- [ ] ch84 conda: what problem it solved that pip could not
- [ ] ch85 Modern tooling: uv and poetry
- [ ] ch86 The editor is a client too: VS Code, language servers, and which interpreter it chose
- [ ] ch87 Packaging and publishing something of our own

### Phase 6: JavaScript and Node Tooling (Part VII)
- [ ] ch88 npm, global installs, and project scope
- [ ] ch89 package.json and semver ranges: declaring what we need
- [ ] ch90 node_modules: nested, flattened, hoisted, and linked
- [ ] ch91 Lockfiles and npm ci: making installs repeatable
- [ ] ch92 npm configuration: .npmrc, npm_config variables, and stricter validation
- [ ] ch93 npx, npm create, and scaffolding CLIs
- [ ] ch94 CommonJS and ES modules: two module systems in one ecosystem
- [ ] ch95 Transpilers, bundlers, and dev servers: what Vite does with our React code
- [ ] ch96 From dev server to production build: what npm run build actually produces
- [ ] ch97 TypeScript: a type system added to JavaScript, then erased before it runs
- [ ] ch98 Accessibility in practice: what the browser exposes, and how we test it
- [ ] ch99 Supply-chain security: every dependency is code we chose to run
- [ ] ch100 Software licenses: what we may use, and what we owe when we publish
- [ ] ch101 Packaging elsewhere: Cargo, Maven, Go modules, and what every ecosystem shares

### Phase 7: APIs: How Applications Talk (Part VIII)
- [ ] ch102 What the browser does with a URL: DevTools as our instrument
- [ ] ch103 APIs over HTTP: endpoints, REST, and JSON
- [ ] ch104 API conventions: status codes, idempotency, pagination, rate limits, and versioning
- [ ] ch105 Authentication vs. authorization
- [ ] ch106 Cookies and sessions: state on a stateless protocol
- [ ] ch107 Tokens and JWT: authentication without server-side sessions
- [ ] ch108 The same-origin policy and CORS: why the browser blocked our request
- [ ] ch109 Webhooks: when the server calls us
- [ ] ch110 Beyond request and response: streaming, WebSockets, and gRPC

### Phase 8: Under the Hood: How Languages, Libraries, and Frameworks Are Built (Part IX)
- [ ] ch111 Language, runtime, standard library: three things we call "Python"
- [ ] ch112 How a language evolves: PEPs, TC39, versions, and deprecations
- [ ] ch113 Building a tiny language, part one: from text to a syntax tree
- [ ] ch114 Building a tiny language, part two: a tree-walking interpreter
- [ ] ch115 Building a tiny language, part three: bytecode and a small virtual machine
- [ ] ch116 What a library really is: public API, internals, and reading the source of one we use
- [ ] ch117 Foreign function interfaces: how Python and JavaScript call C
- [ ] ch118 Library vs. framework: inversion of control, or why the framework calls us
- [ ] ch119 Building a tiny web framework: routing, middleware, and the request object
- [ ] ch120 Functional ideas in everyday tools: immutability and pure functions in Git, React, and builds
- [ ] ch121 Building a tiny React: components, the virtual DOM, and reconciliation
- [ ] ch122 Building a tiny autograd: how PyTorch computes gradients
- [ ] ch123 Plugins and extension points: how tools let us add our own code

### Phase 9: Databases in Practice (Part X)
- [ ] ch124 A database is a server: processes, ports, and connection strings
- [ ] ch125 SQLite: the database that is just a file
- [ ] ch126 SQL at the prompt: psql, sqlite3, and the queries we actually write
- [ ] ch127 Drivers and connection pools: why connections are expensive
- [ ] ch128 Migrations: schema changes as version-controlled code
- [ ] ch129 ORMs vs. raw SQL: what the abstraction hides
- [ ] ch130 Indexes and EXPLAIN: reading what the planner actually did
- [ ] ch131 Transactions and isolation levels in practice: anomalies we can reproduce
- [ ] ch132 Caching and Redis: a second store, and what it costs in consistency
- [ ] ch133 Backups and restores: a backup never restored is only a hope

### Phase 10: Security in Practice (Part XI)
- [ ] ch134 Secrets: environment files, .env, and keeping keys out of Git
- [ ] ch135 When a secret leaks: Git history, rotation, and scanning
- [ ] ch136 Passwords: hashing, salts, and why we never store them
- [ ] ch137 Injection: SQL, shell commands, and the general shape of the bug
- [ ] ch138 XSS and CSRF: attacks that live in the browser
- [ ] ch139 Least privilege: narrow users, narrow permissions, narrow tokens

### Phase 11: Concurrency and Distributed Systems in Practice (Part XII)
- [ ] ch140 Concurrency in practice: threads, processes, and async I/O
- [ ] ch141 Python's GIL and the free-threaded build: what actually runs in parallel
- [ ] ch142 Race conditions and deadlocks we can reproduce: locks, and letting the database be the lock
- [ ] ch143 Queues and background workers: work that should not happen inside the request
- [ ] ch144 More than one machine: partial failure, timeouts, and retries
- [ ] ch145 Replication and consistency in practice: what eventually consistent actually means

### Phase 12: Jupyter and the Notebook Stack (Part XIII)
- [ ] ch146 The frontend/kernel split, and why it exists
- [ ] ch147 The kernel protocol
- [ ] ch148 Kernel specs: where they live, how discovery works
- [ ] ch149 Why notebooks break in ways scripts do not
- [ ] ch150 Notebooks and version control
- [ ] ch151 When a notebook is the wrong tool

### Phase 13: Containers (Part XIV)
- [ ] ch152 The isolation idea, generalized from environments to the whole OS
- [ ] ch153 Namespaces and cgroups: why a container is not a virtual machine
- [ ] ch154 Images, layers, and Dockerfiles
- [ ] ch155 Volumes, ports, and networking
- [ ] ch156 docker-compose
- [ ] ch157 GPU containers

### Phase 14: Automation and Build Tooling (Part XV)
- [ ] ch158 Makefiles
- [ ] ch159 GitHub Actions and CI/CD
- [ ] ch160 Automated testing: what a test proves, from unit to end-to-end
- [ ] ch161 Pre-commit hooks
- [ ] ch162 Linters and formatters
- [ ] ch163 Type checkers: mypy, pyright, and tsc, and what they actually prove
- [ ] ch164 AI coding assistants as tools: what they run, what they see, and how we review them
- [ ] ch165 Reproducible builds
- [ ] ch166 Documents as code: Markdown, LaTeX, and BibTeX
- [ ] ch167 The same pipeline, five languages: CI beyond Python

### Phase 15: Deployment and Operations (Part XVI)
- [ ] ch168 Deploying something small to a real machine
- [ ] ch169 The cloud is someone else's computer: VMs, object storage, and paying by the hour
- [ ] ch170 Keeping a process alive: systemd, restart policies, and graceful shutdown
- [ ] ch171 Scheduled work and time: cron, systemd timers, UTC, and time zones
- [ ] ch172 Application servers: WSGI, ASGI, and what actually serves our code
- [ ] ch173 Reverse proxies: one public port, many services
- [ ] ch174 From a domain name to HTTPS on our own server
- [ ] ch175 HTTP caching and CDNs: the copies between us and our users
- [ ] ch176 Reading logs
- [ ] ch177 Inspecting a running process: ps, top, lsof, ss, and strace
- [ ] ch178 Resource limits and the OOM killer: when the operating system ends our process
- [ ] ch179 Debugging a process that will not start
- [ ] ch180 Profiling: finding out why it is slow
- [ ] ch181 Health checks, monitoring, and observability
- [ ] ch182 Deployment strategies and rollback: shipping without fear
- [ ] ch183 Infrastructure as code: describing machines instead of clicking
- [ ] ch184 Orchestration: what Kubernetes is for, and when we do not need it

### Phase 16: Machine Learning Infrastructure (Part XVII)
- [ ] ch185 CUDA and driver versions
- [ ] ch186 More than one GPU: data parallelism and NCCL in practice
- [ ] ch187 Shared GPU machines: Slurm and job schedulers
- [ ] ch188 Data versioning with DVC
- [ ] ch189 Data formats for data: CSV, Parquet, Arrow, and why loading is slow
- [ ] ch190 Model weights and the Hugging Face cache: where models actually live
- [ ] ch191 Experiment tracking: MLflow and W&B
- [ ] ch192 Configuration management
- [ ] ch193 Serving a model
- [ ] ch194 Running models locally: llama.cpp, Ollama, and quantization
- [ ] ch195 Serving large language models: batching, the KV cache, and vLLM
- [ ] ch196 Why almost every ML project fails to be reproducible

### Phase 17: Capstone: From Source to Production (Part XVIII)
- [ ] ch197 One application through every layer
- [ ] ch198 Breaking it on purpose, one layer at a time
### Cross-Cutting — Professional Habits (reinforce throughout, not a single session)
- [ ] Reading documentation and source instead of guessing
- [ ] Reading error messages carefully and completely
- [ ] Writing a README a stranger can follow
- [ ] Debugging methodically instead of by trial and error
- [ ] Knowing when to ask, and how to ask well

---

## Chapter Plan Notes

Agreed content for chapters not yet taught, so design decisions survive until the session that
needs them. Refer to chapters by title. Check this list when preparing any session.

- **TLS and certificates**: a distinction table (encryption vs. authentication vs. integrity vs.
  trust: what each protects, and what TLS gives us of each); the security part refers back to it.
- **Race conditions and deadlocks we can reproduce**: include a deadlock we cause and diagnose,
  not just a race.
- **Automated testing**: what a test proves; unit vs. integration vs. end-to-end, with the cost
  and confidence of each.
- **HTTP: the anatomy of a request and a response**: method, URL, headers, body; status, headers,
  body; seen raw with `curl -v` before any framework.
- **What the CPU actually executes**: disassemble our own compiled C (`objdump -d`), step it in
  `gdb` to watch registers and the stack, x86-64 vs. ARM64, user vs. kernel mode; feeds the ABI
  chapter and multi-architecture images.
- **Concurrency part, scope guard**: practical mental models only (why production systems behave
  strangely), never a distributed-systems course.
- **Software licenses**: include the licensing of this book and its repository.
- **localhost, loopback, and private vs. public addresses**: NAT, why a friend cannot reach our
  localhost server, tunnels (ngrok-style), VPNs, and IPv6 alongside IPv4.
- **apt, the Linux filesystem hierarchy, and sudo**: Windows package managers too (winget,
  Chocolatey), so the idea is cross-OS.
- **Remotes, pull requests, and code review**: signed commits (SSH or GPG signing).
- **Reading someone else's history**: `git bisect` as debugging through history.
- **Semantic versioning**: Git tags and releases.
- **Makefiles**: CMake, since compiled Python and C++ packages build with it.
- **Deploying something small to a real machine**: a host firewall (ufw).
- **Reading logs**: writing structured logs from our own code.
- **Profiling**: benchmarking honestly (warm-up, variance, what to measure).
- **CUDA and driver versions**: floating-point formats (fp32, fp16, bf16) and why results differ
  across hardware; a CSE330 refresher.
- **Why almost every ML project fails to be reproducible**: random seeds and the limits of
  determinism; pinning the whole stack (Python, wheels, CUDA runtime, driver) as one unit.
- **venv: what it actually does, mechanically**: a breakage where the same import works in the
  terminal and fails elsewhere; revisited in the scheduled-work chapter (cron runs a different
  Python), the systemd chapter (a service's environment), and kernel specs (a kernel pointing at
  the wrong interpreter). Each time: which binary did exec actually launch, and what is its
  sys.path?
- **CUDA and driver versions**: the three CUDAs that collide: the kernel driver, the `nvcc`
  toolkit, and the CUDA runtime bundled inside the PyTorch wheel in our venv; why `nvidia-smi`'s
  "CUDA Version" is not the one our code uses; how to ask the running process which it loaded.
- **Model weights and the Hugging Face cache**: disk space (`du`, cache pruning) when one model is
  30 GB, and moving the cache to another disk.
- **The frontend/kernel split**: a remote kernel on a GPU machine reached through an SSH tunnel
  (builds on "Moving files and ports over SSH").
- **Reverse proxies**: serving the static output of a production frontend build, including the
  single-page-app fallback route; links back to "From dev server to production build".
- **Deploying something small to a real machine**: dev vs. production parity (what differs, and
  why "it works with npm run dev" is not a deployment).
- **Containers, Volumes, ports, and networking**: a container memory limit that triggers the OOM
  killer, diagnosed with `dmesg` (builds on the OOM killer chapter's ideas; whichever is taught
  first introduces it).

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
| 2 | clig.dev (Command Line Interface Guidelines) for CLI design; CS:APP ch. 7 (Linking) and ch. 8 (Exceptional Control Flow: fork/exec); `man 5 elf`, `man 8 ld.so`; *Crafting Interpreters* (Nystrom, free at craftinginterpreters.com) for tree-walking vs. bytecode; the CPython devguide's compiler/interpreter internals; v8.dev blog posts on Ignition, Sparkplug, Maglev; nodejs.org "The Node.js Event Loop" guide |
| 3 | *Pro Git* (Chacon & Straub), especially Git Internals; Missing Semester: Version Control; Learn Git Branching |
| 4 | Julia Evans' networking zines; MDN "An overview of HTTP"; Missing Semester: Security & Cryptography for the TLS/SSH trust model |
| 5 | semver.org; the Python Packaging User Guide (packaging.python.org) and the relevant PEPs (427 wheels, 517/518 build systems, 621 pyproject metadata, 668 externally managed environments) |
| 6 | docs.npmjs.com (package.json, npmrc, config, scripts, folders); nodejs.org module docs (CommonJS vs. ESM); vite.dev guide ("Why Vite"); pnpm.io "Motivation"; TypeScript handbook; MDN Accessibility and WAI-ARIA; choosealicense.com and SPDX |
| 7 | MDN: HTTP, Cookies, CORS; RFC 7519 (JWT) read alongside the OWASP cheat sheets on sessions and JWT |
| 8 | *Crafting Interpreters* (Nystrom) for the tiny language; PEP 1 and the TC39 process document; the Python C API and ctypes docs, pybind11, Node-API; PEP 3333 (WSGI); Rodrigo Pombo, "Build your own React"; Karpathy's micrograd |
| 9 | PostgreSQL documentation (Server Administration; Using EXPLAIN; Transaction Isolation); use-the-index-luke.com; Kleppmann, *Designing Data-Intensive Applications*, ch. 7 |
| 10 | OWASP Top 10 and the OWASP Cheat Sheet Series; Missing Semester: Security & Cryptography |
| 11 | Python docs: `threading`, `multiprocessing`, `asyncio`, PEP 703 (free-threaded CPython); Kleppmann, *Designing Data-Intensive Applications*, ch. 5, 8, 9 |
| 12 | Jupyter client docs: the kernel messaging protocol |
| 13 | Docker's official documentation; docker-curriculum.com; `man 7 namespaces`, `man 7 cgroups` |
| 14 | Missing Semester: Metaprogramming (build systems, CI, dependency management); GitHub Actions docs; mypy and TypeScript handbooks |
| 15 | Missing Semester: Debugging and Profiling; `journalctl`/`systemd` man pages; Brendan Gregg's Linux performance pages |
| 16 | Full Stack Deep Learning (fullstackdeeplearning.com) |
| 17 | Every source above; the capstone has no single text |
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
- **Mathematics and science**: MAT110 Math I (Differential Calculus and Co-ordinate Geometry),
  MAT120 Math II (Integral Calculus and Differential Equations), MAT215 Math III (Complex
  Variables and Laplace Transformations), MAT216 Math IV (Linear Algebra and Fourier Analysis),
  STA201 Elements of Statistics and Probability, PHY111 and PHY112 Principles of Physics I and
  II, CHE101, BIO101
- **Humanities and general education**: ENG101 English Fundamentals, ENG102 English Composition
  I, HUM103 Ethics and Culture, HUM101, BNG103 Bangla Language and Literature, EMB101/DEV101
  Emergence of Bangladesh / Bangladesh Studies, CST301 For the Love of Food
- **Not on the list**: any security, parallel/distributed systems, or HCI course. These shape
  the coverage audit's open questions. HUM103 is the only ethics course and is general rather
  than computing-specific.

Courses taken are not the same as material that landed, or material that stayed. Aksan's own
calibration (2026-10-07): CGPA 3.73, roughly 85 to 89 percent in every course; he knows the
concepts but has not mastered them and does not always remember what he studied. So before
building on any course concept: a short refresher first, then one light check question.
Never skip the refresher on the strength of a course code.

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
| Building a tiny language (lexer, parser, interpreter, bytecode VM) | CSE420 Compiler Design, now built end to end and run |
| Building a tiny autograd | CSE425 Neural Networks and CSE427 ML: backpropagation as code we write |
| Foreign function interfaces | CSE340 calling conventions and the ABI chapter |
| Building a tiny web framework and a tiny React | CSE470 design patterns (inversion of control), MERN apps already built |
| Globbing vs. regular expressions (two different pattern languages) | Regular languages and finite automata, CSE331 |
| Bits on disk, character encodings, two's complement in file formats | Digital Logic Design, CSE260 |
| Floating-point surprises across machines and GPU reproducibility | Numerical Methods, CSE330 |
| Running a database server, connection strings, migrations | Database Systems, CSE370 (theory side) |
| npm, Vite, and the React toolchain | Web development (MERN): the apps were built; the tooling under them was not taught |

---

## Design Freeze Criteria (2026-10-07)

The project is in its design phase. Teaching (starting with the Phase 0 diagnostic) begins only
once the design freezes, and it freezes only when all three hold at the same time:

- [x] **The coverage audit is complete** (2026-10-07): every CS2023 knowledge area in
  `tracking/coverage-audit.md` is labelled degree, project, or out of scope with a reason; no
  row is pending; every open question the audit raised is decided.
- [x] **The design inbox is empty of untriaged items** (as of 2026-10-07; reopens whenever a new item arrives): every entry in
  `tracking/design-inbox.md` has a verdict (covered, fold in, new chapter).
- [x] **Aksan signs off**, explicitly, in a session, recorded in the session log with the date.
  Signed off 2026-10-07 ("design is good enough"). **Design frozen at 198 chapters in 18 parts.**

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
- **2026-10-07, coverage audit pass 3**: Aksan added his maths, science, and general-education
  courses (recorded under "Degree Course List"). MSF is now fully degree-covered (MAT110, MAT120,
  MAT215, MAT216, STA201, STA301, CSE230, CSE330), closing the MAT checkbox. HUM103 Ethics and
  Culture moves SEP's general ethics to the degree; computing-specific professional practice
  (licensing, publishing) stays open question 4. Seven open questions remain.
- **2026-10-07, commit identity**: Aksan asked that every commit show as his and carry no Claude
  attribution. With his explicit go-ahead, `main` was rewritten once and force-pushed: author and
  committer set to `Aksan <92901617+aksaN000@users.noreply.github.com>` (his GitHub no-reply
  address) on every commit, Co-Authored-By and Claude-Session trailers stripped. This also fixed
  the founding commit, whose old address did not link to his account. The session branch
  `claude/brave-feynman-eeu2b0` was deleted from GitHub. Rule added to CLAUDE.md.
- **2026-10-07, external review logged**: Aksan brought a ChatGPT review of the skeleton PDF.
  Logged in `tracking/design-inbox.md` as an untriaged item with twenty proposed verdicts; it
  overlaps the audit's open questions on databases, security and profiling and surfaced one
  real dependency bug (ch65 uses semver, ch91 teaches it 26 chapters later). No syllabus change
  until Aksan decides. Also noted: GitHub still showed two contributors after the history rewrite;
  likely GitHub's contributor cache, and the `book-latest` tag still points at the pre-rewrite
  founding commit.
- **2026-10-07, restructure from the external review**: Aksan set the book's audience to
  computer science enthusiasts who have done the CS courses (the book names course concepts and
  teaches the practical bridge; it never assumes practical fluency), replacing "assume nothing"
  in SKILL.md and the preface. He told Claude to adopt the review suggestions it agreed with
  and reject the rest; full verdicts are in the design inbox's triaged table. Syllabus now 139
  chapters in 16 parts: Part V networking 5 to 9 ch. (ch49 split), Semantic versioning moved
  into Part VI (it was taught 26 chapters after npm first used it), new Part VIII APIs, Part IX
  Databases in Practice, Part X Security in Practice, a namespaces-and-cgroups chapter in
  Containers, Part XIV Deployment 3 to 10 ch., new Part XVI Capstone. Adopted features: part-end
  "Trace it", per-chapter depth tags (both to be built into `boxes.tex` with the first chapter
  that needs them), "How to use this book" in the preface, broken/fixed starting states in the
  exercise template. Book stubs and practice placeholders regenerated (all were still
  placeholders, verified before replacing). Audit open questions 1, 3, 5 closed; 2 (concurrency
  and distributed basics), 4 (licensing), 6 (HCI), 7 (PL theory) still open. Not done: moving
  the `book-latest` tag, which GitHub's connection from this session silently refuses.
- **2026-10-07, audit closed**: Aksan accepted all four remaining audit questions into the
  project, each as its practical face: new Part XI Concurrency and Distributed Systems in
  Practice (6 ch.); a licensing chapter and a functional-ideas chapter in Part VII; HCI as CLI
  design (Part III) and accessibility testing (Part VII); PL theory as TypeScript (Part VII) and
  type checkers (Part XIV). Syllabus now 151 chapters in 17 parts, skeleton regenerated (all
  files verified as placeholders first). He also sharpened the audience rule: studied is not
  mastered, and not always remembered (3.73 CGPA, 85 to 89 percent per course), so both the
  book and live sessions give a short refresher before leaning on any course concept; SKILL.md,
  the preface, and "Degree Course List" updated. Design freeze: audit complete and inbox empty
  are now ticked; only Aksan's sign-off remains. Still outstanding: the founding brief, and the
  `book-latest` tag (needs deleting on GitHub so CI can recreate it).
- **2026-10-07, skill sync**: Aksan asked for a way to save the updated skill to his claude.ai
  account from chat. Rule added to CLAUDE.md: after any SKILL.md change, package it as
  `systems-tooling-tutor.skill` and send it in chat. First copy sent (151-chapter version).
- **2026-10-07, book design rebuild**: Aksan flagged the title page (centered on the text block,
  which sat left of a wide margin column) and asked for a visually stunning, fun, figure-rich
  book. Rebuilt: centered text block with equal margins and sidenotes as styled foot notes;
  full-sheet TikZ title page (a layer stack from hardware to our code) and part pages (with a
  map of all parts, current one lit); new chapter openings; static Lora fonts for real bold;
  quiet contents page; a shared TikZ diagram vocabulary; new boxes (course refresher, back in
  time, mental model, predict first, myth, trace it), drop caps, depth tags, code and
  algorithm listings. Verified by compiling locally and inspecting rendered pages. Rule added to
  SKILL.md: every mechanism gets a figure, and fun is a teaching tool. Also answered: a skill
  saved on claude.ai does not update itself; Aksan re-saves each new `.skill` file sent in chat.
- **2026-10-07, second external review logged**: proposed verdicts in the design inbox (two new
  chapters: CPU, SQL at the prompt; two retitles; three fold-ins; Jupyter stays). Awaiting
  Aksan's decision; design freeze's inbox condition is open again until then.
- **2026-10-07, second review applied**: Aksan said go. New chapters "What the CPU actually
  executes" (Part III, after the C pipeline) and "SQL at the prompt" (Part IX, after SQLite);
  retitled HTTP (request/response anatomy), automated testing (what a test proves, unit to
  end-to-end), and race conditions (now with deadlocks). Fold-ins recorded in the new "Chapter
  Plan Notes" section. Jupyter stays. 153 chapters in 17 parts, skeleton regenerated, compiled
  locally. Design freeze again waits only on Aksan's sign-off.
- **2026-10-07, gap sweep**: Aksan asked whether anything was missed before future exploration
  adds more. Claude's sweep logged in the design inbox: ten candidate chapters (debugger, editor
  and language servers, regex, text/JSON tools, config formats, tmux and long remote jobs,
  scheduling and time, the cloud, AI coding assistants, Slurm) plus fold-ins. Awaiting Aksan.
  Second review applied and skill re-sent (153 chapters).
- **2026-10-07, gap sweep applied and widened**: Aksan: book size does not matter; it is a
  self-improvement book meant to make a CS student complete, so add everything and look for
  more. Claude kept one boundary and recorded it: chapters cover the practical layer; course
  theory gets refresher boxes, not chapters. Added all eleven sweep items plus a second sweep:
  getting help, links, signals and job control, regex, structured text, text/JSON tools, VMs
  and hypervisors, disks and mounts, archives, hashes, tmux; WebAssembly, memory and sanitizers,
  debuggers; Git LFS/submodules/monorepos; editor and language servers; browser DevTools,
  streaming/WebSockets/gRPC; AI coding assistants, documents as code; the cloud, scheduling and
  time, application servers, HTTP caching and CDNs, infrastructure as code, orchestration; multi-GPU,
  Slurm, data formats for data, model weights and the HF cache, local models and quantization,
  LLM serving. Twelve fold-ins in Chapter Plan Notes. 185 chapters in 17 parts, 218 pages,
  compiled locally. Design freeze waits only on Aksan's sign-off.
- **2026-10-07, Under the Hood part**: Aksan asked whether the book should cover how
  programming languages, libraries, and frameworks are built. Yes: new Part IX (after APIs, which
  the web framework needs) with 12 chapters: language vs. runtime vs. standard library; how
  languages evolve (PEPs, TC39); building a tiny language in three chapters (tree, tree-walking
  interpreter, bytecode VM); what a library is; foreign function interfaces; library vs.
  framework; building a tiny web framework, a tiny React, and a tiny autograd; plugins. Part
  pages fixed for long titles and 18 parts. 197 chapters in 18 parts, 231 pages, compiled locally.
- **2026-10-07, Gemini review**: reviewed an older (185-chapter) PDF, so model weights, Git LFS,
  and tmux were already in. Adopted: "Moving files and ports over SSH" (Part II), "From dev server
  to production build" (Part VII), "Resource limits and the OOM killer" (Part XVI); fold-ins for
  the venv-escape breakage, the three-CUDA collision, weights disk space, remote Jupyter through a
  tunnel, static frontend serving, dev/prod parity, and container OOM. Rejected: moving Security
  to right after APIs (its injection chapter needs databases). 200 chapters in 18 parts.
- **2026-10-07, redundancy pass**: Aksan allowed removing anything added unnecessarily. Read
  all 200 titles. Removed "Why works on my machine stops being necessary" (a recap with no new
  mechanism; the isolation chapter and part-end Trace it cover it) and "Reproducible ML
  environments" (overlapped Part VI, the CUDA note, and the ML closing chapter, which absorbs its
  seeds note). Moved "Functional ideas in everyday tools" from Part VII into Part IX, just before
  the tiny React that depends on immutability. 198 chapters in 18 parts.
- **2026-10-07, DESIGN FROZEN**: Aksan signed off ("design is good enough"). All three freeze
  criteria hold: audit complete, inbox empty, sign-off. 198 chapters, 18 parts. From here, new
  confusions still enter through the design inbox, but a new chapter needs Aksan's explicit
  approval. The founding brief: the first request of this session referred to one that was never
  pasted, and Aksan does not recognise the term, so it is dropped; this log and SKILL.md hold the
  project's intent. The `book-latest` tag no longer needs deleting by hand: the build workflow
  now moves the tag to each build's commit before publishing. **Next session: teaching begins
  with the Phase 0 diagnostic** (sent 2026-07-30, never answered; resend it fresh).
- **2026-10-07, Session 2: Phase 0 diagnostic answered (teaching begins)**: the original
  2026-07-30 questions were never saved, so a fresh ten-question diagnostic was sent, one or two
  questions per Phase 0 chapter plus "which shell". Answered from memory. Pattern: the course
  vocabulary is present (syscalls, threads vs. processes, inodes, permission bits), but it is
  not yet connected to the real machine, which is exactly the gap this project assumes. Two
  misses where the theory is on record as known but was not applied: same address in two
  processes called a contradiction (virtual address spaces, CSE321 paging), and no fork/exec
  link to "how a shell runs a program" (fork semantics are listed as solid). Per chapter:
  - ch01 OS role: syscall/kernel boundary right in spirit. Misconception: the OS "sends each
    instruction to the CPU" and scheduling governs how lines run; actually the CPU fetches
    directly and the kernel regains control only via syscalls, interrupts, exceptions. Also
    conflated CPU privilege (cannot touch hardware) with file permissions (not allowed this file).
  - ch02 Processes: process isolation and thread sharing solid. Undercounted VS Code (said 3;
    Electron is many processes, plus the shell, conpty host, language server).
  - ch03 Memory: 3a partial (paging to disk, but framed as whole processes); 3b wrong (see above).
  - ch04 Filesystem: same-volume move = metadata change: solid. Delete marks blocks free: right
    (missed SSD TRIM; Recycle Bin is itself a move). `C:\` and folders as directory files: guess.
  - ch05 Permissions: `-rwxr-xr--` read correctly (missed the leading type char). "Run as
    administrator" misread as setting file bits; process privilege (token) vs. file
    permissions not yet distinguished.
  - ch06 Running a program: believes `train.py` is loaded and executed alongside python and
    interpreted line by line (the July "press Run" blind spot again). fork/exec, CreateProcess
    unknown in practice.
  - ch07 Env vars: no model; `(base)` unknown. Inheritance question guessed correctly.
  - ch08 Paths: relative-to-what unknown (current working directory); thought the terminal
    cannot run `open()`; `.` and `..` reversed/confused and used `.` as a separator.
  - ch09 Encodings: "bytes per character" guessed correctly; CRLF warning and `ï»¿` seen, unknown.
  - Shell: PowerShell by default (5.1 vs. 7 not yet known).
  None of this is ticked; ticks wait for each chapter's recall check. Next: ch01, What does an
  operating system actually do.
- **2026-10-07, same session, method change**: Aksan, concerned by the wrong answers, asked
  whether to re-study all the theory. Answered no: the misses split into untaught practical
  material, theory known but never seen running, and wrong mental pictures; re-reading text
  repeats the original problem. He named the real need himself (he cannot visualize or trace
  the machine the way he traced code in exams). Adopted with his "yes": a trace table before
  every command in mechanism sessions (SKILL.md Step 2b, ladder now 9 steps), carried into
  the book chapters. Targeted reading alongside sessions, not before: OSTEP ch. 4 to 6 (with
  ch01, ch02, ch06) and ch. 13 to 15 (with ch03).
- **2026-10-09, repository housekeeping (no teaching)**: two GitHub fixes Aksan asked for while
  Chapter 1's history check questions were open. (1) A stale "claude" entry in repo sidebars:
  every audited repo's history was already clean (no Claude author, committer, or trailer on
  any ref), so it was GitHub's cached contributors list; switching the default branch away and
  back refreshed it (Aksan confirmed). (2) "Unverified" commits: the Claude Code cloud
  container signs commits with its own SSH key, which is not on his account; only this repo
  had such commits (15 of 21 on main). Signing is now off per session (rule added to
  `CLAUDE.md` and SKILL.md). Stripping the signatures from the existing 15 needs a rewrite of
  main and a force-push: first blocked by the session's safety check, then done on Aksan's
  repeated, explicit instruction (all 22 commit trees, authors, dates, and messages verified
  identical; force-pushed with lease; new head `9620ec7`; CI moves the `book-latest` tag).
  Aksan also asked to git-ignore `CLAUDE.md`, then declined once told a fresh session would
  then commit as Claude, with attribution and signing; `CLAUDE.md` stays tracked. Chapter 1 resumes at the three history check questions.
