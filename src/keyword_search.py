"""Lesson 1: find the policy text that best matches a question.

This is the "R" (Retrieval) in RAG, built in the simplest way possible.
There is no AI here yet. We compare words, then see where that breaks.

Run from the project folder:
    python3 src/keyword_search.py
"""

import re

# Our tiny knowledge base. In Kotlin, this would be a List<Map<String, String>>.
# Each entry is one "chunk": a small piece of a document, plus where it came from.
CHUNKS = [
    {
        "source": "Encryption Policy, section 2.1",
        "text": "All customer data is encrypted at rest using AES-256.",
    },
    {
        "source": "Encryption Policy, section 2.2",
        "text": "All data sent over the network is encrypted in transit using TLS 1.2 or higher.",
    },
    {
        "source": "Security Testing Policy, section 5.1",
        "text": "An independent company performs a penetration test every year.",
    },
    {
        "source": "Access Control Policy, section 3.4",
        "text": "Employees must use multi-factor authentication to access company systems.",
    },
    {
        "source": "Backup Policy, section 4.1",
        "text": "Customer data is backed up every day and backups are kept for 30 days.",
    },
]


def get_words(text):
    """Convert text into a set of lowercase words.

    Args:
        text: Any string, such as "Is data encrypted?".

    Returns:
        A set of unique words, such as {"is", "data", "encrypted"}.
        Lowercasing means "Data" and "data" count as the same word, and the
        regular expression keeps letters, numbers, and hyphens but drops
        punctuation such as "?".
    """
    return set(re.findall(r"[a-z0-9-]+", text.lower()))


def score_chunk(question, chunk):
    """Count how many words a question and a chunk have in common.

    Args:
        question: The question being asked.
        chunk: One entry from CHUNKS, with "source" and "text" keys.

    Returns:
        The number of shared words. A higher number means a better match.
    """
    # The & operator gives the words that appear in both sets.
    shared_words = get_words(question) & get_words(chunk["text"])
    return len(shared_words)


def search(question):
    """Find the chunk that best matches a question.

    Args:
        question: The question being asked.

    Returns:
        A tuple of (best chunk, score). The chunk is None if no words matched.
    """
    best_chunk = None
    best_score = 0

    for chunk in CHUNKS:
        score = score_chunk(question, chunk)
        if score > best_score:
            best_chunk = chunk
            best_score = score

    return best_chunk, best_score


def main():
    """Run a few test questions and print what the search finds."""
    questions = [
        "Is customer data encrypted at rest?",
        "How often is a penetration test performed?",
        "How do you protect stored information?",
        "Do staff need a second login step?",
    ]

    for question in questions:
        chunk, score = search(question)
        print(f"Question: {question}")
        if chunk is None:
            print("  No match found")
        else:
            print(f"  Best match: {chunk['text']}")
            print(f"  Source: {chunk['source']}")
            print(f"  Shared words: {score}")
        print()


# This is true only when you run this file directly, not when another file
# imports it. It works like the entry point of a Kotlin program.
if __name__ == "__main__":
    main()
