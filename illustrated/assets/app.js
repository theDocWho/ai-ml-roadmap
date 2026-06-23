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

  global.Ill = { clamp, lerp, dot, norm, cosine, softmax, rng, randn, $, $$, el, slider, diverge };
})(window);
