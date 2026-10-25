# Decision log

Your methods section, in your own words.
About one to two pages in total.

Answer these as you go, not the night before it is due.
Each answer is easier to write while the decision is still fresh, and prompt 1 only works if you write it before you see your own-corpus numbers.
Specifics beat polish: a short, honest answer with a number in it is worth more than a long vague one.

Each prompt ends with a marker line.
Replace that line with your answer.
`uv run p2 check` reports a marker as unfinished work, and `uv run p2 check --final` fails while any marker is left, so a finished log is part of being done.

Please do not let the agent write these for you.
These answers are about what you chose and what you knew, and the agent cannot know that.
Prompt 3 in particular only works in your own words.

---

## 1. Why this corpus, and what you expected

Why did you pick the corpus you used in stage 2, and why does it belong to a field or a question you care about?
Then say what you expected before you measured anything: which of `bm25`, `dense`, `hybrid` and `rerank` do you think will win on it, and which will do worst, and why?

Commit this answer before your first `uv run p2 score` on the own corpus.
Git history then shows that the expectation came first, which is what lets it be wrong in a way that teaches you something.
If you were surprised later, say so in prompt 4 or in EVAL.md; do not come back and rewrite this one.

My work is mostly on tunneling and underground construction involving geology, geotechnical engineering and rock mechanics, and the five USACE Engineer Manuals cover the ground side of it: rock tunnels and shafts, rock foundations, site investigation, bearing capacity and settlement. I wanted public-domain documents written by the government itself, so I ruled out the FHWA tunnel manuals, which were written with private consulting firms, and chose USACE over NIOSH’s mining-safety research because NIOSH covers safety research, while the USACE manuals cover design and construction, closer to my own work. I also rejected a sixth manual, Geophysical Exploration, because its methods chapters use figures reproduced by permission of publishers and instrument makers.

I wrote this answer after seeing the own-corpus scores, so it is not a blind prediction.
The only prediction I wrote down before scoring was my pre-registration (commit e07a373): that rerank would beat hybrid on nDCG@10 because cross-cutting terms like RQD appear in several manuals for different purposes. It came out inconclusive, with the point estimate in the opposite direction. I discuss the surprise in EVAL.md sections 4 and 7.
---

## 2. A fork in the road

Name one real design choice where you could have gone two ways: the chunk size, the embedding model, how the two systems are fused, how many documents the reranker sees, a sentence in `prompts/answer.txt`, how you cleaned the corpus.

Say which you picked, what the alternative was, and what you gave up by not taking it.
If you measured both, give both numbers.
If you rejected the alternative without measuring it, say why that was a fair call, and what it cost you in time, tokens or complexity.

"There was no alternative" is not an answer.
Find the fork.

When p2 license flagged 129 of the 134 parts of EM 1110-2-3506, Grouting Technology, I could either drop the whole manual or keep it and clear each flagged part, removing or documenting every figure caption credited to a private firm or equipment maker. I dropped it. I did not measure the alternative. Clearing 129 parts would have taken hours of reading, and each wrongly cleared caption would have meant publishing third-party material, so dropping it was the safer call.

It cost me two things. The corpus fell from 246 documents to 112, below the 200-document floor, so I added Bearing Capacity of Soils and Settlement Analysis to reach 212. That shifted the corpus toward shallow foundations and away from tunneling. I also lost the one manual devoted to grouting, which comes back as a gap in prompt 5.

---

## 3. Where you overruled the agent

One time Claude suggested, wrote or claimed something and you did not take it.
It might be a relevance judgment you disagreed with, a retriever it called finished when a run file showed otherwise, a number it summarized wrongly, or a license it said was fine.

What did it do?
How did you notice?
What did you do instead?

If it genuinely never happened, say so plainly, and then say what you would have had to check in order to notice.
Being honest here costs you far less than a story you cannot defend when you record your video.

When Claude first checked Grouting Technology, it found 67 “Courtesy of” lines with its own text search and recommended dropping the whole manual. I didn’t take that recommendation. I chose to look at the evidence first, because a quick search count isn’t the license tool’s verdict. When I ran p2 license, it flagged 129 of the 134 parts, not 67, because it catches more patterns than “courtesy of”, such as “reproduced with permission” and a textbook citation with a permission note.

I didn’t notice the undercount myself; the real check showed it. My part was insisting on that check before deciding. I then dropped the manual, the same decision Claude had recommended, but based on the tool’s count instead of an estimate that was off by almost half. I did not review all 129 parts individually; once the scale was clear, dropping the manual was the reasonable call.

---

## 4. A number you do not trust

Pick one number in `EVAL.md` that you do not fully trust, and say why.
It could be a mean over a small query class, a difference whose interval includes zero, a verified share of 100%, a score on a gold set you wrote yourself, or a result you got only once.

What would have to be true for you to trust it?
Did you do anything to test it, and what did that show?

rerank’s MRR@10 of 0.744 on the 15 cross-cutting queries is the highest of any system in that class, and it is the number that looks most like support for my pre-registered hypothesis. I don’t trust it, for four reasons. It rests on 15 queries with no interval. The nDCG@10 gap behind it is tiny: 0.695 against hybrid’s 0.680. The reranker saw only the first 600 characters of each document, about 7 percent of a four-page part, so whatever drove the score, it wasn’t reading the passages the way my hypothesis assumed. And it comes from a single run of a model whose replies can vary.

To trust it, I would need a paired interval on a cross-cutting-only gold set large enough to power the comparison, reranker runs that pass whole passages, and repeated runs showing the score is stable. I have not tested any of this.

---

## 5. What is still wrong

One thing in your system, your corpus or your gold set that is not right, not finished, or that you do not fully understand.

What would you do next, and how would you find out whether it matters?
Name the file, the query or the document where someone could look.

Dropping Grouting Technology left grouting thinly covered. Grouting is mentioned in about 32 documents across four manuals, but few treat it in depth, and the main ones are rock-foundations__p101-104 and a glossary entry. Query c05, which asks how grouting is used in tunnel support versus foundation treatment, depends on that thin set, so its scores may rest on one or two labels, like c04’s.

Next, I would check c05’s lines in eval/own/qrels.txt to see how many relevant documents it has, and read the documents that mention grouting to see whether any of them answer it and were missed by the top-5 pool. If c05 has only one or two relevant documents, I would either add a properly licensed grouting source or treat c05’s scores as resting on one label in the analysis.
