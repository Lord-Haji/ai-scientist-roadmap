# Research Skills (Level 8, started from Level 3)

Reading papers and running experiments is a skill with its own practice. Do not wait until you "finish the courses".

## 1. Reading papers

### The three passes ([Keshav, *How to Read a Paper*](https://web.stanford.edu/class/ee384m/Handouts/HowtoReadPaper.pdf))

1. **Pass 1 (5-10 min):** title, abstract, intro, section headings, conclusion, figures. Decide: is this worth more time? What category is it? What are the claimed contributions?
2. **Pass 2 (1 h):** read carefully but skip proofs; study figures/tables; note unexplained references.
3. **Pass 3 (hours):** re-derive or re-implement; challenge every assumption; find where it breaks.

### Questions to answer in every note

- What problem, and why does it matter? What was the previous best approach and why did it fail?
- What is the **single core idea**? Write it in two sentences.
- What are the math/mechanism details you must be able to reproduce?
- What evidence is used? Baselines fair? Seeds/variance? Compute disclosed? Contamination?
- What are the limitations the authors admit, and the ones they do not?
- What would you try next? What would falsify the claim?

### Where to find papers

[arXiv](https://arxiv.org/) (cs.LG, cs.CL, cs.CV, cs.AI), [Semantic Scholar](https://www.semanticscholar.org/), [alphaXiv](https://www.alphaxiv.org/), conference proceedings (NeurIPS, ICML, ICLR, ACL/EMNLP, CVPR; CoRL/RSS for robotics), lab blogs and technical reports, [Hugging Face Papers](https://huggingface.co/papers), and the [Alignment Forum](https://www.alignmentforum.org/) for safety. Build a small reading group; explaining a paper aloud is the best test.

### Reading techniques for hard papers

- Read the appendix and code; the appendix contains the real recipe.
- Draw the architecture with tensor shapes.
- Reproduce one table cell, not the whole paper.
- When math is dense, instantiate it with a 2D toy example.

## 2. Reproducing papers

Progress ladder (aim for the numbers in the graduation gate):

1. Run the authors' code; confirm headline numbers.
2. Re-implement the core mechanism at small scale; match qualitative behavior.
3. Reproduce with an ablation the paper did not run.
4. Change one component; test a hypothesis.
5. Write a short report with negative results included.

Use fixed seeds, log everything, write down predictions first. A reproduction that **fails** and is well analyzed is valuable.

## 3. Experiments and taste

- Read John Schulman's [An Opinionated Guide to ML Research](http://joschu.net/blog/opinionated-guide-ml-research.html) and Karpathy's [Recipe for Training Neural Networks](http://karpathy.github.io/2019/04/25/recipe/).
- Take [Harvard CS197: AI Research Experiences](https://www.cs197.seas.harvard.edu/): practical applied-DL research skills, technical writing, release, and presenting.
- Keep an **experiment log**: hypothesis, change, result, interpretation, next step.
- Use experiment tracking (Weights and Biases, MLflow, or plain CSV + git).
- Know your noise floor: run seeds before claiming an improvement.
- Look at the data and at model outputs, not just metrics.

## 4. Writing and communication

- Structure: problem -> idea -> method -> evidence -> limits.
- One figure that carries the main claim.
- Write the abstract and intro last, then reread as a skeptic.
- Release clean code with a README that reproduces the headline result.
- Read Neel Nanda's guides on writing ML papers and doing research (search for the title), and Jason Eisner/other writing advice for papers.

## 5. From reproduction to publication

Reproduction -> reproduction with ablation -> component modification -> original hypothesis -> technical report/blog -> workshop submission -> conference submission. Workshops at NeurIPS/ICML/ICLR and venues like CoRL/RSS are realistic first targets. For safety work: Alignment Forum posts, BlueDot project sprints, and mentored programs (MATS, fellowships).

## 6. Graduation gate before original research

- 3 serious paper reproductions,
- 2 modification/ablation studies,
- 1 independent research-style project,
- 1 academic-style report (6-10 pages),
- 1 carefully analyzed negative or inconclusive result.

## 7. Choosing a direction

Pick a branch (see [`research/`](../research/README.md)), read 20 recent papers in a narrow subarea, list open questions, talk to practitioners, and choose a question you can answer with the compute you have. Prefer questions where a small-scale result is informative.

Template: [`paper-note-template.md`](paper-note-template.md).
