"""Your hybrid retriever (stage 1): fuse the rankings of two systems into one.

Fuses bm25 with dense by reciprocal rank fusion (k = 60): a document scores the sum of
1 / (k + rank + 1) over the rankings it appears in, best rank first (rank 0).
"""

from __future__ import annotations

from p2 import retrievers
from p2.runfile import order

NEEDS_CLAUDE = False
K = 60


def _rrf(rankings: list[list[str]]) -> dict[str, float]:
    scores: dict[str, float] = {}
    for ranking in rankings:
        for rank, item_id in enumerate(ranking):
            scores[item_id] = scores.get(item_id, 0.0) + 1 / (K + rank + 1)
    return scores


class Hybrid:
    model: str | None = None

    def __init__(self, corpus, cfg):
        self.corpus = corpus
        self.base = retrievers.build("bm25", corpus, cfg)
        self.partner = retrievers.build("dense", corpus, cfg)
        self.n_docs = len(corpus.docs)
        self.n_chunks = len(self.base.chunks)

    def search(self, text: str, k: int) -> list[tuple[str, float]]:
        rankings = [
            [docid for docid, _ in self.base.search(text, self.n_docs)],
            [docid for docid, _ in self.partner.search(text, self.n_docs)],
        ]
        return order(_rrf(rankings).items())[:k]

    def search_chunks(self, text: str, k: int) -> list[tuple[str, float]]:
        rankings = [
            [chunk_id for chunk_id, _ in self.base.search_chunks(text, self.n_chunks)],
            [chunk_id for chunk_id, _ in self.partner.search_chunks(text, self.n_chunks)],
        ]
        return order(_rrf(rankings).items())[:k]


def build(corpus, cfg):
    return Hybrid(corpus, cfg)
