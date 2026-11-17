# Job-Ready Guide

The curriculum is designed to qualify you for several role families. Pick the one closest to your goal and make sure its **minimum bar** is met before applying.

## Role families and the minimum bar

| Role | Needs from this curriculum | Portfolio signals |
|---|---|---|
| **Software engineer (any)** | Levels 0-1 fully, interview prep | Deployed service, tests/CI, algorithms kit, OSS PRs |
| **ML engineer / AI engineer (LLM apps)** | Levels 0-1, 3, parts of 4-6, Track G | RAG system with evals, agent workflow, deployed service, OSS contributions |
| **Data scientist** | Levels 0-3, Track H | Experiment/causal analyses, SQL fluency, stakeholder memo, Kaggle/public work |
| **Research engineer (LLM/infra)** | Levels 1-6, Track A and/or F | Mini-foundation-model with scaling curves, kernels/distributed work, reproductions |
| **Applied / research scientist** | Levels 2-6 + a track + research gate | Papers or workshop submissions, strong reproductions, clear research taste |
| **Safety / interpretability researcher** | Levels 2-5, 6A/6C, Track D | Mech-interp replication, evals, a post or paper, fellowship/program participation |

## What employers actually look for (patterns)

- **Evidence you can build**: running code, tests, deployments, readable repos.
- **Evidence you can evaluate**: a metric, a baseline, an ablation, error analysis. Many candidates can call an API; fewer can show their system works.
- **Fundamentals under pressure**: coding rounds, system design, ML basics (bias/variance, metrics, loss functions, optimization), and for research roles, deep dives into your own projects/papers.
- **Communication**: clear README, design docs, and the ability to explain trade-offs.
- **Certificates** (IBM, Coursera, cloud) are weak signals compared with projects. A cloud certificate helps some employers and some countries; do it after you can build.

## Building the portfolio

1. Pick 4-6 projects from [`projects/README.md`](../../projects/README.md): at least one engineering (service), one ML-from-scratch, one LLM/agent system with evals, one research-style reproduction.
2. Write a one-page summary per project: problem, approach, result (with numbers), what failed, what you would do next.
3. Keep a public GitHub profile with pinned repos and clean READMEs; write 2-3 technical blog posts explaining what you learned or found.
4. Contribute to open source: start with docs/tests/bug fixes in LLM tooling repos (LangChain, Haystack, LlamaIndex, vLLM, Hugging Face libraries); progress to features.
5. Participate publicly: Kaggle, Alignment Forum posts, reading groups, workshops, hackathons.

## Application pipeline

- **Resume:** one page; lead with projects and impact numbers; list tech; avoid course lists.
- **Targeting:** apply to 5-10 roles/week, tailor the top section, track in a spreadsheet.
- **Referrals and research paths:** contact authors of papers you reproduced with a short, specific note; join mentored programs (MATS or other fellowships) if aiming at research; consider a PhD if aiming at research scientist roles (see below).
- **Interviews:** see [`interview-prep.md`](interview-prep.md).

## Graduate study and PhD

A PhD or research master's remains the standard route to research scientist roles at labs, though strong research engineers and open-source/paper track records also get in. If you go this way: build a reproduction + one workshop-level paper before applying, choose advisors by their recent papers and compute, and read their last 5 papers deeply. Funded programs exist in many countries (research scholarships and fully funded PhD tracks); check each program's current rules and deadlines.

## Time-boxing

A realistic route for someone who wants a job early: Levels 0-1 (about 1,000 h from scratch, much less with a CS background) -> the core of Level 2 (linear algebra, probability, optimization) -> Level 3 -> Track G with parts of Levels 4-6 -> job -> keep learning the rest of the spine on the job. Research-track people complete Levels 1-6 first. Both can work; choose consciously.

## Market reality (read this before planning)

- Entry-level software and ML hiring is competitive. Expect many applications and long cycles (months, not weeks). Plan for 6-12 months of coding-interview practice at 5-10 problems/week.
- **Referrals and visible work beat cold applications.** Open-source contributions, a reproduced paper with a clear write-up, and a contact who can vouch for you move the needle more than certificates.
- Location, visa and work-authorization constraints change the odds a lot; research them early for each country you target.
- Many research labs do not hire people without a strong paper/OSS record or a PhD; mentored programs (e.g., MATS, safety fellowships, lab-run fellowship programs) are legitimate paths. Check each program's current existence, eligibility and deadlines, as they change yearly.
