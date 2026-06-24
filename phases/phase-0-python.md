# Phase 0 — Python for a Java Developer (≈2–3 weeks)

**Goal:** become fluent in *idiomatic* Python. You already know programming and DSA from Java, so this
is about Python's syntax, data model, and idioms — not "what is a loop." Skip what you know; spend time
on the **Pythonic** rows and OOP differences.

**🖥️ Environment:** do **all** of Phase 0 **locally** (see [setup in the index](README.md#working-environments--where-to-do-the-exercises-set-this-up-once)).
You want real files, a `git` repo, and `pytest` — not a notebook yet.

**🔄 Freshness:** Python evolves — always use the **latest stable Python (3.12+)** and the official
docs (the links below auto-point to current). Concepts are stable, but use modern syntax (f-strings,
`match`, type hints, `dataclasses`).

**Primary resources** (open the linked playlist/site, then the **bold** item):
- [Corey Schafer — *Python Beginners* playlist](https://www.youtube.com/playlist?list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7) · [Corey Schafer — *Python OOP* playlist](https://www.youtube.com/playlist?list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc)
- [Real Python](https://realpython.com) (free articles) · [Official Python Tutorial (3.12+)](https://docs.python.org/3/tutorial/)
- 🆕 [Vizuara](https://www.youtube.com/@vizuara) is more ML/DL-focused — bookmark it now; it becomes a primary source from Phase 2 on.
- 🎨 **[Illustrated explainers](../illustrated/index.html)** (interactive, offline) for this phase: [Names, objects & mutability](../illustrated/python-data-model.html) (Q5), [Truthiness & min/max](../illustrated/python-truthiness.html) (Q3), [Comprehensions](../illustrated/python-comprehensions.html).

---

## Module 0A — Setup, syntax & the data model

| # | Topic | Open exactly this | ~Time |
|---|-------|-------------------|-------|
| 1 | Install Python 3.12+, venv, pip, run scripts | [Corey Schafer Beginners](https://www.youtube.com/playlist?list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7) — **#1 Install and Setup** + [Real Python — "Python Virtual Environments: A Primer"](https://realpython.com/python-virtual-environments-a-primer/) | 30m |
| 2 | Java→Python mindset (dynamic typing, indentation, no `;`) | [Official Tutorial (3.12+)](https://docs.python.org/3/tutorial/introduction.html) — **"An Informal Introduction to Python"** | 20m |
| 3 | Strings (f-strings, slicing) & numbers | [Corey Schafer Beginners](https://www.youtube.com/playlist?list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7) — **#2 Strings** + **#3 Integers and Floats** | 40m |
| 4 | **Mutability vs immutability** (exam Q5) | [Real Python — "Python's Mutable vs Immutable Types"](https://realpython.com/python-mutable-vs-immutable-types/) · 🎨 [Visualize](../illustrated/python-data-model.html) | 25m |
| 5 | Truthiness & `min/max/bool` (exam Q3) | [Real Python — "Python Booleans"](https://realpython.com/python-boolean/) + run the exam Q3 snippet · 🎨 [Visualize](../illustrated/python-truthiness.html) | 20m |

**✅ Checkpoint 0A** — 🖥️ Local REPL, no notes — one item per topic:
- **(T1)** Create & activate a venv, `pip install numpy`, run a script that prints `numpy.__version__`.
- **(T2)** Name three concrete ways Python differs from Java (dynamic typing, indentation blocks, no `;`).
- **(T3)** Slice `"machine"[2:5]`; build an f-string that prints `"3 squared is 9"` from a variable.
- **(T4)** Use `id()` to show a `list` is mutable but a `tuple`/`str` is not; explain why this matters when passing them to functions.
- **(T5)** Predict then verify `min(max(False, -3, -4), 2, 7)` (exam Q3); explain the truthiness of `False`/`0`.

---

## Module 0B — Collections, comprehensions, idioms

| # | Topic | Open exactly this | ~Time |
|---|-------|-------------------|-------|
| 6 | list / tuple / set | [Corey Schafer Beginners](https://www.youtube.com/playlist?list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7) — **#4 Lists, Tuples, and Sets** | 30m |
| 7 | dict (the workhorse) | [Corey Schafer Beginners](https://www.youtube.com/playlist?list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7) — **#5 Dictionaries** | 20m |
| 8 | Comprehensions (list/dict/set) | [Corey Schafer — "Python Tutorial: Comprehensions"](https://www.youtube.com/@coreyms/search?query=comprehensions) · 🎨 [Visualize](../illustrated/python-comprehensions.html) | 15m |
| 9 | `enumerate`, `zip`, unpacking | [Corey Schafer — "Python Tutorial: Zip"](https://www.youtube.com/@coreyms/search?query=zip) + [Real Python — "enumerate()"](https://realpython.com/python-enumerate/) | 20m |
| 10 | `*args` / `**kwargs`, default args | [Corey Schafer — "Python Tutorial: *args and **kwargs"](https://www.youtube.com/@coreyms/search?query=args%20kwargs) | 15m |
| 11 | Generators & `yield` | [Corey Schafer — "Python Tutorial: Generators"](https://www.youtube.com/@coreyms/search?query=generators) | 15m |

**✅ Checkpoint 0B** — 🖥️ Local — one item per topic:
- **(T6)** From `[1,1,2,3]` make a `list`, `tuple`, `set`; show the set de-dupes; say when you'd use each.
- **(T7)** Build a `dict` mapping word→length for `["cat","mouse"]`; iterate with `.items()`.
- **(T8)** Rewrite a Java `for(int i...)` that squares 1..10 as a **list comprehension**; then a dict comp `{n:n*n}`.
- **(T9)** Use `zip` to build `{'a':90,'b':80}` from two lists; loop with `enumerate` to print `"0: a"`.
- **(T10)** Write `total(*args, **kwargs)` that sums positional args and returns kwargs unchanged.
- **(T11)** Write a Fibonacci generator; take 10 with `itertools.islice`; say why it's memory-cheaper than a list.

---

## Module 0C — OOP in Python (differs most from Java)

| # | Topic | Open exactly this | ~Time |
|---|-------|-------------------|-------|
| 12 | Classes & instances | [Corey Schafer OOP](https://www.youtube.com/playlist?list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc) — **#1 Classes and Instances** | 15m |
| 13 | Class vs instance variables | [Corey Schafer OOP](https://www.youtube.com/playlist?list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc) — **#2 Class Variables** | 12m |
| 14 | `classmethod` / `staticmethod` | [Corey Schafer OOP](https://www.youtube.com/playlist?list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc) — **#3 classmethods and staticmethods** | 15m |
| 15 | Inheritance (vs Java `extends`) | [Corey Schafer OOP](https://www.youtube.com/playlist?list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc) — **#4 Inheritance** | 20m |
| 16 | **Dunder/magic methods** (`__init__`, `__repr__`, `__eq__`) | [Corey Schafer OOP](https://www.youtube.com/playlist?list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc) — **#5 Special (Magic/Dunder) Methods** | 18m |
| 17 | `@property` (vs Java getters/setters) | [Corey Schafer OOP](https://www.youtube.com/playlist?list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc) — **#6 Property Decorators** | 12m |
| 18 | `dataclasses` (concise model classes) | [Real Python — "Data Classes in Python 3.7+ (Guide)"](https://realpython.com/python-data-classes/) | 25m |
| 19 | Duck typing & EAFP vs LBYL | [Real Python — "Duck Typing in Python"](https://realpython.com/duck-typing-python/) | 15m |

**✅ Checkpoint 0C** — 🖥️ Local — one item per topic:
- **(T12)** Write an `Account` class with `__init__(self, owner, balance)` and `deposit`; make two instances.
- **(T13)** Add a class variable `bank_name` shared by all instances; show it's shared via the class.
- **(T14)** Add a `@classmethod from_dict(cls, d)` and a `@staticmethod is_valid_amount(x)`; say when each fits.
- **(T15)** Subclass into `SavingsAccount` that adds interest; call the parent `__init__` via `super()`.
- **(T16)** Add `__repr__` and `__eq__` to a `Transaction`; show `==` compares by value.
- **(T17)** Add a `@property is_expense` returning `amount < 0` (accessed without parentheses).
- **(T18)** Rewrite `Transaction` as a `@dataclass`; note the boilerplate it removed.
- **(T19)** In one sentence, why doesn't Python need Java-style interfaces? (duck typing)

---

## Module 0D — Modules, errors, files, tests, DSA-in-Python

| # | Topic | Open exactly this | ~Time |
|---|-------|-------------------|-------|
| 20 | Modules, packages, imports | [Corey Schafer Beginners](https://www.youtube.com/playlist?list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7) — **#9 import Modules** | 20m |
| 21 | Exceptions (`try/except/finally`, custom) | [Corey Schafer — "Using Try/Except Blocks for Error Handling"](https://www.youtube.com/@coreyms/search?query=try%20except) | 20m |
| 22 | File I/O + context managers (`with`) | [Corey Schafer — "File Objects - Reading and Writing to Files"](https://www.youtube.com/@coreyms/search?query=file%20objects) | 18m |
| 23 | Standard library you'll use (`collections`, `itertools`, `pathlib`) | [Official docs (3.12+) — "The Python Standard Library"](https://docs.python.org/3/library/index.html) (skim `collections`, `itertools`, `pathlib`) | 30m |
| 24 | `pytest` basics (needed for the challenges) | [Real Python — "Effective Python Testing With Pytest"](https://realpython.com/pytest-python-testing/) (first half) | 30m |
| 25 | DSA in Python (map your Java knowledge) | [NeetCode roadmap](https://neetcode.io) — do 5 Easy problems in Python | 2–3h |

**✅ Checkpoint 0D** — 🖥️ Local — one item per topic:
- **(T20)** Split `finlytics` into two modules and `import` one from the other; explain `if __name__ == "__main__":`.
- **(T21)** Wrap risky code in `try/except/finally`; define `class InvalidRowError(Exception)` and catch it.
- **(T22)** Read a CSV with `with open(...)`; explain why the context manager beats manual `close()`.
- **(T23)** Tally categories with `collections.Counter`; build a path with `pathlib.Path`; iterate two lists with `itertools`/`zip`.
- **(T24)** Write a `pytest` file with 3 `assert` tests (one using `pytest.raises`) and run `pytest -v`.
- **(T25)** Solve "Two Sum" and "Valid Parentheses" on NeetCode **in Python** — focus on dict/list/set idioms.

---

## 🏁 Phase 0 capstone — `finlytics` CLI  (🖥️ Local)
A real portfolio piece: ingest a CSV of transactions → model rows as `@dataclass` → categorize via a
dict of rules → print monthly totals. Package with `argparse`, add `pytest` tests + a README, commit
to your repo. **Then** start [BYO-1 (autograd)](../challenges/byo-01-autograd/README.md) — Python only.

**Ready for Phase 1 when** you can write a class with dunder methods + a property, use
comprehensions/`zip`/`enumerate` reflexively, handle files/exceptions, and run `pytest` — Java habits gone.
