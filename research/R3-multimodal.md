# R3: Multimodal and generative models

**You become:** someone who builds and studies models that handle images, speech and video, and generative models such as diffusion and flow matching.  
**Time:** 200-300 h. **Needs:** Stages 1-6, and the vision work from Stage 2.

| | Step | Resource | Hours | Notes |
|---|---|---|---:|---|
| ★ | 1 | [Stanford CS231n](https://cs231n.stanford.edu/) lectures on CNNs, ViTs and self-supervision | 40 | Fills the vision gaps. |
| ★ | 2 | [MIT 6.S184: Flow Matching and Diffusion Models](https://diffusion.csail.mit.edu/) | 30 | The shortest path to modern generative models. |
| ★ | 3 | [Hugging Face: Vision Language Models explained](https://huggingface.co/blog/vlms) | 4 | How an image encoder is joined to a language model. |
| ★ | 4 | [MIT Multimodal AI (Spring 2026)](https://mit-mi.github.io/mmai-course/spring2026/) | 50 | Public schedule and slides; open it to confirm it is current. |
| ★ | 5 | Build a small vision-language model: freeze an open image encoder, add a projector, train on image-caption pairs with an open small LLM | 60 | The same recipe as LLaVA. Ablate image resolution and frozen vs tuned encoder. |
| Optional | 6 | Speech: [Whisper paper (2212.04356)](https://arxiv.org/abs/2212.04356) and run it locally | 8 | Local speech-to-text, good with your Stage 4 stack. |
| Optional | 7 | Robotics and vision-language-action models | 40+ | See the [reference robotics track](../reference/tracks/I-robotics-embodied.md). |

**Papers, in order:** ViT (2010.11929) → CLIP (2103.00020) → LLaVA (2304.08485) → DDPM (2006.11239) → Latent Diffusion (2112.10752) → Flow Matching (2210.02747) → Qwen2.5-VL (2502.13923). Full list: [reference papers](../reference/papers/README.md).

## Research project (pick one)

- A mini vision-language model with ablations on connector design and data.
- A flow-matching model on a small image dataset vs a diffusion baseline at equal compute.
- A study of where open VLMs fail on your own images (counting, text in images, spatial relations), with a small benchmark.

## Done when

You can explain how an image becomes tokens for an LLM, train a small generative model, and judge a multimodal benchmark critically.

More depth, if you need it: [reference track C](../reference/tracks/C-vlm-multimodal.md).
