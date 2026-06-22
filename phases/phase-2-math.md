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

**✅ Checkpoint 2A:**
- **By hand**, find the eigenvalues of `[[1,8],[2,1]]` (exam Q10); verify with `np.linalg.eig`.
- Given the custom inner product `⟨x,y⟩ = 3x₁y₁ + 2x₂y₂`, check which pair is orthogonal (exam Q1).
- Explain geometrically: what is an eigenvector, and why is PCA an eigenproblem?
- 🔨 Start **[BYO-4 (K-Means + PCA)](../challenges/byo-04-kmeans-pca/README.md)** — implement PCA via eigendecomposition.

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

**✅ Checkpoint 2B:**
- Find the critical points of `f(x)=2x³−3x²−12x+5` and classify them (exam Q15 + Q6). Verify by plotting.
- State the first- and second-derivative tests for a local maximum in your own words.
- Compute the gradient of `f(x,y)=3x² + 2y²` by hand; what direction does it point?

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

**✅ Checkpoint 2C:**
- State Bayes' theorem and label posterior / likelihood / prior / evidence (exam Q13).
- Explain why the Bayes classifier's max-discriminant = max-posterior = min-conditional-risk (exam Q12).
- Compute cross-entropy between `[1,0,0]` and a softmax output `[0.7,0.2,0.1]` by hand.

---

## Module 2D — Optimization (gradient descent)

| # | Topic | Watch / read exactly this | ~Time |
|---|-------|---------------------------|-------|
| 27 | **Gradient descent, step by step** (exam Q35) | StatQuest — "Gradient Descent, Step-by-Step" | 24m |
| 28 | Stochastic gradient descent | StatQuest — "Stochastic Gradient Descent, Clearly Explained!!!" | 10m |
| 29 | Learning rate intuition; convexity vs local minima | 3B1B Neural Networks **Ch.2 "Gradient descent, how neural networks learn"** (first ~10 min) | 12m |
| 30 | **Adaptive optimizers: Adagrad / RMSprop / Adam** (exam Q7, Q8) | Read: "An overview of gradient descent optimization algorithms" — https://www.ruder.io/optimizing-gradient-descent/ (sections on Adagrad/RMSprop/Adam) | 40m |

**✅ Checkpoint 2D:**
- Write the steepest-descent update `w(n+1) = w(n) − η·∇E` and explain each symbol (exam Q35).
- In one line each, say how Adagrad and RMSprop differ from plain SGD (exam Q7, Q8).
- 🔨 Do **[BYO-2 (regression engine)](../challenges/byo-02-regression/README.md)** — implement gradient
  descent and watch the loss fall. This is your math made real.

---

## 🏁 Phase 2 capstone exercises — math you can *run*
- **Gradient-descent visualizer** (NumPy + Matplotlib): animate descent on `f(x)=x²` and a 2-D bowl.
- **Linear regression from scratch** (normal equation *and* GD) — = BYO-2.
- **PCA from scratch** via covariance eigendecomposition — = BYO-4.

**You're ready for Phase 3 when** you can explain (and code) a gradient, an eigenvector, and a Bayes
update — and you've implemented gradient descent and PCA yourself.
