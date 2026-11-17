# R2: Agents, evals and safety

**You become:** someone who builds agents that work, measures them honestly, and studies how they fail or can be made safe, including interpretability.  
**Time:** 200-300 h. **Needs:** Stages 1-6, especially Stage 5.

This branch merges the old agents and safety tracks, which overlapped heavily.

| | Step | Resource | Hours | Notes |
|---|---|---|---:|---|
| ★ | 1 | [Berkeley Agentic AI MOOC (Fall 2025)](https://rdi.berkeley.edu/agentic-ai/f25) | 26 | About 13 lectures on reasoning, planning, frameworks, and security. |
| ★ | 2 | [Stanford CS329A: Self-Improving AI Agents](https://cs329a.stanford.edu/) | 40 | Test-time compute, verifiers, search. Read the linked papers. |
| ★ | 3 | [UK AISI Inspect](https://inspect.aisi.org.uk/) | 15 | Build a full eval: dataset, scorer, repeated runs, error bars. |
| ★ | 4 | [ARENA curriculum](https://arena.education/): chapters on transformers, mechanistic interpretability and evals | 80-120 | Code-first exercises with TransformerLens. Free notebooks. |
| ★ | 5 | [Neel Nanda: Getting started in mechanistic interpretability](https://www.neelnanda.io/mechanistic-interpretability) | 20 | The practical entry to the field. |
| Optional | 6 | [BlueDot AGI Strategy](https://bluedot.org/courses/agi-strategy) and [Technical AI Safety](https://bluedot.org/courses/technical-ai-safety) | 55 | Cohort-run; check intake dates. Good for the big-picture risks. |

**Papers, in order:** ReAct (2210.03629) → Reflexion (2303.11366) → SWE-bench (2310.06770) → tau-bench (2406.12045) → Indirect prompt injection (2302.12173) → AgentDojo (2406.13352) → AI Control (2312.06942) → Induction heads (2209.11895) → Sparse autoencoders find interpretable features (2309.08600) → Alignment faking (2412.14093). Full list: [reference papers](../reference/papers/README.md).

## Research project (pick one)

- **Eval:** design a new capability or propensity eval with controls, contamination checks and prompt-sensitivity analysis.
- **Interpretability:** replicate an induction-head or sparse-autoencoder result on a small open model, then test one new feature with ablation.
- **Agents:** compare one agent against 2-3 multi-agent designs on success, cost and failure types over many runs. Report when multi-agent is *not* worth it.
- **Red team:** systematic prompt-injection study of your Stage 5 agent, with measured mitigations.

## Done when

You can explain why an agent failed from its trajectory, design an eval that separates skill from luck, and clearly separate what is established from what is speculation.

More depth, if you need it: [reference tracks B and D](../reference/tracks/B-agents-multiagent.md).
