# Track E: Reinforcement Learning and Reasoning

**You become:** someone who builds RL systems (games, control, agents) and RL post-training for reasoning LLMs.  
**Requires:** Levels 4, 6A. **Time:** 300-500 h.

## Learning goals

- Deep RL theory and practice: policy gradients, actor-critic, PPO, SAC, DQN family, exploration, model-based RL, offline RL, imitation learning (BC, DAgger), multi-agent RL, search (MCTS, AlphaZero-style).
- RL for LLMs: reward modeling, RLHF, process vs outcome rewards, verifiable rewards, GRPO-style methods, credit assignment over long trajectories, reward hacking, test-time compute and search.
- Environments and evaluation: building good environments/verifiers; variance and seeds; sample efficiency.

## Resources

| | Resource | Notes |
|---|---|---|
| ★ | [Berkeley CS285 Deep RL](https://rail.eecs.berkeley.edu/deeprlcourse/) | The deep-RL research course; do homeworks. |
| ★ | [Sutton and Barto](http://incompleteideas.net/book/the-book-2nd.html) complete | Reference/spine. |
| ★ | [Stanford CS329A](https://cs329a.stanford.edu/) (RL, verifiers, self-improvement sessions) | Connects RL to agents. |
| ★ | [CleanRL](https://github.com/vwxyzjn/cleanrl), [Spinning Up](https://spinningup.openai.com/), [HF Deep RL course](https://huggingface.co/learn/deep-rl-course) | Implementation references. |
| Companion | [MARL book](https://www.marl-book.com/) | Multi-agent RL. |
| Companion | [Stanford CS224R Deep RL (check current offering)](https://cs224r.stanford.edu/) | RL with robotics/post-training flavour. |
| Depth | RL frameworks for LLMs: TRL, OpenRLHF, veRL | Production-style RL post-training. |

## Papers (in order)

DQN (Nature 2015) -> AlphaGo (Nature 2016) -> AlphaZero (1712.01815) -> PPO (1707.06347) -> MuZero (1911.08265) -> Decision Transformer (2106.01345) -> InstructGPT (2203.02155) -> Let's Verify Step by Step (2305.20050) -> DPO (2305.18290) -> DeepSeekMath (2402.03300) -> DeepSeek-R1 (2501.12948) -> Scaling test-time compute (2408.03314) -> s1 (2501.19393).

## Projects

1. **RL harness**: Q-learning, REINFORCE, A2C, DQN, PPO, with multi-seed statistics and learning-curve confidence intervals; reproduce a published curve.
2. **Search + learning**: MCTS plus a learned value/policy on a small board game (AlphaZero-lite).
3. **LLM RLVR**: GRPO on a small model with a verifiable reward; ablate KL penalty, group size, reward shaping; analyze reward hacking.
4. **Environment design**: build a new environment with an automatic verifier; show the reward is hard to game; release it.
5. **Capstone**: a reproduction-with-ablation of a recent reasoning-RL paper.

## Done when

You can implement PPO from memory, debug a non-learning RL run systematically, and explain what RLVR optimizes and how it can go wrong.
