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
    ["0-python/python-java-mindset.html", "Java → Python mindset"],
    ["0-python/python-data-model.html", "Names & mutability"],
    ["0-python/python-truthiness.html", "Truthiness & bool"],
    ["0-python/python-strings.html", "Strings & slicing"],
    ["0-python/python-collections.html", "list / tuple / set"],
    ["0-python/python-dicts.html", "dict & hashing"],
    ["0-python/python-comprehensions.html", "Comprehensions"],
    ["0-python/python-zip-enumerate.html", "zip & enumerate"],
    ["0-python/python-args-kwargs.html", "*args & **kwargs"],
    ["0-python/python-generators.html", "Generators & yield"],
    ["0-python/python-oop.html", "Classes & namespaces"],
    ["0-python/python-inheritance.html", "Inheritance & MRO"],
    ["0-python/python-dunder.html", "Dunder methods"],
    ["0-python/python-exceptions.html", "Exceptions"],
    ["0-python/python-context-managers.html", "with / context managers"],
    ["1-scientific-stack/numpy-vectorization.html", "Vectorization & ufuncs"],
    ["1-scientific-stack/numpy-broadcasting.html", "Broadcasting"],
    ["1-scientific-stack/numpy-axis.html", "Aggregations & axis"],
    ["1-scientific-stack/numpy-indexing.html", "Indexing: slices/masks/fancy"],
    ["1-scientific-stack/pandas-dataframe.html", "Series, DataFrame, loc/iloc"],
    ["1-scientific-stack/pandas-groupby.html", "GroupBy"],
    ["1-scientific-stack/pandas-merge.html", "merge & join"],
    ["2-math/matrix-transformation.html", "Matrices as transformations"],
    ["2-math/dot-product.html", "Dot product & projection"],
    ["2-math/bayes-theorem.html", "Bayes' theorem"],
    ["2-math/optimizer-comparison.html", "Optimizer comparison"],
    ["3-classic-ml/confusion-matrix.html", "Confusion matrix & metrics"],
    ["3-classic-ml/regularization.html", "Regularization (Ridge/Lasso)"],
    ["3-classic-ml/knn.html", "k-Nearest Neighbors"],
    ["3-classic-ml/svm-margin.html", "SVM & the kernel trick"],
    ["3-classic-ml/kmeans-steps.html", "k-means steps"],
    ["4-deep-learning/activations.html", "Activation functions"],
    ["4-deep-learning/loss-functions.html", "Loss functions"],
    ["4-deep-learning/backprop.html", "Backpropagation"],
    ["4-deep-learning/lstm-gru.html", "LSTM / GRU gates"],
    ["5-nlp-transformers/tfidf.html", "TF-IDF"],
    ["5-nlp-transformers/self-attention.html", "Self-attention"],
    ["5-nlp-transformers/positional-encoding.html", "Positional encoding"],
    ["6-llms-rag-agents/rag-pipeline.html", "RAG pipeline"],
    ["6-llms-rag-agents/react-agent.html", "ReAct agent loop"],
    ["6-llms-rag-agents/vector-search.html", "Vector search"],
    ["6-llms-rag-agents/embeddings.html", "Embeddings & cosine"],
    ["6b-llm-indepth/tokenization-bpe.html", "BPE tokenization"],
    ["6b-llm-indepth/llm-decoding.html", "LLM decoding"],
    ["6b-llm-indepth/moe.html", "Mixture of Experts"],
    ["6b-llm-indepth/lora-quantization.html", "LoRA & quantization"],
    ["6b-llm-indepth/prompt-injection.html", "Prompt injection"],
    ["7-mlops/mlops-lifecycle.html", "MLOps lifecycle & drift"],
    ["8-agentic/agent-patterns.html", "Agent patterns"],
  ];

  function navCard(item, kind) {
    if (!item) return el("span", { class: "pn empty" });
    return el("a", { class: "pn " + kind, href: "../" + item[0] }, [
      el("span", { class: "dir", text: kind === "prev" ? "← Previous" : "Next →" }),
      el("span", { class: "t", text: item[1] }),
    ]);
  }

  function injectNav() {
    const wrap = document.querySelector(".wrap");
    if (!wrap) return;
    const path = location.pathname.split("/").slice(-2).join("/").toLowerCase();
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
      if (prev) mini.appendChild(el("a", { href: "../" + prev[0], title: "Previous: " + prev[1], text: "‹ Prev" }));
      mini.appendChild(el("span", { class: "of", text: (i + 1) + " / " + SEQ.length }));
      if (next) mini.appendChild(el("a", { href: "../" + next[0], title: "Next: " + next[1], text: "Next ›" }));
      const sp = tb.querySelector(".spacer");
      if (sp && sp.nextSibling) tb.insertBefore(mini, sp.nextSibling); else tb.appendChild(mini);
    }
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", injectNav);
  else injectNav();

  global.Ill = { clamp, lerp, dot, norm, cosine, softmax, rng, randn, $, $$, el, slider, diverge, SEQ };
})(window);
