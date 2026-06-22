"""Stage 2 — the rest of the operations."""
import math
from autograd.engine import Value


def test_pow():
    assert (Value(3.0) ** 2).data == 9.0


def test_neg_and_sub():
    assert (-Value(4.0)).data == -4.0
    assert (Value(5.0) - Value(2.0)).data == 3.0


def test_truediv():
    assert (Value(6.0) / Value(2.0)).data == 3.0


def test_reflected_ops():
    assert (2 * Value(3.0)).data == 6.0
    assert (1 + Value(3.0)).data == 4.0
    assert (10 - Value(4.0)).data == 6.0


def test_tanh():
    assert math.isclose((Value(0.5)).tanh().data, math.tanh(0.5), rel_tol=1e-9)


def test_exp():
    assert math.isclose((Value(1.0)).exp().data, math.e, rel_tol=1e-9)


def test_relu():
    assert (Value(-2.0)).relu().data == 0.0
    assert (Value(3.0)).relu().data == 3.0
