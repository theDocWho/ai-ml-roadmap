# BYO-12 — Build Your Own Autoencoder → VAE → GAN

> Reinforces: autoencoders, VAE, GAN (exam Q41, Q48, Q49, Q50) · Phase 4–6 · ⭐⭐⭐
> The three generative ideas, minimal and from scratch (NumPy only).

```bash
cd challenges/byo-12-generative
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pytest tests/ -v
```

## Stages (`generative/models.py`)

1. **Autoencoder** — a linear encode→bottleneck→decode trained with gradient descent; on rank-2
   data the reconstruction error collapses (the bottleneck *learns the structure*, exam Q50).
2. **VAE** — the `reparameterize` trick (`z = mu + e^{0.5·logvar}·eps`) that lets gradients flow
   through sampling, and the `kl_divergence` regularizer (0 at the standard-normal prior).
3. **GAN** — the adversarial losses: `bce`, `discriminator_loss` (real→1, fake→0), `generator_loss`
   (fake→1). Two networks playing a min-max game (exam Q48).

## Stretch (not tested)
Make the VAE and GAN fully trainable by wiring them through your **BYO-5 mini-PyTorch** autograd and
generating samples (e.g. 8×8 digits). Then read why VAEs look blurry (exam Q49) and GANs are unstable.

## Done when
`pytest tests/` is green and you can explain reconstruction vs the KL term vs the adversarial game.
