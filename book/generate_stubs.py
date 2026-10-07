#!/usr/bin/env python3
"""Generates the full chapter-stub skeleton for the book from the syllabus,
and writes the corresponding \\part / \\input block for main.tex."""

import os
import re

BOOK = os.path.dirname(os.path.abspath(__file__))
CH_DIR = os.path.join(BOOK, "chapters")

# (part_dir_slug, part_title, phase_number, [chapter titles in order])
SYLLABUS = [
    ('part01-foundations', 'Mental Foundations', 0, [
        "What does an operating system actually do",
        "Processes: the unit of a running program",
        "Memory: what is actually there",
        "The filesystem: how storage becomes files and folders",
        "File permissions: who is allowed to do what",
        "Running a program: fork, exec, and CreateProcess",
        "Environment variables: the machine's sticky notes",
        "Paths: absolute, relative, and relative to what",
        "Text encodings and line endings: why files disagree",
    ]),
    ('part02-command-line', 'The Command Line', 1, [
        "Terminal, console, shell: three things we call by one name",
        "What a shell is and why it exists",
        "PowerShell vs. bash/zsh: different languages, not different skins",
        "Navigating, creating, moving, deleting",
        "Getting help: man, --help, tldr, and reading documentation properly",
        "Links: symbolic, hard, and Windows junctions",
        "Standard input, output, and error",
        "Pipes and redirection",
        "Exit codes: how a program reports back",
        "Signals and job control: Ctrl+C, kill, and foreground vs. background",
        "Globbing and quoting",
        "Regular expressions: the other pattern language",
        "Structured text: JSON, YAML, TOML, and their traps",
        "Text and JSON at the command line: grep, sed, awk, and jq",
        "Anatomy of a command line: argv, flags, options, and the double dash",
        "PATH: how a name becomes a program",
        "Environment variables in practice",
        "Session versus persistent configuration: dotfiles, profiles, and the registry",
        "Virtual machines and hypervisors: what WSL2 actually is",
        "Installing WSL2",
        "Doing it all again in Ubuntu",
        "apt, the Linux filesystem hierarchy, and sudo",
        "Disks, partitions, and mounts: where storage actually lives",
        "Archives and compression: tar, zip, and gzip",
        "Hashes in practice: checksums, content addressing, and verifying downloads",
        "SSH",
        "Long jobs over SSH: tmux, nohup, and surviving a dropped connection",
        "Moving files and ports over SSH: scp, rsync, sshfs, and port forwarding",
        "Writing real shell scripts",
        "Living comfortably in the terminal",
        "A third machine: where macOS agrees with Linux, and where it quietly doesn't",
    ]),
    ('part03-source-to-process', 'From Source Code to Running Process', 2, [
        "Three kinds of things on PATH: native binaries, language engines, and scripted tools",
        "Executable files: ELF, PE, Mach-O, magic numbers, and shebangs",
        "The C pipeline: preprocess, compile, assemble, link",
        "What the CPU actually executes: instructions, registers, and the stack",
        "Linking and loading: static, dynamic, and the loader that runs first",
        "ABIs: why a binary built here refuses to run there",
        "Interpreters, honestly: line by line, tree walking, and bytecode",
        "Inside CPython: from source to .pyc to the evaluation loop",
        "Bytecode virtual machines: the JVM and .NET",
        "JIT compilation through V8: Ignition, Sparkplug, Maglev, TurboFan",
        "Node.js: a JavaScript engine plus an operating system API",
        "WebAssembly: one portable target for many languages",
        "Memory in practice: garbage collectors, leaks, and sanitizers",
        "Debuggers: breakpoints, stepping, and reading a stack trace",
        "Scripted CLIs: shebangs, launcher shims, and why python -m pip exists",
        "Designing command-line tools for humans: help text, errors, and conventions",
    ]),
    ('part04-version-control', 'Version Control, Properly', 3, [
        "The object model: blobs, trees, and commits",
        "Refs, and what a branch actually is",
        "HEAD",
        "Merge vs. rebase, and when each is correct",
        "Resolving conflicts without panic",
        ".gitignore: what belongs in a repo",
        "Remotes, pull requests, and code review",
        "Large files and many repositories: Git LFS, submodules, and monorepos",
        "Recovering from disasters with reflog",
        "Reading someone else's history",
    ]),
    ('part05-networking', 'Networking Essentials', 4, [
        "Ports and sockets: how a process gets a network address",
        "localhost, loopback, and private vs. public addresses",
        "DNS: from a name to an address",
        "TCP and UDP in practice: connections, handshakes, refusals, and timeouts",
        "HTTP: the anatomy of a request and a response",
        "TLS and certificates",
        "SSH keys",
        "What a server actually is",
        "Network tools as instruments: curl, dig, ss, ping, and traceroute",
    ]),
    ('part06-python-packaging', 'Python Environments and Packaging', 5, [
        "What a package manager actually automates",
        "How the interpreter finds code: sys.path and site-packages",
        "Why global installs cause problems: a tour of our own machine",
        "venv: what it actually does, mechanically",
        "pip, PyPI, sdists, and wheels",
        "Why compiled packages make Python versions matter",
        "Semantic versioning: what a version number promises",
        "requirements.txt, lockfiles, and pyproject.toml",
        "conda: what problem it solved that pip could not",
        "Modern tooling: uv and poetry",
        "The editor is a client too: VS Code, language servers, and which interpreter it chose",
        "Packaging and publishing something of our own",
    ]),
    ('part07-javascript-tooling', 'JavaScript and Node Tooling', 6, [
        "npm, global installs, and project scope",
        "package.json and semver ranges: declaring what we need",
        "node\\_modules: nested, flattened, hoisted, and linked",
        "Lockfiles and npm ci: making installs repeatable",
        "npm configuration: .npmrc, npm\\_config variables, and stricter validation",
        "npx, npm create, and scaffolding CLIs",
        "CommonJS and ES modules: two module systems in one ecosystem",
        "Transpilers, bundlers, and dev servers: what Vite does with our React code",
        "From dev server to production build: what npm run build actually produces",
        "TypeScript: a type system added to JavaScript, then erased before it runs",
        "Accessibility in practice: what the browser exposes, and how we test it",
        "Supply-chain security: every dependency is code we chose to run",
        "Software licenses: what we may use, and what we owe when we publish",
        "Functional ideas in everyday tools: immutability and pure functions in Git, React, and builds",
        "Packaging elsewhere: Cargo, Maven, Go modules, and what every ecosystem shares",
    ]),
    ('part08-apis', 'APIs: How Applications Talk', 7, [
        "What the browser does with a URL: DevTools as our instrument",
        "APIs over HTTP: endpoints, REST, and JSON",
        "API conventions: status codes, idempotency, pagination, rate limits, and versioning",
        "Authentication vs. authorization",
        "Cookies and sessions: state on a stateless protocol",
        "Tokens and JWT: authentication without server-side sessions",
        "The same-origin policy and CORS: why the browser blocked our request",
        "Webhooks: when the server calls us",
        "Beyond request and response: streaming, WebSockets, and gRPC",
    ]),
    ('part09-under-the-hood', 'Under the Hood: How Languages, Libraries, and Frameworks Are Built', 8, [
        "Language, runtime, standard library: three things we call \"Python\"",
        "How a language evolves: PEPs, TC39, versions, and deprecations",
        "Building a tiny language, part one: from text to a syntax tree",
        "Building a tiny language, part two: a tree-walking interpreter",
        "Building a tiny language, part three: bytecode and a small virtual machine",
        "What a library really is: public API, internals, and reading the source of one we use",
        "Foreign function interfaces: how Python and JavaScript call C",
        "Library vs. framework: inversion of control, or why the framework calls us",
        "Building a tiny web framework: routing, middleware, and the request object",
        "Building a tiny React: components, the virtual DOM, and reconciliation",
        "Building a tiny autograd: how PyTorch computes gradients",
        "Plugins and extension points: how tools let us add our own code",
    ]),
    ('part10-databases', 'Databases in Practice', 9, [
        "A database is a server: processes, ports, and connection strings",
        "SQLite: the database that is just a file",
        "SQL at the prompt: psql, sqlite3, and the queries we actually write",
        "Drivers and connection pools: why connections are expensive",
        "Migrations: schema changes as version-controlled code",
        "ORMs vs. raw SQL: what the abstraction hides",
        "Indexes and EXPLAIN: reading what the planner actually did",
        "Transactions and isolation levels in practice: anomalies we can reproduce",
        "Caching and Redis: a second store, and what it costs in consistency",
        "Backups and restores: a backup never restored is only a hope",
    ]),
    ('part11-security', 'Security in Practice', 10, [
        "Secrets: environment files, .env, and keeping keys out of Git",
        "When a secret leaks: Git history, rotation, and scanning",
        "Passwords: hashing, salts, and why we never store them",
        "Injection: SQL, shell commands, and the general shape of the bug",
        "XSS and CSRF: attacks that live in the browser",
        "Least privilege: narrow users, narrow permissions, narrow tokens",
    ]),
    ('part12-concurrency', 'Concurrency and Distributed Systems in Practice', 11, [
        "Concurrency in practice: threads, processes, and async I/O",
        "Python's GIL and the free-threaded build: what actually runs in parallel",
        "Race conditions and deadlocks we can reproduce: locks, and letting the database be the lock",
        "Queues and background workers: work that should not happen inside the request",
        "More than one machine: partial failure, timeouts, and retries",
        "Replication and consistency in practice: what eventually consistent actually means",
    ]),
    ('part13-jupyter', 'Jupyter and the Notebook Stack', 12, [
        "The frontend/kernel split, and why it exists",
        "The kernel protocol",
        "Kernel specs: where they live, how discovery works",
        "Why notebooks break in ways scripts do not",
        "Notebooks and version control",
        "When a notebook is the wrong tool",
    ]),
    ('part14-containers', 'Containers', 13, [
        "The isolation idea, generalized from environments to the whole OS",
        "Namespaces and cgroups: why a container is not a virtual machine",
        "Images, layers, and Dockerfiles",
        "Volumes, ports, and networking",
        "docker-compose",
        "GPU containers",
        "Why \"works on my machine\" stops being necessary",
    ]),
    ('part15-automation-build', 'Automation and Build Tooling', 14, [
        "Makefiles",
        "GitHub Actions and CI/CD",
        "Automated testing: what a test proves, from unit to end-to-end",
        "Pre-commit hooks",
        "Linters and formatters",
        "Type checkers: mypy, pyright, and tsc, and what they actually prove",
        "AI coding assistants as tools: what they run, what they see, and how we review them",
        "Reproducible builds",
        "Documents as code: Markdown, LaTeX, and BibTeX",
        "The same pipeline, five languages: CI beyond Python",
    ]),
    ('part16-deployment-ops', 'Deployment and Operations', 15, [
        "Deploying something small to a real machine",
        "The cloud is someone else's computer: VMs, object storage, and paying by the hour",
        "Keeping a process alive: systemd, restart policies, and graceful shutdown",
        "Scheduled work and time: cron, systemd timers, UTC, and time zones",
        "Application servers: WSGI, ASGI, and what actually serves our code",
        "Reverse proxies: one public port, many services",
        "From a domain name to HTTPS on our own server",
        "HTTP caching and CDNs: the copies between us and our users",
        "Reading logs",
        "Inspecting a running process: ps, top, lsof, ss, and strace",
        "Resource limits and the OOM killer: when the operating system ends our process",
        "Debugging a process that will not start",
        "Profiling: finding out why it is slow",
        "Health checks, monitoring, and observability",
        "Deployment strategies and rollback: shipping without fear",
        "Infrastructure as code: describing machines instead of clicking",
        "Orchestration: what Kubernetes is for, and when we do not need it",
    ]),
    ('part17-ml-infra', 'Machine Learning Infrastructure', 16, [
        "Reproducible ML environments",
        "CUDA and driver versions",
        "More than one GPU: data parallelism and NCCL in practice",
        "Shared GPU machines: Slurm and job schedulers",
        "Data versioning with DVC",
        "Data formats for data: CSV, Parquet, Arrow, and why loading is slow",
        "Model weights and the Hugging Face cache: where models actually live",
        "Experiment tracking: MLflow and W\\&B",
        "Configuration management",
        "Serving a model",
        "Running models locally: llama.cpp, Ollama, and quantization",
        "Serving large language models: batching, the KV cache, and vLLM",
        "Why almost every ML project fails to be reproducible",
    ]),
    ('part18-capstone', 'Capstone: From Source to Production', 17, [
        "One application through every layer",
        "Breaking it on purpose, one layer at a time",
    ]),
]

STUB_TEMPLATE = r"""%% Chapter {num:02d} -- {title}
%% Part {part_num}: {part_title}  |  Syllabus Phase {phase}
%% STATUS: not yet written -- written only after the matching session is
%% FULLY complete (concept taught, command run and interpreted, breakage
%% exercise done if there was one, recall check passed).
%%
%% ADAPTIVE, NOT FIXED. There is no mandatory section sequence -- decide
%% this chapter's actual shape from what it needs to teach, not from a
%% template. The toolkit (book/preamble/boxes.tex), all optional, used
%% only where the content genuinely calls for it:
%%   \theading{{Label}}{{elaboration}} -- a colon heading, when a heading
%%                                     is used at all; label and text
%%                                     are THIS chapter's real words,
%%                                     never generic slot names
%%   \sidenote{{...}}               -- a marginal aside; use 0, 1, or
%%                                     many, wherever they actually land
%%   \epigraph{{quote}}{{attribution}} -- an optional opening frame
%%   terminal environment           -- only if there is a real command
%%                                     and real output to show
%%   breakage box                   -- only if this chapter has a
%%                                     genuine deliberate-failure moment
%%   faqentry{{question}}           -- one per real anticipated question,
%%                                     placed wherever it's relevant,
%%                                     not bundled into a fixed slot
%%   comparetable / booktabs        -- for comparison-shaped chapters
%%     (npm/Cargo/Maven/Go, macOS/Linux) instead of forcing prose
%%     through a shape that wants a table
%% No em dashes anywhere in the prose. Periods, colons, semicolons, or
%% parentheses instead -- see the style rule in SKILL.md.
\chapter{{{title}}}
\label{{ch:{label}}}

% Draft this chapter's prose here once its session is complete. A pure
% mental-model chapter may be almost all flowing text with a sidenote
% or two. A mechanism-plus-hands-on chapter needs a real terminal block
% and probably a breakage box. A comparison capstone probably wants a
% booktabs table more than any of the boxes above. Decide per chapter.
"""

def slugify(title):
    s = title.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    if len(s) > 40:
        s = s[:40].rsplit("-", 1)[0]
    return s

def main():
    chapter_num = 1
    main_tex_blocks = []
    for part_num, (dirslug, part_title, phase, chapters) in enumerate(SYLLABUS, start=1):
        part_dir = os.path.join(CH_DIR, dirslug)
        os.makedirs(part_dir, exist_ok=True)
        block = [f"\\part{{{part_title}}}\n"]
        for title in chapters:
            label = slugify(title)
            fname = f"ch{chapter_num:02d}-{label}.tex"
            fpath = os.path.join(part_dir, fname)
            content = STUB_TEMPLATE.format(
                num=chapter_num, title=title, part_num=part_num,
                part_title=part_title, phase=phase, label=label,
            )
            with open(fpath, "w") as f:
                f.write(content)
            block.append(f"\\input{{chapters/{dirslug}/{fname}}}\n")
            chapter_num += 1
        main_tex_blocks.append("".join(block))

    # The part list feeds the "where we are" map on every part page (boxes.tex).
    part_list = ",".join("{" + title + "}" for _, title, _, _ in SYLLABUS)
    with open(os.path.join(BOOK, "_generated_structure.tex"), "w") as f:
        f.write(f"\\def\\bookparts{{{part_list}}}\n\n")
        f.write("\n".join(main_tex_blocks))

    print(f"Generated {chapter_num - 1} chapter stubs across {len(SYLLABUS)} parts.")

if __name__ == "__main__":
    main()
