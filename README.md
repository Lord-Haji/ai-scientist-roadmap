# AI Scientist Roadmap

> A free, step-by-step path for someone who can code in Python: learn how LLMs work, run and fine-tune **open-weight models on your own machine**, build real LLM systems, then (optionally) do research in one focused area.

**Version:** 2026.11 · **Pace:** written for 20 h/week · **Style:** OSSU-like. One path, in order, no choosing during the build phase.

## The path

| # | Stage | Weeks | Hours | You finish with |
|---|---|---:|---:|---|
| 1 | [Foundations](path/01-foundations.md): math you need, classical ML, first local model | 1-6 | ~110 | A tabular ML project |
| 2 | [Neural networks from scratch](path/02-neural-nets.md) | 7-12 | ~110 | Your own autograd and trained nets |
| 3 | [Transformers and LLM internals](path/03-transformers.md) | 13-16 | ~80 | A GPT you trained |
| 4 | [Open-weight and local LLMs](path/04-local-llms.md) | 17-20 | ~80 | A benchmark of open models on your hardware |
| 5 | [Build with LLMs: RAG, tools, agents, evals](path/05-build-llm-apps.md) | 21-26 | ~110 | **Flagship project**, running locally |
| 6 | [Fine-tune and post-train open models](path/06-fine-tune.md) | 27-30 | ~80 | A fine-tuned model that runs in Ollama |

**Build phase total: about 570 hours, 30 weeks at 20 h/week.** At 10 h/week, double the weeks. Every item in stages 1-6 is in order. Items marked *Optional* can be skipped.

### Then, only if you want research

| Step | What | Time |
|---|---|---|
| Gate | [Reproduce one paper result and ablate it](research/README.md) | 4 weeks |
| Branch (pick **one**) | [R1 Train and scale](research/R1-train-and-scale.md) · [R2 Agents, evals and safety](research/R2-agents-evals-safety.md) · [R3 Multimodal and generative](research/R3-multimodal.md) | 12-16 weeks |
| Research project | One question, controlled experiments, a published report | in the branch |

## What you can do after the build phase

- Pick an open model for a job, fit it to your hardware, quantize and serve it.
- Build a RAG app and an agent, and prove with an eval set that they work.
- Fine-tune a small model with LoRA and show whether it beat prompting.
- Explain how a transformer works, with shapes, because you built one.

## How to start

1. Read [How to study](00-HOW-TO-STUDY.md) (5 minutes).
2. Check your hardware against the table in [Stage 4](path/04-local-llms.md). A laptop with 16 GB RAM is enough to start; free cloud notebooks cover the rest.
3. Copy [the tracker](TRACKER.md) and begin [Stage 1](path/01-foundations.md).
4. Keep one GitHub repo with one folder per project. See [Projects](projects/README.md).

## Ground rules

1. **Build it to learn it.** A video is not finished until you coded the thing.
2. **Free first.** University and open courses, open-source tools, open-weight models.
3. **Local first.** From Stage 4 on, work runs on open weights on your own machine. A hosted model is for comparison only.
4. **Measure everything.** From Stage 4 on, every project has numbers and an honest failure analysis.
5. **One path.** Do not jump ahead. Anything extra is in [side quests](SIDE-QUESTS.md), which you may ignore.

## Repo map

```
path/             stages 1-6, the main path
research/         gate, three branches, research project
projects/         the projects, one per stage
research-skills/  how to read papers, write notes, run experiments
reference/        the original wider roadmap, kept as a library
SIDE-QUESTS.md    optional detours
TRACKER.md        your checklist
```

## Honest limits

- Courses and models change often. Open the newest offering and the current model list before each stage, and see [MAINTENANCE.md](MAINTENANCE.md).
- Hours are estimates and include exercises.
- No credential is awarded. Your public projects are the proof.
