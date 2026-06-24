# Phase 1 — Scientific Python Stack + Plotting (≈3–4 weeks)

**Goal:** fluency in **NumPy**, **Pandas**, **Matplotlib/Seaborn** — the tools every later phase sits on.

**Environment:** mostly **🖥️ Local** in Jupyter; switch to **📊 Kaggle** for the EDA capstone (datasets
are one click away). Each checkpoint is tagged.

**🔄 Freshness:** libraries move — use **current NumPy 2.x / pandas 2.x / Matplotlib** (links point to
"stable" docs). Core APIs are steady, but if a method is deprecated, the current docs will tell you.

**Primary resources** (open the linked playlist/site, then the **bold** item):
- [Corey Schafer — *Pandas* playlist](https://www.youtube.com/playlist?list=PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS) · [Corey Schafer — *Matplotlib* playlist](https://www.youtube.com/playlist?list=PL-osiE80TeTvipOqomVEeZ1HRrcEvtZB_)
- [*Python Data Science Handbook* (free, online)](https://jakevdp.github.io/PythonDataScienceHandbook/) · [NumPy docs (stable)](https://numpy.org/doc/stable/) · [pandas docs (stable)](https://pandas.pydata.org/docs/)
- [Kaggle Learn](https://www.kaggle.com/learn) (hands-on, free certs) · 🆕 [Vizuara](https://www.youtube.com/@vizuara) (good "NumPy/Pandas from scratch" explainers)
- 🎨 **[Illustrated explainers](../illustrated/index.html)** (interactive, offline) for this phase: [Vectorization & ufuncs](../illustrated/numpy-vectorization.html), [Broadcasting](../illustrated/numpy-broadcasting.html), [Aggregations & axis](../illustrated/numpy-axis.html) (Q4), [Indexing: slices/masks/fancy](../illustrated/numpy-indexing.html), [Series/DataFrame & loc/iloc](../illustrated/pandas-dataframe.html) (Q2), [GroupBy](../illustrated/pandas-groupby.html), [merge & join](../illustrated/pandas-merge.html). Pair with the visual [Visual NumPy (Alammar)](https://jalammar.github.io/visual-numpy/).

---

## Module 1A — NumPy

| # | Topic | Open exactly this | ~Time |
|---|-------|-------------------|-------|
| 1 | Arrays, dtypes, creation | [PDS Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/) — **Ch.2 "Understanding Data Types in NumPy"** + **"The Basics of NumPy Arrays"** · 🔗 [Visual NumPy (Alammar)](https://jalammar.github.io/visual-numpy/) | 40m |
| 2 | Indexing, slicing, boolean & fancy indexing | [PDS Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/) — **"Comparisons, Masks, and Boolean Logic"** + **"Fancy Indexing"** · 🎨 [Visualize](../illustrated/numpy-indexing.html) | 40m |
| 3 | Vectorized math (ufuncs) — no loops | [PDS Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/) — **"Computation on Arrays: Universal Functions"** · 🎨 [Visualize: vectorization](../illustrated/numpy-vectorization.html) · 🔗 [Visual NumPy](https://jalammar.github.io/visual-numpy/) | 25m |
| 4 | **Aggregations & `axis`** (exam Q4) | [PDS Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/) — **"Aggregations: Min, Max, and Everything in Between"** · 🎨 [Visualize](../illustrated/numpy-axis.html) | 25m |
| 5 | **Broadcasting** (critical for ML) | [PDS Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/) — **"Computation on Arrays: Broadcasting"** · 🎨 [Visualize](../illustrated/numpy-broadcasting.html) · 🔗 [Visual NumPy](https://jalammar.github.io/visual-numpy/) | 30m |
| 6 | Linear algebra ops: `@`, `dot`, `reshape`, `linalg` | [NumPy docs (stable)](https://numpy.org/doc/stable/reference/routines.linalg.html) — **"Linear algebra (numpy.linalg)"** | 30m |

**✅ Checkpoint 1A** — 🖥️ Local (notebook), no Python loops — one per topic:
- **(T1)** Create a `(3,4)` zeros array, an `arange` array, and a random-float array; print `.shape`/`.dtype`.
- **(T2)** From `arange(10)` select evens with a **boolean mask** and `[1,3,5]` with **fancy indexing**.
- **(T3)** Apply `np.exp`/`np.sqrt` to an array (a **ufunc**); time it vs a list comprehension.
- **(T4)** Recreate exam Q4: `np.sum([[1,2],[3,4]], axis=1)` and `axis=0`; explain each.
- **(T5)** Build a 5×5 multiplication table by **broadcasting** a column × a row.
- **(T6)** Multiply `(2,3)@(3,2)`; take `np.linalg.inv` of a square matrix and `np.linalg.norm` of a vector.
- *(integrative)* Standardize a `(100,3)` matrix to zero-mean/unit-var **per column** using `axis`.

---

## Module 1B — Pandas

| # | Topic | Open exactly this | ~Time |
|---|-------|-------------------|-------|
| 7 | **Series & DataFrame** (exam Q2), loading CSVs | [Corey Schafer Pandas](https://www.youtube.com/playlist?list=PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS) — **Part 1** + **Part 2** · 🎨 [Visualize](../illustrated/pandas-dataframe.html) · 📖 [PDS Handbook: Pandas Objects](https://jakevdp.github.io/PythonDataScienceHandbook/03.01-introducing-pandas-objects.html) | 60m |
| 8 | `loc` vs `iloc`, indexes | [Corey Schafer Pandas](https://www.youtube.com/playlist?list=PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS) — **Part 2** + **Part 3 (Indexes)** · 🎨 [Visualize: loc/iloc](../illustrated/pandas-dataframe.html) · 📖 [PDS Handbook: Data Indexing & Selection](https://jakevdp.github.io/PythonDataScienceHandbook/03.02-data-indexing-and-selection.html) | 45m |
| 9 | Filtering with conditionals | [Corey Schafer Pandas](https://www.youtube.com/playlist?list=PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS) — **Part 4 (Filtering)** · 🎨 [Visualize: boolean masks](../illustrated/numpy-indexing.html) · 📖 [pandas docs: Boolean indexing](https://pandas.pydata.org/docs/user_guide/indexing.html#boolean-indexing) | 25m |
| 10 | Add/update/remove columns | [Corey Schafer Pandas](https://www.youtube.com/playlist?list=PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS) — **Part 5 & 6** · 📖 [PDS Handbook: Operations in Pandas](https://jakevdp.github.io/PythonDataScienceHandbook/03.03-operations-in-pandas.html) | 40m |
| 11 | **GroupBy + aggregation** | [Corey Schafer Pandas](https://www.youtube.com/playlist?list=PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS) — **Part 8 (Grouping & Aggregating)** · 🎨 [Visualize](../illustrated/pandas-groupby.html) · 📖 [PDS Handbook: Aggregation & Grouping](https://jakevdp.github.io/PythonDataScienceHandbook/03.08-aggregation-and-grouping.html) | 35m |
| 12 | Cleaning: dtypes & **missing values** | [Corey Schafer Pandas](https://www.youtube.com/playlist?list=PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS) — **Part 9 (Cleaning Data)** · 📖 [PDS Handbook: Handling Missing Data](https://jakevdp.github.io/PythonDataScienceHandbook/03.04-missing-values.html) | 30m |
| 13 | Merge / join / concat | [Kaggle Learn — Pandas](https://www.kaggle.com/learn/pandas) — **"Combining"** lesson · 🎨 [Visualize: joins](../illustrated/pandas-merge.html) | 40m |
| 14 | Dates & time series (for finance) | [Corey Schafer Pandas](https://www.youtube.com/playlist?list=PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS) — **Part 10 (Dates & Time Series)** · 📖 [pandas docs: Time series](https://pandas.pydata.org/docs/user_guide/timeseries.html) | 30m |

**✅ Checkpoint 1B** — 🖥️ Local or 📊 Kaggle — finishes the free [Kaggle Pandas](https://www.kaggle.com/learn/pandas) cert — one per topic:
- **(T7)** Load a CSV; show `.head()`, `.info()`, `.describe()`; explain Series vs DataFrame (exam Q2).
- **(T8)** Select 1 column (Series) & 2 columns (DataFrame); grab rows with `loc` (label) and `iloc` (position); set an index.
- **(T9)** Filter where A > x **and** B == "y" (masks + `&` + parentheses).
- **(T10)** Add a derived column, update values on a condition, drop a column.
- **(T11)** `groupby` a category and `.agg` mean/count/sum of a numeric column.
- **(T12)** Find missing with `.isna().sum()`; fix with `fillna`/`dropna`; correct a dtype with `astype`.
- **(T13)** `merge` two DataFrames (inner vs left) and `concat` two together.
- **(T14)** Parse dates with `pd.to_datetime`, set as index, resample by month.

---

## Module 1C — Visualization (Matplotlib + Seaborn)

| # | Topic | Open exactly this | ~Time |
|---|-------|-------------------|-------|
| 15 | Matplotlib anatomy: figure/axes, line plots | [Corey Schafer Matplotlib](https://www.youtube.com/playlist?list=PL-osiE80TeTvipOqomVEeZ1HRrcEvtZB_) — **Part 1 (Creating & Customizing Plots)** · 📖 [PDS Handbook: Simple Line Plots](https://jakevdp.github.io/PythonDataScienceHandbook/04.01-simple-line-plots.html) | 35m |
| 16 | Bar charts from CSV data | [Corey Schafer Matplotlib](https://www.youtube.com/playlist?list=PL-osiE80TeTvipOqomVEeZ1HRrcEvtZB_) — **Part 2 (Bar Charts)** · 📖 [Matplotlib: Pyplot tutorial](https://matplotlib.org/stable/tutorials/pyplot.html) | 25m |
| 17 | Histograms (distributions) | [Corey Schafer Matplotlib](https://www.youtube.com/playlist?list=PL-osiE80TeTvipOqomVEeZ1HRrcEvtZB_) — **Part 6 (Histograms)** · 📖 [PDS Handbook: Histograms & Binnings](https://jakevdp.github.io/PythonDataScienceHandbook/04.05-histograms-and-binnings.html) | 20m |
| 18 | Scatter plots (relationships) | [Corey Schafer Matplotlib](https://www.youtube.com/playlist?list=PL-osiE80TeTvipOqomVEeZ1HRrcEvtZB_) — **Part 7 (Scatter Plots)** · 📖 [PDS Handbook: Simple Scatter Plots](https://jakevdp.github.io/PythonDataScienceHandbook/04.02-simple-scatter-plots.html) | 20m |
| 19 | Subplots (multi-panel) | [Corey Schafer Matplotlib](https://www.youtube.com/playlist?list=PL-osiE80TeTvipOqomVEeZ1HRrcEvtZB_) — **Part 10 (Subplots)** · 📖 [PDS Handbook: Multiple Subplots](https://jakevdp.github.io/PythonDataScienceHandbook/04.08-multiple-subplots.html) | 25m |
| 20 | Seaborn: distributions, `heatmap`, `pairplot` | [Kaggle Learn — Data Visualization](https://www.kaggle.com/learn/data-visualization) (full, free) | 2h |

**✅ Checkpoint 1C** — 🖥️ Local — one per topic:
- **(T15)** Plot two lines on one axes with title/labels/legend; save to PNG.
- **(T16)** Bar chart of a categorical count from a DataFrame.
- **(T17)** Histogram of a numeric column; describe its shape (skew/spread).
- **(T18)** Scatter of two columns; say whether they look correlated.
- **(T19)** Put line + bar + histogram in one figure via `plt.subplots(1,3)`.
- **(T20)** Seaborn `histplot`, correlation `heatmap`, and `pairplot`; read off the strongest correlated pair.

---

## Module 1D — Your workbench (free compute)

| # | Topic | Open exactly this | ~Time |
|---|-------|-------------------|-------|
| 21 | Jupyter notebooks (cells, markdown) | [Corey Schafer — "Jupyter Notebook Tutorial: Introduction, Setup, and Walkthrough"](https://www.youtube.com/@coreyms/search?query=jupyter%20notebook) · 📖 [Real Python: Jupyter Notebook Intro](https://realpython.com/jupyter-notebook-introduction/) | 30m |
| 22 | Google Colab (free GPU later) | [colab.research.google.com](https://colab.research.google.com) — open "Welcome" notebook; *Runtime ▸ change to GPU* | 15m |
| 23 | Kaggle Notebooks + datasets | [kaggle.com/code](https://www.kaggle.com/code) — New Notebook ▸ Add Data | 15m |

**✅ Checkpoint 1D** — one per topic:
- **(T21)** 🖥️ In Jupyter: run a code cell and a markdown cell; `Shift+Enter`; restart kernel & run-all.
- **(T22)** ☁️ Open the same notebook in **Colab**, switch runtime to **GPU**, confirm with `!nvidia-smi`.
- **(T23)** 📊 Open a **Kaggle** dataset in a Notebook and load its CSV into a DataFrame.

---

## 🏁 Phase 1 capstone — Real-world EDA notebook  (📊 Kaggle or 🖥️ Local)
Pick a messy public dataset → clean (dtypes, missing) → engineer a couple of columns → **8–10 labeled
visualizations** → a short markdown narrative. Push the `.ipynb` to your GitHub repo.

**Ready for Phase 2 when** you can take a raw CSV to a clean, well-visualized analysis end-to-end, and
you know NumPy `axis` + broadcasting cold (every model uses them).
