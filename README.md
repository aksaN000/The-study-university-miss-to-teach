# The study university miss to teach

A self-paced curriculum, and a book written alongside it, covering the layer of computing that a
computer science degree assumes and rarely teaches: what the operating system does when we run
something, the shell, how source code becomes a running process, Git's internals, networking,
packaging in Python and JavaScript, notebooks, containers, CI, deployment, and machine learning
infrastructure.

## The book: *From Zero*

Written one chapter at a time, each only after the matching session was actually taught, run
hands-on, broken on purpose, and passed a recall check. Chapters that have not been taught yet
are still placeholders.

- **Latest PDF:** see the `book-latest` release of this repository (rebuilt automatically on
  every change).
- **Sources:** `book/` (XeLaTeX; `book/generate_stubs.py` holds the syllabus).

## Repository layout

| Path | What it holds |
|---|---|
| `book/` | LaTeX sources for the book |
| `practice/` | Exercises per chapter, an assignment and an exam per part, and solutions |
| `tracking/curriculum-map.md` | Progress: phase table, chapter checklist, session log |
| `notes/` | The learner's own notes |
| `.claude/skills/` and `CLAUDE.md` | The teaching method, used by the AI instructor |
| `tools/` | Generators that keep every listing in sync with the syllabus |

## Status

Design phase. The curriculum is still being shaped before teaching begins; see
`tracking/curriculum-map.md`.
