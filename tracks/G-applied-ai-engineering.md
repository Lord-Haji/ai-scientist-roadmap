# Track G: Applied AI Engineering (shortest route *from the spine* to a job)

**You become:** an engineer who ships LLM-powered products reliably: retrieval, tools, evals, serving, monitoring, cost control.  
**Requires:** Level 1 (software), Level 3 basics, and the HF LLM + Agents courses from Levels 5-6. You do not need Levels 4-6 depth to start this track, and it complements them.  
**Time:** 150-300 h on top of Level 1 (about 1,000 h from scratch) and Level 3. If you already work as a software engineer, this track really is the fast route.

## Learning goals

- Prompt and context engineering; structured outputs; function calling.
- Retrieval: chunking, embeddings, hybrid search (BM25 + vectors), reranking, vector databases, evaluation of retrieval.
- Agents and workflows in production: orchestration, retries, guardrails, human-in-the-loop, tracing.
- **Evals as a first-class skill**: golden sets, LLM-as-judge with calibration, regression testing, online monitoring.
- Serving: APIs, streaming, caching, batching, cost/latency management; open-model serving (vLLM) vs hosted APIs.
- Fine-tuning when it is justified (LoRA/QLoRA, distillation) vs better prompting/retrieval.
- Cloud and MLOps basics: pick **one** cloud (AWS or GCP), containers, CI/CD, secrets, observability.
- Security and privacy: prompt injection, PII, data governance.

## Resources

| | Resource | Notes |
|---|---|---|
| ★ | [HF LLM Course](https://huggingface.co/learn/llm-course), [HF Agents Course](https://huggingface.co/learn/agents-course), [HF MCP Course](https://huggingface.co/learn/mcp-course) | Free foundation. |
| ★ | Chip Huyen, *AI Engineering* (book) | Best end-to-end treatment of evaluation, RAG, finetuning, inference optimization. |
| ★ | [DeepLearning.AI short courses](https://www.deeplearning.ai/short-courses/) | Quick, practical modules (RAG, evals, agents, MCP). |
| ★ | [Anthropic: Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) and provider docs (Anthropic, OpenAI, Google) | Patterns and API semantics. |
| ★ | [Made With ML](https://madewithml.com/), [Full Stack Deep Learning](https://fullstackdeeplearning.com/) | Production ML workflow. |
| Companion | Cloud certificates: pick one, for example an AWS ML Engineer (Associate) or AWS generative-AI certification (the older AWS ML Specialty was retired after March 2026), or Google Cloud Professional ML Engineer | A signal for some employers; do after you can build, not before. Verify the current certificate catalog. |
| Companion | Open-source contributions: LangChain, Haystack, LlamaIndex, vLLM, HF libraries | Real code review and visible track record. |

## Projects (portfolio)

1. **RAG system with real evaluation**: your own corpus, hybrid retrieval, reranker, retrieval and answer metrics, an ablation table, a failure analysis.
2. **Agentic workflow product**: tool-using assistant with tracing, retries, spend limits, tests and a CI-run eval suite.
3. **Fine-tune vs prompt study**: LoRA fine-tune a small model on a narrow task and compare to prompting a larger model on quality, latency and cost.
4. **Deployed service**: containerized, load-tested, monitored, with a short design doc.
5. **Open-source PR(s)** to a popular LLM tooling repo.

## Done when

Someone can use your project without you, you can show metrics proving it works, and you can explain every cost and failure mode.
