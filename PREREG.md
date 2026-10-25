# Pre-registration (598E)

This file is for 598E students; it is the second half of the 598E rider, and 498E students can ignore it or delete it.

A pre-registration is a claim you write down, with the test that will judge it, before you can see the answer.
Its value is that the claim can be wrong in a way anyone can check, and that you cannot adjust it afterwards to fit the numbers.
A well-powered result that says "no effect as large as the one I cared about" scores as well as a confirmation, so you have no reason to bend the claim.

**Git history is how I will know the order.**
Commit this file, filled in through section 4, before the first commit that puts a judgment line into `eval/own/qrels.txt` (or any other file under `eval/own/`).
`uv run p2 check` reads `git log` to find the first commit in which sections 1 to 4 have no TODO marker left and some words of yours in each, and confirms that it comes before your first judgment; a copy that was filled in afterwards fails.
Right after that commit, `p2 check` names it and waits for your first judgment; it asks for section 5 separately, once you have scored your own corpus.
You may ingest your corpus and write queries first, but not the relevance judgments.
After that first commit, do not edit sections 1 to 4, because `p2 check` compares them with the commit where you filled them in.
If something must change, add a dated entry in section 6 and leave the original as it was.

You need your stage 1 scores for section 3, so score the shared corpus first.

---

## 1. Hypothesis

One sentence, about your own corpus, naming two of your systems and a direction.
For example: "On my corpus of Kubernetes documentation, `rerank` has a higher MRR@10 than `hybrid`, because the queries are paraphrases that a first-stage fusion ranks too low."
It should be something you could be wrong about.

On my corpus of five USACE Engineer Manuals, rerank has a higher nDCG@10 than hybrid, because terms such as RQD appear in several manuals with different purposes, so the first stage ranks every passage that mentions the term, while only some of them answer what the query asks.

---

## 2. The smallest effect that matters

Name one metric, MRR@10 or nDCG@10, and choose it now so you cannot pick the better one afterwards.
Then say how large a difference between the two systems would matter to a person using the search, and why that size.
A difference of 0.02 is usually not worth a reranker's cost in time and tokens.
In this course, choose a Δ of at least 0.15 unless you argue for a larger one, because a smaller gap takes more queries than one project can judge.
Call your number Δ (delta).

The metric is nDCG@10. Relevant passages for a cross-cutting query can sit in several manuals, and nDCG@10 credits ranking all of them well, where MRR@10 would count only the first.

Δ is 0.15. On the shared corpus the reranker cost about 14,000 input tokens and 7 seconds per query (the cost table in EVAL.md section 8), against a few milliseconds for hybrid. A gain smaller than 0.15, roughly one relevant passage moving a few places on an average query, would not be worth that cost to someone searching these manuals.

---

## 3. How many queries you need

The size of the gold set follows from three numbers: how large a difference you want to detect (Δ), how variable the per-query differences are (sd), and the usual choices of a 5% false-alarm rate and 80% power.

```
n = ((1.96 + 0.84) * sd / Δ)^2
```

Here sd is the standard deviation of the per-query differences between your two systems, which `results/results.json` holds for the shared practice queries.
Compute it from your stage 1 runs for the same two systems, or the nearest pair you have, and say which pair you used.
With only 20 practice queries the sd is itself noisy, so be generous and round up.

Some numbers to calibrate against.
At sd 0.3 and Δ 0.10 the formula gives about 71 queries, and with the t distribution's small-sample correction it is a few more, about 73.
At sd 0.3, a gold set of 30 queries can only detect a difference of about 0.15, which is why 30 queries cannot support a claim about a gap of 0.10.
The spreads you will measure on the shared practice queries are mostly larger than 0.3: from about 0.31 for `hybrid` against `bm25` to about 0.66 for `dense` against `bm25`.
For `rerank` against `hybrid` the sd is about 0.39, so a Δ of 0.10 needs about 120 queries, 0.15 about 55, and 0.20 about 31.
So the course's Δ of 0.15 means about 55 queries for that pair; at an sd of 0.66 it would mean about 150, so compare a pair whose spread you can afford.
Choose Δ and the size of your gold set together: the smallest effect that matters to a user, and a number of queries you can write and judge in the time you have.
If the two do not meet, say which one you gave ground on and why.

After you score the own corpus, the minimum detectable difference that `uv run p2 score` prints for your two systems is this same calculation run the other way.
It should come out at or below your Δ.
If it does not, your queries varied more than your stage 1 sd suggested, and you will say so in the outcome.

The sd comes from the same pair and metric on the shared practice queries: rerank minus hybrid, nDCG@10, sd = 0.31 (confirm against results/results.json).

n = ((1.96 + 0.84) × 0.31 / 0.15)² ≈ 33.5, or about 36 with the small-sample correction. Because 20 practice queries give a noisy sd, and because my gold set will lean on cross-cutting queries more than the shared set did, I will write 40 queries, most of them on terms that appear in more than one manual.

---

## 4. The test, and what each result will mean

The test is the paired 95% interval of the mean difference between your two systems on your own gold set, from the `own-pairs` table that `uv run p2 score` writes in `EVAL.md`.
Write the rule now.
This is the default rule, and you can tighten it, but do not loosen it after you see your numbers.

| The interval is | I will say |
|---|---|
| entirely above zero in the direction I predicted | supported: the difference is distinguishable from zero |
| entirely on the other side of zero | contradicted: the opposite of my hypothesis holds on this gold set |
| around zero, with both ends inside plus or minus Δ | well-powered null: a difference as large as Δ is ruled out |
| around zero, with an end beyond plus or minus Δ | inconclusive: the gold set could not settle it, and I say so |

The test is the paired 95% interval of rerank minus hybrid on nDCG@10, from the own-pairs table in EVAL.md. I keep the default rule:
The interval is	I will say
entirely above zero	supported: rerank’s higher nDCG@10 is distinguishable from zero
entirely below zero	contradicted: hybrid ranks better than rerank on this gold set
around zero, with both ends inside ±0.15	well-powered null: a difference as large as 0.15 is ruled out
around zero, with an end beyond ±0.15	inconclusive: the gold set could not settle it, and I say so

---

## 5. Outcome (write this after the fact)

What was the interval?
Which row of the table in section 4 is it?
Did your gold set reach the size section 3 asked for, and what was the minimum detectable difference that `uv run p2 score` printed?
What would you do next, and what would you want a reader to take from this?

The interval for rerank minus hybrid on nDCG@10 was −0.095 [−0.227, +0.028]. It includes zero, with the upper end inside +0.15 and the lower end beyond −0.15, so by my rule the result is inconclusive. The point estimate went the opposite way from my hypothesis. The upper end of +0.028 puts a reranker gain as large as Δ outside the interval, but my rule required both ends inside ±0.15 to rule out a difference, and a hybrid advantage larger than 0.15 is not ruled out.

I did not build the gold set section 3 committed to. I planned 40 queries, most of them cross-cutting, and wrote 37, of which 15 are cross-cutting. The hypothesis is about cross-cutting queries, but most of the set tests something else, which dilutes any effect specific to them. The sd I planned with, which section 3 left to confirm, was 0.307 in results/results.json, so the planned n of about 36 stands. The minimum detectable difference that p2 score printed was 0.187, above my Δ of 0.15, because the per-query differences on my corpus varied more than on the shared one: sd 0.406 against 0.307. At that spread, a test at Δ = 0.15 needs about 58 queries, or about 60 with the small-sample correction.

Judging was also shallower than it should have been. The pool took each system’s top 5, so a relevant document that a system ranked 6 to 10, and that no system had in its top 5, was never judged and counted against that system. rerank is the system most exposed to this, because its ranks 6 to 10 can hold documents promoted from hybrid’s ranks 11 to 20. I did not measure how much this cost it.

Outside the pre-registered test, the per-class scores point in a direction worth testing properly. On the 15 cross-cutting queries, rerank has a higher nDCG@10 than hybrid (0.695 against 0.680), while on the 10 identifier queries it is far lower (0.585 against 0.881). The identifier drop is not a pooling artifact: every relevant identifier document was judged, since bm25, dense and hybrid all reach recall@10 of 1.000 there, so rerank moved judged relevant documents down. All of this is descriptive, with no interval and too few queries per class, and I did not predict the identifier drop.

Next, I would build a gold set of about 60 queries with cross-cutting queries as the majority, pool each system’s top 10, and pre-register the cross-cutting class on its own. Before rerunning, I would count each system’s unjudged top-10 documents to measure the pooling bias, and check two possible causes of the identifier drop: how often the reranker’s reply failed the permutation check and fell back to hybrid’s order, and whether it saw whole four-page documents or truncated ones. What I would want a reader to take from this is that the reranker’s large gain on the shared corpus did not carry over to this one, and that this gold set is too small, too mixed and too shallowly judged to say whether it helped, hurt, or did nothing on the queries the hypothesis was about.

---

## 6. Amendments

Dated entries only, one per change, each saying what changed and why.
Leave this section as it is if nothing changed.
