# Track D: Safety, Alignment, Interpretability and Evaluation

**You become:** someone who can do evals, red teaming, mechanistic interpretability and alignment research, and who understands the strategic landscape.  
**Requires:** Levels 4-5 (6A and 6C helpful). **Time:** 250-500 h. Strong pairing with B (agents) and A (LLMs).

## Learning goals

1. **Strategic landscape:** risks from advanced AI, governance and incentives, what technical safety does and does not address.
2. **Alignment techniques:** RLHF/RLAIF, Constitutional AI, preference learning, scalable oversight, debate, weak-to-strong generalization, AI control, model organisms of misalignment.
3. **Interpretability:** circuits, superposition, sparse autoencoders/dictionary learning, probing, activation steering, attribution, automated interpretability.
4. **Evaluation and red teaming:** capability and propensity evals, dangerous-capability evals, jailbreaks, robustness, deception and scheming evals, sandbagging, eval awareness.
5. **Agent and multi-agent safety:** prompt injection, tool-use risks, monitoring, collusion, strategic deception in agent environments.

## Resources

| | Resource | Hours | Notes |
|---|---|---:|---|
| ★ | [BlueDot Impact: AGI Strategy (25 h)](https://bluedot.org/courses/agi-strategy), then [Technical AI Safety (30 h)](https://bluedot.org/courses/technical-ai-safety) | 55 | Free, cohort-based courses: you apply to a cohort and meet weekly. AGI Strategy is the recommended first step; the technical course covers current techniques, open problems and where to contribute. Check current intake dates; reading materials may be usable independently, but the course itself is cohort-run. |
| ★ | [ARENA curriculum](https://arena.education/) | 150-250 | Code-first exercises: building transformers, mech interp with TransformerLens, RL/RLHF, evals (Inspect), alignment science. Free; also taught in-person in London (e.g., ARENA 9.0 ran Oct 5 to Nov 6, 2026). Self-study is possible with the public notebooks. |
| ★ | [Neel Nanda: Getting started in mechanistic interpretability](https://www.neelnanda.io/mechanistic-interpretability) and the [Transformer Circuits thread](https://transformer-circuits.pub/) | 60 | The practical entry point into the field. |
| ★ | [UK AISI Inspect evals framework](https://inspect.aisi.org.uk/) | 15 | Standard open eval tooling. Build an eval end to end. |
| Companion | [CAIS: Introduction to ML Safety](https://course.mlsafety.org/) | 40 | Robustness, monitoring, alignment, systemic safety from an ML-research angle. |
| Companion | [Alignment Forum](https://www.alignmentforum.org/) and [Anthropic Alignment Science blog](https://alignment.anthropic.com/) | ongoing | Where current research is discussed and published. |
| Depth | [MATS](https://www.matsprogram.org/) (mentored research program), Anthropic Fellows and similar programs; BlueDot project sprints | n/a | The path from learning to doing; apply once you have a reproduction and a small project. |
| Depth | Berkeley Agentic AI MOOC safety and security lectures | 5 | Agent-specific threats. |

## Papers (in order)

Concrete Problems in AI Safety (1606.06565) -> Deep RL from Human Preferences (1706.03741) -> Constitutional AI (2212.08073) -> A Mathematical Framework for Transformer Circuits (transformer-circuits.pub, 2021) -> In-context Learning and Induction Heads (2209.11895) -> Progress measures for grokking (2301.05217) -> Towards Monosemanticity (transformer-circuits.pub, 2023) and Sparse Autoencoders find interpretable features (2309.08600) -> Scaling Monosemanticity (transformer-circuits.pub, 2024) -> Weak-to-strong generalization (2312.09390) -> Sleeper Agents (2401.05566) -> Alignment faking in LLMs (2412.14093) -> Indirect prompt injection (2302.12173). Also: AI Control (2312.06942), AgentDojo (2406.13352), LLM deception sandboxes and detection work (e.g., the Among Us agentic-deception sandbox by Golechha and Garriga-Alonso), and recent AI-control papers.

## Projects

1. **Replicate a mech-interp result** (induction heads, IOI circuit, or a small SAE) with TransformerLens on a small model.
2. **SAE or probe project**: train a sparse autoencoder or linear probes for a concept; evaluate feature quality and causal effect via steering/ablation.
3. **Eval build**: design a propensity or capability eval in Inspect with a rigorous methodology; check for contamination and prompt sensitivity.
4. **Red-team report**: systematic jailbreak/prompt-injection study of an open model or agent with mitigation tests.
5. **Deception/scheming study** in a multi-agent or game environment: measure, detect (probes/monitors) and, where possible, compare against human behavior.
6. **Capstone**: a short research paper or a workshop/Alignment Forum post with reproducible code.

## Done when

You can reproduce a published interpretability or eval result, design a new small experiment with proper controls, and clearly separate what is established from what is speculation.
