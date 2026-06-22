"""BYO-7 starter — a byte-level BPE tokenizer (the thing in front of every LLM). See README.md.

Inspired by Karpathy's minBPE. Pure Python; no deps needed beyond pytest for tests.
"""


def get_stats(ids):
    """Stage 1: count adjacent pairs. Return {(a, b): count} for consecutive ids."""
    raise NotImplementedError("implement get_stats")


def merge(ids, pair, idx):
    """Stage 1: return a new list with every consecutive occurrence of `pair` replaced by `idx`."""
    raise NotImplementedError("implement merge")


class BPETokenizer:
    def __init__(self):
        self.merges = {}        # (a, b) -> new_id, in the order learned

    def train(self, text, vocab_size):
        """Stage 2: start from raw UTF-8 bytes (ids 0..255). Repeatedly find the most frequent
        pair and merge it into a new id (256, 257, ...) until you reach vocab_size (or no pairs
        remain). Record each merge in self.merges. Return self."""
        raise NotImplementedError("implement train")

    def encode(self, text):
        """Stage 3: bytes -> ids, applying learned merges greedily by *lowest merge id first*
        (i.e. in the order they were learned). Return a list of ids."""
        raise NotImplementedError("implement encode")

    def decode(self, ids):
        """Stage 3: ids -> text. Build a vocab mapping id -> bytes (256 base bytes plus each merge =
        concat of its two children), join, and UTF-8 decode. decode(encode(t)) must equal t."""
        raise NotImplementedError("implement decode")
