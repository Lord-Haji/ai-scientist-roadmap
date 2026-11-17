# R1: Train and scale

**You become:** someone who can pretrain, post-train and scale language models, and reason about compute, data and RL for reasoning.  
**Time:** 250-350 h. **Needs:** Stages 1-6.

Do the steps in order.

| | Step | Resource | Hours | Notes |
|---|---|---|---:|---|
| ★ | 1 | GPU basics: [Triton tutorials](https://triton-lang.org/main/getting-started/tutorials/index.html) and the PyTorch profiler | 25 | Fused softmax and a matmul kernel; find where time and memory go. |
| ★ | 2 | [Stanford CS336: Language Modeling from Scratch](https://cs336.stanford.edu/) | 150-200 | The core. Tokenizer, transformer, optimizers, kernels, parallelism, scaling laws, data, evaluation, alignment. Do the assignments. Check the newest offering. |
| ★ | 3 | [Karpathy nanochat](https://github.com/karpathy/nanochat) | 20 | Read the full pipeline end to end, then change one stage. |
| ★ | 4 | [RLHF Book (Nathan Lambert)](https://rlhfbook.com/) | 15 | Reward models, DPO, RL with verifiable rewards. |
| ★ | 5 | [Sutton and Barto, *Reinforcement Learning*](http://incompleteideas.net/book/the-book-2nd.html), chapters 1-6 and 13 | 30 | Enough to understand policy gradients and PPO. |
| ★ | 6 | [Hugging Face Ultra-Scale Playbook](https://huggingface.co/spaces/nanotron/ultrascale-playbook) | 12 | Data, tensor and pipeline parallelism explained with experiments. |

**Papers, in order:** Scaling Laws (2001.08361) → Chinchilla (2203.15556) → FlashAttention (2205.14135) → InstructGPT (2203.02155) → PPO (1707.06347) → DeepSeekMath/GRPO (2402.03300) → DeepSeek-R1 (2501.12948) → Tulu 3 (2411.15124). Full list: [reference papers](../reference/papers/README.md).

## Research project (pick one)

- Fit scaling curves for three model sizes on your own data, and say when the fit breaks.
- Run an RLVR experiment on a verifiable task and study reward design, with at least three seeds.
- Ablate one modern architecture change (GQA, RoPE scaling, MoE) in your Stage 3 model.

## Done when

You can estimate the compute for a training run (`6 × parameters × tokens` FLOPs), diagnose a loss curve, and run a small RL post-training loop.

More depth, if you need it: [reference tracks A, E, F](../reference/tracks/A-llm-research.md).
