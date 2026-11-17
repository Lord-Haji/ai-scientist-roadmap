# Level 6: Frontier Core

**Goal:** the three shared pillars every specialization builds on: (A) post-training and reinforcement learning, (B) multimodal and generative models, (C) agents and reasoning. One medium-depth pass over each; tracks go deep afterwards.  
**Time:** 400-500 h including the five projects. **Prerequisites:** Level 5 (Transformers), Level 3 (probability/ML).  
**Refresh policy:** this is the fastest-moving level. Check the newest offering of every course before starting.

## Test-out

- Derive the policy-gradient theorem and explain how PPO's clipped objective stabilizes updates.
- Explain RLHF, DPO and GRPO/RLVR in one paragraph each and their data requirements.
- Explain how a VLM connects a vision encoder to an LLM (projector vs cross-attention).
- Implement a ReAct-style tool-calling loop without an agent framework.

## 6A. Reinforcement learning and post-training (★)

| | Resource | Hours | Notes |
|---|---|---:|---|
| ★ | [Sutton and Barto, *Reinforcement Learning: An Introduction*](http://incompleteideas.net/book/the-book-2nd.html) | 60 | The book. Chapters 1-6, 9-13 first. |
| ★ | [Stanford CS234 Reinforcement Learning](https://web.stanford.edu/class/cs234/) | 60 | Bandits to policy gradients, offline RL, RLHF intro. |
| Companion | [Reinforcement Learning Specialization (U Alberta)](https://www.coursera.org/specializations/reinforcement-learning) (Coursera, 4 courses) | 50 | By Martha and Adam White, built around Sutton and Barto; rigorous and coding-heavy. Fundamentals of RL has a 92% like rate. The best Coursera course in this roadmap. Do it alongside the book. |
| Companion | [David Silver's RL lectures](https://www.davidsilver.uk/teaching/) | 25 | Timeless clarity. |
| ★ | [Hugging Face Deep RL Course](https://huggingface.co/learn/deep-rl-course) | 30 | Hands-on with Gymnasium, SB3, PPO. |
| Companion | [OpenAI Spinning Up in Deep RL](https://spinningup.openai.com/) and [CleanRL](https://github.com/vwxyzjn/cleanrl) | 15 | Readable reference implementations. |
| ★ | Post-training: CS336 alignment lectures; [Hugging Face TRL docs](https://huggingface.co/docs/trl); papers: InstructGPT, DPO, DeepSeekMath/GRPO, DeepSeek-R1, Tulu 3 | 40 | SFT, preference optimization, verifiable-reward RL. |
| Companion | Nathan Lambert, *RLHF Book* (free online) | 15 | Reward models, RLHF, DPO and successors (KTO 2402.01306, SimPO 2405.14734), RLVR; fills the reward-model gap. |
| Depth | [Berkeley CS285 Deep RL](https://rail.eecs.berkeley.edu/deeprlcourse/) | 100 | Model-based RL, offline RL, exploration. Take for Track E. |

## 6B. Multimodal and generative models (★)

| | Resource | Hours | Notes |
|---|---|---:|---|
| ★ | [CMU 11-777 Multimodal Machine Learning](https://multicomp.cs.cmu.edu/mmml-course/fall2026/) | 60 | Representation, alignment, fusion, generation, VLMs. Check the current term's page; the URL could not be confirmed in November 2026. |
| Alt | [MIT Multimodal AI (Spring 2026, Paul Liang)](https://mit-mi.github.io/mmai-course/spring2026/) | 50 | Public schedule and slides; adapted from 11-777. Use it if the CMU page is not live. |
| ★ | [MIT 6.S184 Flow Matching and Diffusion Models](https://diffusion.csail.mit.edu/) | 30 | ODE/SDE view, score matching, flow matching, guidance. Shortest path to understanding modern generative models. |
| ★ | [Hugging Face: Vision Language Models explained](https://huggingface.co/blog/vlms) plus the HF multimodal materials | 10 | Orientation to architectures and open models. |
| Companion | CS231n generative and VLM lectures | 10 | |
| ★ | Contrastive learning and CLIP: re-do the CLIP-style image-text experiment here (small scale), plus DINOv2 (2304.07193) and MAE (2111.06377) for self-supervised vision | 12 | Prerequisite for modern VLMs. |
| Companion | Whisper (2212.04356) and a video-model survey | 6 | Audio and video are part of "multimodal". |
| Depth | [Stanford CS236 Deep Generative Models](https://deepgenerativemodels.github.io/) | 60 | VAEs, GANs, flows, diffusion theory. |

## 6C. Agents and reasoning (★)

| | Resource | Hours | Notes |
|---|---|---:|---|
| ★ | [Hugging Face Agents Course](https://huggingface.co/learn/agents-course) | 25 | Free; agent basics, tools, smolagents/LangGraph/LlamaIndex, final benchmark assignment. |
| ★ | [Hugging Face MCP Course](https://huggingface.co/learn/mcp-course) | 12 | Model Context Protocol in practice. |
| ★ | [Anthropic: Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) | 2 | Workflows vs agents; practical patterns. Read before touching a framework. |
| ★ | [Berkeley Agentic AI MOOC (Fall 2025, CS294/194-196)](https://rdi.berkeley.edu/agentic-ai/f25) | 26 | About 13 lectures with guest speakers, including a closing safety and security lecture; reasoning, planning, frameworks. Earlier editions: [Advanced LLM Agents (Spring 2025)](https://rdi.berkeley.edu/adv-llm-agents/sp25), [LLM Agents (Fall 2024)](https://rdi.berkeley.edu/llm-agents/f24). |
| ★ | [Stanford CS329A: Self-Improving AI Agents](https://cs329a.stanford.edu/) | 40 | Research-seminar format: test-time compute, verifiers, search, RL for agents, deep research agents. Autumn 2025 offering; the lecture videos are now on the Stanford Online YouTube channel (nine parts, about 10 hours). Read the linked papers too. |
| Companion | [Lilian Weng: LLM Powered Autonomous Agents](https://lilianweng.github.io/posts/2023-06-23-agent/) | 2 | Conceptual survey. |
| ★ | Retrieval and memory: BM25 + dense/hybrid retrieval, DPR, RAG, ColBERT, and agent memory (MemGPT); build a retriever and measure recall@k | 20 | Retrieval is the memory substrate of agents; IDs in [papers](../papers/README.md). |
| ★ | Tool-use training and evaluation: function-calling data (Gorilla, ToolLLM), BFCL-style evals, tau-bench, WebArena, SWE-bench | 15 | How tool use is learned and measured, beyond prompting. |
| ★ | Agent security basics: indirect prompt injection, AgentDojo, sandboxing and permissioning | 8 | Do this before shipping any agent with real tools. |
| Depth | Stanford CS329Z Engineering AI Agents (Fall 2026 offering; public syllabus) | 40 | Build/engineering view. |

## Projects

1. **`50-rl-lab`**: tabular Q-learning, REINFORCE, actor-critic, DQN, PPO in one harness; multi-seed studies of reward design, discount, exploration, LR, target updates, batch size.
2. **`51-posttrain-lab`**: take your Level 5 base model (or a small open model) through SFT, then one preference method (DPO) and one verifiable-reward RL run (GRPO-style on math/code with unit-test rewards).
3. **`52-mini-vlm`**: first a small CLIP-style contrastive experiment; then connect a frozen vision encoder to a small LM via projector; train on image-caption and instruction data; ablate resolution, projector type, frozen vs tuned encoder.
4. **`53-flow-diffusion-lab`**: learn a 2D distribution, then a small image model, then a toy control problem; compare a Gaussian head vs flow-matching head.
5. **`54-agent-lab`**: build an agent without a framework as its reasoning layer: goal decomposition, tool selection, execution, observation, verification, replanning over filesystem, Python, shell sandbox, local search, unit-test runner. Evaluate on ambiguous tasks, misleading outputs, missing tools, long horizons and context exhaustion; report success rate, steps, tool calls, cost and failure categories.

## Done when

You have post-trained a model with RL, built a small VLM, built and evaluated an agent, and can read recent frontier papers in these areas and place them in context.
