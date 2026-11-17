# Research phase

**Starts after Stage 6 · about 4 weeks for the gate, then 12-16 weeks for one branch**

You do this phase only if you want to do research. It has two parts: a short gate everyone does, then **one** branch. Do not mix branches until you have finished one.

## Step 1: The gate (weeks 31-34, about 80 h)

Learn the research habit on something small before you commit to a branch.

| | Resource | Hours | Notes |
|---|---|---:|---|
| ★ | [Research skills](../research-skills/README.md): how to read a paper, keep notes, run clean experiments | 6 | Use the [paper note template](../research-skills/paper-note-template.md) for every paper. |
| ★ | Read 8 papers, one per day for a week, from the list in your branch below | 16 | Write a note for each. |
| ★ | Reproduce one result from a paper at small scale, then change one thing (an ablation) | 50 | Pick a paper whose key result runs on your hardware. A good first choice is one you already touched: LoRA, DPO, RAG, or a small GPT scaling plot. |

**Gate project:** a 4-page report with the claim, your reproduction, your ablation, and what you could not reproduce. Publish it.

- [ ] Reproduction matches the paper's trend, or you explain why not.
- [ ] One ablation changes exactly one variable.
- [ ] Code runs from a clean clone.

## Step 2: Pick one branch

| If you want to... | Pick | Time | Core material |
|---|---|---:|---|
| Train models, understand scale, RL for reasoning | [R1: Train and scale](R1-train-and-scale.md) | 250-350 h | Stanford CS336, RL book, TRL |
| Make agents reliable, safe and measurable; interpretability and evals | [R2: Agents, evals and safety](R2-agents-evals-safety.md) | 200-300 h | Berkeley agentic AI, Inspect, ARENA |
| Work with images, video, speech and generative models | [R3: Multimodal and generative](R3-multimodal.md) | 200-300 h | MIT flow and diffusion, a vision-language model build |

If you cannot decide, take R2 if you liked Stage 5, R1 if you liked Stages 2-3, and R3 if you liked vision work in Stage 2.

## Step 3: The research project

Each branch ends with **one** research project: a question you chose, an experiment with controls and several seeds, a report, and code. Aim for a result a stranger could build on, ideally a workshop-paper-sized write-up. Working with a mentor or community (reading group, Discord, a mentored program) helps more than extra courses.

## Where the old material went

Roadmap parts that overlapped or were too heavy for a direct path are kept in [`reference/`](../reference/README.md): the full CS core, the full math sequence, nine original tracks, and the long reading list. Use them as a library, not as a to-do list.
