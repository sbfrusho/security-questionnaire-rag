# Tech stack

The technologies planned for this project. Each one gets a proper introduction before we use it, and this list may change as we learn what the project needs.

## Already in use

| Technology | What it does |
|---|---|
| Python | Main language for the backend and RAG logic |
| venv | Keeps this project's Python packages separate |
| pip | Installs Python packages |
| FastEmbed | Runs the embedding model that searches by meaning |

## RAG

| Technology | What it does | Stage |
|---|---|---|
| Claude API (`anthropic` package) | The LLM that writes answers from retrieved text | First full RAG |
| pdfplumber | Reads text and tables from PDFs | Real documents |
| openpyxl | Reads and writes Excel questionnaires | Real documents |
| FastEmbed reranker | Reorders search results so the best ones come first | Better results |

## Backend

| Technology | What it does | Stage |
|---|---|---|
| FastAPI | Builds the API that the web app calls | Backend and database |
| Uvicorn | Runs the FastAPI server | Backend and database |
| Pydantic | Validates data, similar to typed Kotlin data classes | Backend and database |
| pydantic-settings | Loads API keys and other settings from the environment | Backend and database |

## Database

| Technology | What it does | Stage |
|---|---|---|
| PostgreSQL | Stores documents, questionnaires, and answers | Backend and database |
| pgvector | Stores and searches embeddings in PostgreSQL | Backend and database |
| PostgreSQL full-text search | Provides the keyword half of hybrid search | Better results |
| SQLAlchemy | Lets Python work with the database, similar to Room on Android | Backend and database |
| Alembic | Manages database schema changes, similar to Room migrations | Backend and database |

## Frontend

| Technology | What it does | Stage |
|---|---|---|
| TypeScript | Adds types to JavaScript, which will feel familiar from Kotlin | Web app |
| React | Builds the user interface from components, similar to Jetpack Compose | Web app |
| Next.js | Provides the structure and routing for the React app | Web app |
| Tailwind CSS | Styles the screens | Web app |

## Testing and code quality

| Technology | What it does | Stage |
|---|---|---|
| pytest | Runs automated tests, similar to JUnit | First full RAG |
| Ruff | Checks and formats Python code | First full RAG |
| Custom evaluation script | Measures retrieval and answer accuracy on a test set | Better results |

## Tools and deployment

| Technology | What it does | Stage |
|---|---|---|
| Git and GitHub | Track changes and host the code | Now |
| Docker | Runs PostgreSQL locally and packages the app for deployment | Backend and database |
| Python `logging` module | Records what the app does, including errors and costs | Launch |
| GitHub Actions | Runs the tests automatically on every push | Launch |
| Hosting provider | Runs the live app; to be chosen when we deploy | Launch |

## Setup still needed

- **Python:** This machine has Python 3.9.6. We should upgrade to a newer version before starting the backend.
- **Docker:** Not installed yet. We need it for the database stage.
- **Node.js:** Needed for the frontend. We'll check and install it at the web app stage.
