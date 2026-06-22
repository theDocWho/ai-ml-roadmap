"""Staged acceptance tests for BYO-9. Everything offline via mock embedder/LLM."""
import numpy as np
from rag.engine import chunk_text, cosine_similarity, RAGEngine


def make_bow_embedder(vocab):
    """A deterministic bag-of-words embedder over a fixed vocab (stand-in for a real model)."""
    def embed(text):
        words = text.lower().split()
        return np.array([float(words.count(w)) for w in vocab])
    return embed


VOCAB = ["cat", "cats", "fur", "dog", "dogs", "bark", "car", "engine", "oil"]
DOCS = [
    "cats have fur and cats purr softly",
    "dogs bark loudly and dogs run",
    "a car engine needs oil regularly",
]


# ----- Stage 1 -----
def test_stage1_chunk_text():
    chunks = chunk_text("a b c d e f", size=3, overlap=1)   # step = 2
    assert chunks[0] == "a b c"
    assert "".join("".join(c.split()) for c in chunks).startswith("abc")
    # every word appears in at least one chunk
    joined = " ".join(chunks)
    for w in "a b c d e f".split():
        assert w in joined.split()


# ----- Stage 2 -----
def test_stage2_cosine():
    assert np.isclose(cosine_similarity([1, 0], [1, 0]), 1.0)
    assert np.isclose(cosine_similarity([1, 0], [0, 1]), 0.0)
    assert cosine_similarity([0, 0], [1, 1]) == 0.0


def test_stage2_retrieve_matches_topic():
    eng = RAGEngine(make_bow_embedder(VOCAB)).add_documents(DOCS)
    top = eng.retrieve("tell me about cats and fur", k=1)
    assert top[0] == DOCS[0]
    top2 = eng.retrieve("car engine oil change", k=1)
    assert top2[0] == DOCS[2]


# ----- Stage 3 -----
def test_stage3_prompt_has_context_and_citations():
    eng = RAGEngine(make_bow_embedder(VOCAB)).add_documents(DOCS)
    chunks = eng.retrieve("dogs bark", k=2)
    prompt = eng.build_prompt("why do dogs bark?", chunks)
    assert "[1]" in prompt and "[2]" in prompt
    assert "why do dogs bark?" in prompt
    assert chunks[0] in prompt


# ----- Stage 4 -----
def test_stage4_answer_end_to_end():
    eng = RAGEngine(make_bow_embedder(VOCAB)).add_documents(DOCS)

    def mock_llm(prompt):
        # a trivial grounded "model": echo the first retrieved context line
        return prompt.split("Context:\n")[1].split("\n")[0]

    out = eng.answer("what do cats have?", mock_llm, k=2)
    assert out["sources"][0] == DOCS[0]
    assert out["answer"].startswith("[1]")


def test_stage4_hit_at_k():
    eng = RAGEngine(make_bow_embedder(VOCAB)).add_documents(DOCS)
    queries = ["cats fur purr", "dogs bark run", "engine oil car"]
    relevant = [DOCS[0], DOCS[1], DOCS[2]]
    hits = sum(rel in eng.retrieve(q, k=1) for q, rel in zip(queries, relevant))
    assert hits / len(queries) == 1.0
