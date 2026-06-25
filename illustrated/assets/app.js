/* Illustrated explainers — shared helpers. Vanilla JS, no external deps. */
(function (global) {
  "use strict";

  // ---- math ----
  const clamp = (x, lo, hi) => Math.max(lo, Math.min(hi, x));
  const lerp = (a, b, t) => a + (b - a) * t;
  const dot = (a, b) => a.reduce((s, v, i) => s + v * b[i], 0);
  const norm = (a) => Math.sqrt(dot(a, a));
  function cosine(a, b) {
    const na = norm(a), nb = norm(b);
    return na === 0 || nb === 0 ? 0 : dot(a, b) / (na * nb);
  }
  function softmax(xs, temp) {
    const t = temp == null ? 1 : Math.max(1e-6, temp);
    const m = Math.max(...xs);
    const ex = xs.map((x) => Math.exp((x - m) / t));
    const s = ex.reduce((a, b) => a + b, 0);
    return ex.map((e) => e / s);
  }
  // deterministic RNG (mulberry32)
  function rng(seed) {
    let a = seed >>> 0;
    return function () {
      a |= 0; a = (a + 0x6D2B79F5) | 0;
      let t = Math.imul(a ^ (a >>> 15), 1 | a);
      t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
      return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
    };
  }
  function randn(r) { // Box-Muller from a uniform rng()
    let u = 0, v = 0;
    while (u === 0) u = r();
    while (v === 0) v = r();
    return Math.sqrt(-2 * Math.log(u)) * Math.cos(2 * Math.PI * v);
  }

  // ---- DOM ----
  const $ = (sel, root) => (root || document).querySelector(sel);
  const $$ = (sel, root) => Array.from((root || document).querySelectorAll(sel));
  function el(tag, attrs, kids) {
    const ns = tag === "svg" || ["g","rect","circle","line","path","text","polyline","polygon","defs","marker","tspan"].includes(tag);
    const node = ns ? document.createElementNS("http://www.w3.org/2000/svg", tag) : document.createElement(tag);
    if (attrs) for (const k in attrs) {
      if (k === "style" && typeof attrs[k] === "object") Object.assign(node.style, attrs[k]);
      else if (k === "text") node.textContent = attrs[k];
      else if (k === "html") node.innerHTML = attrs[k];
      else if (k in node && !ns) node[k] = attrs[k];
      else node.setAttribute(k, attrs[k]);
    }
    if (kids) (Array.isArray(kids) ? kids : [kids]).forEach((c) =>
      node.appendChild(typeof c === "string" ? document.createTextNode(c) : c));
    return node;
  }
  // wire a range input to a callback + live value label
  function slider(input, fmt, onInput) {
    const lab = input.closest(".ctrl") && input.closest(".ctrl").querySelector(".val");
    const update = () => {
      const v = parseFloat(input.value);
      if (lab) lab.textContent = fmt ? fmt(v) : v;
      if (onInput) onInput(v);
    };
    input.addEventListener("input", update);
    update();
    return update;
  }
  // color scale blue->white->green for a value in [-1,1]
  function diverge(t) {
    t = clamp(t, -1, 1);
    if (t >= 0) return `rgb(${Math.round(255 - t*245)},${Math.round(255 - t*125)},${Math.round(255 - t*211)})`;
    const a = -t;
    return `rgb(${Math.round(255 - a*235)},${Math.round(255 - a*169)},${Math.round(255 - a*79)})`;
  }

  // ---- sequential prev/next navigation across our explainer pages ----
  // Single source of truth for "next topic" order (roadmap order). [href, short label].
  const SEQ = [
    ["python-java-mindset.html", "Java → Python mindset"],
    ["python-data-model.html", "Names & mutability"],
    ["python-truthiness.html", "Truthiness & bool"],
    ["python-strings.html", "Strings & slicing"],
    ["python-collections.html", "list / tuple / set"],
    ["python-dicts.html", "dict & hashing"],
    ["python-comprehensions.html", "Comprehensions"],
    ["python-zip-enumerate.html", "zip & enumerate"],
    ["python-args-kwargs.html", "*args & **kwargs"],
    ["python-generators.html", "Generators & yield"],
    ["python-oop.html", "Classes & namespaces"],
    ["python-inheritance.html", "Inheritance & MRO"],
    ["python-dunder.html", "Dunder methods"],
    ["python-exceptions.html", "Exceptions"],
    ["python-context-managers.html", "with / context managers"],
    ["numpy-vectorization.html", "Vectorization & ufuncs"],
    ["numpy-broadcasting.html", "Broadcasting"],
    ["numpy-axis.html", "Aggregations & axis"],
    ["numpy-indexing.html", "Indexing: slices/masks/fancy"],
    ["pandas-dataframe.html", "Series, DataFrame, loc/iloc"],
    ["pandas-groupby.html", "GroupBy"],
    ["pandas-merge.html", "merge & join"],
    ["matrix-transformation.html", "Matrices as transformations"],
    ["dot-product.html", "Dot product & projection"],
    ["bayes-theorem.html", "Bayes' theorem"],
    ["optimizer-comparison.html", "Optimizer comparison"],
    ["confusion-matrix.html", "Confusion matrix & metrics"],
    ["regularization.html", "Regularization (Ridge/Lasso)"],
    ["knn.html", "k-Nearest Neighbors"],
    ["svm-margin.html", "SVM & the kernel trick"],
    ["kmeans-steps.html", "k-means steps"],
    ["activations.html", "Activation functions"],
    ["loss-functions.html", "Loss functions"],
    ["backprop.html", "Backpropagation"],
    ["lstm-gru.html", "LSTM / GRU gates"],
    ["tfidf.html", "TF-IDF"],
    ["self-attention.html", "Self-attention"],
    ["positional-encoding.html", "Positional encoding"],
    ["rag-pipeline.html", "RAG pipeline"],
    ["react-agent.html", "ReAct agent loop"],
    ["vector-search.html", "Vector search"],
    ["embeddings.html", "Embeddings & cosine"],
    ["tokenization-bpe.html", "BPE tokenization"],
    ["llm-decoding.html", "LLM decoding"],
    ["moe.html", "Mixture of Experts"],
    ["lora-quantization.html", "LoRA & quantization"],
    ["prompt-injection.html", "Prompt injection"],
    ["mlops-lifecycle.html", "MLOps lifecycle & drift"],
    ["agent-patterns.html", "Agent patterns"],
  ];

  function navCard(item, kind) {
    if (!item) return el("span", { class: "pn empty" });
    return el("a", { class: "pn " + kind, href: item[0] }, [
      el("span", { class: "dir", text: kind === "prev" ? "← Previous" : "Next →" }),
      el("span", { class: "t", text: item[1] }),
    ]);
  }

  function injectNav() {
    const wrap = document.querySelector(".wrap");
    if (!wrap) return;
    const path = (location.pathname.split("/").pop() || "").toLowerCase();
    const i = SEQ.findIndex((s) => s[0] === path);
    if (i === -1) return; // index/catalog or an unknown page → no sequential nav
    const prev = i > 0 ? SEQ[i - 1] : null;
    const next = i < SEQ.length - 1 ? SEQ[i + 1] : null;

    // bottom prev/next bar (before the footer)
    const bar = el("div", { class: "prevnext" }, [navCard(prev, "prev"), navCard(next, "next")]);
    const footer = wrap.querySelector(".footer");
    if (footer) wrap.insertBefore(bar, footer); else wrap.appendChild(bar);

    // compact prev/next in the sticky topbar (so it's always reachable)
    const tb = document.querySelector(".topbar");
    if (tb) {
      const mini = el("span", { class: "tbnav" });
      if (prev) mini.appendChild(el("a", { href: prev[0], title: "Previous: " + prev[1], text: "‹ Prev" }));
      mini.appendChild(el("span", { class: "of", text: (i + 1) + " / " + SEQ.length }));
      if (next) mini.appendChild(el("a", { href: next[0], title: "Next: " + next[1], text: "Next ›" }));
      const sp = tb.querySelector(".spacer");
      if (sp && sp.nextSibling) tb.insertBefore(mini, sp.nextSibling); else tb.appendChild(mini);
    }
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", injectNav);
  else injectNav();

  global.Ill = { clamp, lerp, dot, norm, cosine, softmax, rng, randn, $, $$, el, slider, diverge, SEQ };
})(window);
