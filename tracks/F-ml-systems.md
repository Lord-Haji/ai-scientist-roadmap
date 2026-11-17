# Track F: ML Systems and Infrastructure

**You become:** someone who makes training and inference fast, scalable and reliable: GPU kernels, distributed training, serving.  
**Requires:** Level 1 systems (CS:APP, OSTEP), Levels 4-5. **Time:** 300-600 h. Pairs with A.

## Learning goals

- GPU architecture, memory hierarchy, CUDA/Triton, profiling, roofline thinking.
- Distributed training: data/tensor/pipeline/sequence/expert parallelism, ZeRO/FSDP, communication collectives, fault tolerance.
- Inference: KV cache, batching (continuous batching), PagedAttention, speculative decoding, quantization, serving frameworks, latency/throughput/cost trade-offs.
- MLOps: data pipelines, experiment tracking, CI for ML, monitoring, reproducibility.

## Resources

| | Resource | Notes |
|---|---|---|
| ★ | [GPU MODE (lectures and community)](https://www.gpumode.com/) | Practical GPU programming community; lecture series on CUDA, Triton, profiling, kernels. |
| ★ | *Programming Massively Parallel Processors* (Hwu, Kirk, El Hajj) | The CUDA textbook. |
| ★ | CS336 systems assignments (Triton FlashAttention, DDP) | Applied practice. |
| ★ | [HF Ultra-Scale Playbook](https://huggingface.co/spaces/nanotron/ultrascale-playbook) | Parallelism. |
| ★ | [Triton tutorials](https://triton-lang.org/main/getting-started/tutorials/index.html) | Write fused kernels. |
| Companion | [CMU 10-414/714 DL Systems](https://dlsyscourse.org/) | If not done at Level 4. |
| Companion | [vLLM docs](https://docs.vllm.ai/) and PagedAttention paper (2309.06180) | Inference engine design. |
| Companion | [Made With ML](https://madewithml.com/), [Full Stack Deep Learning](https://fullstackdeeplearning.com/), Chip Huyen's *Designing Machine Learning Systems* and *AI Engineering* | MLOps and product-side engineering. |
| Depth | Stanford CS149 Parallel Computing; MIT 6.172 Performance Engineering | Performance foundations. |

## Papers

FlashAttention 1/2 (2205.14135, 2307.08691); Megatron-LM (1909.08053); ZeRO (1910.02054); GPipe (1811.06965); Efficient memory management for LLM serving (2309.06180); Speculative decoding (2211.17192); GPTQ (2210.17323); AWQ (2306.00978); LoRA/QLoRA (2106.09685, 2305.14314); DeepSeek-V3 infrastructure sections.

## Projects

1. **Kernel**: fused softmax/attention kernel in Triton, benchmarked against PyTorch with a roofline analysis.
2. **Distributed training**: implement DDP, then FSDP/ZeRO-style sharding; measure scaling efficiency on 2-8 GPUs (rented).
3. **Inference engine toy**: continuous batching + KV cache + paged memory for a small model; compare to vLLM on throughput.
4. **Quantization study**: int8/int4 on a small LLM; measure quality vs latency across methods.
5. **Capstone**: a measurable speedup or memory reduction on a nanochat-class training run, with correctness tests.

## Done when

You can profile a training step, say where time and memory go, and make it faster without breaking numerics.
