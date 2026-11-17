# Projects

Only **two kinds** of project, so there is nothing to puzzle over:

1. **Stage projects.** One small project per stage. They prove you did the stage.
2. **Two big ones.** The **flagship** at the end of Stage 5 and the **research project** at the end of a research branch.

Keep them all in one repo of yours:

```
my-ai-roadmap/
  01-tabular-ml/
  02-from-scratch-nets/
  03-my-gpt/
  04-local-model-bench/
  05-flagship-local-assistant/     <- the flagship
  06-finetune-vs-prompt/
  gate-reproduction/               <- research phase only
  research-project/                <- research phase only
  papers/                          notes, one file per paper
```

| Project | Stage | What | Proves |
|---|---|---|---|
| 1. Tabular ML | [1](../path/01-foundations.md) | Baseline vs models, error bars | You evaluate honestly |
| 2. From-scratch nets | [2](../path/02-neural-nets.md) | Your autograd, makemore, CIFAR | You understand backprop |
| 3. My GPT | [3](../path/03-transformers.md) | Train a small GPT, scaling plot | You understand LLM training |
| 4. Local model bench | [4](../path/04-local-llms.md) | 3 models, 3 quantizations, your tasks | You can pick and run open models |
| **5. Flagship** | [5](../path/05-build-llm-apps.md) | Local-first RAG + tools + evals, in Docker | You can build and measure an LLM system |
| 6. Fine-tune vs prompt | [6](../path/06-fine-tune.md) | LoRA model vs prompting, with error bars | You know when tuning pays off |
| Gate | [Research](../research/README.md) | Reproduce and ablate one paper result | You can do research |
| **Research project** | [R1-R3](../research/README.md) | One question in your branch | You can produce new evidence |

## Quality bar

- Runs from a clean clone with one command.
- A `report.md` with predictions, results, failures and honest limits.
- Seeds fixed, configs saved, a few tests for the core code.
- Public if you are comfortable. A project nobody can run is not a portfolio item.

Start at CPU or small-model scale. Pay for GPU time only after a small run shows the effect.
