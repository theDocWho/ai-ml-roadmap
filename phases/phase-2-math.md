# Phase 2 — Math Foundations, Visual-First (≈5–6 weeks)

**Goal:** the intuition under everything — linear algebra, calculus/gradients, probability, optimization.
Visual-first (3Blue1Brown, StatQuest, Vizuara). Powers exam **Q1, Q6, Q7, Q8, Q10, Q12, Q13, Q15, Q35**
and challenges **BYO-2, BYO-4**.

**Environment:** concepts are pen-and-paper; verification is **🖥️ Local** in a notebook (NumPy). No GPU
needed in this phase.

**🔄 Freshness:** **math doesn't change** — these references stay valid regardless of age; there's no
"latest version" to chase. (Only the *coding* you use to verify it follows current NumPy.)

**Primary resources** (open the linked playlist/site, then the **bold** item):
- [3Blue1Brown — *Essence of Linear Algebra*](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab) · [*Essence of Calculus*](https://www.youtube.com/playlist?list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr) · [*Neural Networks*](https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi)
- [StatQuest — *Statistics Fundamentals*](https://www.youtube.com/playlist?list=PLblh5JKOoLUK0FLuzwntyYI10UQFUhsY9) · [Khan Academy](https://www.khanacademy.org) · [*Mathematics for ML* (free PDF)](https://mml-book.github.io)
- 🆕 [Vizuara](https://www.youtube.com/@vizuara) — excellent "Math for ML" and "from scratch" explainers; a great second angle when a 3B1B chapter doesn't click.
- 🎨 **[Illustrated explainers](https://thedocwho.github.io/ai-ml-roadmap/illustrated/index.html)** (interactive, offline): [Matrices as transformations](https://thedocwho.github.io/ai-ml-roadmap/illustrated/2-math/matrix-transformation.html), [Dot product & projection](https://thedocwho.github.io/ai-ml-roadmap/illustrated/2-math/dot-product.html) (Q1), [Bayes' theorem](https://thedocwho.github.io/ai-ml-roadmap/illustrated/2-math/bayes-theorem.html) (Q12/Q13), [Optimizer comparison](https://thedocwho.github.io/ai-ml-roadmap/illustrated/2-math/optimizer-comparison.html); plus curated [eigenvectors](https://setosa.io/ev/eigenvectors-and-eigenvalues/), [PCA](https://setosa.io/ev/principal-component-analysis/) & [Seeing Theory](https://seeing-theory.brown.edu/).

---

## Module 2A — Linear Algebra

| # | Topic | Open exactly this | ~Time |
|---|-------|-------------------|-------|
| 1 | Vectors, span, basis | [3B1B Essence of LA](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab) — **Ch.1 "Vectors"** + **Ch.2 "Linear combinations, span, basis"** · 📖 [MML book Ch.2 (Linear Algebra)](https://mml-book.github.io) | 30m |
| 2 | Linear transformations = matrices | [3B1B](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab) — **Ch.3 "Linear transformations and matrices"** · 🎨 [Visualize: matrix transforms](https://thedocwho.github.io/ai-ml-roadmap/illustrated/2-math/matrix-transformation.html) · 📖 [MML book §2.7](https://mml-book.github.io) | 12m |
| 3 | Matrix multiply as composition | [3B1B](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab) — **Ch.4 "Matrix multiplication as composition"** · 📖 [MML book §2.2 (Matrices)](https://mml-book.github.io) | 12m |
| 4 | Determinant | [3B1B](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab) — **Ch.6 "The determinant"** · 🎨 [Visualize: det = area](https://thedocwho.github.io/ai-ml-roadmap/illustrated/2-math/matrix-transformation.html) · 📖 [MML book §4.1](https://mml-book.github.io) | 10m |
| 5 | Inverse, rank, column space, null space | [3B1B](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab) — **Ch.7 "Inverse matrices, column space, null space"** · 📖 [MML book §2.3–2.6](https://mml-book.github.io) | 13m |
| 6 | **Dot/inner products & orthogonality** (exam Q1) | [3B1B](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab) — **Ch.9 "Dot products and duality"** · 🎨 [Visualize: dot product](https://thedocwho.github.io/ai-ml-roadmap/illustrated/2-math/dot-product.html) + [MML book](https://mml-book.github.io) **§3.1–3.3** | 45m |
| 7 | Change of basis | [3B1B](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab) — **Ch.13 "Change of basis"** · 📖 [MML book §2.7.2 (Basis Change)](https://mml-book.github.io) | 13m |
| 8 | **Eigenvalues & eigenvectors** (exam Q10) | [3B1B](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab) — **Ch.14 "Eigenvectors and eigenvalues"** + **Ch.15 "Quick trick"** · 📖 [MML book §4.2 (Eigenvalues & Eigenvectors)](https://mml-book.github.io) | 25m |
| 9 | SVD (used in PCA) | [Steve Brunton (YouTube)](https://www.youtube.com/@Eigensteve) — **"Singular Value Decomposition (SVD): Overview"** · 📖 [MML book §4.5 (SVD)](https://mml-book.github.io) | 15m |
| 10 | Do it in NumPy | [NumPy linalg docs (stable)](https://numpy.org/doc/stable/reference/routines.linalg.html) — `eig`, `svd`, `@`, `dot` | 30m |

**✅ Checkpoint 2A** — 🖥️ Local — one per topic:
- **(T1)** Write `(5,3)` as a linear combination of `(1,0)` and `(0,1)`; what is the *span* of two non-parallel 2-D vectors?
- **(T2)** Apply `[[2,0],[0,3]]` to `(1,1)` by hand; what transformation is it?
- **(T3)** Multiply `[[1,1],[0,1]] @ [[2,0],[0,2]]` by hand; explain it as *composing* transformations.
- **(T4)** `det([[2,1],[1,3]])`: what does it say about area scaling, and what does `det=0` mean?
- **(T5)** Invert `[[2,1],[1,1]]`; what do **rank** and **null space** tell you about solving `Ax=b`?
- **(T6)** With `⟨x,y⟩ = 3x₁y₁ + 2x₂y₂`, find the orthogonal pair (exam Q1); are `(1,2)`,`(2,−1)` orthogonal under the standard dot product?
- **(T7)** Express `(3,1)` in the basis `{(1,1),(1,−1)}`.
- **(T8)** **By hand**, eigenvalues of `[[1,8],[2,1]]` (exam Q10); verify with `np.linalg.eig`; what does an eigenvector mean?
- **(T9)** `np.linalg.svd` a `(4,3)` matrix; what do singular values represent, and how does SVD relate to PCA?
- **(T10)** 🔨 Start **[BYO-4 (K-Means + PCA)](../challenges/byo-04-kmeans-pca/README.md)** — PCA via covariance eigendecomposition.

---

## Module 2B — Calculus & Gradients

| # | Topic | Open exactly this | ~Time |
|---|-------|-------------------|-------|
| 11 | What a derivative is | [3B1B Essence of Calculus](https://www.youtube.com/playlist?list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr) — **Ch.1–2** · 📖 [Khan: Differential Calculus](https://www.khanacademy.org/math/differential-calculus) | 35m |
| 12 | Derivative rules via geometry | [3B1B](https://www.youtube.com/playlist?list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr) — **Ch.3 "Derivative formulas through geometry"** · 📖 [Khan: Derivative rules](https://www.khanacademy.org/math/differential-calculus/dc-diff-intro) | 15m |
| 13 | **Chain & product rule** (backbone of backprop) | [3B1B](https://www.youtube.com/playlist?list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr) — **Ch.4 "Visualizing the chain rule and product rule"** · 📖 [Khan: Chain rule](https://www.khanacademy.org/math/differential-calculus/dc-chain) | 15m |
| 14 | `e` and exponentials | [3B1B](https://www.youtube.com/playlist?list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr) — **Ch.5 "What's so special about Euler's number e?"** · 📖 [MML book §5 (Vector Calculus)](https://mml-book.github.io) | 14m |
| 15 | Higher-order derivatives (concavity) | [3B1B](https://www.youtube.com/playlist?list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr) — **Ch.10 "Higher order derivatives"** · 📖 [Khan: Differential Calculus](https://www.khanacademy.org/math/differential-calculus) | 5m |
| 16 | **Maxima/minima & critical points** (exam Q6, Q15) | [Khan — Differential Calculus](https://www.khanacademy.org/math/differential-calculus) — **"Analyzing functions → critical points / 2nd-derivative test"** | 40m |
| 17 | **Partial derivatives & the gradient** | [Khan — Multivariable Calculus](https://www.khanacademy.org/math/multivariable-calculus) — **"Derivatives of multivariable functions → gradient"** | 60m |
| 18 | Taylor series | [3B1B](https://www.youtube.com/playlist?list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr) — **Ch.11 "Taylor series"** · 📖 [Khan: Taylor & Maclaurin series](https://www.khanacademy.org/math/ap-calculus-bc) | 22m |

**✅ Checkpoint 2B** — 🖥️ Local — one per topic:
- **(T11)** Define the derivative as a limit in one sentence; what does `f'(x)` measure?
- **(T12)** Differentiate `f(x)=3x²+5x` (power rule); check the slope at `x=1` numerically.
- **(T13)** Chain-rule `f(x)=(2x+1)³`; why is the chain rule the heart of backprop?
- **(T14)** What is `d/dx eˣ`? Why does `e` show up in softmax/logistic?
- **(T15)** `f''(x)` for `f(x)=2x³−3x²`; how does the sign of `f''` mean concave up/down?
- **(T16)** Critical points of `f(x)=2x³−3x²−12x+5`, classified via the 2nd-derivative test (exam Q15+Q6); verify by plotting.
- **(T17)** Gradient of `f(x,y)=3x²+2y²` by hand; which way does it point, and what does that mean for descent?
- **(T18)** First 3 Taylor terms of `eˣ` at 0; why are Taylor approximations useful in optimization?

---

## Module 2C — Probability & Statistics

| # | Topic | Open exactly this | ~Time |
|---|-------|-------------------|-------|
| 19 | Mean, variance, std, distributions | [StatQuest](https://www.youtube.com/@statquest) — **"Mean, Variance and Standard Deviation"** + **"The Normal Distribution, Clearly Explained!!!"** · 📖 [Khan: Statistics & Probability](https://www.khanacademy.org/math/statistics-probability) | 35m |
| 20 | Expected value | [StatQuest](https://www.youtube.com/@statquest) — **"Expected Values, Clearly Explained!!!"** · 📖 [Khan: Random variables & expected value](https://www.khanacademy.org/math/statistics-probability/random-variables-stats-library) | 12m |
| 21 | Probability vs likelihood | [StatQuest](https://www.youtube.com/@statquest) — **"Probability is not Likelihood. Find out why!!!"** · 📖 [MML book §6.1–6.2 (Probability)](https://mml-book.github.io) | 5m |
| 22 | **Maximum likelihood** | [StatQuest](https://www.youtube.com/@statquest) — **"Maximum Likelihood, clearly explained!!!"** · 📖 [MML book §8.3 (MLE)](https://mml-book.github.io) | 10m |
| 23 | **Bayes' theorem** (exam Q12, Q13) | [StatQuest](https://www.youtube.com/@statquest) — **"Bayes' Theorem, Clearly Explained!!!!"** · 🎨 [Visualize: Bayes update](https://thedocwho.github.io/ai-ml-roadmap/illustrated/2-math/bayes-theorem.html) + [MML book](https://mml-book.github.io) **§6.3** | 30m |
| 24 | Covariance & correlation | [StatQuest](https://www.youtube.com/@statquest) — **"Covariance, Clearly Explained!!!"** + **"Pearson's Correlation"** · 📖 [Khan: Exploring bivariate data](https://www.khanacademy.org/math/statistics-probability/describing-relationships-quantitative-data) | 30m |
| 25 | *(beyond exam)* Entropy, cross-entropy, KL | [StatQuest](https://www.youtube.com/@statquest) — **"Entropy (for data science)"** + [Vizuara](https://www.youtube.com/@vizuara) — search **"Cross-Entropy / KL divergence"** · 📖 [Chris Olah: Visual Information Theory](https://colah.github.io/posts/2015-09-Visual-Information/) | 35m |
| 26 | *(beyond exam)* Hypothesis testing, p-values, A/B testing | [StatQuest](https://www.youtube.com/@statquest) — **"Hypothesis Testing and the Null Hypothesis"** + **"p-values, clearly explained"** · 📖 [Seeing Theory: Frequentist Inference](https://seeing-theory.brown.edu/frequentist-inference/index.html) | 40m |

**✅ Checkpoint 2C** — 🖥️ Local — one per topic:
- **(T19)** Mean/variance/std of `[2,4,4,4,5,5,7,9]` by hand; what do a Normal's μ and σ control?
- **(T20)** Expected value of a die roll; of a bet paying +10 at p=0.3 else −5.
- **(T21)** Distinguish probability vs likelihood in one sentence.
- **(T22)** What does maximum likelihood estimate; why is fitting a model = maximizing likelihood?
- **(T23)** State Bayes' theorem; label posterior/likelihood/prior/evidence (exam Q13); why max-discriminant = max-posterior = min-conditional-risk (exam Q12)?
- **(T24)** Covariance sign for two up-trending variables; what does correlation −0.9 mean?
- **(T25)** Entropy of a fair vs 90/10 coin; cross-entropy of `[1,0,0]` vs softmax `[0.7,0.2,0.1]`; one line on what KL measures.
- **(T26)** In words: what is a p-value, a null hypothesis, and what does an A/B test decide?

---

## Module 2D — Optimization (gradient descent)

| # | Topic | Open exactly this | ~Time |
|---|-------|-------------------|-------|
| 27 | **Gradient descent, step by step** (exam Q35) | [StatQuest](https://www.youtube.com/@statquest) — **"Gradient Descent, Step-by-Step"** · 📖 [d2l.ai: Gradient Descent](https://d2l.ai/chapter_optimization/gd.html) | 24m |
| 28 | Stochastic gradient descent | [StatQuest](https://www.youtube.com/@statquest) — **"Stochastic Gradient Descent, Clearly Explained!!!"** · 📖 [d2l.ai: Stochastic Gradient Descent](https://d2l.ai/chapter_optimization/sgd.html) | 10m |
| 29 | Learning rate; convex vs local minima | [3B1B Neural Networks](https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi) — **Ch.2 "Gradient descent, how neural networks learn"** (first ~10 min) · 📖 [d2l.ai: Optimization & Deep Learning](https://d2l.ai/chapter_optimization/optimization-intro.html) | 12m |
| 30 | **Adagrad / RMSprop / Adam** (exam Q7, Q8) | [Sebastian Ruder — "An overview of gradient descent optimization algorithms"](https://www.ruder.io/optimizing-gradient-descent/) (Adagrad/RMSprop/Adam sections) | 40m |

**✅ Checkpoint 2D** — 🖥️ Local — one per topic:
- **(T27)** Write `w(n+1) = w(n) − η·∇E` and explain each symbol (exam Q35); what does `η` control?
- **(T28)** How does stochastic GD differ from full-batch; one pro/con of each.
- **(T29)** What if `η` is too large vs too small; why can non-convex losses trap GD in a *local* minimum?
- **(T30)** One line each: how Adagrad (Q8) & RMSprop accumulate gradient history; how Adam combines momentum + RMSprop (Q7).
- *(integrative)* 🔨 Do **[BYO-2 (regression engine)](../challenges/byo-02-regression/README.md)** — implement GD and watch the loss fall.

---

## 🏁 Phase 2 capstone — math you can *run*  (🖥️ Local)
- **Gradient-descent visualizer** (NumPy + Matplotlib): animate descent on `f(x)=x²` and a 2-D bowl.
- **Linear regression from scratch** (normal equation + GD) = BYO-2.
- **PCA from scratch** via covariance eigendecomposition = BYO-4.

**Ready for Phase 3 when** you can explain (and code) a gradient, an eigenvector, and a Bayes update —
and you've implemented gradient descent and PCA yourself.
