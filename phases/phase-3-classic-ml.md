# Phase 3 — Classic Machine Learning (≈6–8 weeks)

**Goal:** the core of ML — the workflow, the algorithms, honest evaluation, and the *judgment* to pick
the right tool. Covers exam **Q9, Q11, Q14, Q16–Q31** and many *(beyond-exam)* topics. This is where
you start the **Decision Lens** habit and dip into [research skills](research-skills.md).

**Environment:** **🖥️ Local** or **📊 Kaggle** — classic ML needs **no GPU**. Use Kaggle for its
datasets + competitions.

**🔄 Freshness:** **scikit-learn** moves (use the current **1.x** docs). The *algorithms/concepts* are
timeless — StatQuest and ISLP stay valid regardless of age.

**Primary resources** (open the link, then the **bold** item):
- [StatQuest — *Machine Learning* playlist](https://www.youtube.com/playlist?list=PLblh5JKOoLUICTaGLRoHQDuF_7q2GfuJF) · 🆕 [Vizuara](https://www.youtube.com/@vizuara) (ML-from-scratch)
- [*Intro to Statistical Learning* (ISLP) — free book + videos](https://www.statlearning.com) · [Andrew Ng — ML Specialization (audit free)](https://www.coursera.org/specializations/machine-learning-introduction)
- [Kaggle Learn](https://www.kaggle.com/learn) (Intro/Intermediate ML, Feature Engineering) · [scikit-learn User Guide (1.x)](https://scikit-learn.org/stable/user_guide.html) · [Google ML Crash Course](https://developers.google.com/machine-learning/crash-course)
- 🎨 **[Illustrated explainers](../illustrated/index.html)** (interactive, offline): [Confusion matrix & metrics](../illustrated/confusion-matrix.html) (Q23), [Regularization Ridge/Lasso](../illustrated/regularization.html), [k-Nearest Neighbors](../illustrated/knn.html), [SVM & kernel trick](../illustrated/svm-margin.html), [k-means steps](../illustrated/kmeans-steps.html); plus curated [R2D3 / decision trees](https://r2d3.us/visual-intro-to-machine-learning-part-1/), [bias–variance](https://mlu-explain.github.io/bias-variance/), [cross-validation](https://mlu-explain.github.io/cross-validation/) & [ROC/AUC](https://mlu-explain.github.io/roc-auc/).

---

## Module 3A — ML foundations, workflow & metrics

| # | Topic | Open exactly this | ~Time |
|---|-------|-------------------|-------|
| 1 | Supervised vs unsupervised (exam Q17, Q19, Q25) | [Google ML Crash Course](https://developers.google.com/machine-learning/crash-course) — **"ML Concepts → Framing"** | 30m |
| 2 | Regression vs classification (exam Q16, Q20) | [StatQuest ML](https://www.youtube.com/playlist?list=PLblh5JKOoLUICTaGLRoHQDuF_7q2GfuJF) — **"Machine Learning Fundamentals: Bias and Variance"** (intro framing) · 📖 [ISLP Ch.2 (Statistical Learning)](https://www.statlearning.com) | 15m |
| 3 | Train/validation/test split & data leakage | [Kaggle Learn — Intro to ML](https://www.kaggle.com/learn/intro-to-machine-learning) — **"Model Validation"** | 25m |
| 4 | **Bias–variance, over/underfitting** | [StatQuest](https://www.youtube.com/playlist?list=PLblh5JKOoLUICTaGLRoHQDuF_7q2GfuJF) — **"Machine Learning Fundamentals: Bias and Variance"** · 📖 [MLU-Explain: Bias–Variance](https://mlu-explain.github.io/bias-variance/) | 7m |
| 5 | **Cross-validation** (exam Q22) | [StatQuest](https://www.youtube.com/playlist?list=PLblh5JKOoLUICTaGLRoHQDuF_7q2GfuJF) — **"Machine Learning Fundamentals: Cross Validation"** · 📖 [scikit-learn: Cross-validation](https://scikit-learn.org/stable/modules/cross_validation.html) | 6m |
| 6 | Regression metrics: MAE/RSS/RMSE/R² (exam Q9, Q14) | [ISLP](https://www.statlearning.com) — **Ch.3 "Linear Regression"** (assessing fit) | 30m |
| 7 | **Classification metrics**: confusion matrix, precision/recall/**F1** (exam Q23) | [StatQuest](https://www.youtube.com/playlist?list=PLblh5JKOoLUICTaGLRoHQDuF_7q2GfuJF) — **"The Confusion Matrix"** + **"Sensitivity and Specificity"** · 🎨 [Visualize: confusion matrix](../illustrated/confusion-matrix.html) · 📖 [scikit-learn: Classification metrics](https://scikit-learn.org/stable/modules/model_evaluation.html#classification-metrics) | 20m |
| 8 | **ROC & AUC** | [StatQuest](https://www.youtube.com/playlist?list=PLblh5JKOoLUICTaGLRoHQDuF_7q2GfuJF) — **"ROC and AUC, Clearly Explained!"** · 📖 [MLU-Explain: ROC & AUC](https://mlu-explain.github.io/roc-auc/) | 16m |

**✅ Checkpoint 3A** — 🖥️/📊 — one per topic:
- **(T1)** Classify each as supervised/unsupervised: object detection, k-means, density estimation (exam Q19); what do both *require*? (exam Q17)
- **(T2)** Give two real problems — one regression, one classification; why is linear regression *not* a classifier (exam Q20)?
- **(T3)** Split a dataset 60/20/20; explain one way data leakage sneaks in.
- **(T4)** Draw the bias–variance curve; where do over- and under-fitting sit?
- **(T5)** Explain k-fold cross-validation; why doesn't it *prevent* overfitting (exam Q22)?
- **(T6)** Compute MAE and RSS for `y=[3,5]`, `ŷ=[2,5]` (exam Q9, Q14).
- **(T7)** From a confusion matrix `TP=2,FP=1,FN=1`, compute precision, recall, F1; why is F1 best for imbalance (exam Q23)?
- **(T8)** In words: what do the ROC axes mean, and what does AUC=0.5 vs 1.0 indicate?
- ✍️ Write your first **[Decision Lens](../templates/decision-lens-template.md)** for any dataset.

---

## Module 3B — Supervised algorithms

| # | Topic | Open exactly this | ~Time |
|---|-------|-------------------|-------|
| 9 | Linear regression | [StatQuest](https://www.youtube.com/playlist?list=PLblh5JKOoLUICTaGLRoHQDuF_7q2GfuJF) — **"Linear Regression, Clearly Explained!!!"** · 📖 [ISLP Ch.3 (Linear Regression)](https://www.statlearning.com) | 27m |
| 10 | Logistic regression (classification) | [StatQuest](https://www.youtube.com/playlist?list=PLblh5JKOoLUICTaGLRoHQDuF_7q2GfuJF) — **"Logistic Regression"** series intro · 📖 [ISLP Ch.4 (Classification)](https://www.statlearning.com) | 20m |
| 11 | **Regularization** (Ridge/L2, Lasso/L1, elastic net) | [StatQuest](https://www.youtube.com/playlist?list=PLblh5JKOoLUICTaGLRoHQDuF_7q2GfuJF) — **"Regularization Part 1: Ridge"** + **"Part 2: Lasso"** · 🎨 [Visualize: Ridge vs Lasso](../illustrated/regularization.html) · 📖 [ISLP Ch.6](https://www.statlearning.com) | 35m |
| 12 | KNN | [StatQuest](https://www.youtube.com/playlist?list=PLblh5JKOoLUICTaGLRoHQDuF_7q2GfuJF) — **"K-nearest neighbors, Clearly Explained"** · 🎨 [Visualize: kNN boundary](../illustrated/knn.html) · 📖 [scikit-learn: Nearest Neighbors](https://scikit-learn.org/stable/modules/neighbors.html) | 6m |
| 13 | **Naive Bayes** (exam Q12, Q13, Q20) | [StatQuest](https://www.youtube.com/playlist?list=PLblh5JKOoLUICTaGLRoHQDuF_7q2GfuJF) — **"Naive Bayes, Clearly Explained!!!"** · 🎨 [Visualize: Bayes update](../illustrated/bayes-theorem.html) · 📖 [scikit-learn: Naive Bayes](https://scikit-learn.org/stable/modules/naive_bayes.html) | 15m |
| 14 | **SVM + the kernel trick** *(beyond exam)* | [StatQuest](https://www.youtube.com/playlist?list=PLblh5JKOoLUICTaGLRoHQDuF_7q2GfuJF) — **"Support Vector Machines Part 1"** (+ Parts 2–3) · 🎨 [Visualize: SVM margin & kernel](../illustrated/svm-margin.html) · 📖 [scikit-learn: SVM](https://scikit-learn.org/stable/modules/svm.html) | 40m |
| 15 | **Decision trees** (exam Q11) | [StatQuest](https://www.youtube.com/playlist?list=PLblh5JKOoLUICTaGLRoHQDuF_7q2GfuJF) — **"Decision Trees"** (classification) · 📖 [scikit-learn: Decision Trees](https://scikit-learn.org/stable/modules/tree.html) | 17m |
| 16 | Bagging & **Random Forests** | [StatQuest](https://www.youtube.com/playlist?list=PLblh5JKOoLUICTaGLRoHQDuF_7q2GfuJF) — **"Random Forests Part 1: Building, Using and Evaluating"** · 📖 [scikit-learn: Random Forests](https://scikit-learn.org/stable/modules/ensemble.html#forests-of-randomized-trees) | 10m |
| 17 | **Boosting** (AdaBoost, Gradient Boost, XGBoost) (exam Q21, Q30) | [StatQuest](https://www.youtube.com/playlist?list=PLblh5JKOoLUICTaGLRoHQDuF_7q2GfuJF) — **"AdaBoost"** + **"Gradient Boost Part 1"** + **"XGBoost Part 1"** · 📖 [scikit-learn: Gradient Boosting](https://scikit-learn.org/stable/modules/ensemble.html#gradient-boosting) | 50m |
| 18 | Stacking & voting ensembles | [scikit-learn UG](https://scikit-learn.org/stable/modules/ensemble.html) — **"Ensembles → Stacking"** | 20m |

**✅ Checkpoint 3B** — 🖥️/📊 — one per topic:
- **(T9)** Fit `LinearRegression` in scikit-learn; report R²; 🔨 connect to **[BYO-2](../challenges/byo-02-regression/README.md)**.
- **(T10)** Fit `LogisticRegression` on a 2-class set; plot the decision boundary.
- **(T11)** Compare Ridge vs Lasso coefficients on the same data; which zeros out features and why?
- **(T12)** Classify with KNN for k=1 and k=15; how does k affect bias/variance?
- **(T13)** Hand-compute a Naive Bayes posterior; state Bayes' theorem (exam Q13) and why max-discriminant=max-posterior (exam Q12).
- **(T14)** Train an SVM with linear vs RBF kernel; explain what the kernel trick buys you.
- **(T15)** Fit a decision tree; show it overfits at large depth (exam Q11 disadvantage); 🔨 connect to **[BYO-3](../challenges/byo-03-trees/README.md)**.
- **(T16)** Train a Random Forest; explain how bagging reduces variance vs one tree.
- **(T17)** Train AdaBoost/GradientBoosting/XGBoost; what do boosting algos commonly use as weak learners (exam Q30) and how do they differ from bagging (exam Q21)?
- **(T18)** Stack LogReg + RF + GBM with a meta-learner; does it beat the best single model?

---

## Module 3C — Unsupervised learning & dimensionality reduction

| # | Topic | Open exactly this | ~Time |
|---|-------|-------------------|-------|
| 19 | **K-means** (exam Q31) | [StatQuest](https://www.youtube.com/playlist?list=PLblh5JKOoLUICTaGLRoHQDuF_7q2GfuJF) — **"K-means clustering"** · 📖 [scikit-learn: K-means](https://scikit-learn.org/stable/modules/clustering.html#k-means) | 8m |
| 20 | Hierarchical clustering *(beyond)* | [StatQuest](https://www.youtube.com/playlist?list=PLblh5JKOoLUICTaGLRoHQDuF_7q2GfuJF) — **"Hierarchical Clustering"** · 📖 [scikit-learn: Hierarchical clustering](https://scikit-learn.org/stable/modules/clustering.html#hierarchical-clustering) | 11m |
| 21 | DBSCAN *(beyond)* | [StatQuest](https://www.youtube.com/playlist?list=PLblh5JKOoLUICTaGLRoHQDuF_7q2GfuJF) — **"Clustering with DBSCAN"** · 📖 [scikit-learn: DBSCAN](https://scikit-learn.org/stable/modules/clustering.html#dbscan) | 9m |
| 22 | GMM / EM *(beyond)* | [StatQuest](https://www.youtube.com/playlist?list=PLblh5JKOoLUICTaGLRoHQDuF_7q2GfuJF) — **"Gaussian Mixture Models"** · 📖 [scikit-learn: Gaussian Mixtures](https://scikit-learn.org/stable/modules/mixture.html) | 13m |
| 23 | **PCA** (exam Q18) | [StatQuest](https://www.youtube.com/playlist?list=PLblh5JKOoLUICTaGLRoHQDuF_7q2GfuJF) — **"PCA, Step-by-Step"** · 📖 [scikit-learn: PCA](https://scikit-learn.org/stable/modules/decomposition.html#pca) | 22m |
| 24 | t-SNE & UMAP *(beyond)* | [StatQuest](https://www.youtube.com/playlist?list=PLblh5JKOoLUICTaGLRoHQDuF_7q2GfuJF) — **"t-SNE, Clearly Explained"** · 📖 [Distill: How to Use t-SNE Effectively](https://distill.pub/2016/misread-tsne/) | 12m |
| 25 | Anomaly detection | [scikit-learn UG](https://scikit-learn.org/stable/modules/outlier_detection.html) — **"Novelty and Outlier Detection"** | 25m |

**✅ Checkpoint 3C** — 🖥️/📊 — one per topic:
- **(T19)** Run k-means; explain why it finds only a *local* optimum and is unsupervised (exam Q31); 🔨 **[BYO-4](../challenges/byo-04-kmeans-pca/README.md)**.
- **(T20)** Cluster the same data with hierarchical; read a dendrogram.
- **(T21)** Run DBSCAN; show it finds non-spherical clusters + noise that k-means can't.
- **(T22)** Fit a GMM; how does soft assignment differ from k-means' hard assignment?
- **(T23)** PCA to 2 components; report explained-variance ratio; why is PCA *feature extraction* not selection (exam Q18)?
- **(T24)** Visualize a high-dim dataset with t-SNE/UMAP; why is it for *viz*, not features?
- **(T25)** Build an anomaly detector; 🔨 connect to **[BYO-14 (intrusion)](../challenges/byo-14-intrusion/README.md)**.

---

## Module 3D — Feature engineering & practical ML

| # | Topic | Open exactly this | ~Time |
|---|-------|-------------------|-------|
| 26 | **Scaling/normalization & preprocessing** (exam Q24) | [scikit-learn UG](https://scikit-learn.org/stable/modules/preprocessing.html) — **"Preprocessing data"** | 30m |
| 27 | Encoding categoricals; feature engineering | [Kaggle Learn — Feature Engineering](https://www.kaggle.com/learn/feature-engineering) (full course) | 3h |
| 28 | **Feature selection** (forward/backward) (exam Q18) | [scikit-learn UG](https://scikit-learn.org/stable/modules/feature_selection.html) — **"Feature selection"** | 25m |
| 29 | Imbalanced learning (SMOTE, class weights) *(beyond)* | [imbalanced-learn docs](https://imbalanced-learn.org/stable/user_guide.html) — **"Over-sampling → SMOTE"** | 25m |
| 30 | **Pipelines** & the scikit-learn API | [scikit-learn UG](https://scikit-learn.org/stable/modules/compose.html) — **"Pipelines and composite estimators"** | 25m |
| 31 | **Hyperparameter tuning** (grid/random search) | [scikit-learn UG](https://scikit-learn.org/stable/modules/grid_search.html) — **"Tuning the hyper-parameters"** | 25m |
| 32 | **Explainability** (SHAP, LIME) — Responsible-AI | [SHAP docs](https://shap.readthedocs.io/en/latest/) — **"An introduction to explainable AI with Shapley values"** + [Molnar — Interpretable ML book](https://christophm.github.io/interpretable-ml-book/) | 45m |
| 33 | Recommender systems *(beyond)* | [Google — Recommendation Systems Crash Course](https://developers.google.com/machine-learning/recommendation) | 1h |
| 34 | **Time-series forecasting** (ARIMA/ETS/Prophet) *(beyond; finance)* | [*Forecasting: Principles & Practice* (free)](https://otexts.com/fpp3/) — **Ch.8–9 (ETS, ARIMA)** | 2h |

**✅ Checkpoint 3D** — 🖥️/📊 — one per topic:
- **(T26)** Standardize features, then PCA, then train — in the right order (exam Q24); why does order matter?
- **(T27)** One-hot encode a categorical; engineer one new feature that helps a model.
- **(T28)** Use forward/backward selection; contrast with PCA (selection vs extraction, exam Q18).
- **(T29)** On an imbalanced set, apply SMOTE/class-weights; show recall on the minority class improves.
- **(T30)** Wrap preprocessing + model in a `Pipeline`; explain why this prevents leakage.
- **(T31)** Tune a model with `GridSearchCV`; report the best params and CV score.
- **(T32)** Explain a prediction with SHAP; name one fairness/interpretability concern (Responsible-AI thread).
- **(T33)** Build a tiny collaborative-filtering recommender; evaluate with a ranking metric.
- **(T34)** Forecast a stock/series with ETS or Prophet; 🔨 connect to **[BYO-15 (backtester)](../challenges/byo-15-backtester/README.md)**.

---

## 🏁 Phase 3 capstone — end-to-end ML app  (📊 Kaggle or 🖥️ Local)
Pick churn or fraud: EDA → feature engineering → cross-validated model comparison (LogReg/RF/GBM) →
tune → **SHAP** explanation → deploy as a **Streamlit** app. Enter one **Kaggle competition**. Write a
**Decision Lens** for it. *(This is a flagship resume project.)*

**Ready for Phase 4 when** you can frame a problem, pick the right model + metric, validate honestly,
explain predictions, and you've shipped one end-to-end ML app.
