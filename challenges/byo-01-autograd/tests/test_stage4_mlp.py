"""Stage 4 — train a tiny MLP on your own engine; the loss must go down."""
import random
from autograd.nn import MLP


def test_mlp_forward_shape():
    random.seed(0)
    net = MLP(3, [4, 4, 1])
    out = net([1.0, 2.0, -1.0])
    # single output neuron -> a scalar Value (not a list)
    assert not isinstance(out, list)
    assert -1.0 <= out.data <= 1.0   # tanh output


def test_mlp_has_parameters():
    random.seed(0)
    net = MLP(3, [4, 4, 1])
    # 3->4 (16) + 4->4 (20) + 4->1 (5) = 41 params
    assert len(net.parameters()) == 41


def test_training_reduces_loss():
    random.seed(1)
    net = MLP(3, [4, 4, 1])
    xs = [
        [2.0, 3.0, -1.0],
        [3.0, -1.0, 0.5],
        [0.5, 1.0, 1.0],
        [1.0, 1.0, -1.0],
    ]
    ys = [1.0, -1.0, -1.0, 1.0]

    def total_loss():
        preds = [net(x) for x in xs]
        return sum((p - y) ** 2 for p, y in zip(preds, ys))

    initial = total_loss().data
    for _ in range(50):
        loss = total_loss()
        net.zero_grad()
        loss.backward()
        for p in net.parameters():
            p.data -= 0.05 * p.grad
    final = total_loss().data

    assert final < initial * 0.5   # loss at least halves
