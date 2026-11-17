# Level 3: Classical Machine Learning and Data

**Goal:** a solid ML foundation (the CS229 level) plus honest data-science practice. Classical ML stays relevant: evaluation, baselines, data work and tabular problems are everyday work in many roles.  
**Time:** 150-200 h. **Prerequisites:** Levels 0 and 2 (probability, optimization); Python.

## Test-out

- Implement logistic regression with gradient descent and L2 regularization in NumPy; verify against scikit-learn.
- Explain bias/variance, cross-validation, data leakage, and calibration with an example for each.
- Fit PCA by SVD and explain reconstruction error. Derive the EM updates for a Gaussian mixture.

## Resources

| | Resource | Hours | Notes |
|---|---|---:|---|
| ★ | [Stanford CS229 Machine Learning](https://cs229.stanford.edu/) (notes and lectures) | 80 | The rigorous core: regression, GLMs, generative models, SVMs, EM, learning theory, RL intro. |
| Companion (on-ramp) | [Andrew Ng, Machine Learning Specialization (Coursera, 2022 relaunch)](https://www.coursera.org/specializations/machine-learning-introduction) | 60 | Gentler on-ramp; take it first if CS229 feels steep, then CS229 is the single starred course. Python/NumPy based (the original 2011 Octave course is obsolete). Free for you on Coursera; DeepLearning.AI refreshed it in September 2026. |
| ★ | [*An Introduction to Statistical Learning with Python* (ISLP)](https://www.statlearning.com/) | 40 | Practical classical ML in Python; free PDF. |
| Companion | [*Probabilistic Machine Learning: An Introduction* (Murphy)](https://probml.github.io/pml-book/book1.html) | reference | The best modern reference. |
| Depth | *The Elements of Statistical Learning* (free PDF) | reference | Deeper theory. |
| Depth | [Probabilistic Machine Learning: Advanced Topics (Murphy)](https://probml.github.io/pml-book/book2.html) | reference | When probabilistic modeling/world models become central. |
| ★ | [Kaggle Learn: Intro and Intermediate ML, Feature Engineering](https://www.kaggle.com/learn) and one beginner competition | 30 | Practical pipeline and leakage lessons. |
| ★ | [scikit-learn user guide](https://scikit-learn.org/stable/user_guide.html) | 15 | Pipelines, model selection, metrics. |
| Depth | SQL for analysis + pandas/Polars; experiment design and A/B testing (basics) | 30 | Needed for Track H and for evaluating products. |

## Topics checklist

Linear/logistic/softmax regression; regularization; bias-variance; model selection and cross-validation; Naive Bayes and discriminant analysis; k-means, GMM and EM; PCA/SVD; kernels (conceptual); decision trees, random forests, gradient boosting (XGBoost/LightGBM); evaluation (precision/recall, ROC/PR, calibration, confidence intervals); leakage; learning theory intuition (VC, generalization); time-series basics; recommender basics (optional).

## Data science practice (do not skip)

- Always build a **dumb baseline** before a model.
- Plot before you fit. Check label quality and class balance.
- Report uncertainty. A single test number is not a result.
- Keep a train/validation/test discipline; hold out the final test set until the end.

## Projects

1. **`20-ml-from-first-principles`** (NumPy only): linear regression (closed form and GD), logistic regression, softmax classifier, PCA, k-means, GMM with EM. Use scikit-learn only as the reference baseline. Report: overfitting, regularization, feature scaling, data-size effects, PCA reconstruction, leakage demonstration.
2. **`21-tabular-end-to-end`**: a real dataset, EDA, baseline, gradient-boosted model, proper CV, calibration, error analysis, short report. Publish it.

## Done when

You can choose, train and honestly evaluate a classical model on a messy dataset, and explain why it works or fails mathematically.
