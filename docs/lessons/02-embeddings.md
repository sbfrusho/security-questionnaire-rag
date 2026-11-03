# Lesson 2: Searching by meaning

**Goal:** Fix the failures from Lesson 1 by comparing meaning instead of spelling.

**Code:** `src/embedding_search.py`

**Set up once:**

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
```

**Run it:** `.venv/bin/python src/embedding_search.py`

The first run downloads the model. You may also see a `NotOpenSSLWarning`, which is harmless here.

## New terms

- **Embedding:** A list of numbers that represents the meaning of a piece of text. Our model produces 384 numbers for each text.
- **Embedding model:** The AI model that turns text into an embedding. It doesn't write answers, so it isn't the LLM from Lesson 1.
- **Cosine similarity:** A score for how closely two embeddings point in the same direction. Higher means closer in meaning.
- **Virtual environment:** A private folder of Python packages for one project, here `.venv`. It's similar to how Gradle keeps dependencies per project.

## The idea

Picture a map where related ideas sit close together, so "dog" is near "puppy" and far from "invoice". An embedding is a position on that kind of map, with 384 directions instead of 2.

The model learned those positions from a huge amount of text. Words used in similar ways end up nearby, even when they're spelled differently.

Searching then has three steps:

1. Turn every chunk into an embedding.
2. Turn the question into an embedding, using the same model.
3. Pick the chunk with the highest cosine similarity.

Embeddings from different models can't be compared, because each model builds its own map.

## Python for Kotlin developers

| Python | Kotlin | Notes |
|---|---|---|
| `from keyword_search import CHUNKS` | `import keyword_search.CHUNKS` | Reuses Lesson 1's chunks |
| `[c["text"] for c in CHUNKS]` | `chunks.map { it["text"] }` | Called a list comprehension |
| `sum(x * y for x, y in zip(a, b))` | `a.zip(b).sumOf { (x, y) -> x * y }` | Pairs two lists, then adds the products |
| `for a, b in zip(xs, ys):` | `for ((a, b) in xs.zip(ys))` | Loops over two lists together |
| `f"{score:.2f}"` | `"%.2f".format(score)` | Prints 2 decimal places |

## How the code works

1. `main()` loads the model and embeds every chunk once.
2. `search()` embeds the question and scores it against each chunk.
3. `cosine_similarity()` does the comparison. Libraries can do this for you, but it's only three lines of arithmetic, so we write it out here.

## Results

| Question | Lesson 1 result | Lesson 2 result | Similarity | Correct now? |
|---|---|---|---|---|
| Is customer data encrypted at rest? | Encryption Policy, section 2.1 | Encryption Policy, section 2.1 | 0.74 | Yes |
| How often is a penetration test performed? | Security Testing Policy, section 5.1 | Security Testing Policy, section 5.1 | 0.67 | Yes |
| How do you protect stored information? | No match | Encryption Policy, section 2.1 | 0.38 | Yes |
| Do staff need a second login step? | Security Testing Policy, section 5.1 | Access Control Policy, section 3.4 | 0.47 | Yes |

Both Lesson 1 failures are fixed. "Second login step" shares no useful words with "multi-factor authentication", but the model still places them close together.

## What's still weak

**It always returns something.** We added a fifth question, "What is the office dog called?". The knowledge base has no answer, yet the search still returned the penetration test chunk, with a similarity of 0.08. In a questionnaire tool, that could lead to a confident answer citing the wrong policy.

The low score is a useful signal. A minimum score could reject matches like this one.

**Scores aren't percentages.** A score of 0.38 doesn't mean 38% correct. Scores are only useful relative to each other, and a good cutoff depends on the model and your documents.

**Some wins are narrow.** For "How do you protect stored information?", the encryption chunk scored 0.38 and the backup chunk scored 0.33. That's why real systems usually pass several top chunks to the LLM instead of one.

**Five chunks hide a cost.** We compare the question with every chunk, which is fine here but slow with millions of them. A **vector database** is built to solve this, and we can come back to it later.

## Exercises

1. Add a chunk about password rules to `CHUNKS`, then ask about it without using the word "password".
2. Print the score for every chunk, not only the best one. Which question has the closest race?
3. Add a `MIN_SCORE` constant and print "No match found" below it. Which value rejects the dog question but keeps the other four?

## Check your understanding

1. What is an embedding?
2. Why must the question and the chunks use the same embedding model?
3. Why did "second login step" find the multi-factor authentication chunk this time?
4. Why is always returning a result dangerous for security questionnaires?
