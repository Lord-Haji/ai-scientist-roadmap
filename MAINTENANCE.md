# Maintenance

This curriculum should stay selective. Do not rebuild it every time a new model drops.

## What changes slowly (check yearly)

MIT/Harvard math, CS50-style intros, algorithms, CS:APP, OSTEP, CS229, Sutton and Barto, Understanding Deep Learning, Stat 110.

## What changes quickly (check before starting the stage)

CS224N, CS231n, CS234, **CS336**, CS329A/CS329Z, CMU 11-777, Berkeley Agentic AI MOOC, CS285, CS224R, HF courses, BlueDot/ARENA offerings, and all "frontier" readings: latest LLM technical reports, reasoning, agents, VLMs, VLA.

Rule: before starting a fast-moving stage, open the newest public offering of the same course, update the link in your own fork, and refresh only that stage's reading list.

## Check every time you start a stage

- **Stage 4**: open the Hugging Face trending page and the Ollama library; swap the model families in the stage for whatever is current. Quantization names and tools (llama.cpp, Ollama, vLLM) change fast.
- **Stages 5-6**: re-check Unsloth, TRL and Ollama docs; their APIs move often.
- Research branches: use the newest offering of each course.

## Link checking

`python scripts/check_links.py` scans the markdown files and reports URLs that do not respond with success. Some sites block automated requests or require JavaScript; treat failures as "check manually". Run it quarterly.

## Known caveats at time of writing (November 2026)

- **CS50** (Harvard College) is changing lecture format and grading in fall 2026; confirm what applies to the online CS50x.
- **CS329A**: lecture videos are public (nine-part series on Stanford Online YouTube, about 10 hours, Autumn 2025 offering; confirmed by search in November 2026). **CS329Z** (Fall 2026) links slides; check whether videos exist.
- **11-777 URL** is still unverified; older terms live at other CMU hosts. The MIT Multimodal AI course (Spring 2026) is listed in research branch R3.
- **BlueDot** courses are cohort-run; check intake dates.
- **CMU 11-777**, **MIT robotics**, **Stanford CS224R** URLs are for the term in the link; use the newest term.
- **ARENA** and **BlueDot** run cohorts on a schedule; self-paced access to materials exists.
- arXiv IDs in `reference/papers/README.md` were assembled from memory and reference lists; spot-check titles after opening.

## Contributing to your own copy

Keep a `CHANGELOG` in your fork: which course you replaced, why, and the date.

## The website

The site is built from these markdown files by `site/build.py` (needs `pip install markdown beautifulsoup4`). Run `python site/build.py` and open `_site/index.html` to preview. Pushing to `main` deploys it through GitHub Pages (Settings, Pages, Source: GitHub Actions). Checkbox progress is stored in the browser's local storage, so it is per browser and per device. Course "checked" badges are set in the `VERIFY` table in `site/build.py`.
