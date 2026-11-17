# AI Scientist Roadmap

> A free, self-study path from zero to **computer scientist and AI researcher**: OSSU-style CS core, a modern AI/LLM core, and specialization tracks (LLMs, agents and multi-agent systems, vision-language models, safety and interpretability, ML systems, applied AI engineering).

**Version:** 2026.11  
**Built from:** [OSSU Computer Science](https://github.com/ossu/computer-science), [leviance/AI-Research-Curriculum](https://github.com/leviance/AI-Research-Curriculum), a classic Coursera data-science roadmap (audited, see [`levels/AUDIT-OLD-ROADMAP.md`](levels/AUDIT-OLD-ROADMAP.md)), and 2026 course research.  
**Default pace:** 10-15 hours/week. A fast path exists for people who already have a CS degree (see below).

## What you can do when you finish

- Read a new LLM / VLM / agent paper and explain the problem, the math, the mechanism, and where it fails.
- Implement and train a small GPT, a small VLM, and an RL post-training loop yourself.
- Build, evaluate, and break tool-using and multi-agent systems.
- Be a credible candidate for software engineering, ML/AI engineering, or research-engineer roles. The CS core is real (about 1,000 h), so the job-ready claim only holds once Level 1 and interview practice are done; see [`career/job-ready.md`](career/job-ready.md).
- Run your own experiments and write them up well enough that a workshop submission (ideally with a mentor or co-author, and some rented compute) is a realistic next step.

## The shape of the curriculum

```
 LEVEL 0  Foundations           Python, shell, git, math refresher
 LEVEL 1  CS Core (job-ready)   programming, algorithms, systems, databases, networks, SWE
 LEVEL 2  Math for AI           linear algebra, calculus, probability, statistics, optimization
 LEVEL 3  Classical ML + data   CS229-level ML, data science, evaluation
 LEVEL 4  Deep learning         from-scratch autograd, CNNs/RNNs, PyTorch, DL systems
 LEVEL 5  Transformers + LLMs   NLP, build GPT, CS336, pretraining and inference
 LEVEL 6  Frontier core         post-training + RL, multimodal/diffusion, agents
 LEVEL 7  Specializations       pick 1-2 (see tracks/)
 LEVEL 8  Research + career     paper reproduction, original work, portfolio, interviews
```

Levels 1 and 2 can run **in parallel** (split every week by days, e.g., CS Mon/Wed/Fri and math Tue/Thu, so practice stays spaced). Everything marked **★ must-do** is the non-negotiable spine. Everything else is depth you take when a track or a project needs it.

| Level | Content | Must-do hours (approx.) |
|---|---|---:|
| 0 | [Foundations](levels/L0-foundations.md) | 60-100 |
| 1 | [CS Core](levels/L1-cs-core.md) | 900-1,100 (less with test-outs) |
| 2 | [Math for AI](levels/L2-math.md) | 250-350 |
| 3 | [Classical ML + data](levels/L3-classical-ml.md) | 150-200 |
| 4 | [Deep learning](levels/L4-deep-learning.md) | 300-450 |
| 5 | [Transformers + LLMs](levels/L5-transformers-llms.md) | 350-500 |
| 6 | [Frontier core](levels/L6-frontier-core.md) | 400-500 |
| 7 | [Specializations](tracks/) | 300-600 each |
| 8 | [Research + career](research-skills/README.md) | ongoing |

The spine (levels 0-6) adds up to roughly **2,500-3,200 hours** if you do everything from zero. That is about **5+ years at 10 h/week**, **3.5-4 years at 15 h/week**, or **~2.5-3 years at 20 h/week**. With test-outs (people with a CS degree typically skip most of Levels 0-1, about 700-1,000 h), the remaining ~1,700 h is roughly **18-24 months at 20 h/week** (see [Fast path](#fast-path-if-you-already-know-cs)). These are planning estimates, not promises; exercises and projects are included in the hours.

## How to start

1. Read [`00-HOW-TO-STUDY.md`](00-HOW-TO-STUDY.md) (the study loop, the project standard, the paper-reading protocol).
2. Take the **test-out checks** at the top of each level file; skip what you already pass.
3. Copy [`TRACKER.md`](TRACKER.md) into your own notes and tick items as you go.
4. Keep **one long-lived code repo** of your own with a folder per project ([`projects/README.md`](projects/README.md)).
5. From Level 3 onward start reading papers weekly ([`papers/README.md`](papers/README.md)).

## Specialization tracks (Level 7)

| Track | You become... | File |
|---|---|---|
| A. LLM research and training | someone who can pretrain, post-train, scale and evaluate LLMs | [tracks/A-llm-research.md](tracks/A-llm-research.md) |
| B. Agents and multi-agent systems | someone who designs, evaluates and secures agentic systems | [tracks/B-agents-multiagent.md](tracks/B-agents-multiagent.md) |
| C. Vision-language and generative models | someone fluent in VLMs, diffusion/flow, video, VLA | [tracks/C-vlm-multimodal.md](tracks/C-vlm-multimodal.md) |
| D. Safety, alignment and interpretability | someone who can do evals, red teaming, mech interp, alignment research | [tracks/D-safety-interpretability.md](tracks/D-safety-interpretability.md) |
| E. RL and reasoning | someone who can build RL post-training and game/agent RL | [tracks/E-rl-reasoning.md](tracks/E-rl-reasoning.md) |
| F. ML systems and infrastructure | someone who makes training and inference fast and reliable | [tracks/F-ml-systems.md](tracks/F-ml-systems.md) |
| G. Applied AI engineering (fastest to a job) | someone who ships LLM products: RAG, evals, serving, MLOps | [tracks/G-applied-ai-engineering.md](tracks/G-applied-ai-engineering.md) |
| H. Data science and classical ML | someone who answers business questions with data | [tracks/H-data-science.md](tracks/H-data-science.md) |
| I. Robotics and embodied AI (optional) | someone building robot learning and VLA policies | [tracks/I-robotics-embodied.md](tracks/I-robotics-embodied.md) |

Typical combinations: **A+F** (research engineer), **B+D** (agent safety), **A+B+E** (frontier agents/reasoning), **C+I** (embodied), **G+H** (fast employability).

## Fast path if you already know CS

If you hold a CS/engineering degree or have several years of professional programming:

- Level 0: skip after the test-out.
- Level 1: only do what you cannot pass a test-out for; most people still gain from **algorithms**, **systems (CS:APP / OSTEP)**, and **distributed systems**.
- Level 2: do not skip. Most people think they know linear algebra and probability and find gaps once they derive backprop.
- Then go straight through Levels 3-6 in order. Build the projects. Skipping the from-scratch projects is the most common reason people can use LLMs but cannot reason about them.

## Principles

1. **Implement the mechanism.** A course counts as done only when you can explain it, derive the key math, implement it small, break it, and reproduce one non-trivial result.
2. **Free, university-grade first.** MIT/Stanford/Berkeley/CMU/Harvard open material over paid certificates. Certificates are optional signals, never the spine.
3. **Papers inside the course.** Papers are read at the point where their prerequisites are satisfied, not as a separate track.
4. **Depth over breadth, but not blind.** The frontier moves fast. Levels 0-5 age slowly; Level 6 and the tracks are the part to refresh yearly ([`MAINTENANCE.md`](MAINTENANCE.md)).
5. **Job-ready is a first-class goal.** Level 1 and the career files exist so you can pass software interviews, not just read papers.

## Repo map

```
README.md                  you are here
00-HOW-TO-STUDY.md         study loop, project standard, notes system
TRACKER.md                 checklist for the whole path
MAINTENANCE.md             how to keep resources current, link checking
levels/                    the spine, level by level
tracks/                    specializations
papers/                    staged reading lists with arXiv IDs
research-skills/           reading, reproducing, experimenting, writing
projects/                  capstone and per-level projects
career/                    job-ready guidance, interviews, portfolio
scripts/                   link checker
```

## Honest limits

- Course offerings change every term. Links here point at the course home pages; check the newest offering before you start (Level 6 and tracks especially).
- Time estimates are rough and assume focused work including exercises.
- No credential is awarded. The portfolio and papers you produce are the proof.
