"""Stage 1 — the Value object and the two core ops."""
from autograd.engine import Value


def test_value_holds_data_and_zero_grad():
    v = Value(5.0)
    assert v.data == 5.0
    assert v.grad == 0.0


def test_add():
    out = Value(2.0) + Value(3.0)
    assert isinstance(out, Value)
    assert out.data == 5.0


def test_mul():
    out = Value(2.0) * Value(3.0)
    assert out.data == 6.0


def test_add_with_python_number():
    assert (Value(2.0) + 4).data == 6.0


def test_graph_is_tracked():
    a, b = Value(2.0), Value(3.0)
    out = a * b
    assert a in out._prev and b in out._prev
    assert out._op == "*"


def test_repr():
    assert repr(Value(5.0)) == "Value(data=5.0, grad=0.0)"
