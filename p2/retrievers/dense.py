"""Your dense retriever (stage 1): embed every chunk once, embed the query, and rank chunks by cosine similarity.

Uses bge-small-en-v1.5 (see DECISIONS.md for why).
"""

from __future__ import annotations

from p2 import embed
from p2.retrievers import ChunkScorer

NEEDS_CLAUDE = False


class Dense(ChunkScorer):
    def __init__(self, corpus, cfg):
        super().__init__(corpus, cfg)
        self.model = cfg.table("dense").get("model", embed.BGE)
        self.embedder = embed.load(self.model)
        self.doc_vecs = embed.doc_vectors(self.embedder, [c.text for c in self.chunks], cfg.root)

    def score_chunks(self, text: str) -> list[float]:
        query_vec = self.embedder.encode([text])
        return (query_vec @ self.doc_vecs.T)[0].tolist()


def build(corpus, cfg):
    return Dense(corpus, cfg)
