"""Stage 3 — backpropagation: the canonical example + a numerical gradient check."""
import math
from autograd.engine import Value


def test_canonical_backward_example():
    # L = ((a*b) + c) * f   — the hand-worked micrograd example.
    a = Value(2.0)
    b = Value(-3.0)
    c = Value(10.0)
    e = a * b           # -6
    d = e + c           #  4
    f = Value(-2.0)
    L = d * f           # -8
    L.backward()

    assert math.isclose(L.data, -8.0)
    assert math.isclose(a.grad, 6.0)
    assert math.isclose(b.grad, -4.0)
    assert math.isclose(c.grad, -2.0)
    assert math.isclose(d.grad, -2.0)
    assert math.isclose(e.grad, -2.0)
    assert math.isclose(f.grad, 4.0)


def test_node_reused_accumulates_gradient():
    # a is used twice: y = a*a + a  -> dy/da = 2a + 1
    a = Value(3.0)
    y = a * a + a
    y.backward()
    assert math.isclose(a.grad, 7.0)   # 2*3 + 1


def test_matches_numerical_gradient():
    def f(x_val):
        x = Value(x_val)
        # a smooth nonlinear function using several ops
        out = (x * x * x + (2.0 * x) + 1.0).tanh()
        return x, out

    x0 = 0.37
    x, out = f(x0)
    out.backward()
    analytic = x.grad

    h = 1e-6
    _, out_p = f(x0 + h)
    _, out_m = f(x0 - h)
    numeric = (out_p.data - out_m.data) / (2 * h)

    assert math.isclose(analytic, numeric, rel_tol=1e-4, abs_tol=1e-6)
