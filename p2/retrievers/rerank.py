"""Your reranker (stage 1): ask Claude to reorder a first-stage system's top 20.

NEEDS_CLAUDE = True tells p2 that searching calls claude -p, so CI never regenerates this system's
runs; you produce them on your machine and commit them, together with their traces.
"""

from __future__ import annotations

from p2 import claude, retrievers

NEEDS_CLAUDE = True
CANDIDATES = 20
PASSAGE_CHARS = 600

PROMPT = """Below are {n} passages, numbered 1 to {n}, and a search query.
Order the passages from the most useful for answering the query to the least useful.
Reply with all {n} passage numbers, each exactly once, best first.

Query: {query}

{passages}"""


def _schema(n: int) -> dict:
    return {
        "type": "object",
        "properties": {
            "order": {
                "type": "array",
                "items": {"type": "integer", "minimum": 1, "maximum": n},
                "minItems": n,
                "maxItems": n,
            }
        },
        "required": ["order"],
    }


class Rerank:
    def __init__(self, corpus, cfg):
        self.corpus = corpus
        self.first = retrievers.build("hybrid", corpus, cfg)
        self.model = cfg.model
        self.cache_dir = claude.cache_folder(cfg)
        self.chunk_text = {c.id: c.text for c in corpus.chunks(cfg.chunk_words, cfg.chunk_overlap)}

    def _reorder(self, query: str, candidates: list[str], texts: list[str]) -> list[str]:
        n = len(candidates)
        passages = "\n\n".join(f"[{i}] {t[:PASSAGE_CHARS]}" for i, t in enumerate(texts, 1))
        prompt = PROMPT.format(n=n, query=query, passages=passages)
        reply = claude.call(prompt, _schema(n), model=self.model, cache_dir=self.cache_dir)
        order_nums = reply.output.get("order") if reply.output else None
        if not isinstance(order_nums, list) or sorted(order_nums) != list(range(1, n + 1)):
            return candidates  # a missing or invalid reply keeps the first stage's order
        return [candidates[i - 1] for i in order_nums]

    def _rank(self, text: str, k: int, hits: list[tuple[str, float]], text_of) -> list[tuple[str, float]]:
        candidates = [item for item, _ in hits[:CANDIDATES]]
        rest = [item for item, _ in hits[CANDIDATES:]]
        new_order = self._reorder(text, candidates, [text_of(c) for c in candidates]) if candidates else candidates
        combined = new_order + rest
        total = len(combined)
        return [(item, float(total - i)) for i, item in enumerate(combined)][:k]

    def search(self, text: str, k: int) -> list[tuple[str, float]]:
        hits = self.first.search(text, max(k, CANDIDATES))
        return self._rank(text, k, hits, lambda d: self.corpus.docs[d].text)

    def search_chunks(self, text: str, k: int) -> list[tuple[str, float]]:
        hits = self.first.search_chunks(text, max(k, CANDIDATES))
        return self._rank(text, k, hits, lambda c: self.chunk_text[c])


def build(corpus, cfg):
    return Rerank(corpus, cfg)
