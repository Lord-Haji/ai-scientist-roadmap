# Level 4: Deep Learning

**Goal:** understand neural networks from first principles (backprop, autograd, optimization, architectures), then use PyTorch fluently and understand how a DL framework works.  
**Time:** 300-450 h (Zero to Hero alone is 60-100 h if you code along). **Prerequisites:** Levels 2 and 3, Python fluency. CMU 10-414 additionally needs the Level 1 systems material (C++ basics, CS:APP-level memory/caches).

## Test-out

- Implement a 2-layer MLP with manual backprop in NumPy and gradient-check it.
- Explain why residual connections and normalization help optimization; what initialization does to activations.
- Write a PyTorch training loop with data loader, mixed precision, checkpointing, and evaluation, without copy-pasting.

## 4.1 Foundations and first-principles build (★)

| | Resource | Hours | Notes |
|---|---|---:|---|
| ★ | [Andrej Karpathy: Neural Networks, Zero to Hero](https://karpathy.ai/zero-to-hero.html) | 60-100 with coding | micrograd, makemore, activations/batchnorm, backprop by hand, WaveNet, then GPT. **Code along; do not just watch.** |
| ★ | [*Understanding Deep Learning* (Prince)](https://udlbook.github.io/udlbook/) | 50 | Modern, clear, with notebooks. Primary text. |
| Companion | *Deep Learning: Foundations and Concepts* (Bishop and Bishop, 2024) | reference | Rigorous. |
| Companion | [Dive into Deep Learning (d2l.ai)](https://d2l.ai/) | 40 | Code-heavy; PyTorch/JAX/TF. |
| Companion | [fast.ai Practical Deep Learning for Coders](https://course.fast.ai/) | 40 | Top-down: ship first, then understand. Great for intuition and practice. |
| Reference | [PyTorch tutorials](https://pytorch.org/tutorials/) and docs | n/a | |
| Depth | *Deep Learning* (Goodfellow, Bengio, Courville) | reference | Classic, partly dated on architectures. |
| Companion | [Ng Deep Learning Specialization](https://www.coursera.org/specializations/deep-learning) (Coursera, 5 courses) | 60 | Fine on-ramp, but see [`AUDIT-OLD-ROADMAP.md`](AUDIT-OLD-ROADMAP.md): lecture content is good; its TensorFlow-era assignments are dated. |

## 4.2 Deep learning systems (★ for builders)

| | Resource | Hours | Notes |
|---|---|---:|---|
| ★ | [CMU 10-414/714 Deep Learning Systems](https://dlsyscourse.org/) | 120 | Build a mini-PyTorch (needle): autodiff, modules, optimizers, NDArray, GPU backend, conv, attention. After this, you cannot be mystified by a framework. |
| Depth | [Stanford CS149 Parallel Computing](https://gfxcourses.stanford.edu/cs149/) | 60 | Parallel programming foundations. |

## 4.3 Vision and sequence models (★)

| | Resource | Hours | Notes |
|---|---|---:|---|
| ★ | [Stanford CS231n: Deep Learning for Computer Vision](https://cs231n.stanford.edu/) | 80 | Linear classifiers to CNNs, ResNets, ViTs, self-supervision, generative models, VLM basics. |
| Depth | [Michigan EECS 498-007 / 598-005 (Justin Johnson)](https://web.eecs.umich.edu/~justincj/teaching/eecs498/) | 80 | Alternative/complement to CS231n with excellent assignments. |
| ★ | RNN/LSTM/seq2seq/attention: covered in CS224N (Level 5), with the papers below | n/a | Learn them as the historical bridge to Transformers. |

## Papers inside Level 4

Read in this order ([full list](../papers/README.md)): Rumelhart-Hinton-Williams backprop (1986), Adam (1412.6980), BatchNorm (1502.03167), LayerNorm (1607.06450), ResNet (1512.03385), AlexNet (2012), ViT (2010.11929), and Karpathy's [A Recipe for Training Neural Networks](http://karpathy.github.io/2019/04/25/recipe/).

## Projects

1. **`30-neural-nets-from-numpy`**: perceptron and 2-layer MLP with manual backprop; AND/OR/XOR; sigmoid vs ReLU; initialization and depth experiments; write up each failure and the fix it motivates.
2. **`31-mini-pytorch`**: build the CMU course framework (autodiff, modules, optimizers, NDArray, selected kernels). Then switch to real PyTorch for research.
3. **`32-vision-evolution`**: on CIFAR-10 compare linear, MLP, CNN, small ResNet, small ViT under matched budgets; study residuals, receptive fields, augmentation and normalization. (The CLIP-style contrastive experiment comes later, in Level 6B, after contrastive learning is taught.)
4. **`33-reproduce-a-classic`**: reproduce ResNet or a small-scale ImageNet-style result with a fixed compute budget; write a 2-page report.

## Done when

You can derive backprop, implement autograd, train CNN/ViT models, diagnose a training run that is not learning (data, loss, init, LR, bugs) using the Karpathy recipe, and explain a framework's internals.
