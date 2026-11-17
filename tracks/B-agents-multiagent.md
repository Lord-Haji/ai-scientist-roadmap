# Track B: Agents and Multi-Agent Systems

**You become:** someone who designs, evaluates, debugs and secures agentic and multi-agent LLM systems, and can read the research on them.  
**Requires:** Levels 5 and 6C (and 6A helpful). **Time:** 300-500 h. Pairs with D (safety) and E (RL).

## Learning goals

1. **Single-agent foundations:** the agent loop, tool/function calling, planning, memory (short/long-term, retrieval), context management, reflection, structured outputs.
2. **Protocols and infrastructure:** [Model Context Protocol](https://modelcontextprotocol.io/), tool schemas, sandboxes (code execution, browsers), observability and tracing.
3. **Multi-agent systems:** role specialization, debate, orchestrator-worker, blackboard/shared memory, negotiation; communication topologies; failure modes (coordination failure, cascading errors, collusion, sycophancy between agents).
4. **Agent evaluation:** benchmarks (SWE-bench, WebArena-style, tau-bench-style tool-use), trajectory-level analysis, cost/latency accounting, reliability over repeated runs.
5. **Learning agents:** RL for agents, self-improvement, verifiers, test-time search (ties to Track E and CS329A).
6. **Security and safety of agents:** prompt injection, tool abuse, sandbox escapes, permissioning, monitoring; deception and strategic behavior in multi-agent environments (ties to Track D).

## Resources

| | Resource | Notes |
|---|---|---|
| ★ | [HF Agents Course](https://huggingface.co/learn/agents-course), [HF MCP Course](https://huggingface.co/learn/mcp-course) | Free, hands-on, covers multiple frameworks. |
| ★ | [Berkeley Agentic AI MOOC, Fall 2025 (CS294/194-196, ~13 lectures)](https://rdi.berkeley.edu/agentic-ai/f25) and the [Spring 2025 Advanced LLM Agents](https://rdi.berkeley.edu/adv-llm-agents/sp25) | Reasoning, planning, frameworks, multi-agent, safety and security lectures. |
| ★ | [Stanford CS329A](https://cs329a.stanford.edu/) | Research frontier; read the linked papers. |
| ★ | [Anthropic: Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) and other lab engineering posts | Pragmatic patterns; prefer simple workflows before complex autonomy. |
| ★ | Agent SDK/framework docs: LangGraph, OpenAI Agents SDK, Claude Agent SDK, AutoGen, smolagents | Learn two; know how to build without them (Level 6 project 54). |
| Companion | DeepLearning.AI [short courses](https://www.deeplearning.ai/short-courses/) on agents, evaluation, MCP | Short and practical; vendor-flavoured. |
| Depth | Stanford CS329Z Engineering AI Agents (Fall 2026 syllabus is public) | Engineering-focused view. |
| Depth | [Multi-Agent RL book (Albrecht, Christianos, Schafer)](https://www.marl-book.com/) | Theory for game-theoretic and learning multi-agent systems. |
| Depth | Game-theory basics (e.g., Shoham and Leyton-Brown, *Multiagent Systems*, free PDF) | Equilibria, mechanism design, negotiation. |

## Papers (in order)

CoT (2201.11903) -> ReAct (2210.03629) -> Toolformer (2302.04761) -> Self-consistency (2203.11171) -> Tree of Thoughts (2305.10601) -> Reflexion (2303.11366) -> Generative Agents (2304.03442) -> Voyager (2305.16291) -> CAMEL (2303.17760) -> AutoGen (2308.08155) -> MetaGPT (2308.00352) -> SWE-bench (2310.06770) -> SWE-agent (2405.15793) -> Indirect prompt injection (2302.12173). Also read: retrieval and memory (DPR, RAG, MemGPT), tool-use training and agent evals (Gorilla, ToolLLM, WebArena, tau-bench), agent security (AgentDojo, AI Control), multi-agent debate (2305.14325), multi-agent failure analysis (2503.13657), and the Among Us deception sandbox. IDs in [`papers/README.md`](../papers/README.md).

## Projects

1. **Framework-free agent** (from Level 6) hardened with logging, replay, budget limits and tests.
2. **Tool ecosystem:** build two MCP servers (one read-only, one with side effects and approval gates) and evaluate an agent using them; document the permission model.
3. **Multi-agent study:** pick a task (collaborative coding, negotiation, social-deduction game, research-assistant swarm). Compare single-agent vs 2-3 multi-agent topologies on success, cost and failure types, with several seeds. Report when multi-agent is *not* worth it.
4. **Agent evaluation harness:** reproducible runner, trajectory viewer, failure taxonomy, repeated-trial reliability (pass^k style), cost tracking.
5. **Red-team your agent:** prompt injection through tools/documents, tool misuse, privilege escalation; implement and measure mitigations.
6. **Capstone:** a reproducible research-grade multi-agent experiment (e.g., deception, coordination or oversight) with human baselines where possible.

## Done when

You can explain why an agent failed from its trajectory, design an evaluation that separates capability from luck, and say when a multi-agent design helps or hurts.
