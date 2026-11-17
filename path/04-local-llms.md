# Stage 4: Open-weight and local LLMs

**Weeks 17-20 · about 80 h · output: a benchmark of open models on your own hardware and a local stack you control**

Open-weight models (weights you can download and run) are the base for everything after this stage. You learn to pick a model, fit it into your memory, quantize it, serve it, and judge it on your own tasks.

## Vocabulary first

| Term | Meaning |
|---|---|
| Open weights | You can download the model. Not the same as open source: training data and code may be closed, and the license may restrict use. |
| Quantization | Storing weights in fewer bits (for example 4-bit) so the model fits in less memory, with a small quality loss. |
| GGUF | The file format used by llama.cpp, Ollama and LM Studio. One file holds weights and metadata. |
| Dense vs MoE | A mixture-of-experts model has many parameters but uses only some per token ("active parameters"). It needs memory for all of them, but runs faster than its size suggests. |
| Context length | How many tokens the model can read. Longer context costs more memory (the KV cache). |

## Memory rule of thumb

Weights need about `parameters × bits / 8` bytes. Then add the KV cache and about 1-2 GB overhead.

| Model size | 16-bit | 8-bit | 4-bit (for example Q4_K_M) |
|---|---:|---:|---:|
| 1B | 2 GB | 1 GB | 0.7 GB |
| 8B | 16 GB | 8.5 GB | 5 GB |
| 14B | 28 GB | 15 GB | 9 GB |
| 32B | 64 GB | 34 GB | 19 GB |
| 70B | 140 GB | 75 GB | 40 GB |

Rough numbers; check the file size on the model page. On Apple Silicon the unified memory is shared, so use total RAM minus a few GB. No GPU: use [Google Colab](https://colab.research.google.com/) or [Kaggle notebooks](https://www.kaggle.com/) for free GPU time, and rent a cloud GPU only when a run needs it.

## Week 17: Run models locally

| | Resource | Hours | Notes |
|---|---|---:|---|
| ★ | [Ollama](https://github.com/ollama/ollama): pull models, write a `Modelfile`, call the HTTP API from Python | 6 | Ollama exposes an OpenAI-compatible endpoint, so most tools can point at it. |
| ★ | [LM Studio](https://lmstudio.ai/) | 2 | A GUI for trying many models quickly. |
| ★ | [llama.cpp](https://github.com/ggml-org/llama.cpp): build it, run `llama-cli` and `llama-server` | 8 | The engine under many local tools. Learn the flags for context size, GPU layers, threads. |
| ★ | [Hugging Face: GGUF docs](https://huggingface.co/docs/hub/gguf) | 2 | Naming such as Q4_K_M, Q5_K_M, Q8_0. Know the trade-off. |
| Optional | [MLX LM](https://github.com/ml-explore/mlx-lm) (Apple Silicon only) | 4 | The fastest route on a Mac. |

**Exercise:** write a 20-line script that estimates memory for a given model size, bit width and context length. Check it against what you really see.

## Week 18: Choose models

| | Resource | Hours | Notes |
|---|---|---:|---|
| ★ | [Hugging Face model hub](https://huggingface.co/models): read five model cards | 4 | Parameters, context, license, languages, benchmarks the authors report, and what they do *not* report. |
| ★ | [OSI: Open Source AI Definition](https://opensource.org/ai/open-source-ai-definition) | 1 | Why "open weights" is not "open source". |
| ★ | Try one model from each major family and size class: for example Llama, Qwen, Gemma, Mistral, DeepSeek, OpenAI gpt-oss, and a small one such as SmolLM or Phi | 8 | Families and versions change every few months. Check what is current on the Hub trending page before you pick. |
| ★ | [EleutherAI lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) | 8 | Run a standard benchmark on a local model. Learn why scores vary with prompt format. |
| Optional | [r/LocalLLaMA](https://www.reddit.com/r/LocalLLaMA/) | ongoing | Where practical results appear first. Treat claims as leads, then test them yourself. |

## Week 19: Serve models

| | Resource | Hours | Notes |
|---|---|---:|---|
| ★ | [vLLM docs](https://docs.vllm.ai/): serve one model, send concurrent requests | 8 | Continuous batching and paged KV cache. Needs an NVIDIA GPU (use a rented one). Read the PagedAttention paper ([arXiv 2309.06180](https://arxiv.org/abs/2309.06180)). |
| ★ | Structured output: JSON schema and grammar-constrained decoding in llama.cpp or vLLM | 4 | Makes small models reliable enough for tools. |
| ★ | [Open WebUI](https://github.com/open-webui/open-webui) in front of Ollama | 3 | A chat UI you host yourself. |
| ★ | Measure it: tokens per second, time to first token, memory, at batch size 1 and at 8 | 5 | Write the numbers down. They go into the project. |

## Week 20: Embeddings and your private stack

| | Resource | Hours | Notes |
|---|---|---:|---|
| ★ | [Sentence Transformers](https://www.sbert.net/) | 4 | Run a local embedding model. |
| ★ | [MTEB leaderboard](https://huggingface.co/spaces/mteb/leaderboard) | 1 | How embedding models are compared, and why you must test on your own data. |
| ★ | Docker Compose: Ollama + Open WebUI + an embedding service in one file | 4 | A stack anyone can start with one command. |
| ★ | Write a one-page decision note: when local beats a hosted API (privacy, cost at volume, offline, control) and when it does not (quality ceiling, hardware, maintenance) | 2 | Honest trade-offs are the point. |

## Project 4: Local model bench (about 20 h)

- [ ] Pick 3 open models and 3 quantization levels of one of them.
- [ ] Write 30 or more test questions from a task you care about, with expected answers or a checking rule.
- [ ] Record for each: memory use, tokens per second, time to first token, and accuracy on your questions.
- [ ] Plot quality against memory and speed. Which quantization is the sweet spot on your machine?
- [ ] End with a recommendation: which model for which job, and why.

## Done when

- [ ] You can look at a model card and say whether it fits your hardware and license needs.
- [ ] You serve a local model behind an OpenAI-compatible API and call it from Python.
- [ ] Project 4 is on GitHub with the table and plots.

Next: [Stage 5: Build with LLMs](05-build-llm-apps.md).
