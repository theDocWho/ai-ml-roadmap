# Phase 1 — Scientific Python Stack + Plotting (≈3–4 weeks)

**Goal:** fluency in **NumPy**, **Pandas**, and **Matplotlib/Seaborn** — the tools every later phase
sits on. You explicitly wanted charts/graphs and package usage; this is where you get it.

**Primary free resources:**
- Corey Schafer — *Pandas* playlist — https://www.youtube.com/playlist?list=PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS
- Corey Schafer — *Matplotlib* playlist — https://www.youtube.com/playlist?list=PL-osiE80TeTvipOqomVEeZ1HRrcEvtZB_
- *Python Data Science Handbook* (free) — https://jakevdp.github.io/PythonDataScienceHandbook/
- Kaggle Learn (hands-on, free) — https://www.kaggle.com/learn

---

## Module 1A — NumPy

| # | Topic | Watch / read exactly this | ~Time |
|---|-------|---------------------------|-------|
| 1 | Why arrays beat lists; creating arrays, dtypes | PDS Handbook **Ch.2 "Understanding Data Types in NumPy"** + "The Basics of NumPy Arrays" | 40m |
| 2 | Indexing, slicing, boolean masks, fancy indexing | PDS Handbook **Ch.2 "Comparisons, Masks, and Boolean Logic"** + "Fancy Indexing" | 40m |
| 3 | Vectorized math (ufuncs) — no Python loops | PDS Handbook **Ch.2 "Computation on Arrays: Universal Functions"** | 25m |
| 4 | **Aggregations & `axis`** (your exam Q4) | PDS Handbook **Ch.2 "Aggregations: Min, Max, and Everything in Between"** | 25m |
| 5 | **Broadcasting** (critical for ML) | PDS Handbook **Ch.2 "Computation on Arrays: Broadcasting"** | 30m |
| 6 | Linear algebra ops: `@`, `dot`, `reshape`, `linalg` | Kaggle Learn isn't enough here — read NumPy docs "Linear algebra (numpy.linalg)" quickstart | 30m |

**✅ Checkpoint 1A** (in a notebook, no loops allowed):
- Recreate your exam Q4: `np.sum([[1,2],[3,4]], axis=1)` and `axis=0`; explain each result.
- Build a 5×5 multiplication table with broadcasting (`np.arange(1,6)` row × column).
- Standardize a random `(100, 3)` matrix to zero-mean/unit-variance **per column** using `axis`.

---

## Module 1B — Pandas

| # | Topic | Watch / read exactly this | ~Time |
|---|-------|---------------------------|-------|
| 7 | **Series & DataFrame** (your exam Q2), loading CSVs | Corey Schafer — Pandas **Part 1 (Getting Started)** + **Part 2 (DataFrame & Series Basics)** | 60m |
| 8 | Selecting rows/cols: `loc` vs `iloc`, indexes | Corey Schafer — Pandas **Part 2** + **Part 3 (Indexes)** | 45m |
| 9 | Filtering with conditionals | Corey Schafer — Pandas **Part 4 (Filtering)** | 25m |
| 10 | Adding/updating/removing columns | Corey Schafer — Pandas **Part 5 & 6** | 40m |
| 11 | **GroupBy + aggregation** (the analysis workhorse) | Corey Schafer — Pandas **Part 8 (Grouping and Aggregating)** | 35m |
| 12 | Cleaning: dtypes & **missing values** | Corey Schafer — Pandas **Part 9 (Cleaning Data)** | 30m |
| 13 | Merge / join / concat | Kaggle Learn — **Pandas** course, "Combining" + PDS Handbook Ch.3 "Combining Datasets: Merge and Join" | 40m |
| 14 | Dates & time series (you'll need for finance) | Corey Schafer — Pandas **Part 10 (Dates and Time Series)** | 30m |

**✅ Checkpoint 1B** — also finishes the **Kaggle "Pandas"** course (free certificate):
- Load a real CSV; show `.head()`, `.info()`, `.describe()`.
- `groupby` one categorical column and compute mean of a numeric column.
- Filter rows on two conditions combined with `&`; handle missing values with `fillna`/`dropna`.
- State the difference between `loc` and `iloc` in one sentence.

---

## Module 1C — Visualization (Matplotlib + Seaborn)

| # | Topic | Watch / read exactly this | ~Time |
|---|-------|---------------------------|-------|
| 15 | Matplotlib anatomy: figure/axes, line plots | Corey Schafer — Matplotlib **Part 1 (Creating & Customizing Plots)** | 35m |
| 16 | Bar charts from real CSV data | Corey Schafer — Matplotlib **Part 2 (Bar Charts)** | 25m |
| 17 | Histograms (distributions) | Corey Schafer — Matplotlib **Part 6 (Histograms)** | 20m |
| 18 | Scatter plots (relationships) | Corey Schafer — Matplotlib **Part 7 (Scatter Plots)** | 20m |
| 19 | Subplots (multi-panel figures) | Corey Schafer — Matplotlib **Part 10 (Subplots)** | 25m |
| 20 | Seaborn: distributions, `heatmap` (correlations), `pairplot` | Kaggle Learn — **Data Visualization** course (full, free) | 2h |

**✅ Checkpoint 1C:**
- Plot a line chart with title, axis labels, and a legend.
- From a DataFrame, make a histogram of one column and a scatter of two columns.
- Make a Seaborn correlation `heatmap` of a numeric DataFrame and read off the strongest pair.

---

## Module 1D — Your workbench (free compute)

| # | Topic | Watch / read exactly this | ~Time |
|---|-------|---------------------------|-------|
| 21 | Jupyter notebooks (cells, markdown) | Corey Schafer — "Jupyter Notebook Tutorial: Introduction, Setup, and Walkthrough" | 30m |
| 22 | Google Colab (free GPU later) | colab.research.google.com — "Welcome" notebook (skim) | 15m |
| 23 | Kaggle Notebooks + datasets | kaggle.com/learn — **Intro to Programming / Python** if rusty; else just open a dataset | 15m |

---

## 🏁 Phase 1 capstone exercise — Real-world EDA notebook
The resume piece from the roadmap:
- Pick a messy public dataset (Kaggle, or scrape one). Load → clean (dtypes, missing) → engineer a
  couple of columns → **8–10 well-labeled visualizations** → write a short markdown narrative of what
  you found. Push the `.ipynb` to your GitHub repo.

**You're ready for Phase 2 when** you can take a raw CSV to a clean, well-visualized analysis
end-to-end, and you understand NumPy `axis` + broadcasting cold (you'll use them in every model).
