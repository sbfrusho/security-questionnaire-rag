"""Lesson 2: find the policy text closest in meaning to a question.

This uses the same chunks and questions as Lesson 1, so you can compare results.
The only change is how we score a match: meaning instead of shared words.

Run from the project folder:
    .venv/bin/python src/embedding_search.py
"""

import math

from fastembed import TextEmbedding

from keyword_search import CHUNKS

# A small model that runs on your computer. It needs no API key, and it
# downloads once (about 90 MB) the first time you run this file.
MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"


def cosine_similarity(a, b):
    """Measure how closely two embeddings point in the same direction.

    Args:
        a: One embedding, which is a list of numbers.
        b: Another embedding of the same length.

    Returns:
        A number up to 1.0. A higher number means closer in meaning.
    """
    dot_product = sum(x * y for x, y in zip(a, b))
    length_a = math.sqrt(sum(x * x for x in a))
    length_b = math.sqrt(sum(y * y for y in b))
    return dot_product / (length_a * length_b)


def search(question, model, chunk_embeddings):
    """Find the chunk closest in meaning to a question.

    Args:
        question: The question being asked.
        model: The embedding model. It must be the one that embedded the chunks.
        chunk_embeddings: One embedding per entry in CHUNKS, in the same order.

    Returns:
        A tuple of (best chunk, score). Unlike Lesson 1, there is always a
        best chunk, even when the question has nothing to do with any of them.
    """
    # embed() takes a list and gives back one embedding per item.
    question_embedding = list(model.embed([question]))[0]

    best_chunk = None
    best_score = -1.0  # The lowest possible cosine similarity.

    # zip() walks two lists together, like Kotlin's chunks.zip(embeddings).
    for chunk, chunk_embedding in zip(CHUNKS, chunk_embeddings):
        score = cosine_similarity(question_embedding, chunk_embedding)
        if score > best_score:
            best_chunk = chunk
            best_score = score

    return best_chunk, best_score


def main():
    """Embed the chunks, run the test questions, and print what is found."""
    model = TextEmbedding(MODEL_NAME)

    # Embed every chunk once up front, so each search only embeds the question.
    chunk_embeddings = list(model.embed([chunk["text"] for chunk in CHUNKS]))
    print(f"Each embedding has {len(chunk_embeddings[0])} numbers.\n")

    questions = [
        "Is customer data encrypted at rest?",
        "How often is a penetration test performed?",
        "How do you protect stored information?",
        "Do staff need a second login step?",
        "What is the office dog called?",
    ]

    for question in questions:
        chunk, score = search(question, model, chunk_embeddings)
        print(f"Question: {question}")
        print(f"  Best match: {chunk['text']}")
        print(f"  Source: {chunk['source']}")
        print(f"  Similarity: {score:.2f}")
        print()


if __name__ == "__main__":
    main()
