# Security Questionnaire RAG

A learning project that will grow into a RAG system for drafting cited answers to security questionnaires.

## Lessons

| Lesson | Topic | Status |
|---|---|---|
| [1](docs/lessons/01-keyword-search.md) | Finding text with keyword search | Ready |
| [2](docs/lessons/02-embeddings.md) | Searching by meaning with embeddings | Ready |

## Run the current lesson

Set up once:

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
```

Then run:

```bash
.venv/bin/python src/embedding_search.py
```
