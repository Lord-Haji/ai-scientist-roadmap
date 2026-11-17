# Level 0: Foundations

**Goal:** be comfortable in a terminal, Git, and Python, and have working high-school math.  
**Time:** 60-100 h. **Unlocks:** everything.

## Test-out (skip if you pass all, cold)

- Write a Python script that reads a CSV, computes grouped statistics, and plots a chart, using a virtualenv and pytest for one function.
- In a shell: find the 5 largest files under a directory, grep with regex, pipe and redirect, write a small bash loop.
- Git: branch, rebase, resolve a merge conflict, open a PR.
- Math: solve a quadratic, simplify logs/exponents, sum an arithmetic and a geometric series, take a simple derivative.

## Resources

| | Resource | Hours | Notes |
|---|---|---:|---|
| ★ | [CS50P: Introduction to Programming with Python](https://cs50.harvard.edu/python/) | 40-60 | Best gentle start in Python. Skip if you can already do the Python test-out. |
| ★ | [MIT Missing Semester](https://missing.csail.mit.edu/) | 15-20 | Shell, editors, Git, debugging, profiling, tooling. Do it early; it pays back forever. |
| ★ | [Official Python Tutorial](https://docs.python.org/3/tutorial/) + [NumPy Learn](https://numpy.org/learn/) | 15 | Typing, venvs, iterators, vectorization. |
| ★ | [Khan Academy: Algebra and Precalculus](https://www.khanacademy.org/math) | 20-40 | Only the parts you fail in the test-out. |
| Companion | [Pro Git](https://git-scm.com/book/en/v2) | 5 | Reference. |
| Companion | [Python for Everybody](https://www.py4e.com/) | 40 | Alternative if CS50P is too fast. |
| Companion | [Kaggle Learn: Python, Pandas](https://www.kaggle.com/learn) | 10 | Quick data-wrangling reps. |

## Project: `00-scientific-python`

A small package/notebook implementing vector and matrix operations in plain Python then NumPy, finite-difference derivatives, Monte Carlo estimation of pi, plotting, and a timing comparison of loops vs vectorization, with pytest tests.  
Done when Python syntax is no longer the main obstacle when reading ML repos.

## Habits to start now

- Use a virtual environment (or `uv`) for every project.
- Write tests for numerical code (shapes, known values, gradients).
- Commit early and often, with messages that say why.
