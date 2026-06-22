"""Staged acceptance tests for BYO-7."""
from bpe.tokenizer import get_stats, merge, BPETokenizer


# ----- Stage 1 -----
def test_stage1_get_stats():
    stats = get_stats([1, 2, 1, 2, 3])
    assert stats[(1, 2)] == 2
    assert stats[(2, 3)] == 1


def test_stage1_merge():
    assert merge([1, 2, 1, 2, 3], (1, 2), 99) == [99, 99, 3]
    assert merge([5, 6, 7], (1, 2), 99) == [5, 6, 7]


# ----- Stage 2 -----
def test_stage2_train_learns_merges():
    tok = BPETokenizer().train("ababababab", vocab_size=258)
    assert len(tok.merges) >= 1
    assert all(idx >= 256 for idx in tok.merges.values())


# ----- Stage 3 -----
def test_stage3_roundtrip():
    text = "the quick brown fox jumps over the quick brown fox"
    tok = BPETokenizer().train(text, vocab_size=300)
    assert tok.decode(tok.encode(text)) == text


def test_stage3_roundtrip_unicode():
    text = "café déjà vu — café déjà vu"
    tok = BPETokenizer().train(text, vocab_size=300)
    assert tok.decode(tok.encode(text)) == text


def test_stage3_compresses_repetition():
    text = "abc " * 50
    tok = BPETokenizer().train(text, vocab_size=300)
    assert len(tok.encode(text)) < len(text.encode("utf-8"))
