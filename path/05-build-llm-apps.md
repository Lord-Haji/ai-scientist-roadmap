# Stage 5: Build with LLMs (RAG, tools, agents, evals)

**Weeks 21-26 · about 110 h · output: your flagship project**

All work here runs on the local open-weight models from Stage 4. You may swap in a hosted API for comparison, but the project must work locally.

## Week 21: Prompts, structure, tool calling

| | Resource | Hours | Notes |
|---|---|---:|---|
| ★ | [Anthropic: Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) | 2 | Read before touching any framework. Prefer a simple workflow to a free-roaming agent. |
| ★ | Function calling with a local model through the Ollama or llama.cpp API | 8 | Define two tools, parse the call, run it, return the result. |
| ★ | [Hugging Face Agents Course](https://huggingface.co/learn/agents-course), units 1-2 | 8 | The basics of the agent loop. |

## Weeks 22-23: Retrieval (RAG) done properly

| | Resource | Hours | Notes |
|---|---|---:|---|
| ★ | Chip Huyen, *AI Engineering* (book): the chapters on RAG, evaluation and prompt engineering | 12 | The best end-to-end treatment. |
| ★ | [DeepLearning.AI short courses](https://www.deeplearning.ai/short-courses/): one on RAG, one on evaluation | 6 | Quick and practical. |
| ★ | Build it: chunking, a local embedding model, a vector index ([FAISS](https://github.com/facebookresearch/faiss) or [Qdrant](https://qdrant.tech/documentation/)), keyword search (BM25), a reranker | 20 | Combine keyword and vector search. Measure recall@k against questions you wrote by hand. |
| ★ | Paper: [Retrieval-Augmented Generation (Lewis et al.)](https://arxiv.org/abs/2005.11401) | 2 | Origin of the term. |

## Week 24: Agents without magic

| | Resource | Hours | Notes |
|---|---|---:|---|
| ★ | Write a ReAct-style loop yourself: plan, call tool, observe, stop. About 100 lines, no framework | 10 | Add a step limit and a spend limit. |
| ★ | [Model Context Protocol](https://modelcontextprotocol.io/) and the [HF MCP Course](https://huggingface.co/learn/mcp-course) | 10 | Build one MCP server with a read-only tool and use it from your agent. |
| ★ | Prompt injection: read the [indirect prompt injection paper](https://arxiv.org/abs/2302.12173) and test your agent against a malicious document | 4 | Never give an agent a tool you would not give a stranger who can write into its context. |
| Optional | One framework (LangGraph, smolagents or similar) | 6 | Learn it only after you can build the loop yourself. |

## Week 25: Evals and tracing

The skill that separates demos from products.

| | Resource | Hours | Notes |
|---|---|---:|---|
| ★ | [Hamel Husain: Your AI product needs evals](https://hamel.dev/blog/posts/evals/) | 2 | Read it, then do what it says. |
| ★ | [UK AISI Inspect](https://inspect.aisi.org.uk/) | 6 | A solid open framework for running evals. |
| ★ | Build a golden set of 50 or more cases for your project, run it on every change | 8 | Include failures you saw by hand. |
| ★ | LLM-as-judge: check the judge against 20 cases you graded yourself | 4 | Judges favour long answers and their own style. Measure it. |
| ★ | Add tracing: log every prompt, tool call and result to a file you can replay | 3 | |

## Flagship project (week 26 plus spare time, about 25 h)

Build one real tool for a domain you care about. Examples: a research assistant over your own papers, a private notes search, a code-review helper for your repos, a study buddy for this roadmap.

- [ ] Runs fully on a local open-weight model (state which, and why).
- [ ] RAG over your own documents, with hybrid search and a measured recall@k.
- [ ] At least two tools, one of them served through MCP.
- [ ] 50+ eval cases, run by one command, with results saved per change.
- [ ] Step and time limits, logging, replay.
- [ ] `docker compose up` starts it.
- [ ] README with a failure analysis: three real failures, their cause and what you changed.
- [ ] Someone else, not you, has run it from a clean clone.

## Done when

You can show numbers that prove the project works, name its top three failure modes, and say what each change did to the eval score.

Next: [Stage 6: Fine-tune and post-train open models](06-fine-tune.md).
