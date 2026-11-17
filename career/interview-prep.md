# Interview Prep

Start by the end of Level 1 and keep a weekly rhythm. Most failures come from lack of reps, not lack of intelligence.

## 1. Coding

- Follow the [NeetCode roadmap](https://neetcode.io/roadmap): arrays/hashing, two pointers, stack, binary search, sliding window, linked list, trees, tries, heap, backtracking, graphs, DP, greedy, intervals, bit tricks.
- Aim for 5-10 problems/week for 6-12 months before a serious interview cycle (3-5/week is a maintenance rate, not a preparation rate). Re-solve what you failed after 1 week. Always say your approach, complexity, and edge cases aloud.
- Practice in the language of the interview (Python is usually fine).

## 2. System design

- Resources: *Designing Data-Intensive Applications*, Alex Xu's *System Design Interview*, [system-design-primer](https://github.com/donnemartin/system-design-primer).
- Practice: URL shortener, feed, chat, rate limiter, search, notification system.
- **ML system design**: *Designing Machine Learning Systems* (Huyen), *AI Engineering* (Huyen). Frame: requirements and metrics -> data -> baseline -> model -> training -> evaluation (offline/online) -> serving -> monitoring -> iteration. Examples: recommendation system, search ranking, fraud detection, RAG assistant, content moderation, an LLM agent platform.

## 3. ML fundamentals (be fluent)

- Loss functions and their probabilistic meaning, bias/variance, regularization, cross-validation, metrics (precision/recall, ROC/PR, calibration), class imbalance, leakage.
- Optimization: SGD vs Adam, learning-rate schedules, initialization, normalization.
- Deep learning: backprop on a whiteboard, attention math with shapes, why residuals/LayerNorm, KV cache.
- LLMs: tokenization, pretraining vs SFT vs RLHF/DPO, scaling laws, hallucination, evals, RAG vs fine-tuning, quantization.
- Be ready to derive: softmax cross-entropy gradient, attention complexity, Adam update, KL divergence.

## 4. Research interviews (research roles)

- Deep dive into your own papers/projects: why this design, what failed, what you would change, what would invalidate the result.
- Paper discussion: given an unseen paper, summarize, critique, propose a follow-up.
- Research taste questions: what are the most important open problems in your area and why?
- Sometimes a live coding of an ML mechanism (attention, a training loop, a loss, a sampler).

## 5. Behavioral

Prepare 6-8 stories (conflict, failure, leadership, ambiguity, impact, learning) in STAR format with numbers.

## 6. Take-home / project interviews

Treat as a mini research project: README, assumptions, baseline, evaluation, error analysis, next steps. Time-box and be explicit about trade-offs.

## Weekly rhythm (example)

| Day | Practice |
|---|---|
| Mon | 2 coding problems |
| Wed | 1 system or ML design problem, out loud |
| Fri | 2 coding problems + 1 ML derivation |
| Sun | Mock interview with a peer, or record yourself |
