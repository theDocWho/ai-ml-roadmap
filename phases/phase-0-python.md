# Phase 0 — Python for a Java Developer (≈2–3 weeks)

**Goal:** become fluent in *idiomatic* Python. You already know programming and DSA from Java, so
this is about Python's syntax, data model, and idioms — not "what is a loop." Skip anything you
already know; spend your time on the **Pythonic** rows and OOP differences.

**Primary free resources** (we point at specific videos inside these):
- Corey Schafer — *Python Programming Beginner Tutorials* playlist — https://www.youtube.com/playlist?list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7
- Corey Schafer — *Python OOP Tutorials* playlist — https://www.youtube.com/playlist?list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc
- Real Python (free articles) — https://realpython.com
- Official Python Tutorial — https://docs.python.org/3/tutorial/

---

## Module 0A — Setup, syntax & the data model

| # | Topic | Watch / read exactly this | ~Time |
|---|-------|---------------------------|-------|
| 1 | Install Python, venv, pip, running scripts | Corey Schafer — "Python Tutorial for Beginners 1: Install and Setup" + Real Python "Python Virtual Environments: A Primer" | 30m |
| 2 | Java→Python mindset (dynamic typing, indentation, no `;`, no types) | Real Python — "Python vs Java" article (skim) | 20m |
| 3 | Numbers & strings (f-strings, slicing) | Corey Schafer — Beginner Tutorials **#2 Strings** and **#3 Integers and Floats** | 40m |
| 4 | **Mutability vs immutability** (exam Q5) | Real Python — "Immutable vs Mutable Data Types in Python" | 25m |
| 5 | Truthiness & `min/max/bool` behavior (exam Q3) | Real Python — "Python Booleans" + try the exam Q3 snippet in a REPL | 20m |

**✅ Checkpoint 0A** (do in a Python REPL, no notes) — one item per topic:
- **(T1)** Create & activate a venv, `pip install numpy`, run a script that prints `numpy.__version__`.
- **(T2)** Name three concrete ways Python differs from Java (e.g. dynamic typing, indentation blocks, no `;`).
- **(T3)** Slice `"machine"[2:5]`; then build an f-string that prints `"3 squared is 9"` from a variable.
- **(T4)** Use `id()` to show a `list` is mutable but a `tuple`/`str` is not; explain why this matters when passing them to a function.
- **(T5)** Predict then verify `min(max(False, -3, -4), 2, 7)` (exam Q3) and explain the truthiness of `False`/`0`.

---

## Module 0B — Collections, comprehensions, idioms

| # | Topic | Watch / read exactly this | ~Time |
|---|-------|---------------------------|-------|
| 6 | list / tuple / set | Corey Schafer — Beginner Tutorials **#4 Lists, Tuples, and Sets** | 30m |
| 7 | dict (the workhorse) | Corey Schafer — Beginner Tutorials **#5 Dictionaries** | 20m |
| 8 | Comprehensions (list/dict/set) | Corey Schafer — "Python Tutorial: Comprehensions" | 15m |
| 9 | Pythonic iteration: `enumerate`, `zip`, unpacking | Corey Schafer — "Python Tutorial: Zip" + Real Python "enumerate()" | 20m |
| 10 | `*args` / `**kwargs`, default args | Corey Schafer — "Python Tutorial: *args and **kwargs" | 15m |
| 11 | Generators & `yield` | Corey Schafer — "Python Tutorial: Generators" | 15m |

**✅ Checkpoint 0B** — one item per topic:
- **(T6)** Make a `list`, a `tuple`, and a `set` from `[1,1,2,3]`; show the set de-duplicates and explain when you'd use each.
- **(T7)** Build a `dict` mapping word→length for `["cat","mouse"]`; iterate it with `.items()`.
- **(T8)** Rewrite a Java-style `for (int i...)` loop that squares 1..10 as a **list comprehension**; then a dict comprehension `{n: n*n}`.
- **(T9)** Given `names=['a','b']` and `scores=[90,80]`, build `{'a':90,'b':80}` with `zip`; then loop with `enumerate` to print "0: a".
- **(T10)** Write a function `total(*args, **kwargs)` that sums positional args and returns kwargs unchanged.
- **(T11)** Write a generator yielding Fibonacci; take the first 10 with `itertools.islice`. Why is a generator memory-cheaper than a list?

---

## Module 0C — OOP in Python (the part that differs most from Java)

| # | Topic | Watch / read exactly this | ~Time |
|---|-------|---------------------------|-------|
| 12 | Classes & instances | Corey Schafer — **OOP #1 Classes and Instances** | 15m |
| 13 | Class vs instance variables | Corey Schafer — **OOP #2 Class Variables** | 12m |
| 14 | `classmethod` / `staticmethod` | Corey Schafer — **OOP #3 classmethods and staticmethods** | 15m |
| 15 | Inheritance (vs Java's `extends`) | Corey Schafer — **OOP #4 Inheritance** | 20m |
| 16 | **Dunder / magic methods** (`__init__`, `__repr__`, `__eq__`) | Corey Schafer — **OOP #5 Special (Magic/Dunder) Methods** | 18m |
| 17 | `@property` (vs Java getters/setters) | Corey Schafer — **OOP #6 Property Decorators** | 12m |
| 18 | `dataclasses` (concise model classes) | Real Python — "Data Classes in Python 3.7+ (Guide)" | 25m |
| 19 | Duck typing & EAFP vs LBYL | Real Python — "Duck Typing in Python" | 15m |

**✅ Checkpoint 0C** — one item per topic:
- **(T12)** Write a plain `Account` class with `__init__(self, owner, balance)` and a `deposit` method; create two instances.
- **(T13)** Add a **class variable** `bank_name` shared by all instances; show it's shared via the class, not per-instance.
- **(T14)** Add a `@classmethod` `from_dict(cls, d)` and a `@staticmethod` `is_valid_amount(x)`; explain when each is appropriate.
- **(T15)** Subclass `Account` into `SavingsAccount` that adds interest; call the parent `__init__` via `super()`.
- **(T16)** Add `__repr__` and `__eq__` to a `Transaction`; show `==` compares by value.
- **(T17)** Add a `@property` `is_expense` returning `amount < 0` (no parentheses to call it).
- **(T18)** Rewrite `Transaction` as a `@dataclass`; note what boilerplate it removed.
- **(T19)** Explain in one sentence why Python doesn't need Java-style interfaces (duck typing).

---

## Module 0D — Modules, errors, files, tests, DSA-in-Python

| # | Topic | Watch / read exactly this | ~Time |
|---|-------|---------------------------|-------|
| 20 | Modules, packages, imports | Corey Schafer — Beginner Tutorials **#9 import Modules** | 20m |
| 21 | Exceptions (`try/except/finally`, custom) | Corey Schafer — "Python Tutorial: Using Try/Except Blocks for Error Handling" | 20m |
| 22 | File I/O + context managers (`with`) | Corey Schafer — "Python Tutorial: File Objects - Reading and Writing to Files" | 18m |
| 23 | The standard library you'll actually use (`collections`, `itertools`, `pathlib`, `csv`) | Real Python — "Python's collections" + "Itertools" (skim) | 30m |
| 24 | `pytest` basics (you'll need it for the challenges) | Real Python — "Effective Python Testing With Pytest" (first half) | 30m |
| 25 | DSA in Python (map your Java knowledge) | NeetCode roadmap — https://neetcode.io ; do 5 Easy problems in Python | 2–3h |

**✅ Checkpoint 0D** — one item per topic:
- **(T20)** Split your `finlytics` code into two modules and `import` one from the other; what does `if __name__ == "__main__":` do?
- **(T21)** Wrap risky code in `try/except/finally`; raise a custom `class InvalidRowError(Exception)` and catch it.
- **(T22)** Read a CSV with a `with open(...)` block; explain why the context manager is better than manual `close()`.
- **(T23)** Use `collections.Counter` to tally categories and `pathlib.Path` to build a file path; iterate two lists with `itertools`/`zip`.
- **(T24)** Write a `pytest` file with 3 `assert` tests (one expected-failure with `pytest.raises`) and run `pytest -v`.
- **(T25)** Solve "Two Sum" and "Valid Parentheses" on NeetCode **in Python** — focus on dict/list/set idioms, not the algorithm.

---

## 🏁 Phase 0 capstone exercise — `finlytics` CLI
Build the project from the roadmap (a real portfolio piece, not a toy):
- Ingest a CSV of transactions → model each row as a `@dataclass` → categorize with a dict of rules →
  print monthly totals. Package it with `argparse`, add `pytest` tests, and a README.
- **Then** start [BYO-1 (autograd)](../challenges/byo-01-autograd/README.md) — it only needs Python.

**You're ready for Phase 1 when** you can: write a class with dunder methods + a property, use
comprehensions/`zip`/`enumerate` reflexively, handle files and exceptions, and run `pytest` — all
without checking Java habits.
