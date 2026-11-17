# Projects and Capstones

Every level has projects. Keep them in **one long-lived repo of your own**, one folder per project, each with `README.md`, `src/`, `tests/`, `experiments/`, `configs/`, `report.md`. See [`00-HOW-TO-STUDY.md`](../00-HOW-TO-STUDY.md) for the standard.

## Suggested repo layout

```
my-ai-from-first-principles/
  00-scientific-python/
  01-algorithms-kit/            (L1)
  02-mini-shell-or-kv-store/    (L1)
  03-web-service/               (L1)
  10-mini-numpy/                (L2)
  11-gradient-explorer/
  12-probability-lab/
  13-optimizer-lab/
  20-ml-from-first-principles/  (L3)
  21-tabular-end-to-end/
  30-neural-nets-from-numpy/    (L4)
  31-mini-pytorch/
  32-vision-evolution/
  33-reproduce-a-classic/
  40-sequence-evolution/        (L5)
  41-mini-foundation-model/
  42-modern-arch-lab/
  43-reproduce-gpt2-small/
  50-rl-lab/                    (L6)
  51-posttrain-lab/
  52-mini-vlm/
  53-flow-diffusion-lab/
  54-agent-lab/
  6x-track-projects/            (L7)
  papers/                       (notes + reproductions)
```

## The eight signature capstones (portfolio targets)

| # | Capstone | Proves |
|---|---|---|
| 1 | Build-your-own autograd + mini-framework (31) | You understand frameworks. |
| 2 | Small GPT family with scaling curves (41) | You can train and reason about LLMs. |
| 3 | Post-training: SFT -> DPO -> verifiable-reward RL (51) | You understand modern alignment/reasoning training. |
| 4 | Mini-VLM with ablations (52) | You understand multimodal models. |
| 5 | Framework-free agent + evaluation harness (54) | You can build and measure agents. |
| 6 | Multi-agent study with failure taxonomy (Track B) | You can do multi-agent research. |
| 7 | Reproduced + ablated paper with report (Level 8 gate) | You do research. |
| 8 | Deployed, monitored LLM product with evals (Track G) | You ship. |

## Project quality bar

- Reproducible in one command from a clean clone.
- A report with predictions, results, failure analysis, and honest limits.
- Tests for the numerical core; seeds fixed; configs saved.
- Public (if you are comfortable) with a clear README: a project nobody can run is not a portfolio item.

## Choosing scale

Always start with CPU-sized versions. Spend GPU money only when a small run already shows the effect you want to test.
