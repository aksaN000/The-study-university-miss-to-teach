#!/usr/bin/env python3
"""Rebuilds the practice repo skeleton (exercises/assignments/exams placeholders) from the
book's SYLLABUS. Usage: python3 generate_practice_skeleton.py <path-to-practice-repo>
Templates and READMEs are copied from tools/practice-templates/. Never deletes real content:
a placeholder file is only (re)written if it is missing or still a placeholder."""
import os, sys, shutil, importlib.util
HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("g", os.path.join(HERE, "..", "book", "generate_stubs.py"))
g = importlib.util.module_from_spec(spec); spec.loader.exec_module(g)
REPO = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "..", "practice")
MARK = "Not yet available."
clean = lambda t: t.replace("\\_", "_").replace("\\&", "&")
def put(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if os.path.exists(path) and MARK not in open(path).read():
        return  # real content: leave it alone
    open(path, "w").write(text)
for rel in ["README.md", "solutions/README.md", "exercises/TEMPLATE.md", "assignments/TEMPLATE.md", "exams/TEMPLATE.md"]:
    dst = os.path.join(REPO, rel); os.makedirs(os.path.dirname(dst), exist_ok=True)
    shutil.copy(os.path.join(HERE, "practice-templates", rel.replace("/", "__")), dst)
n = 1
for pnum, (slug, title, phase, chs) in enumerate(g.SYLLABUS, start=1):
    for c in chs:
        s = g.slugify(clean(c))
        put(os.path.join(REPO, "exercises", slug, f"ch{n:03d}-{s}.md"),
            f"# Chapter {n}: {clean(c)}\n\n{MARK} Written once this chapter's session is fully complete; format in `exercises/TEMPLATE.md`.\n")
        n += 1
    put(os.path.join(REPO, "assignments", f"{slug}.md"),
        f"# Part {pnum}, {title}: assignment\n\n{MARK} Written once every chapter in this part is complete; format in `assignments/TEMPLATE.md`.\n")
    put(os.path.join(REPO, "exams", f"{slug}.md"),
        f"# Part {pnum}, {title}: exam\n\n{MARK} Written after this part's assignment is done; closed book, from memory. Format in `exams/TEMPLATE.md`.\n")
print(f"{n-1} chapters, {len(g.SYLLABUS)} parts")
