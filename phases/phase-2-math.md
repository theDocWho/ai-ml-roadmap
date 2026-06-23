# Phase 2 — Math Foundations, Visual-First (≈5–6 weeks)

**Goal:** the intuition under everything else — linear algebra, calculus/gradients, probability, and
optimization. Visual-first (3Blue1Brown, StatQuest) the way you like it. This directly powers exam
**Q1, Q6, Q7, Q8, Q10, Q12, Q13, Q15, Q35** and challenges **BYO-2, BYO-4**.

**Primary free resources** (we point at exact chapters/videos):
- 3Blue1Brown — *Essence of Linear Algebra* — https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab
- 3Blue1Brown — *Essence of Calculus* — https://www.youtube.com/playlist?list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr
- StatQuest — *Statistics Fundamentals* — https://www.youtube.com/playlist?list=PLblh5JKOoLUK0FLuzwntyYI10UQFUhsY9
- Khan Academy — https://www.khanacademy.org (Linear Algebra · Multivariable Calculus · Statistics & Probability)
- *Mathematics for Machine Learning* (free PDF) — https://mml-book.github.io

---

## Module 2A — Linear Algebra

| # | Topic | Watch / read exactly this | ~Time |
|---|-------|---------------------------|-------|
| 1 | Vectors, span, basis | 3B1B Essence of LA **Ch.1–2** ("Vectors" / "Linear combinations, span, basis") | 30m |
| 2 | Linear transformations = matrices | 3B1B **Ch.3 "Linear transformations and matrices"** | 12m |
| 3 | Matrix multiply as composition | 3B1B **Ch.4 "Matrix multiplication as composition"** | 12m |
| 4 | Determinant (what it *means*) | 3B1B **Ch.6 "The determinant"** | 10m |
| 5 | Inverse, rank, column space, null space | 3B1B **Ch.7 "Inverse matrices, column space and null space"** | 13m |
| 6 | **Dot / inner products & orthogonality** (exam Q1) | 3B1B **Ch.9 "Dot products and duality"** + MML book **Ch.3 "Analytic Geometry"** (§3.1–3.3 inner products, orthogonality) | 45m |
| 7 | Change of basis | 3B1B **Ch.13 "Change of basis"** | 13m |
| 8 | **Eigenvalues & eigenvectors** (exam Q10) | 3B1B **Ch.14 "Eigenvectors and eigenvalues"** + **Ch.15 "Quick trick for eigenvalues"** | 25m |
| 9 | SVD (used in PCA, dimensionality reduction) | Steve Brunton — "Singular Value Decomposition (SVD): Overview" (YouTube) | 15m |
| 10 | Do it in NumPy | Practice: `np.linalg.eig`, `np.linalg.svd`, `@`, `np.dot` | 30m |

**✅ Checkpoint 2A** — one item per topic:
- **(T1)** Write `(5,3)` as a linear combination of `(1,0)` and `(0,1)`; in one sentence, what is the *span* of two non-parallel 2-D vectors?
- **(T2)** Apply the matrix `[[2,0],[0,3]]` to vector `(1,1)` by hand; what transformation is it (geometrically)?
- **(T3)** Multiply `[[1,1],[0,1]] @ [[2,0],[0,2]]` by hand; explain it as *composing* two transformations.
- **(T4)** Compute `det([[2,1],[1,3]])`; what does its value say about area scaling, and what would `det = 0` mean?
- **(T5)** Invert `[[2,1],[1,1]]`; state what the **rank** and **null space** tell you about whether `Ax=b` is solvable.
- **(T6)** With the custom inner product `⟨x,y⟩ = 3x₁y₁ + 2x₂y₂`, find the orthogonal pair (exam Q1); separately, are `(1,2)` and `(2,−1)` orthogonal under the *standard* dot product?
- **(T7)** Express the vector `(3,1)` in the basis `{(1,1),(1,−1)}` (solve for the coordinates).
- **(T8)** **By hand**, find the eigenvalues of `[[1,8],[2,1]]` (exam Q10); verify with `np.linalg.eig`; explain what an eigenvector *means* geometrically.
- **(T9)** Run `np.linalg.svd` on a `(4,3)` matrix; what do the singular values represent, and how does SVD relate to PCA?
- **(T10)** 🔨 Start **[BYO-4 (K-Means + PCA)](../challenges/byo-04-kmeans-pca/README.md)** — implement PCA via covariance eigendecomposition.

---

## Module 2B — Calculus & Gradients

| # | Topic | Watch / read exactly this | ~Time |
|---|-------|---------------------------|-------|
| 11 | What a derivative really is | 3B1B Essence of Calculus **Ch.1–2** ("Essence" / "Paradox of the derivative") | 35m |
| 12 | Derivative rules via geometry | 3B1B **Ch.3 "Derivative formulas through geometry"** | 15m |
| 13 | **Chain rule & product rule** (backbone of backprop) | 3B1B **Ch.4 "Visualizing the chain rule and product rule"** | 15m |
| 14 | `e` and exponentials (logits, softmax later) | 3B1B **Ch.5 "What's so special about Euler's number e?"** | 14m |
| 15 | Higher-order derivatives (concavity → maxima/minima) | 3B1B **Ch.10 "Higher order derivatives"** | 5m |
| 16 | **Local maxima / minima & critical points** (exam Q6, Q15) | Khan Academy — "Applications of derivatives → Critical points & the first/second derivative test" | 40m |
| 17 | **Partial derivatives & the gradient** (multivariable) | Khan Academy — "Multivariable calculus → Derivatives of multivariable functions → Gradient and directional derivatives" | 60m |
| 18 | Taylor series (used in optimization theory) | 3B1B **Ch.11 "Taylor series"** | 22m |

**✅ Checkpoint 2B** — one item per topic:
- **(T11)** In one sentence, define the derivative as a limit; what does `f'(x)` measure at a point?
- **(T12)** Differentiate `f(x)=3x² + 5x` using the power rule; check the slope at `x=1` numerically.
- **(T13)** Use the **chain rule** to differentiate `f(x)=(2x+1)³`; explain why the chain rule is the heart of backprop.
- **(T14)** What is `d/dx eˣ`? Why does `e` keep showing up in softmax/logistic functions?
- **(T15)** Compute `f''(x)` for `f(x)=2x³−3x²`; how does the sign of `f''` tell you concave up vs down?
- **(T16)** Find the critical points of `f(x)=2x³−3x²−12x+5` and classify each as min/max using the second-derivative test (exam Q15 + Q6); verify by plotting.
- **(T17)** Compute the **gradient** of `f(x,y)=3x² + 2y²` by hand; which direction does it point, and what does that mean for gradient *descent*?
- **(T18)** Write the first 3 terms of the Taylor series of `eˣ` around 0; why are Taylor approximations useful in optimization?

---

## Module 2C — Probability & Statistics

| # | Topic | Watch / read exactly this | ~Time |
|---|-------|---------------------------|-------|
| 19 | Mean, variance, std, distributions | StatQuest — "Mean, Variance and Standard Deviation" + "The Normal Distribution, Clearly Explained!!!" | 35m |
| 20 | Expected value | StatQuest — "Expected Values, Clearly Explained!!!" | 12m |
| 21 | Probability vs likelihood | StatQuest — "Probability is not Likelihood. Find out why!!!" | 5m |
| 22 | **Maximum likelihood** (foundation of model fitting) | StatQuest — "Maximum Likelihood, clearly explained!!!" | 10m |
| 23 | **Bayes' theorem** (exam Q12, Q13) | StatQuest — "Bayes' Theorem, Clearly Explained!!!!" + MML book **Ch.6 §6.3** | 30m |
| 24 | Covariance & correlation (→ PCA, features) | StatQuest — "Covariance, Clearly Explained!!!" + "Pearson's Correlation, Clearly Explained!!!" | 30m |
| 25 | *(beyond exam)* Entropy, cross-entropy, KL (loss functions) | StatQuest — "Entropy (for data science) Clearly Explained!!!" + Aurélien Géron — "A Short Introduction to Entropy, Cross-Entropy and KL-Divergence" | 35m |
| 26 | *(beyond exam)* Hypothesis testing, p-values, A/B testing | StatQuest — "Hypothesis Testing and the Null Hypothesis" + "p-values, clearly explained" | 40m |

**✅ Checkpoint 2C** — one item per topic:
- **(T19)** Compute the mean, variance, and std of `[2,4,4,4,5,5,7,9]` by hand; sketch what a Normal distribution's μ and σ control.
- **(T20)** Compute the **expected value** of a die roll; of a bet that pays +10 with p=0.3 and −5 otherwise.
- **(T21)** In one sentence, distinguish *probability* (fixed model, varying data) from *likelihood* (fixed data, varying model).
- **(T22)** Explain what **maximum likelihood** estimates; intuitively, why does fitting a model = maximizing likelihood?
- **(T23)** State **Bayes' theorem** and label posterior / likelihood / prior / evidence (exam Q13); explain why max-discriminant = max-posterior = min-conditional-risk (exam Q12).
- **(T24)** Compute the **covariance** sign for two up-trending variables; what does a correlation of −0.9 mean?
- **(T25)** *(beyond exam)* Compute the **entropy** of a fair coin vs a 90/10 coin; compute **cross-entropy** between `[1,0,0]` and softmax `[0.7,0.2,0.1]`; one line on what **KL divergence** measures.
- **(T26)** *(beyond exam)* In words: what is a **p-value**, what's a null hypothesis, and what does an **A/B test** decide?

---

## Module 2D — Optimization (gradient descent)

| # | Topic | Watch / read exactly this | ~Time |
|---|-------|---------------------------|-------|
| 27 | **Gradient descent, step by step** (exam Q35) | StatQuest — "Gradient Descent, Step-by-Step" | 24m |
| 28 | Stochastic gradient descent | StatQuest — "Stochastic Gradient Descent, Clearly Explained!!!" | 10m |
| 29 | Learning rate intuition; convexity vs local minima | 3B1B Neural Networks **Ch.2 "Gradient descent, how neural networks learn"** (first ~10 min) | 12m |
| 30 | **Adaptive optimizers: Adagrad / RMSprop / Adam** (exam Q7, Q8) | Read: "An overview of gradient descent optimization algorithms" — https://www.ruder.io/optimizing-gradient-descent/ (sections on Adagrad/RMSprop/Adam) | 40m |

**✅ Checkpoint 2D** — one item per topic:
- **(T27)** Write the steepest-descent update `w(n+1) = w(n) − η·∇E` and explain each symbol (exam Q35); what does `η` (learning rate) control?
- **(T28)** Explain how **stochastic** GD differs from full-batch GD, and one pro/con of each.
- **(T29)** Describe what happens if `η` is too large vs too small; why can non-convex losses trap GD in a *local* minimum?
- **(T30)** In one line each, say how **Adagrad** (exam Q8) and **RMSprop** accumulate gradient history, and how **Adam** combines momentum + RMSprop (exam Q7).
- *(integrative)* 🔨 Do **[BYO-2 (regression engine)](../challenges/byo-02-regression/README.md)** — implement gradient descent and watch the loss fall. Your math, made real.

---

## 🏁 Phase 2 capstone exercises — math you can *run*
- **Gradient-descent visualizer** (NumPy + Matplotlib): animate descent on `f(x)=x²` and a 2-D bowl.
- **Linear regression from scratch** (normal equation *and* GD) — = BYO-2.
- **PCA from scratch** via covariance eigendecomposition — = BYO-4.

**You're ready for Phase 3 when** you can explain (and code) a gradient, an eigenvector, and a Bayes
update — and you've implemented gradient descent and PCA yourself.
