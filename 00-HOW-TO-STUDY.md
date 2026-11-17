# How to study

## The completion rule

An item is **done** when you can explain it without notes, implement the key part yourself, and say how it fails. Watching is the entry fee, not the work.

## A week at 20 hours

| Day | Focus | Hours |
|---|---|---:|
| Mon | New material: course or reading | 3 |
| Tue | Code along or implement it yourself | 3 |
| Wed | Code along or implement it yourself | 3 |
| Thu | Experiment: write your prediction first, then run | 3 |
| Fri | Project work | 3 |
| Sat | Project work, or catch up | 4 |
| Sun | Review notes, plan next week | 1 |

At 10 h/week, halve each block. Rest weeks are fine; do not skip the review.

## Resource labels

| Label | Meaning |
|---|---|
| ★ | Do it, in order. |
| Optional | Skip unless you have a reason. |

## Projects

One GitHub repo, one folder per project (see [Projects](projects/README.md)). Each folder has a `README.md`, a way to run it with one command, and a `report.md` that says what you predicted, what happened, and where it failed.

Habits that save time:

- Write the expected result **before** you run an experiment.
- Change one thing at a time.
- Keep a held-out test set you do not touch until the end.
- Before a big run, overfit one tiny batch on a small model.
- Report failed runs. They are the useful part.

## Compute

| Stage | What you need |
|---|---|
| 1-3 | Any laptop. Free Colab or Kaggle GPU for the GPT run. |
| 4 | A laptop with 16 GB RAM can run small models. 8 GB or more of GPU memory, or an Apple Silicon Mac with 16 GB or more, runs 7-8B models comfortably. |
| 5-6 | Same as stage 4. Fine-tuning small models fits free Colab or Kaggle GPUs. |
| Research | Rent a cloud GPU only after the idea already works at small scale. |

## Using AI assistants

Use them as a tutor and reviewer, not as the author. Try first, then ask for a critique. For the from-scratch projects (autograd, tokenizer, GPT, agent loop) write the core yourself. Use assistants freely for boilerplate, plotting and setup.

## When you are stuck

1. Shrink the problem until it works, then grow it.
2. Re-derive on paper.
3. Read a minimal implementation (nanoGPT, nanochat, llama.cpp examples), close it, and write yours.
4. Ask a specific question with a minimal example.
