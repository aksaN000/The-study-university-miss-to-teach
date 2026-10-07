#!/usr/bin/env python3
"""Generates the full chapter-stub skeleton for the book from the syllabus,
and writes the corresponding \\part / \\input block for main.tex."""

import os
import re

BOOK = os.path.dirname(os.path.abspath(__file__))
CH_DIR = os.path.join(BOOK, "chapters")

# (part_dir_slug, part_title, phase_number, [chapter titles in order])
SYLLABUS = [
    ("part01-foundations", "Mental Foundations", 0, [
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
    ("part02-command-line", "The Command Line", 1, [
        "Terminal, console, shell: three things we call by one name",
        "What a shell is and why it exists",
        "PowerShell vs. bash/zsh: different languages, not different skins",
        "Navigating, creating, moving, deleting",
        "Standard input, output, and error",
        "Pipes and redirection",
        "Exit codes: how a program reports back",
        "Globbing and quoting",
        "Anatomy of a command line: argv, flags, options, and the double dash",
        "PATH: how a name becomes a program",
        "Environment variables in practice",
        "Session versus persistent configuration: dotfiles, profiles, and the registry",
        "Installing WSL2",
        "Doing it all again in Ubuntu",
        "apt, the Linux filesystem hierarchy, and sudo",
        "SSH",
        "Writing real shell scripts",
        "Living comfortably in the terminal",
        "A third machine: where macOS agrees with Linux, and where it quietly doesn't",
    ]),
    ("part03-source-to-process", "From Source Code to Running Process", 2, [
        "Three kinds of things on PATH: native binaries, language engines, and scripted tools",
        "Executable files: ELF, PE, Mach-O, magic numbers, and shebangs",
        "The C pipeline: preprocess, compile, assemble, link",
        "Linking and loading: static, dynamic, and the loader that runs first",
        "ABIs: why a binary built here refuses to run there",
        "Interpreters, honestly: line by line, tree walking, and bytecode",
        "Inside CPython: from source to .pyc to the evaluation loop",
        "Bytecode virtual machines: the JVM and .NET",
        "JIT compilation through V8: Ignition, Sparkplug, Maglev, TurboFan",
        "Node.js: a JavaScript engine plus an operating system API",
        "Scripted CLIs: shebangs, launcher shims, and why python -m pip exists",
    ]),
    ("part04-version-control", "Version Control, Properly", 3, [
        "The object model: blobs, trees, and commits",
        "Refs, and what a branch actually is",
        "HEAD",
        "Merge vs. rebase, and when each is correct",
        "Resolving conflicts without panic",
        ".gitignore: what belongs in a repo",
        "Remotes, pull requests, and code review",
        "Recovering from disasters with reflog",
        "Reading someone else's history",
    ]),
    ("part05-networking", "Networking Essentials", 4, [
        "Ports, localhost, and IP vs. DNS",
        "HTTP basics",
        "TLS and certificates",
        "SSH keys",
        "What a server actually is",
    ]),
    ("part06-python-packaging", "Python Environments and Packaging", 5, [
        "What a package manager actually automates",
        "How the interpreter finds code: sys.path and site-packages",
        "Why global installs cause problems: a tour of our own machine",
        "venv: what it actually does, mechanically",
        "pip, PyPI, sdists, and wheels",
        "Why compiled packages make Python versions matter",
        "requirements.txt, lockfiles, and pyproject.toml",
        "conda: what problem it solved that pip could not",
        "Modern tooling: uv and poetry",
        "Packaging and publishing something of our own",
    ]),
    ("part07-javascript-tooling", "JavaScript and Node Tooling", 6, [
        "npm, global installs, and project scope",
        "package.json and semver ranges: declaring what we need",
        "node\\_modules: nested, flattened, hoisted, and linked",
        "Lockfiles and npm ci: making installs repeatable",
        "npm configuration: .npmrc, npm\\_config variables, and stricter validation",
        "npx, npm create, and scaffolding CLIs",
        "CommonJS and ES modules: two module systems in one ecosystem",
        "Transpilers, bundlers, and dev servers: what Vite does with our React code",
        "Supply-chain security: every dependency is code we chose to run",
        "Packaging elsewhere: Cargo, Maven, Go modules, and what every ecosystem shares",
    ]),
    ("part08-jupyter", "Jupyter and the Notebook Stack", 7, [
        "The frontend/kernel split, and why it exists",
        "The kernel protocol",
        "Kernel specs: where they live, how discovery works",
        "Why notebooks break in ways scripts do not",
        "Notebooks and version control",
        "When a notebook is the wrong tool",
    ]),
    ("part09-containers", "Containers", 8, [
        "The isolation idea, generalized from environments to the whole OS",
        "Images, layers, and Dockerfiles",
        "Volumes, ports, and networking",
        "docker-compose",
        "GPU containers",
        "Why \"works on my machine\" stops being necessary",
    ]),
    ("part10-automation-build", "Automation and Build Tooling", 9, [
        "Makefiles",
        "GitHub Actions and CI/CD",
        "Automated testing as a habit, not a chore",
        "Pre-commit hooks",
        "Linters and formatters",
        "Semantic versioning",
        "Reproducible builds",
        "The same pipeline, five languages: CI beyond Python",
    ]),
    ("part11-deployment-ops", "Deployment and Operations", 10, [
        "Deploying something small to a real machine",
        "Reading logs",
        "Debugging a process that will not start",
    ]),
    ("part12-ml-infra", "Machine Learning Infrastructure", 11, [
        "Reproducible ML environments",
        "CUDA and driver versions",
        "Data versioning with DVC",
        "Experiment tracking: MLflow and W\\&B",
        "Configuration management",
        "Serving a model",
        "Why almost every ML project fails to be reproducible",
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

    with open(os.path.join(BOOK, "_generated_structure.tex"), "w") as f:
        f.write("\n".join(main_tex_blocks))

    print(f"Generated {chapter_num - 1} chapter stubs across {len(SYLLABUS)} parts.")

if __name__ == "__main__":
    main()
