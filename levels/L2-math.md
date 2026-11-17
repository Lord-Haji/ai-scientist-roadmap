# Level 2: Math for AI

**Goal:** fluency in the math you meet in every ML paper: vectors/matrices, gradients, probability, information, optimization.  
**Time:** 250-350 h. **Runs in parallel with Level 1.** **Prerequisites:** Level 0 (high-school algebra, functions).  
**Do not skip.** Most gaps in LLM understanding are math gaps found late.

## Test-out

- Compute the SVD of a small matrix by hand-assisted code and explain what each factor means.
- Derive the gradient of softmax cross-entropy with respect to logits.
- State and use Bayes' rule, linearity of expectation, and the law of total variance.
- Derive KL divergence between two Gaussians; explain why minimizing cross-entropy equals maximum likelihood.
- Explain why gradient descent on an ill-conditioned quadratic is slow and what momentum does.

## Resources

### Linear algebra (★)

| | Resource | Hours | Notes |
|---|---|---:|---|
| ★ | [MIT 18.06SC Linear Algebra (Strang)](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/) | 80 | The standard. Focus: subspaces, rank, orthogonality, eigen, SVD, positive-definite. |
| Companion | [3Blue1Brown: Essence of Linear Algebra](https://www.3blue1brown.com/topics/linear-algebra) | 4 | Intuition first. Watch before 18.06. |
| Companion | [Mathematics for Machine Learning](https://mml-book.github.io/), Ch. 2-4 | 25 | ML-flavoured; free PDF. |
| Companion (on-ramp) | [Imperial: Mathematics for Machine Learning](https://www.coursera.org/specializations/mathematics-machine-learning) (Coursera: Linear Algebra, Multivariate Calculus, PCA) | 60 | Applied and intuitive; learners rate the linear algebra course 4.7. Weak on proofs, and the PCA course is the hard one. Use it before 18.06 if rusty, never instead of it. |
| Companion (on-ramp) | [DeepLearning.AI: Math for ML and Data Science](https://www.coursera.org/specializations/mathematics-for-machine-learning-and-data-science) (Coursera: Linear Algebra, Calculus, Probability and Statistics) | 80 | Gentle and visual (Luis Serrano). A reviewer calls it shallow, which is fair. Fine to rebuild confidence, not a substitute for Stat 110. |

### Calculus (★)

| | Resource | Hours | Notes |
|---|---|---:|---|
| ★ | [MIT 18.01SC Single Variable Calculus](https://ocw.mit.edu/courses/18-01sc-single-variable-calculus-fall-2010/) | 60 | Skip if strong. |
| ★ | Multivariable: selected MIT 18.02 (gradients, Jacobians, Hessians, chain rule, Lagrange multipliers) | 40 | The multivariable chain rule is backprop. |
| Companion | [3Blue1Brown: Essence of Calculus](https://www.3blue1brown.com/topics/calculus) | 4 | |
| Companion | *The Matrix Calculus You Need For Deep Learning* (Parr and Howard) | 4 | Short and exactly on target. |

### Probability and statistics (★)

| | Resource | Hours | Notes |
|---|---|---:|---|
| ★ | [Harvard Stat 110 (Blitzstein)](https://stat110.hsites.harvard.edu/) | 100 | The best intuition-building probability course. Do the problem sets. |
| ★ | MML Ch. 6 plus statistics basics (estimation, confidence intervals, hypothesis tests); ISLP Ch. 1-5 is covered in [Level 3](L3-classical-ml.md), so do it there | 15 | Avoid doing ISLP twice. |
| Depth | [MIT 6.041 Probabilistic Systems Analysis](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) | 80 | Alternative to Stat 110. |

### Information theory and optimization (★)

| | Resource | Hours | Notes |
|---|---|---:|---|
| ★ | MML Ch. 7 plus CS229 optimization/convex notes | 25 | Gradient descent, convexity, Lagrangians. |
| ★ | Entropy, cross-entropy, KL, mutual information: [MacKay, *Information Theory, Inference, and Learning Algorithms*](https://www.inference.org.uk/itila/) Ch. 1-4 | 20 | Free book; the cleanest treatment for ML. |
| Depth | [Boyd and Vandenberghe, *Convex Optimization*](https://web.stanford.edu/~boyd/cvxbook/) + Stanford EE364A lectures | 100 | For theory-leaning research. |
| Depth | *Linear Algebra Done Right* (Axler), *Understanding Analysis* (Abbott) | 100+ | For readers who want rigor; needed for theory-heavy research only. |

## What you really need for LLM/agent research (the "spine" subset)

SVD and low-rank structure; eigenvalues and conditioning; matrix calculus and backprop; probability distributions, expectation, likelihood, Bayes; entropy/cross-entropy/KL; SGD/Adam and why they behave as they do; basic concentration and sampling (Monte Carlo); a little stochastic calculus and ODE/SDE intuition if you go to diffusion/flow (Track C).

## Projects

1. **`10-mini-numpy`**: a pure-Python n-d array with shape, strides, broadcasting, reductions and matmul.
2. **`11-gradient-explorer`**: finite-difference vs analytic gradients; optimize quadratic bowl, Rosenbrock and logistic loss; study learning rate and scaling failures.
3. **`12-probability-lab`**: samplers, Monte Carlo estimators, Bayesian coin inference, MLE, entropy/KL experiments, calibration study.
4. **`13-optimizer-lab`**: implement SGD, momentum, RMSProp, Adam under controlled settings; compare stability and sensitivity.

## Done when

You can derive backprop for an MLP on paper, explain why cross-entropy training is MLE, and say what the Hessian eigenvalues tell you about optimization.
