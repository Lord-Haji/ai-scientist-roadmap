# Audit of the Older Coursera-Style Data Science Roadmap

The older roadmap you gave (IBM Data Science Certificate, Ng ML, Imperial Math for ML, Stanford Algorithms, Deep Learning Specialization, TensorFlow courses, AWS/GCP, NLP, Spark, RL, IBM Full Stack) was a reasonable 2020-2022 data-science path. For an LLM/agents/VLM research goal in 2026 it needs these changes. Course-by-course:

| Old item | Verdict | What this curriculum does instead |
|---|---|---|
| IBM Data Science Professional Certificate | **Weak signal, shallow.** Fine as a gentle start to Python/SQL/pandas, but not a substitute for stats or ML depth, and employers do not treat it as strong evidence. | Python/SQL basics in [L0](L0-foundations.md) and [L3](L3-classical-ml.md) (Kaggle Learn, ISLP, a real end-to-end tabular project); Track H for a DS job. |
| Andrew Ng ML (Stanford/Coursera) | **Keep, via the 2022 Python relaunch.** Original Octave version is obsolete. | [L3](L3-classical-ml.md): Ng's *Machine Learning Specialization* as on-ramp, **CS229** as the rigorous core. |
| UW ML Specialization | **Optional.** | Covered by CS229 + ISLP. |
| Imperial *Mathematics for ML* | **Keep as a companion.** | [L2](L2-math.md): MIT 18.06 + Stat 110 + MML book are stronger primary sources. |
| Stanford Algorithms Specialization | **Keep, upgrade.** Great for algorithmic thinking. | [L1](L1-cs-core.md): Princeton Algorithms + MIT 6.006 + the Roughgarden specialization as companion; interview practice added. |
| Deep Learning Specialization (Ng) | **Fine on-ramp, not a research foundation.** Lectures good; programming assignments aged. | [L4](L4-deep-learning.md): Karpathy Zero to Hero + *Understanding Deep Learning* + CMU 10-414 for depth. |
| TensorFlow in Practice / Advanced TensorFlow | **Outdated for research.** PyTorch dominates research; JAX at Google-style labs. | PyTorch throughout; JAX as optional depth. |
| AWS Practical Data Science / GCP Big Data and ML | **Optional, job-specific.** | [Track G](../tracks/G-applied-ai-engineering.md): cloud basics + deployment when job-hunting; pick one cloud. |
| DeepLearning.AI NLP Specialization | **Superseded.** Pre-LLM-era NLP content. | CS224N + CS336 + HF LLM Course ([L5](L5-transformers-llms.md)). |
| U Alberta RL Specialization | **Good, rigorous fundamentals.** | [L6A](L6-frontier-core.md): Sutton-Barto + CS234; the Alberta specialization is a fine alternative companion. |
| Databricks Spark | **Optional.** Needed only for big-data engineering roles. | Track H / G, as needed. |
| IBM Full Stack Cloud Developer | **Low priority.** | [L1](L1-cs-core.md) web service project + Docker/CI is enough. |

## Biggest gaps in the old roadmap (now filled)

1. Computer science core (systems, databases, distributed systems, software engineering).
2. Deep learning internals (autograd, frameworks) and Transformer/LLM training from scratch.
3. Post-training and RL for LLMs; reasoning models.
4. Agents, tool use, MCP, multi-agent systems, agent evaluation and security.
5. Vision-language and generative models.
6. Safety, alignment, interpretability, evaluation.
7. Paper reading, reproduction, research skills.
