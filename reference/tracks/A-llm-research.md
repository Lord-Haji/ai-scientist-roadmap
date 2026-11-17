# Track A: LLM Research and Training

**You become:** someone who can pretrain, post-train, scale, evaluate and diagnose LLMs.  
**Requires:** Levels 4, 5, 6A. **Time:** 300-600 h. Pairs well with Track F (systems) and E (RL).

## Learning goals

- Scaling laws and compute-optimal design; hyperparameter transfer; training stability.
- Data: sourcing, filtering, deduplication, mixtures, synthetic data, contamination.
- Architecture: attention variants, MoE, long context, state-space hybrids.
- Post-training: SFT, preference optimization, RLVR/GRPO, reasoning models, test-time compute.
- Evaluation: benchmarks, contamination, LLM-as-judge pitfalls, held-out evals you design.

## Resources

| | Resource | Notes |
|---|---|---|
| ★ | Finish [CS336](https://cs336.stanford.edu/) assignments including the scaling and alignment ones | The backbone of this track. |
| ★ | Technical reports, read closely: Llama 3 herd, DeepSeek-V3, DeepSeek-R1, Qwen2.5, Tulu 3 | One report per month; write a note for each. |
| ★ | [HF Ultra-Scale Playbook](https://huggingface.co/spaces/nanotron/ultrascale-playbook) | Parallelism intuition. |
| ★ | [nanochat](https://github.com/karpathy/nanochat) and nanoGPT speedrun-style repos | Study the optimization tricks; try to beat a baseline loss at fixed compute. |
| Depth | [HF TRL](https://huggingface.co/docs/trl), [OpenRLHF](https://github.com/OpenRLHF/OpenRLHF), [veRL](https://github.com/volcengine/verl) | RL post-training frameworks; read before building your own. |
| Depth | FineWeb paper (2406.17557), Dolma (2402.00159), the Pile (2101.00027) | Pretraining data recipes. |
| Depth | Lilian Weng posts on training/data/reasoning | Surveys. |

## Papers (in order)

GPT-3 -> Scaling Laws -> Chinchilla -> LLaMA 1/2/3 -> DeepSeek-V3 (MoE, MLA, multi-token prediction) -> InstructGPT -> DPO -> DeepSeekMath (GRPO) -> DeepSeek-R1 -> s1 test-time scaling (2501.19393) -> Scaling LLM test-time compute (2408.03314) -> Let's Verify Step by Step (2305.20050). IDs in [`papers/README.md`](../papers/README.md).

## Projects

1. **Scaling study**: train a model family at 4+ sizes with a fixed data recipe, fit scaling curves, predict a held-out larger run, report the error.
2. **Data ablation**: change one data-quality filter or mixture ratio at small scale; measure downstream eval differences with multiple seeds.
3. **Reasoning post-training**: GRPO/RLVR on a small model with a verifiable reward (math or code unit tests); analyze reward hacking and response-length behavior.
4. **Eval harness**: build a contamination-aware eval for a niche capability; compare against a public benchmark.
5. **Capstone**: reproduce a small-scale result from a recent technical report (e.g., an architectural change or a data trick) with ablations.

## Done when

You can propose, run and defend an experiment that changes one component of an LLM pipeline and show whether it helps at your scale, and you know what may not transfer to larger scale.
