# Track C: Vision-Language and Generative Models

**You become:** someone fluent in VLMs and multimodal LLMs, diffusion/flow generative models, video, and (optionally) VLA policies.  
**Requires:** Levels 4, 5, 6B. **Time:** 300-500 h.

## Learning goals

- Visual representation learning: supervised, self-supervised (DINO/MAE), contrastive language-image (CLIP, SigLIP).
- VLM architectures: frozen-encoder + projector (LLaVA), cross-attention (Flamingo), Q-Former (BLIP-2), natively multimodal/early-fusion (Chameleon-style); tokenization of images, resolution/visual-token budgets, OCR/document understanding, grounding, video.
- Training recipes: alignment stage, instruction tuning, data curation, evaluation (MMMU-type benchmarks, hallucination/grounding tests).
- Generative models: VAE/GAN history; diffusion (DDPM, latent diffusion), flow matching, DiT, guidance, distillation; text-to-image/video; discrete diffusion.
- Embodied extension: VLA models (see Track I).

## Resources

| | Resource | Notes |
|---|---|---|
| ★ | [CMU 11-777 Multimodal ML](https://multicomp.cs.cmu.edu/mmml-course/fall2026/) | Full course; check the current term. |
| ★ | [MIT 6.S184 Flow Matching and Diffusion](https://diffusion.csail.mit.edu/) | Short, rigorous, modern. |
| ★ | [CS231n](https://cs231n.stanford.edu/) (generative and VLM lectures) | If not done in Level 4. |
| ★ | [HF VLM blog](https://huggingface.co/blog/vlms), HF Transformers VLM docs, open models (Qwen-VL, LLaVA, PaliGemma, SmolVLM) | Run them, read their model cards and code. |
| Companion | [Intro to Multimodal AI with Hugging Face (Coursera, updated June 2026)](https://www.coursera.org/learn/introduction-to-multimodal-ai-with-hugging-face) | Practical pipelines: VLMs, Whisper, Diffusers, safety filtering. **Paid** (Coursera Plus or course purchase), unlike the free HF courses. |
| Depth | [Stanford CS236](https://deepgenerativemodels.github.io/) | Generative-model theory. |
| Depth | [HF Diffusion Models Course](https://huggingface.co/learn/diffusion-course) | Hands-on diffusion. |
| Depth | [HF Computer Vision Course](https://huggingface.co/learn/computer-vision-course) | Community CV course. |

## Papers (in order)

ViT (2010.11929) -> CLIP (2103.00020) -> SigLIP (2303.15343) -> Flamingo (2204.14198) -> BLIP-2 (2301.12597) -> LLaVA (2304.08485) -> LLaVA-1.5 (2310.03744) -> Qwen-VL (2308.12966) -> PaliGemma (2407.07726) -> Chameleon (2405.09818) -> Idefics2 (2405.02246) -> Molmo (2409.17146) -> Qwen2.5-VL (2502.13923) -> InternVL (2312.14238); self-supervised vision: DINOv2 (2304.07193), MAE (2111.06377); benchmark: MMMU (2311.16502); generative: DDPM (2006.11239) -> Latent Diffusion (2112.10752) -> Flow Matching (2210.02747) -> DiT (2212.09748) -> Stable Diffusion 3 / rectified flow (2403.03206).

## Projects

1. **Mini-VLM** (Level 6 project) extended: ablate image resolution, projector design, and data mixture; add a grounding or OCR evaluation.
2. **CLIP from scratch** at small scale (contrastive loss, temperature, batch-size effect) and zero-shot evaluation.
3. **Flow/diffusion lab**: unconditional -> class/text-conditional -> classifier-free guidance on a small dataset.
4. **VLM failure analysis**: build a 200-item probe set (counting, spatial relations, text in images, hallucination) and categorize errors across 2-3 open VLMs.
5. **Capstone**: a research question about visual-token efficiency, grounding, or multimodal reasoning, with an ablation table and a report.

## Done when

You can explain how pixels become tokens a language model reasons over, why VLMs fail at what they fail at, and how a diffusion/flow model is trained and sampled.
