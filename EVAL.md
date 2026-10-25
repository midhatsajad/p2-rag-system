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

rerank takes hybrid’s top 20 candidates and sends them to Claude Sonnet as numbered passages. It asks for the best order back as {"order": [...]}, with a schema that keeps every number between 1 and 20. If the reply is not a permutation of the candidate numbers, it falls back to hybrid’s order. That check covers both a malformed reply and a failed call, since a failed call returns nothing. It reranks documents for p2 run and chunks for p2 answer.

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

a02 ("what minimum incombustible content must the combined dust keep where no methane is present?") has a real problem. The claim says the 80 percent incombustible content "must be maintained throughout the top, floor, and sides of all underground areas." The cited chunk (`cfr30-75.403#0`) opens with a condition the claim drops: "Where rock dust is required to be applied, it shall be distributed... and maintained in such quantities that the incombustible content... shall be not less than 80 percent." The claim states the 80 percent rule as if it always applies, when the regulation states it only where rock dust is required to be applied. I checked that this is not a chunk boundary problem: chunk `#0` starts at the section heading, and the conditional opening is the actual first sentence of 30 CFR 75.403. So the quote is a real piece of the chunk, but the claim is broader than the law it cites.

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

The interval is a paired bootstrap (10,000 resamples of the queries); MDD is the smallest difference this many queries detect 80% of the time.
<!-- p2:end own-pairs -->

Which differences are distinguishable and which are not, at your gold-set size?
Do the `hand` queries and the `claude` queries tell the same story?
Did your prediction in `DECISIONS.md` prompt 1 hold?

On 37 queries, one pair is distinguishable: hybrid is higher than bm25 on recall@10 (+0.095, [+0.027, +0.176]) and nDCG@10 (+0.109, [+0.033, +0.181]). Its MRR@10 gain (+0.113, [−0.007, +0.231]) is not distinguishable, though the interval only just reaches zero. Both detected gains sit at about their minimum detectable difference (0.106 and 0.107), so their size is rough.

Every other difference is not distinguishable. rerank separates from no system on any score. Its point estimates are below hybrid on all three scores and below dense on MRR@10 and nDCG@10, but none of those intervals excludes zero. The minimum detectable differences run from 0.106 to 0.270, so on MRR@10 a gap of about 0.25 between rerank and any other system could go unseen. Because the pool took only each system’s top 5, these scores also carry a bias against systems whose ranks 6 to 10 hold documents the pool never covered, and rerank, whose 6 to 10 slots can hold documents promoted from hybrid’s ranks 11 to 20, is the system most exposed to it. I did not measure this; counting each system’s unjudged top-10 documents would. Here rerank cost about 15,170 input tokens and 10.2 seconds per query, against under 10 milliseconds for the other three, for no distinguishable gain.

The per-class table has 10 to 15 queries per class and no intervals, so I read it descriptively. rerank’s overall deficit comes almost entirely from identifier queries. There its MRR@10 is 0.484 against hybrid’s 0.850, and its nDCG@10 is 0.585 against 0.881. On cross-cutting queries, the class my pre-registered hypothesis is about, rerank has the highest MRR@10 (0.744) and nDCG@10 (0.695, against hybrid’s 0.680). One reading is that the reranker demotes exact-identifier matches that the first stage had already placed at the top, while helping slightly where the query needs a passage’s purpose read. Pooling does not explain the identifier drop: bm25, dense and hybrid all reach recall@10 of 1.000 on identifier queries, so every relevant identifier document was judged, and rerank’s 0.900 there comes from moving judged relevant documents below rank 10. Because rerank only reorders hybrid’s top 20, it cannot find a document hybrid missed. When hybrid already ranks the right document first, reordering can only keep it there or move it down. The cross-cutting gap is far too small to claim with 15 queries.

The hand and claude queries mostly tell the same story. The only distinguishable origin difference is bm25’s recall@10, which is higher on claude queries (hand minus claude −0.198, [−0.399, −0.018]). The table that asks directly whether drafted queries favor keyword search finds no distinguishable difference in bm25’s lead over dense between the two origins on any score. Drafted queries echoing the documents’ wording would not explain the recall gap either, since hand queries share more content words with their best relevant document (0.74) than claude queries do (0.69). A likelier explanation is the class mix: 7 of the 10 identifier queries are claude queries, while 9 of the 15 hand queries are cross-cutting, so the origin comparison is partly a class comparison. I did not test this.

---

## 5. The ablation

Change one thing and keep everything else the same.
Write your hypothesis here before you run it, in one sentence with a direction: "I expect X to raise MRR@10 on my corpus because Y."
The run file for it lives in `runs/own/ablation/`.

<!-- p2:begin own-ablation -->
_No ablation runs yet: `uv run p2 run --corpus own --system NAME --ablation` writes one to runs/own/ablation/, then `uv run p2 score` fills this table._
<!-- p2:end own-ablation -->

The queries your ablation helped and hurt, against the system it varies, by reciprocal rank.
`p2 score` finds that system from a line such as `BASE = "bm25"` in your variant's file, or else from its name: `bm25_lab` varies `bm25`.

<!-- p2:begin own-ablation-queries -->
_No ablation runs yet: `uv run p2 run --corpus own --system NAME --ablation` writes one to runs/own/ablation/, then `uv run p2 score` fills this table._
<!-- p2:end own-ablation-queries -->

What did you change, what happened, and does the interval support the claim you want to make?
If the result is not distinguishable, say what size of effect your gold set could have seen.
Read the queries at the top of each list in the second table, and say whether your change explains them.

TODO: write the ablation: the one change, the hypothesis, the result and the claim.

---

## 6. Failure analysis

Pick the queries where your best system on your own corpus failed: the relevant document is missing from the top 10, or sits far below the top.
Take at least five, and read what the system returned next to what was relevant.
Then sort the failures by cause, for example a vocabulary mismatch, near-duplicate documents, a chunk that cut the answer in half, a query that is ambiguous, or a label that was wrong, because sometimes the gold set is what failed.

| qid | what the best system returned | what was relevant | cause | what you would try |
|---|---|---|---|---|

TODO: add one row for each failure you analyzed, and write two or three sentences on the pattern you see across them.

---

## 7. Cross-corpus comparison

The two tables to compare are the shared-corpus scores in section 1 and your own-corpus scores in section 4, with their intervals.
If you want them side by side, copy the rows you need into a table here and say that you copied them.

Did the winner change between the shared corpus and yours?
Why, or why not: what is different about the two collections (document length, vocabulary, identifiers, near-duplicates, how the queries were written), and which of your explanations did you test and which are guesses?
Say what 20 queries on one side and your gold-set size on the other cannot support.

TODO: write the cross-corpus comparison.

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
| traces/own-own-rerank.jsonl | rerank | 37 | 37 | 36 | 561,273 | 29,280 | 376.7 | 15,170 | 791 | 10.2 |
| traces/shared-practice-rerank.jsonl | rerank | 20 | 20 | 20 | 286,944 | 9,111 | 142.0 | 14,347 | 456 | 7.1 |
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

---

## 9. 598E only - repeats and the pre-registered claim

498E students can leave this section as it is; nothing checks it.
598E students replace each line that starts with "598E: write", and `uv run p2 check --final` counts those lines as work still to do until they are gone.

### Repeats on the shared corpus

Three runs of the reranker on the practice queries, and three answers files, with their run-to-run spread and Wilson intervals.

<!-- p2:begin repeats -->
_No repeated runs or answers files yet (598E: `p2 run ... --repeat 3` and `p2 answer ... --repeat 3`)._
<!-- p2:end repeats -->

Does the reranker's gain over its first stage survive the run-to-run variation?
Write what the spread is, how it compares with the gain, and what the Wilson intervals on the verified share and the declined share say about 8 and 4 questions.

598E: write the repeats result here.

### The pre-registered claim

The claim, the smallest effect, the gold-set size and the test are in `PREREG.md`, committed before your own gold-set judgments.
Here, say whether you followed the plan, what the interval turned out to be, and what that means.
The outcome section of `PREREG.md` holds the short version.

598E: write the claim and its outcome here.
