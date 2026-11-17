# Stage 2: Neural networks from scratch

**Weeks 7-12 · about 110 h · output: your own autograd engine and a small trained language model**

One main course: Andrej Karpathy's *Neural Networks: Zero to Hero*. You code along, you do not just watch. Everything else is small and supporting.

## Weeks 7-10: Zero to Hero, part 1

| | Resource | Hours | Notes |
|---|---|---:|---|
| ★ | [Karpathy: Neural Networks, Zero to Hero](https://karpathy.ai/zero-to-hero.html): **micrograd** | 12 | Build backprop yourself. Pause the video and write each piece before he does. |
| ★ | Same course: **makemore** parts 1-5 (bigram, MLP, activations and batch norm, backprop by hand, WaveNet) | 35 | This is where you learn why training breaks and how to see it. |
| ★ | [PyTorch: Learn the Basics](https://pytorch.org/tutorials/beginner/basics/intro.html) | 8 | Tensors, datasets, the training loop. Re-do one makemore model in plain PyTorch. |
| ★ | [Karpathy: A Recipe for Training Neural Networks](http://karpathy.github.io/2019/04/25/recipe/) | 1 | Read it now and again after Stage 3. |

## Weeks 11-12: Vision and the practical loop

| | Resource | Hours | Notes |
|---|---|---:|---|
| ★ | [fast.ai Practical Deep Learning: lessons 1-3](https://course.fast.ai/) | 12 | Ship an image classifier fast, then ask why it worked. |
| ★ | Train a small CNN on CIFAR-10 in PyTorch | 8 | Compare to your MLP. Write down why it wins. |
| Optional | [Understanding Deep Learning (Prince)](https://udlbook.github.io/udlbook/) | 30 | Best free textbook. Read the chapters on what you just built. |
| Optional | [Stanford CS231n](https://cs231n.stanford.edu/) | 80 | Only for a vision-focused research branch later. |

## Project 2: from-scratch networks (about 25 h)

- [ ] Your micrograd matches PyTorch gradients on a small network (gradient check).
- [ ] A makemore-style model generates names (or any text of your choice).
- [ ] You can diagnose three failures: bad initialization, dead ReLUs, too high learning rate. Show a plot for each.
- [ ] A CIFAR-10 report with predictions written before the runs.

## Done when

- [ ] You explain backprop on a whiteboard without notes.
- [ ] You can overfit one tiny batch, and you know why that is the first debugging step.
- [ ] Project 2 is on GitHub.

Next: [Stage 3: Transformers and LLM internals](03-transformers.md).
