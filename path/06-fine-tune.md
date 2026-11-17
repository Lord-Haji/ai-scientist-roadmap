# Stage 6: Fine-tune and post-train open models

**Weeks 27-30 · about 80 h · output: a fine-tuned model you can run locally, with evidence it is better**

Fine-tuning is a tool of last resort, not first. Try prompting, then retrieval. Fine-tune when you need a fixed style or format, lower cost on a narrow task, or behaviour prompts cannot reach. This stage teaches you to do it and, as important, to prove it helped.

## Week 27: Decide, then prepare data

| | Resource | Hours | Notes |
|---|---|---:|---|
| ★ | Chip Huyen, *AI Engineering*: the finetuning chapters | 6 | When to fine-tune, and when not to. |
| ★ | [Hugging Face LLM Course](https://huggingface.co/learn/llm-course): fine-tuning chapters | 8 | Datasets, tokenization, the `Trainer`. |
| ★ | Chat templates and data format: learn the template for your chosen model | 3 | The most common silent bug in fine-tuning. |
| ★ | Build a dataset of 500-2,000 high-quality examples for one narrow task | 12 | Quality beats quantity. Hold out 100 examples and never train on them. |

## Weeks 28-29: LoRA and QLoRA

| | Resource | Hours | Notes |
|---|---|---:|---|
| ★ | [Unsloth](https://docs.unsloth.ai/) notebooks, or [TRL](https://huggingface.co/docs/trl) with [PEFT](https://huggingface.co/docs/peft) | 15 | Fine-tune a 1B-8B model with LoRA/QLoRA on a single consumer or free-tier GPU. |
| ★ | Papers: [LoRA (2106.09685)](https://arxiv.org/abs/2106.09685) and [QLoRA (2305.14314)](https://arxiv.org/abs/2305.14314) | 4 | Why a small low-rank update works. |
| ★ | [Hugging Face smol course](https://github.com/huggingface/smol-course) | 10 | A practical course on tuning small models. |
| ★ | Evaluate before and after on your held-out set, with confidence intervals | 6 | A gain smaller than the noise is not a gain. |
| ★ | Merge the adapter, convert to GGUF, quantize, run it in Ollama | 5 | Closes the loop with Stage 4. |

## Week 30: Preference tuning and reasoning with RL

| | Resource | Hours | Notes |
|---|---|---:|---|
| ★ | Paper: [DPO (2305.18290)](https://arxiv.org/abs/2305.18290) and a DPO run with TRL | 8 | Train on preference pairs without a separate reward model. |
| ★ | Paper: [DeepSeek-R1 (2501.12948)](https://arxiv.org/abs/2501.12948) | 4 | Reinforcement learning with verifiable rewards (RLVR) for reasoning. |
| ★ | A tiny GRPO run with TRL or Unsloth on a task with an automatic checker (for example arithmetic or unit tests) | 10 | A toy, but you will see reward rise and understand the loop. |

## Project 6: Fine-tune vs prompt study (about 20 h)

- [ ] Task, data, split, and why fine-tuning might help.
- [ ] Baselines: the base model with a good prompt, and a larger model with a good prompt.
- [ ] Your LoRA model, scored on the same held-out set with error bars.
- [ ] Cost and speed table: training time, memory, tokens per second, quality.
- [ ] A clear answer: did fine-tuning beat prompting, and by how much?
- [ ] The model is published or reproducible, and runs in Ollama.

## Done when

- [ ] You have fine-tuned and served a model on your own hardware.
- [ ] You can explain LoRA, SFT, DPO and RLVR in one paragraph each.
- [ ] Project 6 is on GitHub.

## You have finished the build phase

You can now run, serve, evaluate, build with, and fine-tune open-weight LLMs. That is a strong practical skill set.

- Want a job first? Use [the career files](../reference/career/job-ready.md) and the [side quests](../SIDE-QUESTS.md).
- Want research? Continue to [the research phase](../research/README.md).
