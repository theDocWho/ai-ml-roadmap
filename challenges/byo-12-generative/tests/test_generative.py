"""Staged acceptance tests for BYO-12."""
import numpy as np
from generative.models import (
    Autoencoder, reparameterize, kl_divergence, bce,
    discriminator_loss, generator_loss,
)


# ----- Stage 1: autoencoder -----
def test_stage1_autoencoder_reconstructs_lowrank():
    rng = np.random.default_rng(0)
    Z = rng.normal(size=(200, 2))
    B = rng.normal(size=(2, 8))
    X = Z @ B                                  # rank-2 data living in 8-D
    ae = Autoencoder(8, 2, seed=1)
    init = np.mean((ae.reconstruct(X) - X) ** 2)
    ae.train(X, lr=0.02, epochs=3000)
    final = np.mean((ae.reconstruct(X) - X) ** 2)
    assert final < init * 0.1                  # bottleneck captures the 2-D structure


# ----- Stage 2: VAE -----
def test_stage2_reparameterize():
    mu = np.array([1.0, 2.0])
    logvar = np.array([0.0, 0.0])              # sigma = 1
    eps = np.array([0.5, -1.0])
    assert np.allclose(reparameterize(mu, logvar, eps), [1.5, 1.0])


def test_stage2_kl_zero_at_standard_normal():
    assert np.isclose(kl_divergence(np.zeros(5), np.zeros(5)), 0.0)


def test_stage2_kl_positive_away_from_prior():
    assert kl_divergence(np.array([3.0]), np.array([0.0])) > 0
    assert kl_divergence(np.array([0.0]), np.array([2.0])) > 0


# ----- Stage 3: GAN losses -----
def test_stage3_bce():
    assert bce(np.array([1.0]), 1) < 1e-3      # confident & correct -> ~0
    assert bce(np.array([0.0]), 1) > 5         # confident & wrong -> large


def test_stage3_discriminator_loss_lower_when_accurate():
    good = discriminator_loss(np.array([0.99, 0.98]), np.array([0.01, 0.02]))
    bad = discriminator_loss(np.array([0.5, 0.5]), np.array([0.5, 0.5]))
    assert good < bad


def test_stage3_generator_loss_lower_when_fooling():
    assert generator_loss(np.array([0.99])) < generator_loss(np.array([0.01]))
