"""BYO-9 starter — a Retrieval-Augmented Generation engine from scratch (NumPy only, no LangChain).

The `embedder` (text -> vector) and `llm` (prompt -> text) are **injected** so everything runs
offline and deterministically. In production you'd pass a real embedding model and a real LLM; here
the tests pass simple deterministic mocks. See README.md.
"""
import numpy as np


def chunk_text(text, size, overlap=0):
    """Stage 1: split `text` into word chunks of `size` words, sliding by (size - overlap).
    Return a list of chunk strings that together cover the whole text."""
    raise NotImplementedError("implement chunk_text")


def cosine_similarity(a, b):
    """Stage 2: cosine similarity of two vectors. Return 0.0 if either has zero norm."""
    raise NotImplementedError("implement cosine_similarity")


class RAGEngine:
    def __init__(self, embedder):
        self.embedder = embedder        # callable: text -> 1-D np.ndarray
        self.chunks = []
        self.vectors = []

    def add_documents(self, docs, chunk_size=None, overlap=0):
        """Stage 2: for each doc, optionally chunk it (if chunk_size given), embed each chunk, and
        store (chunk_text, vector). Return self."""
        raise NotImplementedError("implement add_documents")

    def retrieve(self, query, k=3):
        """Stage 2: embed the query, rank stored chunks by cosine similarity, return the top-k
        chunk strings (most similar first)."""
        raise NotImplementedError("implement retrieve")

    def build_prompt(self, query, chunks):
        """Stage 3: assemble a grounded prompt with numbered citations, e.g.:
            Answer the question using only the context.
            Context:
            [1] <chunk 1>
            [2] <chunk 2>

            Question: <query>
            Answer:
        """
        raise NotImplementedError("implement build_prompt")

    def answer(self, query, llm, k=3):
        """Stage 4: retrieve -> build_prompt -> call llm(prompt). Return
        {"answer": <llm output>, "sources": <list of retrieved chunks>}."""
        raise NotImplementedError("implement answer")
