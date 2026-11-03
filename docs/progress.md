# Project progress

Last updated: 2026-11-03

## Current status

- **Current stage:** Search basics
- **Lessons written:** 1 and 2
- **Understanding check:** Lesson 1 question not answered yet
- **Next lesson:** Lesson 3, after your setup is done and we've reviewed Lessons 1 and 2

## Your next steps

- [x] Install Docker Desktop
- [ ] Open Docker Desktop, finish its setup, then run `docker run hello-world`
- [ ] Rebuild `.venv` with Python 3.12
- [ ] Move `src/keyword_search.py` and `src/embedding_search.py` to `lessons/`
- [ ] Answer the Lesson 1 question: why did "How do you protect stored information?" fail?
- [ ] Do the Lesson 1 exercises

## Learning path

- [ ] **Search basics:** keyword search, then searching by meaning
- [ ] **First full RAG:** connect search to an LLM and add citations
- [ ] **Real documents:** read PDFs and spreadsheets, and split them into chunks
- [ ] **Backend and database:** build an API with FastAPI and store data in PostgreSQL
- [ ] **Web app:** create the upload and review screens
- [ ] **Better results:** add hybrid search, reranking, and accuracy testing
- [ ] **Launch:** add logging and cost limits, then deploy

## Tools

| Tool | Status |
|---|---|
| Homebrew | Installed |
| Python 3.12.13 | Installed, but `.venv` still uses 3.9.6 |
| Node.js 26.9.0 and npm 11.19.1 | Installed |
| Docker 29.9.2 | Installed, but Docker Desktop hasn't been started yet |
| Git repository | Not set up for this project yet |

## Decisions

| Decision | Reason |
|---|---|
| Build a security questionnaire assistant | It solves a problem companies already pay to solve, and a student-focused project sounded like a university project |
| You write the code | You learn better by adding small, explained pieces yourself |
| Keep practice code in `lessons/` and the real app in `backend/` and `frontend/` | This gives the project a proper structure |

## Open items

- `docs/tech-stack.md` wrongly says this machine needs a newer Python. Python 3.12.13 is already installed.
- The README and lesson notes still say `src/`. They'll need updating once the lesson scripts move to `lessons/`.

## Work log

### 2026-11-03

- Chose the project and planned the learning path.
- Wrote Lesson 1 (keyword search) and Lesson 2 (embeddings), including their code. This was before the rule that you write the code.
- Created `docs/tech-stack.md` and planned the project structure.
- Checked the tools. Python and Node.js were already installed, and my Docker installation stopped because it needed your password.
- Created this progress file.
- You installed Docker Desktop. The `docker` command works, but Docker Desktop still needs to be started and tested.
