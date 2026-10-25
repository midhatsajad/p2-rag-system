"""Ablation: dense with potion-retrieval-32M instead of bge-small-en-v1.5.

Tests the claim in EVAL.md section 1 that bge's contextual encoding is what dense's score on
paraphrase and cross-cutting queries depends on, not just the paraphrase class alone; potion gives
every word one fixed vector regardless of its sentence, so it should do worse where a query's wording
differs from the manuals' or where the same term (RQD) needs a different passage depending on purpose.
"""

from __future__ import annotations

from p2 import embed
from p2.retrievers.dense import Dense

NEEDS_CLAUDE = False
BASE = "dense"


def build(corpus, cfg):
    return Dense(corpus, cfg.replace(tables={**cfg.tables, "dense": {"model": embed.POTION}}))
