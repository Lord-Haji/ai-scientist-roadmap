# Staged Reading List

Papers are read **inside the level where their prerequisites are met**. Labels: **H** historical (abstract, intro, key sections), **C** core (method, equations, experiments, limitations), **R** reproduce one decisive mechanism or result at small scale. arXiv IDs are given where one exists; use `https://arxiv.org/abs/<id>`.

> Pace: one paper per week from Level 3, two per week from Level 5. Always write a note ([template](../../research-skills/paper-note-template.md)). Re-check IDs before relying on them; mistakes are possible. Run [`scripts/check_links.py`](../../scripts/check_links.py) for course links.

## Level 3-4: Learning and deep learning

| Type | Paper | ID |
|---|---|---|
| H | Rumelhart, Hinton, Williams: Learning representations by back-propagating errors (1986) | Nature 323 |
| C | Adam | 1412.6980 |
| C | Decoupled weight decay (AdamW) | 1711.05101 |
| C | Batch Normalization | 1502.03167 |
| C | Layer Normalization | 1607.06450 |
| R | Deep Residual Learning (ResNet) | 1512.03385 |
| H | AlexNet: ImageNet classification with deep CNNs (2012) | NeurIPS 2012 |
| C | An Image is Worth 16x16 Words (ViT) | 2010.11929 |
| C | Karpathy: A Recipe for Training Neural Networks | blog (2019) |

## Level 5: Transformers and LLMs

| Type | Paper | ID |
|---|---|---|
| H | word2vec: Efficient estimation of word representations | 1301.3781 |
| C | Sequence to sequence learning | 1409.3215 |
| R | Bahdanau attention (NMT by jointly learning to align and translate) | 1409.0473 |
| R | **Attention Is All You Need** | 1706.03762 |
| C | BERT | 1810.04805 |
| C | GPT-3: Language models are few-shot learners | 2005.14165 |
| R | Scaling laws for neural language models | 2001.08361 |
| C | Chinchilla: Training compute-optimal LLMs | 2203.15556 |
| C | LLaMA | 2302.13971 |
| C | Llama 2 | 2307.09288 |
| C | The Llama 3 herd of models | 2407.21783 |
| R | FlashAttention | 2205.14135 |
| C | FlashAttention-2 | 2307.08691 |
| C | RoFormer (RoPE) | 2104.09864 |
| C | GQA | 2305.13245 |
| C | Switch Transformers | 2101.03961 |
| C | Mixtral of Experts | 2401.04088 |
| C | DeepSeek-V3 technical report | 2412.19437 |
| C | Mamba | 2312.00752 |
| C | LoRA | 2106.09685 |
| C | QLoRA | 2305.14314 |
| C | Efficient memory management for LLM serving (vLLM/PagedAttention) | 2309.06180 |
| C | Fast inference via speculative decoding | 2211.17192 |
| C | FineWeb | 2406.17557 |

## Level 6A: RL and post-training

| Type | Paper | ID |
|---|---|---|
| R | DQN: Human-level control through deep RL | Nature 518 (2015) |
| C | AlphaGo | Nature 529 (2016) |
| C | AlphaZero | 1712.01815 |
| R | PPO | 1707.06347 |
| C | MuZero | 1911.08265 |
| C | Deep RL from human preferences | 1706.03741 |
| R | InstructGPT | 2203.02155 |
| C | Constitutional AI | 2212.08073 |
| C | DPO | 2305.18290 |
| C | Let's Verify Step by Step | 2305.20050 |
| C | DeepSeekMath (GRPO) | 2402.03300 |
| C | DeepSeek-R1 | 2501.12948 |
| C | Tulu 3 | 2411.15124 |
| C | Scaling LLM test-time compute optimally | 2408.03314 |
| C | s1: Simple test-time scaling | 2501.19393 |
| C | Decision Transformer | 2106.01345 |

## Level 6B: Multimodal and generative

| Type | Paper | ID |
|---|---|---|
| R | CLIP | 2103.00020 |
| C | SigLIP | 2303.15343 |
| C | Flamingo | 2204.14198 |
| C | BLIP-2 | 2301.12597 |
| R | LLaVA (Visual instruction tuning) | 2304.08485 |
| C | Improved baselines with visual instruction tuning (LLaVA-1.5) | 2310.03744 |
| C | Qwen-VL | 2308.12966 |
| C | PaliGemma | 2407.07726 |
| C | Chameleon | 2405.09818 |
| C | Idefics2: What matters when building vision-language models? | 2405.02246 |
| C | Molmo and PixMo | 2409.17146 |
| C | Qwen2-VL | 2409.12191 |
| C | Qwen2.5-VL | 2502.13923 |
| C | InternVL | 2312.14238 |
| C | DINOv2 | 2304.07193 |
| C | Masked Autoencoders (MAE) | 2111.06377 |
| C | Whisper (robust speech recognition at scale) | 2212.04356 |
| C | MMMU | 2311.16502 |
| H | GAN | 1406.2661 |
| R | DDPM | 2006.11239 |
| C | Latent Diffusion (Stable Diffusion) | 2112.10752 |
| R | Flow Matching | 2210.02747 |
| C | DiT: Scalable diffusion models with transformers | 2212.09748 |
| C | Stable Diffusion 3 (rectified flow Transformers) | 2403.03206 |

## Level 6C: Reasoning and agents

| Type | Paper | ID |
|---|---|---|
| C | Chain-of-thought prompting | 2201.11903 |
| C | Self-consistency | 2203.11171 |
| C | Tree of Thoughts | 2305.10601 |
| R | ReAct | 2210.03629 |
| C | Toolformer | 2302.04761 |
| C | Reflexion | 2303.11366 |
| C | Generative Agents | 2304.03442 |
| C | Voyager | 2305.16291 |
| C | CAMEL | 2303.17760 |
| C | AutoGen | 2308.08155 |
| C | MetaGPT | 2308.00352 |
| C | SWE-bench | 2310.06770 |
| C | SWE-agent | 2405.15793 |
| C | Not what you've signed up for: indirect prompt injection | 2302.12173 |

### Retrieval and memory

| Type | Paper | ID |
|---|---|---|
| C | Dense Passage Retrieval (DPR) | 2004.04906 |
| C | Retrieval-Augmented Generation (Lewis et al.) | 2005.11401 |
| C | ColBERT | 2004.12832 |
| C | RETRO: Improving LMs by retrieving from trillions of tokens | 2112.04426 |
| C | Lost in the Middle | 2307.03172 |
| C | MemGPT | 2310.08560 |
| C | YaRN (RoPE context extension) | 2309.00071 |
| C | RULER (long-context evaluation) | 2404.06654 |
| C | Ring Attention | 2310.01889 |

### Tool use, agent evaluation, multi-agent, agent security

| Type | Paper | ID |
|---|---|---|
| C | Gorilla: LLM connected with massive APIs | 2305.15334 |
| C | ToolLLM | 2307.16789 |
| C | WebArena | 2307.13854 |
| C | tau-bench | 2406.12045 |
| C | AgentDojo (prompt-injection benchmark for agents) | 2406.13352 |
| C | AI Control: improving safety despite intentional subversion | 2312.06942 |
| C | Improving factuality and reasoning through multi-agent debate | 2305.14325 |
| C | Why do multi-agent LLM systems fail? | 2503.13657 |
| C | Among Us: a sandbox for measuring and detecting agentic deception (Golechha and Garriga-Alonso) | 2504.04072 (spot-check this ID) |

### Post-training extras

| Type | Paper | ID |
|---|---|---|
| C | KTO | 2402.01306 |
| C | SimPO | 2405.14734 |

> IDs in these new tables were assembled from memory by a reviewer pass and could not be live-checked from the build sandbox. Open each one and confirm the title before reading.

## Safety and interpretability (Track D)

| Type | Paper | ID |
|---|---|---|
| H | Concrete problems in AI safety | 1606.06565 |
| C | A Mathematical Framework for Transformer Circuits | transformer-circuits.pub (2021) |
| C | In-context learning and induction heads | 2209.11895 |
| R | Progress measures for grokking | 2301.05217 |
| C | Towards Monosemanticity | transformer-circuits.pub (2023) |
| C | Sparse autoencoders find highly interpretable features | 2309.08600 |
| C | Scaling Monosemanticity | transformer-circuits.pub (2024) |
| C | Weak-to-strong generalization | 2312.09390 |
| C | Sleeper Agents | 2401.05566 |
| C | Alignment faking in large language models | 2412.14093 |

## Robotics and VLA (Track I)

| Type | Paper | ID |
|---|---|---|
| R | DAgger | 1011.0686 |
| C | World Models | 1803.10122 |
| C | RT-2 | 2307.15818 |
| C | Open X-Embodiment | 2310.08864 |
| R | OpenVLA | 2406.09246 |
| C | pi0 | 2410.24164 |
| C | pi0.5 | 2504.16054 |

## Refresh rule

Frontier readings (latest technical reports, reasoning, agents, VLA) should be refreshed when you start the relevant stage: skim the newest strong papers (arXiv listing, alphaXiv, lab blogs, conference proceedings) and replace stale entries. Do not accumulate; keep the list selective.
