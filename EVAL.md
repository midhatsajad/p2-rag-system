# Evaluation report

This is the report on what you built and what the numbers let you claim.
Two kinds of text live here.

The tables between a `p2:begin` comment line and its matching `p2:end` comment line are written by `uv run p2 score` from your committed run files and answers files.
Please do not edit anything between those two lines, because `uv run p2 check` recomputes them and fails when they differ.
A table that says no runs or answers exist yet is waiting for data; run `uv run p2 score` after you commit the files it needs.

Everything else is yours.
Each prompt ends with a marker line that you replace with your own writing; `uv run p2 check --final` fails while one is left.
Write what you measured, including what did not work.
What I read for is whether each claim matches its interval, not whether the result is good news.

Words used below: recall@10, MRR@10 and nDCG@10 are the three scores, each averaged over the queries of a set; step 7 of stage 1 in the README defines them, and lecture 14 goes deeper.
A paired interval is the 95% interval of the mean difference between two systems on the same queries, found by resampling the queries 10,000 times.
When an interval includes zero, the gold set cannot tell the two systems apart, and the right words are "not distinguishable on this gold set".
The minimum detectable difference is the smallest gap this many queries could reliably show, so a difference below it is invisible to this gold set, not absent.

---

## 1. Stage 1 - the shared corpus (30 CFR Chapter I)

### What you built

For each of `dense`, `hybrid` and `rerank`, one or two sentences: the embedding model, how documents were chunked, what was fused and how, how many candidates the reranker saw, and anything you changed from the 12 and 13 lab code.

dense embeds every chunk of the corpus with bge-small-en-v1.5. Chunks are 300 words long, with 50 words of overlap between neighbors (p2.toml, [chunking]). It caches the vectors through p2/embed.py and scores a query against all chunks at once with a single cosine-similarity matrix product. A document’s score is its best chunk’s score, the maximum, through the `search()` it inherits from `ChunkScorer`. It is the embedding arm of lab 12’s retrieve.py, using the contextual model bge-small-en-v1.5 instead of the faster static model potion-retrieval-32M, because I expected the paraphrase queries, which share few words with the regulation text, to need a model that reads each word in its sentence rather than averaging fixed word vectors.

hybrid fuses the full bm25 and dense rankings of every document with reciprocal rank fusion at k = 60. Each document’s score is the sum of 1/(60 + rank) over the two rankings, with ranks counted from 1. It is lab 13’s rrf().

rerank takes hybrid’s top 20 candidates and sends them to Claude Sonnet as numbered passages. Each passage is the candidate’s text truncated to its first 600 characters (`PASSAGE_CHARS`). It asks for the best order back as {"order": [...]}, with a schema that keeps every number between 1 and 20. If the reply is not a permutation of the candidate numbers, it falls back to hybrid’s order. That check covers both a malformed reply and a failed call, since a failed call returns nothing. It reranks documents for p2 run and chunks for p2 answer.

### Practice queries (20)

Scores per system.

<!-- p2:begin shared-practice -->
| System | Recall@10 | MRR@10 | nDCG@10 |
| --- | ---: | ---: | ---: |
| bm25 | 0.625 | 0.507 | 0.518 |
| dense | 0.558 | 0.562 | 0.480 |
| hybrid | 0.592 | 0.471 | 0.443 |
| rerank | 0.733 | 0.800 | 0.746 |

20 judged queries; nDCG uses binary labels; a random ranking of the 2,484 documents would get recall@10 near 0.004.
<!-- p2:end shared-practice -->

The same scores per query class.

<!-- p2:begin shared-practice-classes -->
| System | Metric | identifier (n=7) | paraphrase (n=7) | mixed (n=6) |
| --- | --- | ---: | ---: | ---: |
| bm25 | Recall@10 | 1.000 | 0.000 | 0.917 |
| bm25 | MRR@10 | 0.810 | 0.000 | 0.746 |
| bm25 | nDCG@10 | 0.857 | 0.000 | 0.728 |
| dense | Recall@10 | 0.214 | 0.595 | 0.917 |
| dense | MRR@10 | 0.333 | 0.714 | 0.653 |
| dense | nDCG@10 | 0.211 | 0.593 | 0.661 |
| hybrid | Recall@10 | 0.500 | 0.405 | 0.917 |
| hybrid | MRR@10 | 0.514 | 0.152 | 0.792 |
| hybrid | nDCG@10 | 0.397 | 0.202 | 0.779 |
| rerank | Recall@10 | 0.643 | 0.595 | 1.000 |
| rerank | MRR@10 | 0.714 | 0.714 | 1.000 |
| rerank | nDCG@10 | 0.659 | 0.626 | 0.987 |
<!-- p2:end shared-practice-classes -->

Differences between every pair of systems, each with its paired interval and the minimum detectable difference.

<!-- p2:begin shared-practice-pairs -->
| Comparison | Metric | Mean difference | 95% interval | MDD | Reading |
| --- | --- | ---: | ---: | ---: | --- |
| dense minus bm25 | Recall@10 | -0.067 | [-0.350, +0.225] | 0.415 | not distinguishable |
| dense minus bm25 | MRR@10 | +0.055 | [-0.225, +0.343] | 0.412 | not distinguishable |
| dense minus bm25 | nDCG@10 | -0.039 | [-0.302, +0.231] | 0.385 | not distinguishable |
| hybrid minus bm25 | Recall@10 | -0.033 | [-0.250, +0.192] | 0.324 | not distinguishable |
| hybrid minus bm25 | MRR@10 | -0.037 | [-0.178, +0.083] | 0.192 | not distinguishable |
| hybrid minus bm25 | nDCG@10 | -0.075 | [-0.238, +0.075] | 0.228 | not distinguishable |
| hybrid minus dense | Recall@10 | +0.033 | [-0.125, +0.192] | 0.231 | not distinguishable |
| hybrid minus dense | MRR@10 | -0.092 | [-0.306, +0.109] | 0.301 | not distinguishable |
| hybrid minus dense | nDCG@10 | -0.036 | [-0.200, +0.113] | 0.227 | not distinguishable |
| rerank minus bm25 | Recall@10 | +0.108 | [-0.133, +0.350] | 0.351 | not distinguishable |
| rerank minus bm25 | MRR@10 | +0.293 | [+0.043, +0.533] | 0.353 | rerank higher |
| rerank minus bm25 | nDCG@10 | +0.227 | [-0.009, +0.452] | 0.335 | not distinguishable |
| rerank minus dense | Recall@10 | +0.175 | [+0.033, +0.333] | 0.221 | rerank higher |
| rerank minus dense | MRR@10 | +0.237 | [+0.083, +0.408] | 0.239 | rerank higher |
| rerank minus dense | nDCG@10 | +0.266 | [+0.123, +0.424] | 0.219 | rerank higher |
| rerank minus hybrid | Recall@10 | +0.142 | [+0.050, +0.258] | 0.160 | rerank higher |
| rerank minus hybrid | MRR@10 | +0.329 | [+0.164, +0.504] | 0.247 | rerank higher |
| rerank minus hybrid | nDCG@10 | +0.302 | [+0.173, +0.436] | 0.192 | rerank higher |

The interval is a paired bootstrap (10,000 resamples of the queries); MDD is the smallest difference this many queries detect 80% of the time.
<!-- p2:end shared-practice-pairs -->

The 40 test queries have no answer key in this repo.
Your test run files are scored by the course and the score comes back to you as feedback, so nothing goes here for them.

### What the intervals let you claim

Which differences are distinguishable from zero and which are not?
What is the minimum detectable difference at 20 queries, and what does that say about any gap smaller than it?
Which claim from lecture 12 or 13 did your numbers support, and which did they leave open?

On the 20 practice queries, the reranker is the only system distinguishable from any other.

It is higher than dense and higher than hybrid on all three scores, and all six intervals lie above zero. For example, its MRR@10 is +0.329 over hybrid, with interval [+0.164, +0.504].

Against bm25, it is higher only on MRR@10: +0.293, with interval [+0.043, +0.533]. Its recall@10 gain (+0.108, [−0.133, +0.350]) and its nDCG@10 gain (+0.227, [−0.009, +0.452]) are not distinguishable on this gold set, though the nDCG interval only just reaches zero. So the numbers support the claim that reranking puts the first relevant document higher than bm25 does. They do not support the claim that it finds more relevant documents.

Because rerank reorders hybrid’s top 20, the rerank-minus-hybrid rows measure what the reordering itself adds. Its recall@10 gain of +0.142 [+0.050, +0.258] means it moved relevant documents from hybrid’s ranks 11–20 into the top 10. Its MRR@10 gain of +0.329 [+0.164, +0.504] means the first relevant document sits higher on average. These two scores can’t separate how much of that gain came from reordering documents already in hybrid’s top 10 and how much from documents brought in from ranks 11–20.

bm25, dense and hybrid are not distinguishable from each other: all nine of their pairwise intervals include zero.

At 20 queries, the minimum detectable difference ranges from 0.160 (rerank minus hybrid, recall@10) to 0.415 (dense minus bm25, recall@10). It is largest for pairs of systems that fail on different queries. For those pairs, the per-query differences swing between large positive and large negative values.

The gaps among bm25, dense and hybrid are all 0.092 or smaller, far below what this gold set can see. A real difference of 0.3 to 0.4 between bm25 and dense could also go unseen. “Not distinguishable” here means the gold set is too small to tell them apart, not that the systems perform the same.

Several of the reranker’s detected gains are at or below their minimum detectable difference. For example, its MRR@10 gain over dense is +0.237, against an MDD of 0.239. Those intervals clear zero, but a gold set this size would often miss gains this large, so the sizes of those gains are rough.

The per-class table has only 6 or 7 queries per class and no intervals, so I read it descriptively. bm25 found a relevant document in the top 10 for every identifier query (recall@10 1.000) and for none of the paraphrase queries (0.000). Dense showed the opposite pattern, less sharply: 0.214 on identifier queries and 0.595 on paraphrase queries. The identifier class tests the finding in Sciavolino et al., “Simple Entity-Centric Questions Challenge Dense Retrievers,” cited in lecture 12: dense retrievers lose to keyword search on rare names and strings. My numbers point the same way, but with 7 queries per class they are consistent with that finding, not a test of it.

Cormack, Clarke and Buettcher’s claim, cited in lecture 13, that reciprocal rank fusion outperforms the individual systems it fuses is left open here. hybrid’s point estimates are below bm25’s on all three scores and below dense’s on MRR@10 and nDCG@10, though none of those differences is distinguishable.

By class, hybrid lands between the two systems instead of taking the better of each. On paraphrase queries, its MRR@10 is 0.152, against dense’s 0.714. On identifier queries, its recall@10 is 0.500, against bm25’s 1.000. This also limits the reranker, which can only reorder what hybrid hands it: its identifier recall@10 of 0.643 stays well below bm25’s. My untested guess is that each system’s ranking is close to noise on the class where it fails, and RRF with k = 60 weights that noise equally with the other system’s good ranking. A weighted fusion or a smaller k would test this guess.

---

## 2. Stage 1 - cited answers on the 12 shared questions

<!-- p2:begin answers -->
| Label | System | Verified (in) | 95% interval | not_found (in) | Declined (out) | 95% interval | Quotes found |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| rerank | rerank | 8 of 8 (100%) | [0.676, 1.000] | 0 of 8 (0%) | 4 of 4 (100%) | [0.510, 1.000] | 9 of 9 |
<!-- p2:end answers -->

Which system answered, and why that one?
What did you change in `prompts/answer.txt`, if anything, and did the verified share or the declined share move?

Then read three in-corpus answers that `uv run p2 verify` passed.
For each one, open the cited chunk and say whether the quote really supports the claim next to it.
The check proves a quote is a real piece of the chunk and cannot prove that it supports the claim, so this reading is the part only you can do.

The answers come from rerank working at the chunk level. It was the only system distinguishable from the others on the practice queries, and its clearest gain was in MRR@10. MRR@10 matters most here because it measures whether the right chunk is near the top of what the answer prompt sees. I did not change `prompts/answer.txt`; it is still the lab 13 default prompt.

All 8 in-corpus questions were verified, all 4 out-of-corpus questions were declined, and all 9 quotes were found in their cited chunks. With this few questions, a perfect score is weak evidence. The intervals put the true verified share anywhere from 0.676 to 1, and the true declined share anywhere from 0.510 to 1. These results rule out a system that fails most of the time. They don’t rule out one that answers wrongly one time in three, or declines only half the time it should.

I read a01, a02 and a03 against their cited chunks.

a01 ("within how many minutes must a mine operator call MSHA after an accident that kills a miner?") is fully supported. It has two claims on the same chunk (`cfr30-50.10#0`): one quotes "within 15 minutes... once the operator knows or should know that an accident has occurred involving:", the other quotes "(a) A death of an individual at the mine;". Read alone, neither claim answers the question: the first gives the time limit but not the triggering accident, the second names the accident but not the time limit. Together, they do. `p2 verify` checks each claim's quote against its chunk, not whether the set of claims together answers the question, so this is the kind of gap that check cannot see on its own.

a02 ("what minimum incombustible content must the combined dust keep where no methane is present?") has a real problem. The claim says the incombustible content “must be not less than 80 percent, maintained throughout the top, floor, and sides of all underground areas." The cited chunk (`cfr30-75.403#0`) opens with a condition the claim drops: "Where rock dust is required to be applied, it shall be distributed... and maintained in such quantities that the incombustible content... shall be not less than 80 percent." The claim states the 80 percent rule as if it always applies, when the regulation states it only where rock dust is required to be applied. I checked that this is not a chunk boundary problem: chunk `#0` starts at the section heading, and the conditional opening is the actual first sentence of 30 CFR 75.403. So the quote is a real piece of the chunk, but the claim is broader than the law it cites.

a03 ("how long must the self-rescue device given to each underground coal miner be able to protect that person?") is fully supported. The quote states the 1-hour requirement directly, and the claim answers the question. It narrows the regulation in two small ways that do not change that answer: it drops "and to visitors authorized to enter the mine by the operator," which the question does not ask about, and it changes "device or devices" to "a device," which understates that more than one device may add up to the hour.

---

## 3. Stage 2 - your corpus and your gold set

### The corpus

What is it, where did it come from, how many documents and how many megabytes, and what is the license basis for publishing it?
Name the one or two documents you were least sure about and what you decided.
Say which of the allowed sources in the brief it comes from.

The corpus is five US Army Corps of Engineers Engineer Manuals on underground and foundation engineering: EM 1110-2-2901, *Tunnels and Shafts in Rock* (1997); EM 1110-1-2908, *Rock Foundations* (1994); EM 1110-1-1804, *Geotechnical Investigations* (2001); EM 1110-1-1905, *Bearing Capacity of Soils* (1992); and EM 1110-1-1904, *Settlement Analysis* (1990).
They were downloaded as PDFs from the USACE publications site and ingested with `p2 ingest --part-pages 4`, which splits each manual into parts of about four pages, giving 212 documents, about 316,000 words (about 442,000 estimated tokens) and 2.1 MB.
All five are works of the Department of the Army, approved for public release, so the license basis is US government public domain (`us-gov-public-domain`), which is the brief's allowed source for US federal works.

The manual I was least sure about was EM 1110-2-3506, *Grouting Technology*, and I dropped it.
`p2 license` flagged 129 of its 134 parts, mostly figure captions credited to private consulting firms and equipment makers ("Courtesy of Gannett Fleming" and similar) and reprints used with permission, so too much of it was not the government's own work to clear part by part.
I also checked EM 1110-1-1802, *Geophysical Exploration*, and rejected it before ingesting, because its methods chapters are illustrated with figures reproduced by permission of publishers and instrument makers.
In the manuals I kept, every flag was reviewed and recorded in the manifest: 58 flags in *Tunnels and Shafts in Rock* trace to one bibliography citation that ingest dropped with the reference list, and 10 flags in *Bearing Capacity* and *Settlement Analysis* are captions for borrowed figures whose images are not in the text-only corpus.
`p2 license` now reports 212 documents, 212 ok, 0 flagged.

### The gold set

How many queries, how many with origin `hand` and how many with origin `claude`, and which query classes did you use and why?
How did you decide that a document is relevant: write your relevance rule in two or three sentences, the way the brief does for the shared corpus.
How did you find candidates (the systems' top 10, a keyword search, reading), and did you read every document before you labeled it?
Your labels are binary (`rel` 1) unless you say otherwise: if you use graded labels, declare the scale here, for example 2 means the document answers the query fully and 1 means it helps.

The gold set has 37 queries: 15 with origin hand (c23–c37), written from my own tunnel-engineering questions, and 22 with origin claude (c01–c22), drafted by Claude and edited by me.
I used three query classes. cross-cutting (15: c01–c06 and c23–c31) queries ask about a term that appears in several manuals for different purposes, such as RQD, grouting or groundwater. They are the class my pre-registered hypothesis tests. identifier (10: c07–c13 and c32–c34) and paraphrase (12: c14–c22 and c35–c37) mirror the shared corpus’s classes. Several identifier queries name an equation, figure or citation directly (for example “Equation 1-4a” and “Deere 1964”), which gives bm25 an exact string to match.

Relevance rule: a document is relevant if, after reading its full text, I judged that it substantively answers the query in the setting the query asks about. A document that only shares the query’s vocabulary, or defines a term when the query asks how it is used, is not relevant. For a cross-cutting query, a passage in any manual counts if it answers for that manual’s purpose, so one query can have relevant documents in several manuals.

Candidates came from the union of the top 5 of all four systems (bm25, dense, hybrid and rerank), so no single system, including the one my hypothesis is about, shaped the pool alone. Where the pool looked weak (c04, c23 and c35), a keyword search across the corpus found further candidates. One drafted query, about permission to reuse figures, had no answer anywhere in the corpus after that search, so I dropped and replaced it. I read every candidate’s full text before labeling it. Documents outside the pool were not judged and count as not relevant, so recall@10 is measured against the relevant documents the pool found. A system is penalized when it ranks a relevant document at 6 to 10 that no system, itself included, put in its top 5, because that document was never judged and counts as not relevant. c04 (liquefaction) has only one relevant document, so its scores rest on a single label.
Labels are binary: rel 1 means relevant under the rule above.

---

## 4. Stage 2 - results on your corpus

Scores per system on your gold set.

<!-- p2:begin own -->
| System | Recall@10 | MRR@10 | nDCG@10 |
| --- | ---: | ---: | ---: |
| bm25 | 0.829 | 0.602 | 0.622 |
| dense | 0.856 | 0.710 | 0.707 |
| hybrid | 0.923 | 0.715 | 0.731 |
| rerank | 0.878 | 0.623 | 0.636 |
| ablation/dense_potion | 0.842 | 0.595 | 0.630 |

37 judged queries; nDCG uses binary labels; a random ranking of the 212 documents would get recall@10 near 0.047.
<!-- p2:end own -->

The same scores per query class.

<!-- p2:begin own-classes -->
| System | Metric | cross-cutting (n=15) | identifier (n=10) | paraphrase (n=12) |
| --- | --- | ---: | ---: | ---: |
| bm25 | Recall@10 | 0.778 | 1.000 | 0.750 |
| bm25 | MRR@10 | 0.616 | 0.798 | 0.420 |
| bm25 | nDCG@10 | 0.580 | 0.846 | 0.488 |
| dense | Recall@10 | 0.778 | 1.000 | 0.833 |
| dense | MRR@10 | 0.663 | 0.795 | 0.699 |
| dense | nDCG@10 | 0.636 | 0.845 | 0.682 |
| hybrid | Recall@10 | 0.911 | 1.000 | 0.875 |
| hybrid | MRR@10 | 0.652 | 0.850 | 0.681 |
| hybrid | nDCG@10 | 0.680 | 0.881 | 0.671 |
| rerank | Recall@10 | 0.867 | 0.900 | 0.875 |
| rerank | MRR@10 | 0.744 | 0.484 | 0.588 |
| rerank | nDCG@10 | 0.695 | 0.585 | 0.605 |
| ablation/dense_potion | Recall@10 | 0.778 | 1.000 | 0.792 |
| ablation/dense_potion | MRR@10 | 0.513 | 0.753 | 0.565 |
| ablation/dense_potion | nDCG@10 | 0.544 | 0.815 | 0.585 |
<!-- p2:end own-classes -->

The same scores for the queries you wrote yourself (`hand`) and the ones a model drafted (`claude`), with the difference between the two groups and its interval.
Once both groups have queries, the table also says whether `bm25`'s lead over `dense` differs between them, and what share of each query's content words its best relevant document contains, which is stretch option 6.

<!-- p2:begin own-origins -->
| System | Metric | hand (n=15) | claude (n=22) | hand minus claude | 95% interval | Reading |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| bm25 | Recall@10 | 0.711 | 0.909 | -0.198 | [-0.399, -0.018] | claude higher |
| bm25 | MRR@10 | 0.572 | 0.622 | -0.050 | [-0.307, +0.202] | not distinguishable |
| bm25 | nDCG@10 | 0.534 | 0.682 | -0.148 | [-0.350, +0.054] | not distinguishable |
| dense | Recall@10 | 0.778 | 0.909 | -0.131 | [-0.320, +0.048] | not distinguishable |
| dense | MRR@10 | 0.590 | 0.792 | -0.202 | [-0.448, +0.048] | not distinguishable |
| dense | nDCG@10 | 0.600 | 0.780 | -0.180 | [-0.382, +0.026] | not distinguishable |
| hybrid | Recall@10 | 0.878 | 0.955 | -0.077 | [-0.199, +0.036] | not distinguishable |
| hybrid | MRR@10 | 0.667 | 0.748 | -0.081 | [-0.292, +0.128] | not distinguishable |
| hybrid | nDCG@10 | 0.679 | 0.767 | -0.087 | [-0.237, +0.059] | not distinguishable |
| rerank | Recall@10 | 0.833 | 0.909 | -0.076 | [-0.288, +0.092] | not distinguishable |
| rerank | MRR@10 | 0.678 | 0.586 | +0.091 | [-0.153, +0.329] | not distinguishable |
| rerank | nDCG@10 | 0.648 | 0.628 | +0.019 | [-0.176, +0.205] | not distinguishable |
| ablation/dense_potion | Recall@10 | 0.744 | 0.909 | -0.165 | [-0.376, +0.015] | not distinguishable |
| ablation/dense_potion | MRR@10 | 0.519 | 0.647 | -0.128 | [-0.362, +0.103] | not distinguishable |
| ablation/dense_potion | nDCG@10 | 0.561 | 0.677 | -0.116 | [-0.326, +0.087] | not distinguishable |

The hand and claude queries are different queries, so the interval of hand minus claude comes from resampling the queries within each group (10,000 times), not from pairing them.

Do model-written queries favor keyword search? bm25's lead over dense (bm25 minus dense, per query) on the claude queries and on the hand queries, and claude minus hand:

| Metric | Lead on claude | Lead on hand | Claude minus hand | 95% interval | Reading |
| --- | ---: | ---: | ---: | ---: | --- |
| Recall@10 | +0.000 | -0.067 | +0.067 | [-0.159, +0.279] | not distinguishable |
| MRR@10 | -0.170 | -0.018 | -0.152 | [-0.511, +0.213] | not distinguishable |
| nDCG@10 | -0.098 | -0.066 | -0.032 | [-0.301, +0.227] | not distinguishable |

Mean content-word overlap, the share of a query's content words found in its best relevant document: hand 0.74 (15 queries), claude 0.69 (22 queries).

Stretch option 6 asks for at least 20 judged queries of each origin; here there are 15 hand and 22 claude.
<!-- p2:end own-origins -->

Differences between every pair of systems.

<!-- p2:begin own-pairs -->
| Comparison | Metric | Mean difference | 95% interval | MDD | Reading |
| --- | --- | ---: | ---: | ---: | --- |
| dense minus bm25 | Recall@10 | +0.027 | [-0.081, +0.122] | 0.153 | not distinguishable |
| dense minus bm25 | MRR@10 | +0.109 | [-0.073, +0.282] | 0.257 | not distinguishable |
| dense minus bm25 | nDCG@10 | +0.085 | [-0.050, +0.214] | 0.191 | not distinguishable |
| hybrid minus bm25 | Recall@10 | +0.095 | [+0.027, +0.176] | 0.106 | hybrid higher |
| hybrid minus bm25 | MRR@10 | +0.113 | [-0.007, +0.231] | 0.173 | not distinguishable |
| hybrid minus bm25 | nDCG@10 | +0.109 | [+0.033, +0.181] | 0.107 | hybrid higher |
| hybrid minus dense | Recall@10 | +0.068 | [-0.027, +0.176] | 0.145 | not distinguishable |
| hybrid minus dense | MRR@10 | +0.005 | [-0.093, +0.100] | 0.141 | not distinguishable |
| hybrid minus dense | nDCG@10 | +0.024 | [-0.052, +0.101] | 0.112 | not distinguishable |
| rerank minus bm25 | Recall@10 | +0.050 | [-0.072, +0.167] | 0.176 | not distinguishable |
| rerank minus bm25 | MRR@10 | +0.022 | [-0.165, +0.205] | 0.270 | not distinguishable |
| rerank minus bm25 | nDCG@10 | +0.014 | [-0.135, +0.154] | 0.210 | not distinguishable |
| rerank minus dense | Recall@10 | +0.023 | [-0.108, +0.149] | 0.186 | not distinguishable |
| rerank minus dense | MRR@10 | -0.087 | [-0.265, +0.088] | 0.259 | not distinguishable |
| rerank minus dense | nDCG@10 | -0.071 | [-0.221, +0.080] | 0.220 | not distinguishable |
| rerank minus hybrid | Recall@10 | -0.045 | [-0.149, +0.050] | 0.144 | not distinguishable |
| rerank minus hybrid | MRR@10 | -0.091 | [-0.269, +0.083] | 0.258 | not distinguishable |
| rerank minus hybrid | nDCG@10 | -0.095 | [-0.227, +0.028] | 0.187 | not distinguishable |
| ablation/dense_potion minus bm25 | Recall@10 | +0.014 | [-0.041, +0.068] | 0.086 | not distinguishable |
| ablation/dense_potion minus bm25 | MRR@10 | -0.007 | [-0.166, +0.149] | 0.227 | not distinguishable |
| ablation/dense_potion minus bm25 | nDCG@10 | +0.008 | [-0.101, +0.114] | 0.156 | not distinguishable |
| ablation/dense_potion minus dense | Recall@10 | -0.014 | [-0.122, +0.108] | 0.158 | not distinguishable |
| ablation/dense_potion minus dense | MRR@10 | -0.115 | [-0.223, -0.004] | 0.157 | dense higher |
| ablation/dense_potion minus dense | nDCG@10 | -0.077 | [-0.161, +0.016] | 0.128 | not distinguishable |
| ablation/dense_potion minus hybrid | Recall@10 | -0.081 | [-0.149, -0.027] | 0.086 | hybrid higher |
| ablation/dense_potion minus hybrid | MRR@10 | -0.120 | [-0.237, +0.003] | 0.175 | not distinguishable |
| ablation/dense_potion minus hybrid | nDCG@10 | -0.101 | [-0.180, -0.018] | 0.117 | hybrid higher |
| ablation/dense_potion minus rerank | Recall@10 | -0.036 | [-0.162, +0.095] | 0.181 | not distinguishable |
| ablation/dense_potion minus rerank | MRR@10 | -0.029 | [-0.179, +0.134] | 0.229 | not distinguishable |
| ablation/dense_potion minus rerank | nDCG@10 | -0.006 | [-0.131, +0.129] | 0.190 | not distinguishable |

The interval is a paired bootstrap (10,000 resamples of the queries); MDD is the smallest difference this many queries detect 80% of the time.
<!-- p2:end own-pairs -->

Which differences are distinguishable and which are not, at your gold-set size?
Do the `hand` queries and the `claude` queries tell the same story?
Did your prediction in `DECISIONS.md` prompt 1 hold?

On 37 queries, one pair is distinguishable: hybrid is higher than bm25 on recall@10 (+0.095, [+0.027, +0.176]) and nDCG@10 (+0.109, [+0.033, +0.181]). Its MRR@10 gain (+0.113, [−0.007, +0.231]) is not distinguishable, though the interval only just reaches zero. Both detected gains sit at about their minimum detectable difference (0.106 and 0.107), so their size is rough.

Every other difference is not distinguishable. rerank separates from no system on any score. Its point estimates are below hybrid on all three scores and below dense on MRR@10 and nDCG@10, but none of those intervals excludes zero. The minimum detectable differences run from 0.106 to 0.270, so on MRR@10 a gap of about 0.25 between rerank and any other system could go unseen. Because the pool took only each system’s top 5, these scores also carry a bias against systems whose ranks 6 to 10 hold documents the pool never covered, and rerank, whose 6 to 10 slots can hold documents promoted from hybrid’s ranks 11 to 20, is the system most exposed to it. I did not measure this; counting each system’s unjudged top-10 documents would. Here rerank cost about 15,170 input tokens and 10.2 seconds per query, against under 10 milliseconds for the other three, for no distinguishable gain.

The per-class table has 10 to 15 queries per class and no intervals, so I read it descriptively. rerank’s overall deficit comes almost entirely from identifier queries. There its MRR@10 is 0.484 against hybrid’s 0.850, and its nDCG@10 is 0.585 against 0.881. On cross-cutting queries, the class my pre-registered hypothesis is about, rerank has the highest MRR@10 (0.744) and nDCG@10 (0.695, against hybrid’s 0.680). One reading is that the reranker demotes exact-identifier matches that the first stage had already placed at the top, while helping slightly where the query needs a passage’s purpose read. One confirmed factor may matter here: `rerank.py` sends Claude only the first 600 characters of each candidate, about 7 percent of a four-page part, so a fact past a document’s opening is invisible to it when reordering. Pooling does not explain the identifier drop: bm25, dense and hybrid all reach recall@10 of 1.000 on identifier queries, so every relevant identifier document was judged, and rerank’s 0.900 there comes from moving judged relevant documents below rank 10. Because rerank only reorders hybrid’s top 20, it cannot find a document hybrid missed. When hybrid already ranks the right document first, reordering can only keep it there or move it down. The cross-cutting gap is far too small to claim with 15 queries.

The hand and claude queries mostly tell the same story. The only distinguishable origin difference is bm25’s recall@10, which is higher on claude queries (hand minus claude −0.198, [−0.399, −0.018]). The table that asks directly whether drafted queries favor keyword search finds no distinguishable difference in bm25’s lead over dense between the two origins on any score. Drafted queries echoing the documents’ wording would not explain the recall gap either, since hand queries share more content words with their best relevant document (0.74) than claude queries do (0.69). A likelier explanation is the class mix: 7 of the 10 identifier queries are claude queries, while 9 of the 15 hand queries are cross-cutting, so the origin comparison is partly a class comparison. I did not test this.

---

## 5. The ablation

Change one thing and keep everything else the same.
Write your hypothesis here before you run it, in one sentence with a direction: "I expect X to raise MRR@10 on my corpus because Y."
The run file for it lives in `runs/own/ablation/`.

I swap dense's embedding model from bge-small-en-v1.5 to potion-retrieval-32M (`dense_potion`, varies `dense`). This tests the claim I made for choosing bge in section 1: that its contextual encoding, not just the paraphrase class, is what dense's score depends on. I chose it over a tokenizer or reranker-candidate-count ablation because it is free (dense makes no Claude calls), and because a variant and its base usually agree on most queries, giving a smaller spread of per-query differences than a comparison between two different systems, so a real effect has a better chance of being detectable at this gold-set size.

I expect dense_potion to score lower than dense on nDCG@10, mostly on paraphrase and cross-cutting queries, because potion gives every word one fixed vector regardless of its sentence, so it cannot match everyday wording to the manuals' technical terms or tell RQD used for foundation design from RQD used for tunnel excavation.

<!-- p2:begin own-ablation -->
| Comparison | Metric | Mean difference | 95% interval | MDD | Reading |
| --- | --- | ---: | ---: | ---: | --- |
| ablation/dense_potion minus bm25 | Recall@10 | +0.014 | [-0.041, +0.068] | 0.086 | not distinguishable |
| ablation/dense_potion minus bm25 | MRR@10 | -0.007 | [-0.166, +0.149] | 0.227 | not distinguishable |
| ablation/dense_potion minus bm25 | nDCG@10 | +0.008 | [-0.101, +0.114] | 0.156 | not distinguishable |
| ablation/dense_potion minus dense | Recall@10 | -0.014 | [-0.122, +0.108] | 0.158 | not distinguishable |
| ablation/dense_potion minus dense | MRR@10 | -0.115 | [-0.223, -0.004] | 0.157 | dense higher |
| ablation/dense_potion minus dense | nDCG@10 | -0.077 | [-0.161, +0.016] | 0.128 | not distinguishable |
| ablation/dense_potion minus hybrid | Recall@10 | -0.081 | [-0.149, -0.027] | 0.086 | hybrid higher |
| ablation/dense_potion minus hybrid | MRR@10 | -0.120 | [-0.237, +0.003] | 0.175 | not distinguishable |
| ablation/dense_potion minus hybrid | nDCG@10 | -0.101 | [-0.180, -0.018] | 0.117 | hybrid higher |
| ablation/dense_potion minus rerank | Recall@10 | -0.036 | [-0.162, +0.095] | 0.181 | not distinguishable |
| ablation/dense_potion minus rerank | MRR@10 | -0.029 | [-0.179, +0.134] | 0.229 | not distinguishable |
| ablation/dense_potion minus rerank | nDCG@10 | -0.006 | [-0.131, +0.129] | 0.190 | not distinguishable |

The interval is a paired bootstrap (10,000 resamples of the queries); MDD is the smallest difference this many queries detect 80% of the time.
<!-- p2:end own-ablation -->

The queries your ablation helped and hurt, against the system it varies, by reciprocal rank.
`p2 score` finds that system from a line such as `BASE = "bm25"` in your variant's file, or else from its name: `bm25_lab` varies `bm25`.

<!-- p2:begin own-ablation-queries -->
ablation/dense_potion against dense (BASE = "dense" in p2/retrievers/dense_potion.py): it helped 7 queries, hurt 14 and left 16 unchanged.

| Query | Class | Origin | dense RR | ablation/dense_potion RR | Change | Effect |
| --- | --- | --- | ---: | ---: | ---: | --- |
| c26 | cross-cutting | hand | 0.000 | 1.000 | +1.000 | helped |
| c03 | cross-cutting | claude | 0.000 | 0.250 | +0.250 | helped |
| c18 | paraphrase | claude | 0.250 | 0.500 | +0.250 | helped |
| c25 | cross-cutting | hand | 0.167 | 0.333 | +0.167 | helped |
| c32 | identifier | hand | 0.200 | 0.333 | +0.133 | helped |
| c20 | paraphrase | claude | 0.100 | 0.167 | +0.067 | helped |
| c24 | cross-cutting | hand | 0.200 | 0.250 | +0.050 | helped |
| c23 | cross-cutting | hand | 1.000 | 0.167 | -0.833 | hurt |
| c04 | cross-cutting | claude | 1.000 | 0.250 | -0.750 | hurt |
| c05 | cross-cutting | claude | 1.000 | 0.250 | -0.750 | hurt |
| c02 | cross-cutting | claude | 1.000 | 0.500 | -0.500 | hurt |
| c13 | identifier | claude | 1.000 | 0.500 | -0.500 | hurt |
| c19 | paraphrase | claude | 1.000 | 0.500 | -0.500 | hurt |
| c22 | paraphrase | claude | 1.000 | 0.500 | -0.500 | hurt |
| c30 | cross-cutting | hand | 1.000 | 0.500 | -0.500 | hurt |
| c36 | paraphrase | hand | 1.000 | 0.500 | -0.500 | hurt |
| c29 | cross-cutting | hand | 0.333 | 0.000 | -0.333 | hurt |
| c16 | paraphrase | claude | 0.333 | 0.111 | -0.222 | hurt |
| c35 | paraphrase | hand | 0.200 | 0.000 | -0.200 | hurt |
| c12 | identifier | claude | 0.250 | 0.200 | -0.050 | hurt |
| c27 | cross-cutting | hand | 0.250 | 0.200 | -0.050 | hurt |

RR is the reciprocal rank of the first relevant document in the top 10 (0 when none is there), the per-query value behind MRR@10; the queries at the top of each list are the ones to read.
<!-- p2:end own-ablation-queries -->

What did you change, what happened, and does the interval support the claim you want to make?
If the result is not distinguishable, say what size of effect your gold set could have seen.
Read the queries at the top of each list in the second table, and say whether your change explains them.

On the metric I chose in advance, the result is not distinguishable. dense_potion minus dense on nDCG@10 is −0.077, with interval [−0.161, +0.016]. The point estimate goes the way I predicted, but the interval includes zero, so this gold set cannot tell the two models apart on nDCG@10. With an MDD of 0.128, it could reliably have seen a drop of about 0.13 or more, so a smaller real drop would be invisible here.

On MRR@10 the drop is distinguishable: −0.115, with interval [−0.223, −0.004]. I did not choose MRR@10 in advance, so I report it as a secondary result rather than as support for the hypothesis. The interval also only just clears zero, and the point estimate is below the MDD of 0.157, so its size is rough.

The variant's spread was smaller than for pairs of different systems, as I expected. The nDCG@10 MDD of 0.128 compares with 0.191 for dense minus bm25, so the paired design bought some power.

The per-class scores, read descriptively, point the way the hypothesis predicts. dense_potion loses most on paraphrase queries (nDCG@10 0.682 to 0.585) and cross-cutting queries (0.636 to 0.544), and least on identifier queries (0.845 to 0.815), where exact terms do the work for either model.

By reciprocal rank, the swap hurt 14 queries, helped 7 and left 16 unchanged. The hurt list leads with cross-cutting queries. In c23, c04 and c05, dense ranked a relevant document first and dense_potion ranked it fourth to sixth. c02, which asks how RQD is used differently for foundations and for tunnel excavation, the exact case my hypothesis names, fell from rank 1 to rank 2. Overall, 7 of the 14 hurt queries are cross-cutting and 5 are paraphrase. c04 rests on a single relevant document, so its swing is one label. Reading the three by hand splits the hurt list two ways. In c23, four of dense_potion's five wrong top candidates mention groundwater, dewatering or hydraulic controls, the same term used for a different purpose, which is what the hypothesis predicts. c05's relevant document is a glossary entry defining grouting's several senses, including both tunnel-lining and foundation-treatment uses; dense_potion's three wrong top candidates are substantive grouting sections (test-grouting procedures, shaft-sinking ground improvement) that share the term "grout" (39 to 68 mentions each) without matching the role comparison the query asks for, the same mechanism as c23. In c04, none of the wrong top candidates mention liquefaction at all; the drop there is topical drift toward other short, similarly worded sections of the same manuals, with no shared vocabulary, not the mechanism I named. So of the three, c23 and c05 test the hypothesis; c04 does not.

The helped list is not what the hypothesis predicts. The biggest gain is c26, a cross-cutting query where dense found nothing relevant in its top 10 and dense_potion ranked a relevant document first. That document is titled "Core Logging" and is dense with the query's own words, logging, core, description, investigation. A static model, closer to keyword averaging than a contextual one, may reward that direct lexical overlap, while dense's contextual reading pulled it toward structurally similar chapter-opening passages (scope and purpose statements from the same two manuals) that never use those words together. If so, this is a case where context-sensitivity cost dense a query, the opposite of what I predicted.

So the claim the intervals support is narrow. Swapping to a static model lowered the rank of the first relevant document (MRR@10, a secondary metric), and the pre-chosen nDCG@10 drop is not distinguishable. The class pattern and the hurt list are consistent with the reason I gave for choosing bge, but they do not test it, and reading the actual queries shows the mechanism holding for two of three hurt cross-cutting queries (c23, c05), failing for the third (c04), and failing for the clearest helped one. dense_potion was also about eight times faster per query (0.8 ms against 6.6 ms), a saving this gold set cannot weigh against a drop smaller than 0.13.

---

## 6. Failure analysis

Pick the queries where your best system on your own corpus failed: the relevant document is missing from the top 10, or sits far below the top.
Take at least five, and read what the system returned next to what was relevant.
Then sort the failures by cause, for example a vocabulary mismatch, near-duplicate documents, a chunk that cut the answer in half, a query that is ambiguous, or a label that was wrong, because sometimes the gold set is what failed.

The best system on my corpus is hybrid (nDCG@10 0.731, recall@10 0.923). It rarely misses a relevant document entirely, so these are its worst cases: queries where the first relevant document sits at rank 3 or lower, or where one relevant document is missing from the top 10.

| qid | what the best system returned | what was relevant | cause | what you would try |
|---|---|---|---|---|
| c27 | ranks 1-5: a swell-potential table, an exploration-strategy passage, a discontinuity-definitions passage, and two manual intros | tunnels-shafts-rock__p113-116 (rank 6), rock-foundations__p109-112 (rank 8) | vocabulary mismatch: generic rock-description and exploration-strategy chunks share surface words (rock, discontinuity) without the specific weathered-rock-and-design content | weight passages whose section heading shares more query terms, or chunk by section so a "design considerations" subsection isn't diluted by its neighbors |
| c03 | rank 1: a general passage defining consolidation settlement | settlement-analysis__p077-080 (rank 5), the actual dam-vs-footing comparison | a general-definition chunk states the query's key term directly, outranking the specific comparison passage, which uses different concrete vocabulary (FD31, CSANDSET, embankment) | for comparison queries, weight passages that name both compared items, or add a synonym map (embankment ~ dam) |
| c26 | ranks 1-3: a pointer to another manual and two geotechnical-investigations chapter openers | geotechnical-investigations__p065-068, the Core Logging section (rank 4) | chapter-opening and scope-statement boilerplate shares manual-level framing without the chapter's specific content; my reading of the ablation suggested the same mechanism behind dense_potion's win on this query | down-weight or separately classify recurring "purpose and scope" boilerplate, which adds little retrieval signal |
| c18 | ranks 1-3: unrelated TBM and swelling passages, before rock-foundations__p069-072 at rank 4; tunnels-shafts-rock__p217-220, which also fully defines both rock bolt and rock dowel, sits at rank 6 | rock-foundations__p069-072 (the only document judged relevant) | two problems: the first three results are unrelated TBM and swelling passages, a retrieval failure, and the gold set is incomplete, since p217-220 also answers the query but was never judged, so hybrid gets no credit for ranking it 6th | find out why the TBM and swelling passages outrank a direct definition; add p217-220 to c18's qrels in a re-scored version |
| c35 | ranks 1-3: unrelated pipe-infiltration and joint-orientation passages, before tunnels-shafts-rock__p117-120 at rank 4; the other relevant document never appears in the top 10 | tunnels-shafts-rock__p157-160 (missing), p117-120 (rank 4) | vocabulary mismatch: p157-160's register ("convergence-confinement," "ground relaxation") shares almost no words with the plain-language query | write a hand paraphrase using the convergence-confinement vocabulary and check whether recall improves, which would confirm the mismatch rather than a real absence |
| c01 | rank 1: the Core Logging section, which only mentions RQD in passing; rank 2: rock-foundations__p021-024, the Deere 1964 RQD definition | tunnels-shafts-rock__p037-040 (rank 4), geotechnical-investigations__p069-072 (rank 3) | the same label gap as c18: p021-024 answers this query as directly as the judged documents, but was never added, because the RQD definition appears in more than one manual and not every copy was labeled | add p021-024 to c01's qrels; audit the other "define X" queries for the same gap |

Four of the six failures (c27, c03, c26, c35) share one mechanism: a passage with generic, chapter-level, or differently worded content outranks the specific answer, because both halves of hybrid reward surface similarity, shared words for bm25 and similar framing for dense, rather than whether the passage actually answers the query. The other two (c18, c01) also show a gap in the gold set itself. In both, the same fact appears in more than one place in the corpus, once in its own section and once in a later section or a sibling manual, and only one copy was judged, so a system that finds the unjudged copy gets no credit for it. I have not changed qrels.txt, because that would rescore every table and change the pre-registered result. Any score that depends on these two queries should be read with that gap in mind.

---

## 7. Cross-corpus comparison

The two tables to compare are the shared-corpus scores in section 1 and your own-corpus scores in section 4, with their intervals.
If you want them side by side, copy the rows you need into a table here and say that you copied them.

Did the winner change between the shared corpus and yours?
Why, or why not: what is different about the two collections (document length, vocabulary, identifiers, near-duplicates, how the queries were written), and which of your explanations did you test and which are guesses?
Say what 20 queries on one side and your gold-set size on the other cannot support.

I copied these rows from the shared-practice table in section 1 and the own table in section 4.

| System | Shared MRR@10 (n=20) | Shared nDCG@10 | Own MRR@10 (n=37) | Own nDCG@10 |
| --- | ---: | ---: | ---: | ---: |
| bm25 | 0.507 | 0.518 | 0.602 | 0.622 |
| dense | 0.562 | 0.480 | 0.710 | 0.707 |
| hybrid | 0.471 | 0.443 | 0.715 | 0.731 |
| rerank | 0.800 | 0.746 | 0.623 | 0.636 |

The winner changed, though how far depends on what "winner" means here. On the shared practice queries, rerank was the only system distinguishable from any other: higher than dense and hybrid on all three scores, and higher than bm25 on MRR@10. On my corpus, the only distinguishable pair is hybrid over bm25, on recall@10 and nDCG@10. hybrid has the highest point estimates, but it is not distinguishable from dense or rerank, so I can say the reranker's clear lead disappeared and hybrid moved from last to first by point estimate, but not that hybrid beats every other system here.

The clearest difference between the collections shows up in the per-class tables. On the shared corpus, bm25 and dense failed on complementary classes: bm25 had recall@10 of 1.000 on identifier queries and 0.000 on paraphrase queries, while dense had 0.214 and 0.595. On my corpus, neither system fails a whole class. bm25 reaches 0.750 recall@10 on paraphrase queries, and both reach 1.000 on identifier queries. That fits the guess in section 1 that RRF suffers when one input's ranking is close to noise for a class: on the shared corpus, hybrid landed between its two inputs, and on mine, where both inputs are usable everywhere, it is the one system distinguishable from bm25. The manuals' explanatory prose may share more everyday words with plain-language queries than regulation text does, which would explain why bm25 holds up on paraphrases here. I did not test either explanation; a fusion with a smaller k or weighted inputs, run on both corpora, would test the first.

The reranker’s collapse has one confirmed factor and no tested explanation. `rerank.py` truncates each candidate’s text to `PASSAGE_CHARS = 600` before sending it to Claude. My documents are four-page parts of about 1,500 words, roughly 8,500 characters, so Claude sees only about 7 percent of each one, essentially its heading and first paragraph. The same code ran on the shared corpus, so if CFR sections are much shorter than my parts, Claude saw far more of each shared document; I did not measure their length. If the answer to a query sits past the opening of a part, Claude cannot see it when reordering, which would explain the identifier drop (MRR@10 0.484 against hybrid’s 0.850), where it moved judged relevant documents down. I did not test this; rerunning rerank with a larger `PASSAGE_CHARS` on my corpus would. The query classes also differ: my cross-cutting class has no equivalent on the shared corpus, and that is the one class where rerank has the highest point estimates on my corpus.

The failure analysis and the ablation add one observation that applies to my corpus only. Both found generic chapter openings and scope statements outranking the specific answer (c26 in both, plus c27 and c03 in the failure analysis). Each manual has many such passages, and my four-page parts often contain one. I did not look for the same pattern on the shared corpus, so I cannot say whether it explains part of the difference.

What the gold sets cannot support: the two corpora have different queries and different documents, so no paired interval compares them, and nothing here measures whether the reranker's gain really shrank between corpora rather than varying with the queries. Within each corpus, 20 practice queries give minimum detectable differences of 0.160 to 0.415, and my 37 give 0.106 to 0.270, so most gaps on either side are invisible. Per-class comparisons rest on 6 to 15 queries with no intervals. Every explanation in this section is a guess consistent with the numbers, not a tested claim.

---

## 8. Stretch

498E: the stretch is one of the six options in the brief's "One stretch" section, and that section says what earns the 25 points for each.
It is optional, so `uv run p2 check --final` never waits on this section.
598E: the rider is your stretch, so write "rider" below and put its results in section 9; the other options add no points, because the project is capped at 150.

Whichever option you chose, write these five things:

1. The option's name.
2. What you did, and the files that hold it.
3. The table `p2 score` wrote for it, by name: one of the three below, `own-ablation` and `own-ablation-queries` in section 5 for a second ablation, `own-origins` in section 4 for the hand and claude queries, or `repeats` in section 9 for the rider.
4. What its interval lets you claim, and what it does not.
5. One thing you would do next, and what result would tell you it worked.

For a second ablation, write its hypothesis here before you run it, and commit it, so your history shows that it came first.
For the hand and claude queries, do the same with your prediction before you score.

### Claim-level faithfulness check (option 2)

Claude's verdicts from `p2 judge` against your own verdicts in the calibration file.

<!-- p2:begin stretch-judge -->
_No judged answers yet (stretch option 2): `uv run p2 judge answers/shared/LABEL.json` writes them, your own verdicts go in answers/shared/LABEL.calibration.tsv, and then `uv run p2 score` fills this table._
<!-- p2:end stretch-judge -->

### Cost and latency (option 3)

The Claude calls, tokens and seconds in every trace you committed, and what a cheaper system or answers file saves against what it loses.

<!-- p2:begin stretch-cost -->
Every trace in traces/ that records a Claude call:

| Trace | System | Spans | Claude calls | Saved | Input tokens | Output tokens | Seconds | Input per span | Output per span | Seconds per span |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| traces/answers-rerank.jsonl | rerank | 12 | 24 | 0 | 229,273 | 9,624 | 134.7 | 19,106 | 802 | 11.2 |
| traces/answers-rerank.r1.jsonl | rerank | 12 | 24 | 0 | 206,522 | 9,619 | 138.4 | 17,210 | 802 | 11.5 |
| traces/answers-rerank.r2.jsonl | rerank | 12 | 24 | 0 | 204,858 | 10,393 | 146.0 | 17,072 | 866 | 12.2 |
| traces/answers-rerank.r3.jsonl | rerank | 12 | 24 | 0 | 213,245 | 9,504 | 140.1 | 17,770 | 792 | 11.7 |
| traces/own-own-rerank.jsonl | rerank | 37 | 37 | 36 | 561,273 | 29,280 | 376.7 | 15,170 | 791 | 10.2 |
| traces/shared-practice-rerank.jsonl | rerank | 20 | 20 | 20 | 286,944 | 9,111 | 142.0 | 14,347 | 456 | 7.1 |
| traces/shared-practice-rerank.r1.jsonl | rerank | 20 | 20 | 0 | 298,359 | 6,787 | 111.4 | 14,918 | 339 | 5.6 |
| traces/shared-practice-rerank.r2.jsonl | rerank | 20 | 20 | 0 | 287,799 | 7,286 | 113.6 | 14,390 | 364 | 5.7 |
| traces/shared-practice-rerank.r3.jsonl | rerank | 20 | 20 | 0 | 298,191 | 6,530 | 103.4 | 14,910 | 326 | 5.2 |
| traces/shared-test-rerank.jsonl | rerank | 40 | 40 | 40 | 648,150 | 19,162 | 300.1 | 16,204 | 479 | 7.5 |

A span is one query of a run, one question of an answers file, or one claim of a judged file. A saved reply costs nothing now, so it counts the tokens and the seconds of the call that made it.

Every pair of systems on the same queries where at least one calls Claude, the one with fewer Claude input tokens per query first:

| Cheaper minus dearer | Queries | MRR@10 difference | 95% interval | Input tokens saved per query | Seconds saved per query | Reading |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| shared practice: bm25 minus rerank | 20 | -0.293 | [-0.533, -0.043] | 14,347 | 7.1 | rerank higher |
| shared practice: dense minus rerank | 20 | -0.237 | [-0.408, -0.083] | 14,347 | 7.1 | rerank higher |
| shared practice: hybrid minus rerank | 20 | -0.329 | [-0.504, -0.164] | 14,347 | 7.1 | rerank higher |
| own: bm25 minus rerank | 37 | -0.022 | [-0.205, +0.165] | 15,170 | 10.2 | not distinguishable |
| own: dense minus rerank | 37 | +0.087 | [-0.088, +0.265] | 15,170 | 10.2 | not distinguishable |
| own: hybrid minus rerank | 37 | +0.091 | [-0.083, +0.269] | 15,170 | 10.2 | not distinguishable |

The difference is the cheaper system's score minus the dearer one's, with its paired interval; the savings count Claude calls only, so a system that makes none saves all of the other's.

Systems that do not call Claude, from traces/retrieval/ on the machine that last ran `p2 score` (git ignores that folder, so `p2 check` does not compare this part):

| Trace | System | Queries | Seconds | Milliseconds per query |
| --- | --- | ---: | ---: | ---: |
| traces/retrieval/own-own-ablation-dense_potion.jsonl | dense_potion | 37 | 0.03 | 0.8 |
| traces/retrieval/own-own-bm25.jsonl | bm25 | 37 | 0.03 | 0.7 |
| traces/retrieval/own-own-dense.jsonl | dense | 37 | 0.24 | 6.6 |
| traces/retrieval/own-own-hybrid.jsonl | hybrid | 37 | 0.30 | 8.1 |
| traces/retrieval/shared-practice-bm25.jsonl | bm25 | 20 | 0.05 | 2.3 |
| traces/retrieval/shared-practice-dense.jsonl | dense | 20 | 0.21 | 10.7 |
| traces/retrieval/shared-practice-hybrid.jsonl | hybrid | 20 | 0.29 | 14.5 |
| traces/retrieval/shared-test-bm25.jsonl | bm25 | 40 | 0.07 | 1.9 |
| traces/retrieval/shared-test-dense.jsonl | dense | 40 | 0.32 | 8.0 |
| traces/retrieval/shared-test-hybrid.jsonl | hybrid | 40 | 0.41 | 10.4 |
<!-- p2:end stretch-cost -->

### The grep agent (option 5)

Your stretch run on some of your own queries against the four systems on the same queries.

<!-- p2:begin stretch-agent -->
_No stretch runs yet (stretch option 5): `uv run p2 run --corpus own --queries eval/own/agent.queries.tsv --system agent --stretch` writes one to runs/own/stretch/, then `uv run p2 score` fills this table._
<!-- p2:end stretch-agent -->

### Your stretch

Write the five things here.

1. Option: rider (598E).
2. What I did and the files: I pre-registered a claim about my own corpus in PREREG.md, committed at e07a373 before the first judgment in eval/own/qrels.txt, then built and judged the gold set (eval/own/queries.tsv, eval/own/qrels.txt) and scored it. I ran the reranker three times on the shared practice queries (runs/shared/rerank.practice.r1.trec to .r3.trec) and generated three answers files (answers/shared/rerank.r1.json to .r3.json), with three records in r3 regenerated after a session-limit error.
3. Tables: repeats in section 9 for the repeated runs, and the rerank minus hybrid nDCG@10 row of own-pairs in section 4 for the pre-registered test.
4. What the intervals let me claim: on the 20 shared practice queries, the reranker’s gain over hybrid reproduces across three runs, with a spread of at most 0.006 against gains of 0.14 to 0.33. The answers were identical in all three files, but the Wilson intervals on 8 and 4 questions stay wide. The pre-registered own-corpus test is inconclusive, not a well-powered null: its interval [−0.227, +0.028] rules out a reranker gain as large as 0.15, but not a hybrid advantage that large.
5. Next: build a gold set of about 60 queries with cross-cutting queries as the majority, pool each system’s top 10, and rerun rerank with passages long enough to hold each document’s content. If the rerank minus hybrid interval on nDCG@10 then lies entirely above zero, the hypothesis is supported; if both ends fall inside ±0.15, a difference that large is ruled out.

---

## 9. 598E only - repeats and the pre-registered claim

498E students can leave this section as it is; nothing checks it.
598E students replace each line that starts with "598E: write", and `uv run p2 check --final` counts those lines as work still to do until they are gone.

### Repeats on the shared corpus

Three runs of the reranker on the practice queries, and three answers files, with their run-to-run spread and Wilson intervals.

<!-- p2:begin repeats -->
Repeated runs of rerank on shared/practice:

| Run | Recall@10 | MRR@10 | nDCG@10 |
| --- | ---: | ---: | ---: |
| rerank.r1 | 0.733 | 0.800 | 0.746 |
| rerank.r2 | 0.733 | 0.800 | 0.739 |
| rerank.r3 | 0.733 | 0.800 | 0.742 |
| range (max minus min) | 0.000 | 0.000 | 0.006 |

| Comparison | Metric | Mean difference | 95% interval | Reading |
| --- | --- | ---: | ---: | --- |
| rerank.r1 minus hybrid | Recall@10 | +0.142 | [+0.050, +0.258] | rerank.r1 higher |
| rerank.r2 minus hybrid | Recall@10 | +0.142 | [+0.050, +0.258] | rerank.r2 higher |
| rerank.r3 minus hybrid | Recall@10 | +0.142 | [+0.050, +0.258] | rerank.r3 higher |
| rerank.r1 minus hybrid | MRR@10 | +0.329 | [+0.164, +0.504] | rerank.r1 higher |
| rerank.r2 minus hybrid | MRR@10 | +0.329 | [+0.164, +0.504] | rerank.r2 higher |
| rerank.r3 minus hybrid | MRR@10 | +0.329 | [+0.164, +0.504] | rerank.r3 higher |
| rerank.r1 minus hybrid | nDCG@10 | +0.302 | [+0.173, +0.436] | rerank.r1 higher |
| rerank.r2 minus hybrid | nDCG@10 | +0.296 | [+0.167, +0.430] | rerank.r2 higher |
| rerank.r3 minus hybrid | nDCG@10 | +0.298 | [+0.170, +0.430] | rerank.r3 higher |

Repeated answers shared/rerank:

| File | Verified (in) | 95% interval | Declined (out) | 95% interval |
| --- | ---: | ---: | ---: | ---: |
| rerank.r1 | 8 of 8 (100%) | [0.676, 1.000] | 4 of 4 (100%) | [0.510, 1.000] |
| rerank.r2 | 8 of 8 (100%) | [0.676, 1.000] | 4 of 4 (100%) | [0.510, 1.000] |
| rerank.r3 | 8 of 8 (100%) | [0.676, 1.000] | 4 of 4 (100%) | [0.510, 1.000] |
| range (max minus min) | 0.000 |  | 0.000 |  |

Each repeat answers the same questions, so the repeats are not independent trials and their counts are not pooled into one interval.
<!-- p2:end repeats -->

Does the reranker's gain over its first stage survive the run-to-run variation?
Write what the spread is, how it compares with the gain, and what the Wilson intervals on the verified share and the declined share say about 8 and 4 questions.

The reranker’s gain over its first stage, hybrid, survives the run-to-run variation on the practice queries. I ran rerank three times with fresh Claude calls and no saved replies (runs/shared/rerank.practice.r1.trec to .r3.trec). Recall@10 (0.733) and MRR@10 (0.800) were identical in all three runs. The only score that varied, nDCG@10, moved by 0.006, about 2 percent of its gain over hybrid (+0.296 to +0.302 across the repeats). In every repeat, the interval against hybrid clears zero on all three scores, as in the original run. This shows the gain does not depend on one lucky run of the model. It does not widen the evidence beyond these 20 queries: every repeat answers the same queries, so the intervals still come from 20 queries.

The three answers files (answers/shared/rerank.r1.json to .r3.json) were identical: 8 of 8 in-corpus questions verified and 4 of 4 out-of-corpus questions declined, every time. In the third run, the calls for a10, a11 and a12 failed with a session-limit error, and the failed records scored as answered rather than declined. I regenerated those three questions in a separate fresh run and merged the three corrected records into rerank.r3.json by question id, so that file combines two runs.

Repeating does not tighten the Wilson intervals, because the three runs answer the same questions and cannot be pooled as new evidence. The intervals stay [0.676, 1.000] for the verified share and [0.510, 1.000] for the declined share. With 8 and 4 questions, a perfect score rules out a system that fails most of the time, but not one that answers wrongly one time in three or declines only half the time it should. The repeats show that the answering behavior is stable across runs, not that the true rates are 100 percent.

### The pre-registered claim

The claim, the smallest effect, the gold-set size and the test are in `PREREG.md`, committed before your own gold-set judgments.
Here, say whether you followed the plan, what the interval turned out to be, and what that means.
The outcome section of `PREREG.md` holds the short version.

My pre-registered claim (PREREG.md, commit e07a373, before any judgment) was that rerank would have a higher nDCG@10 than hybrid on my corpus, with Δ = 0.15 and a planned 40 queries, most of them cross-cutting. I did not fully follow the plan: I wrote 37 queries, 15 of them cross-cutting. The interval for rerank minus hybrid on nDCG@10 was −0.095 [−0.227, +0.028]. It includes zero and its lower end is beyond −0.15, so by my rule the result is inconclusive, with the point estimate opposite to my prediction. The minimum detectable difference was 0.187, above Δ, because the per-query sd was 0.406 rather than the 0.307 I planned with. After scoring, I also found that rerank.py sends Claude only the first 600 characters of each document, about 7 percent of one of my four-page parts, so the test did not compare hybrid with a reranker that could read the passages my hypothesis was about. The full outcome is in PREREG.md section 5.
