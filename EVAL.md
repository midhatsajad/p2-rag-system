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

TODO: describe your corpus and its license basis.

### The gold set

How many queries, how many with origin `hand` and how many with origin `claude`, and which query classes did you use and why?
How did you decide that a document is relevant: write your relevance rule in two or three sentences, the way the brief does for the shared corpus.
How did you find candidates (the systems' top 10, a keyword search, reading), and did you read every document before you labeled it?
Your labels are binary (`rel` 1) unless you say otherwise: if you use graded labels, declare the scale here, for example 2 means the document answers the query fully and 1 means it helps.

TODO: describe your gold set and your relevance rule.

---

## 4. Stage 2 - results on your corpus

Scores per system on your gold set.

<!-- p2:begin own -->
_No scored runs here yet: run `uv run p2 run --corpus own --system bm25` (or `--all`), then `uv run p2 score`._
<!-- p2:end own -->

The same scores per query class.

<!-- p2:begin own-classes -->
_No scored runs here yet: run `uv run p2 run --corpus own --system bm25` (or `--all`), then `uv run p2 score`._
<!-- p2:end own-classes -->

The same scores for the queries you wrote yourself (`hand`) and the ones a model drafted (`claude`), with the difference between the two groups and its interval.
Once both groups have queries, the table also says whether `bm25`'s lead over `dense` differs between them, and what share of each query's content words its best relevant document contains, which is stretch option 6.

<!-- p2:begin own-origins -->
_No scored runs here yet: run `uv run p2 run --corpus own --system bm25` (or `--all`), then `uv run p2 score`._
<!-- p2:end own-origins -->

Differences between every pair of systems.

<!-- p2:begin own-pairs -->
_No scored runs here yet: run `uv run p2 run --corpus own --system bm25` (or `--all`), then `uv run p2 score`._
<!-- p2:end own-pairs -->

Which differences are distinguishable and which are not, at your gold-set size?
Do the `hand` queries and the `claude` queries tell the same story?
Did your prediction in `DECISIONS.md` prompt 1 hold?

TODO: write what your own-corpus intervals let you claim.

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
| traces/shared-practice-rerank.jsonl | rerank | 20 | 20 | 2 | 286,944 | 9,111 | 143.1 | 14,347 | 456 | 7.2 |
| traces/shared-test-rerank.jsonl | rerank | 40 | 40 | 0 | 648,150 | 19,162 | 303.9 | 16,204 | 479 | 7.6 |

A span is one query of a run, one question of an answers file, or one claim of a judged file. A saved reply costs nothing now, so it counts the tokens and the seconds of the call that made it.

Every pair of systems on the same queries where at least one calls Claude, the one with fewer Claude input tokens per query first:

| Cheaper minus dearer | Queries | MRR@10 difference | 95% interval | Input tokens saved per query | Seconds saved per query | Reading |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| shared practice: bm25 minus rerank | 20 | -0.293 | [-0.533, -0.043] | 14,347 | 7.2 | rerank higher |
| shared practice: dense minus rerank | 20 | -0.237 | [-0.408, -0.083] | 14,347 | 7.2 | rerank higher |
| shared practice: hybrid minus rerank | 20 | -0.329 | [-0.504, -0.164] | 14,347 | 7.2 | rerank higher |

The difference is the cheaper system's score minus the dearer one's, with its paired interval; the savings count Claude calls only, so a system that makes none saves all of the other's.

Systems that do not call Claude, from traces/retrieval/ on the machine that last ran `p2 score` (git ignores that folder, so `p2 check` does not compare this part):

| Trace | System | Queries | Seconds | Milliseconds per query |
| --- | --- | ---: | ---: | ---: |
| traces/retrieval/shared-practice-bm25.jsonl | bm25 | 20 | 0.04 | 2.2 |
| traces/retrieval/shared-practice-dense.jsonl | dense | 20 | 0.24 | 11.8 |
| traces/retrieval/shared-practice-hybrid.jsonl | hybrid | 20 | 0.29 | 14.7 |
| traces/retrieval/shared-test-bm25.jsonl | bm25 | 40 | 0.09 | 2.2 |
| traces/retrieval/shared-test-dense.jsonl | dense | 40 | 0.36 | 8.9 |
| traces/retrieval/shared-test-hybrid.jsonl | hybrid | 40 | 1.30 | 32.4 |
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
