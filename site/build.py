#!/usr/bin/env python3
"""Build the static site from the roadmap's markdown files.

    python site/build.py          # writes ./_site
"""
import html, json, re, shutil
from pathlib import Path
import markdown
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "_site"
HERE = Path(__file__).resolve().parent

LEVELS = [
    ("levels/L0-foundations.md", "0", "Foundations", "60-100 h"),
    ("levels/L1-cs-core.md", "1", "CS core", "900-1,100 h"),
    ("levels/L2-math.md", "2", "Math for AI", "250-350 h"),
    ("levels/L3-classical-ml.md", "3", "Classical ML", "150-200 h"),
    ("levels/L4-deep-learning.md", "4", "Deep learning", "300-450 h"),
    ("levels/L5-transformers-llms.md", "5", "Transformers and LLMs", "350-500 h"),
    ("levels/L6-frontier-core.md", "6", "Frontier core", "400-500 h"),
]
TRACKS = [
    ("tracks/A-llm-research.md", "A", "LLM research"),
    ("tracks/B-agents-multiagent.md", "B", "Agents and multi-agent"),
    ("tracks/C-vlm-multimodal.md", "C", "Vision-language, generative"),
    ("tracks/D-safety-interpretability.md", "D", "Safety and interpretability"),
    ("tracks/E-rl-reasoning.md", "E", "RL and reasoning"),
    ("tracks/F-ml-systems.md", "F", "ML systems"),
    ("tracks/G-applied-ai-engineering.md", "G", "Applied AI engineering"),
    ("tracks/H-data-science.md", "H", "Data science"),
    ("tracks/I-robotics-embodied.md", "I", "Robotics (optional)"),
]
START = [("README.md", "Overview"), ("00-HOW-TO-STUDY.md", "How to study"), ("TRACKER.md", "Tracker")]
LEVEL8 = [
    ("research-skills/README.md", "Research skills"),
    ("papers/README.md", "Papers"),
    ("projects/README.md", "Projects"),
    ("career/job-ready.md", "Job-ready guide"),
    ("career/interview-prep.md", "Interview prep"),
]
EXTRA = [("coursera.md", "Coursera picks"), ("levels/AUDIT-OLD-ROADMAP.md", "Old roadmap audit"), ("MAINTENANCE.md", "Maintenance")]

# Courses checked by web search on 2026-11-17. Anything not listed was not re-checked.
CHECKED = "Checked by web search, Nov 2026"
VERIFY = {
    "https://cs336.stanford.edu/": ("ok", "Spring 2026 offering, 18 lectures on YouTube. " + CHECKED),
    "https://web.stanford.edu/class/cs224n/": ("ok", "Page live; 2026 offering taught by Diyi Yang and Yejin Choi. " + CHECKED),
    "https://cs329a.stanford.edu/": ("ok", "Autumn 2025 schedule; nine-part lecture series on YouTube. " + CHECKED),
    "https://rdi.berkeley.edu/agentic-ai/f25": ("ok", "Recordings on YouTube, about 12 lectures. " + CHECKED),
    "https://multicomp.cs.cmu.edu/mmml-course/fall2026/": ("warn", "URL could not be confirmed. Try the MIT Multimodal AI alternative."),
    "https://mit-mi.github.io/mmai-course/spring2026/": ("warn", "Found in search; open it to confirm."),
}
for slug in ["specializations/machine-learning-introduction", "specializations/deep-learning",
             "specializations/mathematics-machine-learning",
             "specializations/mathematics-for-machine-learning-and-data-science",
             "specializations/algorithms", "specializations/reinforcement-learning",
             "learn/algorithms-part1", "learn/nand2tetris2", "learn/crypto",
             "learn/programming-languages", "learn/generative-ai-with-llms"]:
    VERIFY["https://www.coursera.org/" + slug] = ("ok", "Listing found and live. " + CHECKED)

def out_path(md: Path) -> Path:
    rel = md.relative_to(ROOT)
    if rel.name == "README.md":
        return rel.with_name("index.html")
    return rel.with_suffix(".html")

def rel_url(frm: Path, to: Path) -> str:
    depth = len(frm.parent.parts)
    return "../" * depth + str(to).replace("\\", "/")

def label_class(text: str) -> str:
    t = text.strip().lower()
    if t.startswith("★"): return "core"
    if t.startswith("companion") or t.startswith("alt") or t.startswith("optional"): return "comp"
    if t.startswith("depth"): return "depth"
    if t.startswith("reference"): return "ref"
    return "other"

ARXIV = re.compile(r"^(\d{4}\.\d{4,5})(\s*\(.*\))?$")
PAGES = {}

def render(md_path: Path):
    src = md_path.read_text(encoding="utf-8")
    body = markdown.markdown(src, extensions=["tables", "fenced_code", "sane_lists", "toc"],
                             extension_configs={"toc": {"permalink": False}})
    soup = BeautifulSoup(body, "html.parser")
    me = out_path(md_path)
    key = str(me).replace("\\", "/")
    h1 = soup.find("h1")
    title = h1.get_text() if h1 else md_path.stem

    for a in soup.find_all("a", href=True):
        h = a["href"]
        if re.match(r"^[a-z]+://", h) or h.startswith("#"):
            if h.startswith("http"):
                a["target"] = "_blank"; a["rel"] = "noopener"
                if "coursera.org" in h:
                    a["class"] = a.get("class", []) + ["cc"]
                    tag = soup.new_tag("span", **{"class": "pill-c"}); tag.string = "Coursera"
                    a.insert_after(tag)
                if h in VERIFY:
                    st, note = VERIFY[h]
                    v = soup.new_tag("span", **{"class": "vf " + st, "title": note, "tabindex": "0"})
                    v.string = "checked" if st == "ok" else "check"
                    (a.find_next_sibling("span") if (a.find_next_sibling("span") and "pill-c" in a.find_next_sibling("span").get("class", [])) else a).insert_after(v)
            continue
        m = re.match(r"^(.*?)([^/]*)\.md(#.*)?$", h)
        if m:
            name = m.group(2) + ".html"
            if m.group(2) == "README": name = "index.html"
            a["href"] = m.group(1) + name + (m.group(3) or "")
        elif h.startswith("../scripts/") or h.startswith("scripts/"):
            pass

    star_idx, n = [], 0
    for table in soup.find_all("table"):
        wrap = soup.new_tag("div", **{"class": "tw"})
        table.wrap(wrap)
        first = table.find("th")
        head = first.get_text().strip() if first else ""
        if head in ("", "Type"):
            table["class"] = ["res"]
            hr = table.find("thead").find("tr")
            hr.insert(0, soup.new_tag("th", **{"class": "chk-h"}))
            for tr in table.find("tbody").find_all("tr"):
                tds = tr.find_all("td")
                lab = tds[0].get_text() if tds else ""
                cls = label_class(lab) if head == "" else "paper"
                tr["class"] = ["r-" + cls]
                tr["data-i"] = str(n)
                if cls == "core": star_idx.append(n)
                cell = soup.new_tag("td", **{"class": "chk"})
                cb = soup.new_tag("input", type="checkbox", **{"class": "ck", "data-i": str(n), "aria-label": "Mark done"})
                cell.append(cb); tr.insert(0, cell)
                if head == "" and tds:
                    tds[0]["class"] = ["lab", "lab-" + cls]
                if head == "Type" and len(tds) >= 3:
                    mm = ARXIV.match(tds[2].get_text().strip())
                    if mm:
                        tds[2].string = ""
                        a = soup.new_tag("a", href="https://arxiv.org/abs/" + mm.group(1), target="_blank", rel="noopener")
                        a.string = tds[2].get_text() or mm.group(1)
                        tds[2].append(a)
                        if mm.group(2): tds[2].append(mm.group(2))
                n += 1
    for li in soup.find_all("li"):
        txt = li.get_text()
        first = next(iter(li.contents), None)
        if isinstance(first, str) and first.lstrip().startswith("[ ]"):
            first.replace_with(first.lstrip()[3:].lstrip())
            cb = soup.new_tag("input", type="checkbox", **{"class": "ck", "data-i": str(n), "aria-label": "Mark done"})
            li.insert(0, cb); li["class"] = ["task"]; n += 1
    PAGES[key] = {"n": n, "star": star_idx}
    return title, str(soup), me, key

def rail(cur: Path) -> str:
    def link(md, txt, extra=""):
        t = out_path(ROOT / md)
        cls = "cur" if t == cur else ""
        return f'<a class="{cls}" href="{rel_url(cur, t)}" {extra}>{txt}</a>'
    o = ['<nav class="rail" id="rail" aria-label="Curriculum">']
    o.append('<div class="grp">' + "".join(link(p, t) for p, t in START) + "</div>")
    o.append('<ol class="path">')
    for p, num, name, hrs in LEVELS:
        t = out_path(ROOT / p); key = str(t).replace("\\", "/")
        cls = "cur" if t == cur else ""
        o.append(f'<li class="{cls}" data-page="{key}"><a href="{rel_url(cur, t)}"><span class="node" aria-hidden="true">{num}</span>'
                 f'<span class="nm">{name}<small>{hrs}</small></span><span class="pc" data-pc></span></a></li>')
    o.append('</ol>')
    o.append('<p class="sub">Level 7: specializations, pick 1-2</p><ol class="path tracks">')
    for p, let, name in TRACKS:
        t = out_path(ROOT / p); key = str(t).replace("\\", "/")
        cls = "cur" if t == cur else ""
        o.append(f'<li class="{cls}" data-page="{key}"><a href="{rel_url(cur, t)}"><span class="node sm" aria-hidden="true">{let}</span>'
                 f'<span class="nm">{name}</span><span class="pc" data-pc></span></a></li>')
    o.append('</ol><p class="sub">Level 8: research and career</p><div class="grp">' + "".join(link(p, t) for p, t in LEVEL8) + "</div>")
    o.append('<p class="sub">Reference</p><div class="grp">' + "".join(link(p, t) for p, t in EXTRA) + "</div></nav>")
    return "".join(o)

def main():
    if OUT.exists(): shutil.rmtree(OUT)
    OUT.mkdir()
    shutil.copytree(HERE / "static", OUT / "static")
    (OUT / "scripts").mkdir()
    shutil.copy(ROOT / "scripts" / "check_links.py", OUT / "scripts" / "check_links.py")
    tmpl = (HERE / "template.html").read_text(encoding="utf-8")
    mds = sorted(p for p in ROOT.rglob("*.md") if not any(x in p.parts for x in ("_site", ".git", "node_modules")))
    rendered = [render(p) for p in mds]
    pages_json = json.dumps(PAGES)
    for title, body, me, key in rendered:
        root = "../" * len(me.parent.parts)
        page = (tmpl.replace("{{title}}", html.escape(title))
                    .replace("{{root}}", root).replace("{{rail}}", rail(me))
                    .replace("{{body}}", body).replace("{{key}}", key)
                    .replace("{{pages}}", pages_json))
        dest = OUT / me; dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(page, encoding="utf-8")
    (OUT / ".nojekyll").write_text("")
    print(f"built {len(rendered)} pages -> {OUT}")

if __name__ == "__main__":
    main()
