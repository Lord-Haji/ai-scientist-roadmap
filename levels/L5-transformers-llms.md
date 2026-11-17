# Level 5: Transformers and Large Language Models

**Goal:** understand LLMs end to end: tokenization, architecture, training, scaling, data, evaluation, inference. Build a small GPT yourself and train a model family.  
**Time:** 350-500 h. **Prerequisites:** Level 4 (and Level 1 systems for 5.2).

## Test-out

- Explain scaled dot-product attention, multi-head attention, positional encoding (RoPE), and why KV caching works, with shapes.
- Implement a BPE tokenizer and a decoder-only Transformer in PyTorch and train it on a small corpus.
- Explain the Chinchilla result and what "compute-optimal" means; estimate FLOPs for a training run (6ND rule of thumb).

## 5.1 NLP and the road to Transformers (★)

| | Resource | Hours | Notes |
|---|---|---:|---|
| ★ | [Stanford CS224N: NLP with Deep Learning](https://web.stanford.edu/class/cs224n/) | 70 | Word vectors, RNNs, attention, Transformers, pretraining, post-training, LLM topics. Use the latest offering (the 2026 offering is taught by Diyi Yang and Yejin Choi, with a Manning guest lecture). |
| Companion | [Jay Alammar: The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/) | 2 | Best visual first pass. |
| ★ | [Andrej Karpathy: Let's build GPT, tokenizer, and "Let's reproduce GPT-2"](https://karpathy.ai/zero-to-hero.html) | 15 | Code along. |
| Depth | CMU 11-711 Advanced NLP and CMU LLM courses (check the newest offering) | 60 | Broader NLP coverage than CS224N. |
| Depth | [Stanford CS25: Transformers United](https://web.stanford.edu/class/cs25/) | 30 | Guest talks on frontier topics; watch selectively. |

## 5.1b GPU programming and PyTorch internals (★ before CS336)

CS336's assignments (Triton FlashAttention, DDP) assume this. Do it first.

| | Resource | Hours | Notes |
|---|---|---:|---|
| ★ | [Triton tutorials](https://triton-lang.org/main/getting-started/tutorials/index.html) | 15 | Write fused softmax, matmul, attention kernels. |
| ★ | *Programming Massively Parallel Processors* (Hwu, Kirk, El Hajj), Ch. 1-6 | 25 | GPU memory hierarchy, tiling, occupancy. |
| ★ | PyTorch profiler, `torch.compile`, automatic mixed precision, DDP basics (official docs/tutorials) | 15 | Find where time and memory go. |
| ★ | Numerics: floating point, bf16/fp16/fp8, loss scaling, why training goes NaN | 8 | Read the mixed-precision docs and Karpathy's debugging advice. |
| Companion | [GPU MODE](https://www.gpumode.com/) lectures | 20 | Community lecture series. |
| Companion | [JAX docs](https://docs.jax.dev/) and the Google DeepMind "How to Scale Your Model" scaling book | 30 | Several labs use JAX; the scaling book is an excellent systems primer. |

## 5.2 Build an LLM (★)

| | Resource | Hours | Notes |
|---|---|---:|---|
| ★ | [Stanford CS336: Language Modeling from Scratch (Spring 2026 offering)](https://cs336.stanford.edu/) | 150-250 | Tokenization, Transformer implementation, optimization, GPU/Triton kernels, FlashAttention, parallelism, scaling laws, data, evaluation, inference, alignment/RL. Public lectures and assignments; the hardest, best-regarded from-scratch LLM course. Prereqs: strong Python/PyTorch, DL basics. |
| ★ | [Sebastian Raschka: *Build a Large Language Model (From Scratch)* + code](https://github.com/rasbt/LLMs-from-scratch) | 40 | Gentler companion to CS336. |
| ★ | [Karpathy nanochat](https://github.com/karpathy/nanochat) | 20 | Minimal full-stack pipeline: tokenizer, pretrain, mid-train, SFT, RL, eval, chat UI. Read the code end to end, then modify it. It was designed as the capstone of Eureka Labs' LLM101n. |
| Companion | [Hugging Face LLM Course](https://huggingface.co/learn/llm-course) | 25 | Transformers/Datasets/Tokenizers libraries, fine-tuning, evaluation. Job-useful. |
| Companion | [HF Ultra-Scale Playbook](https://huggingface.co/spaces/nanotron/ultrascale-playbook) | 15 | Data/tensor/pipeline/ZeRO parallelism explained with experiments. |
| Optional | [Generative AI with LLMs](https://www.coursera.org/learn/generative-ai-with-llms) (Coursera, DeepLearning.AI + AWS) | 15 | Short conceptual tour of pretraining, fine-tuning and RLHF; 4.7+ rated. Labs are mostly run-the-cells, and some learners report AWS charges from the SageMaker labs, so read the lab notes first. Skip it if you are doing CS336 and the HF LLM Course. |
| Depth | Lilian Weng's blog (attention, scaling, post-training, hallucination, etc.) | reference | Superb surveys. |

## 5.2b Evaluation methodology (★)

An LLM you cannot evaluate is an LLM you do not understand.

| | Resource | Notes |
|---|---|---|
| ★ | [EleutherAI lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) and [UK AISI Inspect](https://inspect.aisi.org.uk/) | Run standard benchmarks; build one custom eval. |
| ★ | Statistics for evals: confidence intervals and error bars on benchmark scores, paired comparisons, multiple seeds | Most reported "improvements" are within noise. |
| ★ | Contamination checks and held-out evals; LLM-as-judge biases (position, length, self-preference) and how to calibrate against human labels | Read CS336's evaluation lecture and recent evaluation-methodology papers. |
| Companion | HELM (2211.09110), MMLU (2009.03300), MMMU (2311.16502) | Know what benchmarks measure and where they break. |

## 5.3 Modern architecture and efficiency lab (★ for track A/F, recommended for all)

Study: RMSNorm, RoPE, SwiGLU, MQA/GQA, KV cache, FlashAttention, sparse MoE and routing, long-context methods (RoPE scaling/YaRN 2309.00071, ring attention 2310.01889, Lost in the Middle 2307.03172, RULER 2404.06654), state-space alternatives (Mamba), speculative decoding, quantization, LoRA/QLoRA. Also LLM data engineering: MinHash/near-duplicate removal, quality classifiers, data cards and licensing (see FineWeb, Dolma). Use **official technical reports** (Llama 3, DeepSeek-V3, Qwen, Mistral/Mixtral) instead of secondary summaries. Refresh this list when you start; models change quarterly.

## Papers inside Level 5

Word2vec; seq2seq; Bahdanau attention; **Attention Is All You Need**; BERT; GPT-2/GPT-3; Scaling Laws; Chinchilla; LLaMA 1/2/3; FlashAttention; RoPE; GQA; Switch/Mixtral; DeepSeek-V3; InstructGPT. Arxiv IDs and reading order in [`papers/README.md`](../papers/README.md).

## Projects

1. **`40-sequence-evolution`**: character n-gram, RNN, LSTM/GRU, attention seq2seq, small Transformer on one dataset; explain exactly what attention changes relative to recurrence.
2. **`41-mini-foundation-model`**: BPE tokenizer; decoder-only Transformer; train 5M -> 15M -> 50M -> 100M+ models and fit scaling curves; data pipeline (filtering, dedup, tokenization, clean val split); profile compute/memory; implement one optimized kernel (Triton/CUDA) or FlashAttention-style tiling; then SFT; **finish with an eval report** (benchmark scores with confidence intervals, a contamination check, error analysis).
3. **`42-modern-arch-lab`**: add GQA, RoPE, SwiGLU, a small sparse MoE and a long-context synthetic benchmark to your model; report loss, stability, active params/token, throughput, memory and expert utilization.
4. **`43-reproduce-gpt2-small`**: reproduce GPT-2 124M-level quality on a public dataset at a budget you can afford (nanoGPT/nanochat give you the baseline to beat).

## Done when

You can train a language model from scratch, reason about its compute, data and failure modes, and read a frontier technical report without unfamiliar boxes.
