# Lesson 1: Finding the right text

**Goal:** Understand retrieval, the first step of RAG, by building a simple search.

**Code:** `src/keyword_search.py`

**Run it:** `python3 src/keyword_search.py`

## What is RAG?

RAG stands for Retrieval-Augmented Generation.

| Step | Meaning | Example |
|---|---|---|
| Retrieval | Find relevant text | Find the encryption policy |
| Augmented | Add that text to the prompt | "Using this policy, answer the question..." |
| Generation | The LLM writes an answer | "Yes, data is encrypted using AES-256." |

An LLM doesn't know a company's private policies. RAG gives it the right pages before it answers, like an open-book exam.

## New terms

- **LLM (large language model):** An AI model that generates text, such as Claude.
- **Chunk:** A small piece of a document. We search chunks because a whole document would contain too much unrelated text.
- **Knowledge base:** The collection of information we search.
- **Source:** Where a chunk came from. We need it for citations.

## Python for Kotlin developers

| Python | Kotlin | Notes |
|---|---|---|
| `def search(question):` | `fun search(question: String)` | Python doesn't require types |
| Indentation | `{ }` | Spaces define code blocks, so they matter |
| `None` | `null` | Means no value |
| `{"source": "..."}` | `mapOf("source" to "...")` | Called a dictionary |
| `[a, b]` | `listOf(a, b)` | Called a list |
| `set(...)` | `setOf(...)` | Stores unique values |
| `a & b` | `a intersect b` | Items in both sets |
| `return chunk, score` | `Pair(chunk, score)` | Returns a tuple |
| `f"Score: {score}"` | `"Score: $score"` | String formatting |

## How the code works

1. `get_words()` turns text into a set of lowercase words.
2. `score_chunk()` counts the words shared by a question and a chunk.
3. `search()` checks every chunk and keeps the highest score.
4. `main()` runs the test questions and prints the results.

## Results

| Question | Result | Correct? |
|---|---|---|
| Is customer data encrypted at rest? | Encryption Policy, section 2.1 | Yes |
| How often is a penetration test performed? | Security Testing Policy, section 5.1 | Yes |
| How do you protect stored information? | No match | No |
| Do staff need a second login step? | Security Testing Policy, section 5.1 | No |

## What went wrong

**Question 3 missed the answer.** "Protect stored information" means nearly the same as "encrypted at rest", but the two share no words.

**Question 4 found the wrong answer.** It should match the multi-factor authentication rule. The only shared word with the chosen chunk was "a", which says nothing about the meaning.

Word matching compares spelling, not meaning. Lesson 2 introduces **embeddings**, which let us search by meaning.

## Exercises

1. Add a chunk about password rules to `CHUNKS`, then ask a question that finds it.
2. Add a list of common words such as "a", "is", and "the", then ignore them in `get_words()`. These are called **stop words**. What happens to question 4?
3. Change `search()` so it returns the top 2 chunks instead of one.

## Check your understanding

1. What does each letter in RAG stand for?
2. Why do we split documents into chunks?
3. Why do we store a source with each chunk?
4. Why did question 3 fail even though the answer was in the knowledge base?
