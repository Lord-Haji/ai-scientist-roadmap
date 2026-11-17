# Stage 3: Transformers and LLM internals

**Weeks 13-16 · about 80 h · output: a GPT you trained yourself**

After this stage no part of an LLM is a black box: tokens, attention, training loop, sampling.

## Weeks 13-14: Build GPT

| | Resource | Hours | Notes |
|---|---|---:|---|
| ★ | [Jay Alammar: The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/) | 2 | Visual first pass. |
| ★ | [3Blue1Brown: Neural networks, chapters on attention and transformers](https://www.3blue1brown.com/topics/neural-networks) | 2 | Intuition for attention. |
| ★ | [Karpathy Zero to Hero](https://karpathy.ai/zero-to-hero.html): **Let's build GPT**, then **Let's build the GPT Tokenizer** | 15 | Code along. Write your own BPE tokenizer. |
| ★ | Same course: **Let's reproduce GPT-2 (124M)** | 12 | Training at scale: mixed precision, gradient accumulation, learning-rate schedule. You need a GPU for the full run; use a rented one only after the small version works on CPU. |
| ★ | Read *Attention Is All You Need* ([arXiv 1706.03762](https://arxiv.org/abs/1706.03762)) | 3 | After the videos it will read easily. |

## Weeks 15-16: A second pass from a different angle

| | Resource | Hours | Notes |
|---|---|---:|---|
| ★ | [Sebastian Raschka: Build a Large Language Model (From Scratch)](https://github.com/rasbt/LLMs-from-scratch) | 30 | Chapters on attention, the GPT model, pretraining, and loading pretrained weights. The code repo is free. |
| ★ | [Hugging Face LLM Course](https://huggingface.co/learn/llm-course), chapters 1-4 | 10 | The `transformers` library: models, tokenizers, datasets, the Hub. You will use it every day from here on. |
| ★ | The Llama 3 paper, skim sections on architecture and training ([arXiv 2407.21783](https://arxiv.org/abs/2407.21783)) | 3 | See a real frontier-scale recipe. |
| Optional | [Stanford CS224N: NLP with Deep Learning](https://web.stanford.edu/class/cs224n/) | 70 | Broader NLP background. Needed for the research phase only if you pick a language-model branch. |

## Things you must be able to explain

- What the KV cache is and why it makes generation fast.
- Why a 7B model needs about 14 GB in 16-bit precision (parameters times bytes).
- What RoPE, RMSNorm, SwiGLU and grouped-query attention change versus the 2017 transformer. Use the Llama 3 paper to look each up.

## Project 3: your own GPT (about 20 h)

- [ ] Train a small GPT on a text corpus you care about (your own writing, a book, code).
- [ ] Your tokenizer round-trips text exactly.
- [ ] Plot validation loss against model size for at least three sizes.
- [ ] Generate text with temperature and top-p, and show what each setting does.
- [ ] Write what surprised you in `report.md`.

## Done when

- [ ] You can sketch a decoder-only transformer with tensor shapes from memory.
- [ ] Project 3 is on GitHub.

Next: [Stage 4: Open-weight and local LLMs](04-local-llms.md).
