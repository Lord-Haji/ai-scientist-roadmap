# Level 1: CS Core (job-ready)

**Goal:** the equivalent of the first three years of an undergraduate CS degree, enough to pass software-engineering interviews and to understand what runs under your models.  
**Time:** 900-1,100 h if you do every starred item from scratch (people with a CS degree should test out of most of it). **Runs in parallel with Level 2** (split each week by days). **Prerequisites:** Level 0.

**Recommended order:** 1.1 programming -> **1.3 discrete math (6.042J) first** -> 1.2 algorithms -> 1.4 systems -> 1.5 applications. Where two starred items cover the same ground, the table marks one as the choice and the other as optional.

Structure follows [OSSU Computer Science](https://github.com/ossu/computer-science) (which follows the ACM/IEEE CS2013 guidelines), re-weighted toward what AI engineers and researchers actually need. OSSU's own categories: Intro CS, Core programming, Core math, CS tools, Core systems, Core theory, Core security, Core applications, Core ethics, then Advanced CS and a final project. Check the current OSSU README before starting; their course list changes when upstream courses retire.

> Harvard's on-campus CS50 is changing format in fall 2026 (lecture format, assessments, grading; Prof. Malan is on sabbatical), per the [Harvard Crimson](https://www.thecrimson.com/article/2026/9/3/cs50-malan-sabbatical/). That report covers the campus course, not the online CS50x; check the current CS50x page for what is available to you.

## Test-out

- Implement a hash map, a binary heap, and Dijkstra from scratch without looking anything up.
- Explain virtual memory, a page fault, and what happens between typing a URL and the page rendering.
- Write a SQL query with a join, a window function and an index-aware filter, and read an `EXPLAIN` plan.
- Explain CAP/consensus at the level of "why Raft needs a majority".

## 1.1 Intro and programming (★)

| | Resource | Hours | Notes |
|---|---|---:|---|
| ★ | [CS50x: Introduction to Computer Science](https://cs50.harvard.edu/x/) | 100-150 | C, memory, data structures, Python, SQL, web. Skip if you pass the test-out. |
| Depth (pick CS50x *or* CS61A as your main intro) | [Berkeley CS61A: Structure and Interpretation of Computer Programs](https://cs61a.org/) | 100 | Abstraction, recursion, interpreters. Choose this instead of CS50x if you already program. |
| Depth | [How to Design Programs / Systematic Program Design](https://htdp.org/) | 60 | OSSU's choice; more software-design flavour. |
| Depth | [Crafting Interpreters](https://craftinginterpreters.com/) | 40-60 | Free book; build two interpreters. The most approachable compilers resource, and it helps with understanding tool-calling DSLs and ML compilers later. |
| Depth | [Dan Grossman, *Programming Languages*, Part A](https://www.coursera.org/learn/programming-languages) (Coursera; Parts B and C follow) | 60 | OSSU's earlier choice; ML, Racket and Ruby; functional programming, types, language semantics. Rated 4.9 by learners. Good use of Coursera access. |
| ★ (for AI) | **C++ or Rust basics** via [Learn C++](https://www.learncpp.com/) or [The Rust Book](https://doc.rust-lang.org/book/) | 40 | You need to read C++/CUDA and sometimes Rust (tokenizers, inference engines). |

## 1.2 Data structures and algorithms (★)

| | Resource | Hours | Notes |
|---|---|---:|---|
| ★ | [Princeton Algorithms (Sedgewick and Wayne)](https://algs4.cs.princeton.edu/) | 100 | Book + lectures; clear and implementation-focused. |
| Companion | [Princeton Algorithms, Part I](https://www.coursera.org/learn/algorithms-part1) (Coursera; Part II follows) | 60 | Same lectures with graded Java assignments and autograder; 97% of learners liked it. Use it as the structured way through algs4. |
| Companion | [MIT 6.006 Introduction to Algorithms](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/) | 80 | More proof-oriented alternative to algs4; take it if you want rigor. Overlaps with algs4, so do not do both in full. |
| Companion | [Stanford Algorithms Specialization (Roughgarden)](https://www.coursera.org/specializations/algorithms) (Coursera, 4 courses) | 80 | OSSU's choice; excellent divide-and-conquer and randomized-algorithm explanations. Also overlaps. |
| ★ | [NeetCode roadmap](https://neetcode.io/roadmap) | 150-250 over time | Interview-pattern practice. Plan on 5-10 problems/week for 6-12 months before interviewing. Keep going in the background. |
| Reference | *Algorithm Design* (Kleinberg and Tardos), *CLRS* | n/a | Reference. |

## 1.3 Core math for CS (★, overlaps Level 2)

| | Resource | Hours | Notes |
|---|---|---:|---|
| ★ | [MIT 6.042J Mathematics for Computer Science](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/) | 100 | Proofs, induction, graphs, counting, probability basics. |
| Depth | [Sipser, Introduction to the Theory of Computation](https://math.mit.edu/~sipser/book.html) | 60 | Automata, decidability, NP-completeness. |

## 1.4 Systems (★)

| | Resource | Hours | Notes |
|---|---|---:|---|
| Depth | [Nand to Tetris, parts 1 and 2](https://www.nand2tetris.org/) ([Part I](https://www.coursera.org/learn/build-a-computer) and [Part II](https://www.coursera.org/learn/nand2tetris2) on Coursera) | 60-100 | Hardware to compiler to OS. Optional if you take CS:APP, but wonderful. |
| ★ | [CMU 15-213 / *CS:APP*](https://csapp.cs.cmu.edu/) | 120 | Machine representation, assembly, caches, linking, concurrency. Most valuable systems course for anyone who later does GPU/ML systems. |
| ★ | [Operating Systems: Three Easy Pieces](https://pages.cs.wisc.edu/~remzi/OSTEP/) | 60 | Virtualization, concurrency, persistence. Free book. |
| ★ | [Computer Networking: A Top-Down Approach (Kurose and Ross)](http://gaia.cs.umass.edu/kurose_ross/) | 50 | Needed for distributed systems and serving. |
| Depth | [Berkeley CS61C: Great Ideas in Computer Architecture](https://cs61c.org/) | 80 | Pipelines, caches, SIMD, parallelism. Good bridge to GPUs. |

## 1.5 Applications and software engineering (★ for jobs)

| | Resource | Hours | Notes |
|---|---|---:|---|
| ★ | [CMU 15-445 Database Systems](https://15445.courses.cs.cmu.edu/) | 80 | Storage, indexes, query processing, transactions. Also learn SQL fluently. |
| ★ | *Designing Data-Intensive Applications* (Kleppmann) | 40 | The practical distributed-data book. |
| ★ | [MIT 6.5840 Distributed Systems](https://pdos.csail.mit.edu/6.824/) | 100 | Labs implement Raft and a sharded KV store. Hard and worth it. |
| ★ | A software-engineering course: OSSU lists the UBC *Software Construction/Design* sequence; alternatives: [MIT 6.031](https://web.mit.edu/6.031/www/), *A Philosophy of Software Design* (Ousterhout) | 60 | Testing, design, code review, version control in teams. |
| Depth | Docker and Kubernetes (official tutorials), basic CI/CD with GitHub Actions | 20 | Job-ready baseline. |

## 1.6 Security and ethics (breadth)

| | Resource | Hours | Notes |
|---|---|---:|---|
| ★ | [Stanford CS253 Web Security](https://web.stanford.edu/class/cs253/) (or MIT 6.5660 Computer Systems Security; check the current page) and the OWASP Top 10 | 30-40 | Threat modeling, injection, authentication, sandboxing. Direct background for LLM/agent security later. |
| Companion | [Stanford Cryptography I (Boneh)](https://www.coursera.org/learn/crypto) | 40 | Optional but useful. |
| ★ | Ethics: OSSU's ethics requirement, plus the policy/safety material in Track D | 15 | |

## Level 1 projects (do all)

1. **`01-algorithms-kit`**: implement and test core structures (hash map, heap, balanced tree or skip list, graph algorithms, union-find) with benchmarks.
2. **`02-mini-shell-or-kv-store`**: a small shell, or a persistent key-value store with a write-ahead log; or finish the MIT 6.5840 Raft lab.
3. **`03-web-service`**: a small API service with a database, tests, Docker, CI, and a README that a stranger can run.

## Interview prep (start by the end of Level 1, never stop)

See [`career/interview-prep.md`](../career/interview-prep.md): coding (NeetCode/LeetCode rhythm), system design, behavioral, then ML-specific rounds.

## Done when

You can build, test, containerize and deploy a service with a database; reason about time/space cost; read someone else's systems code; and explain memory, processes, networking and transactions without handwaving.
