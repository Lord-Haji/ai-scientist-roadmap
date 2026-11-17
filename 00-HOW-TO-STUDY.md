# How to Study This Curriculum

## The completion rule

A course or book is **done** when you can:

1. explain the main idea without notes,
2. derive the central math,
3. implement the important mechanism at small scale,
4. name its failure modes,
5. reproduce one non-trivial result.

Watching videos is the entry fee, not the work.

## The weekly loop (10-15 h/week)

| Day | Focus | Typical block |
|---|---|---|
| Mon | Theory and math | 60 min concepts, 45 min derivation, 15 min recall |
| Tue | Implementation | 20 min recall, 90 min coding, 10 min notes |
| Wed | Implementation | 90 min coding, 30 min tests and debugging |
| Thu | Experiments | 30 min prediction, 60 min experiment, 30 min analysis |
| Fri | Paper (from Level 3 onward) | 45 min reading, 60 min reproduction, 15 min notes |
| Weekend | Review and spaced repetition | 60 min |

For serious experiments **write the predicted outcome before running** it. This is how you build taste.

## Resource labels used in every level file

| Label | Meaning |
|---|---|
| ★ **Core** | Follow as the main course. Part of the must-do spine. |
| **Companion** | Read selectively alongside a core resource. |
| **Reference** | Look things up when needed. |
| **Depth** | Optional deepening; take when a track or project needs it. |

## Test-out checks

Each level starts with a short test-out. If you can do it cold in the stated time, skip the level or the sub-block. Be honest: run the code, derive the equation on paper.

## Project standard

Keep **one long-lived repository** of your own, one folder per project:

```
my-ai-from-first-principles/
  00-.../  01-.../  ...
  papers/            notes and reproductions
```

Each serious project contains `README.md`, `src/`, `tests/`, `experiments/`, `configs/`, `report.md`. The report states: problem, relevant math, implementation, **predictions made before experiments**, results, failure analysis, reproduction target, conclusions.

Rules of experimental hygiene:

- fixed seeds where appropriate, and several seeds when variance matters,
- keep configs and raw metrics, never only the final number,
- strictly separate train / validation / test,
- report failed runs,
- ablations change **one** variable at a time.

Before scaling up any experiment: unit-test on CPU, overfit one tiny batch, run a tiny model, profile.

## Notes system

- One note per paper (template in [`research-skills/paper-note-template.md`](research-skills/paper-note-template.md)).
- One "derivations" notebook per level: write every key derivation by hand once.
- Spaced repetition (Anki or similar) for definitions, shapes, and standard equations only. Not for trivia.

## Learning with AI assistants

Use LLMs as tutors and reviewers, not as the author of your solutions:

- Attempt first, then ask for a critique of your attempt.
- Ask for counter-examples and edge cases to your understanding.
- For from-scratch projects (autograd, GPT, RL loop) write the core yourself. The point is the struggle.
- Use coding assistants freely for tooling, plotting, boilerplate, and infra.

## Compute plan

| Phase | Work | Compute |
|---|---|---|
| Levels 0-3 | math, classical ML, small nets | CPU / laptop |
| Level 4-5 | CNNs, small GPT, small diffusion/VLM | consumer GPU or free cloud notebooks |
| Level 5-6 end, tracks | 100M+ param runs, RL post-training, serving | rented cloud GPU, only when an experiment justifies it |

Rule: never rent big compute for something you have not first run on a tiny model on CPU.

## When you are stuck

1. Shrink the problem until it works, then grow it.
2. Re-derive on paper.
3. Read someone else's minimal implementation (nanoGPT, nanochat, CleanRL, minGPT-style repos), then close it and re-write yours.
4. Ask a specific question in a community with your minimal reproduction.
