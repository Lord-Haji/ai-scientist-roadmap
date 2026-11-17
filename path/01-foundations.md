# Stage 1: Foundations

**Weeks 1-6 · about 110 h · output: a tabular ML project and your first local model running**

You can code in Python. This stage gives you the minimum math and classical ML you need so that the neural-network stage does not feel like magic. Nothing here is optional except what is marked *Optional*.

**Skip rule:** if you can do these cold, skip the matching weeks. (1) Write a NumPy function for logistic regression with gradient descent. (2) Explain the chain rule for `f(g(x))` with vectors. (3) Explain what overfitting is and how you detect it.

## Week 1: Tools, and run a model today

| | Resource | Hours | Notes |
|---|---|---:|---|
| ★ | [Ollama](https://ollama.com/) | 3 | Install it and run one small open-weight model (for example a 1B-4B model) in the terminal. Ask it five questions. This is your first taste of Stage 4. |
| ★ | [Kaggle Learn: Python and Pandas](https://www.kaggle.com/learn) | 10 | Short exercises in the browser. |
| ★ | [NumPy quickstart](https://numpy.org/doc/stable/user/quickstart.html) | 4 | Arrays, shapes, broadcasting. Type every example. |
| ★ | [Pro Git, chapters 1-3](https://git-scm.com/book) | 3 | Commit, branch, push. Put all your work on GitHub from now on. |

## Weeks 2-3: Math you actually need

You need intuition plus the ability to compute gradients. Not a math degree.

| | Resource | Hours | Notes |
|---|---|---:|---|
| ★ | [3Blue1Brown: Essence of Linear Algebra](https://www.3blue1brown.com/topics/linear-algebra) | 4 | Vectors, matrix multiply as transformation, eigenvectors. |
| ★ | [3Blue1Brown: Essence of Calculus](https://www.3blue1brown.com/topics/calculus) | 4 | Derivatives and the chain rule. |
| ★ | [The Matrix Calculus You Need For Deep Learning](https://explained.ai/matrix-calculus/) | 4 | Short and exactly on target for backprop. |
| ★ | [Khan Academy: Statistics and probability](https://www.khanacademy.org/math/statistics-probability) | 12 | Do only: probability basics, conditional probability, Bayes, distributions, expected value. |
| ★ | [Mathematics for Machine Learning (book)](https://mml-book.github.io/), chapters 2, 3, 5, 6 | 10 | Read for the parts the videos skipped. Free PDF. |
| Optional | [MIT 18.06 Linear Algebra (Strang)](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/) | 80 | Only if you later feel weak. Not needed to continue. |

**Done when:** you can compute the derivative of `softmax` cross-entropy with respect to the logits on paper.

## Weeks 4-6: Classical machine learning

| | Resource | Hours | Notes |
|---|---|---:|---|
| ★ | [Andrew Ng: Machine Learning Specialization](https://www.coursera.org/specializations/machine-learning-introduction), courses 1 and 2 | 35 | Regression, classification, neural-network basics. Audit free on Coursera. Course 3 is optional. |
| ★ | [Kaggle Learn: Intro to ML and Intermediate ML](https://www.kaggle.com/learn) | 10 | Pipelines and data leakage. |
| ★ | [scikit-learn user guide](https://scikit-learn.org/stable/user_guide.html): model selection and metrics | 5 | Cross-validation, precision/recall. |
| Optional | [An Introduction to Statistical Learning with Python](https://www.statlearning.com/) | 40 | Good depth if you want it. |

## Project 1: tabular ML, end to end (about 15 h)

- [ ] Pick a real dataset (Kaggle or UCI). Plot it before modelling.
- [ ] Build a dumb baseline, then logistic regression, then a gradient-boosted model.
- [ ] Use cross-validation. Report error bars, not one number.
- [ ] Write `report.md`: what worked, what did not, one leakage risk you checked.
- [ ] Implement logistic regression in plain NumPy and match scikit-learn's result.

## Done when

- [ ] A local model runs on your machine.
- [ ] You pass the skip-rule questions above.
- [ ] Project 1 is on GitHub with a report.

Next: [Stage 2: Neural networks from scratch](02-neural-nets.md).
