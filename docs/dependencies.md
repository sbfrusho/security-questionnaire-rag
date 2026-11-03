# Dependencies

Why each Python package is in this project. Versions are what's installed in `.venv` as of 2026-11-03.

- **Direct dependency:** We chose it and listed it in `requirements.txt`.
- **Indirect dependency:** Another package needs it, so pip installs it automatically.

Keep this file updated whenever packages change. Every package is code from someone else that runs on your machine, so each one should have a reason to be here.

## Direct dependencies

| Package | Version | Why we use it |
|---|---|---|
| fastembed | 0.7.4 | Runs the embedding model that turns text into numbers for searching by meaning. It works on a laptop without a paid API |

## Indirect dependencies

### Running the model

| Package | Version | Needed by | Why it's needed |
|---|---|---|---|
| onnxruntime | 1.31.1 | fastembed | Runs the embedding model |
| tokenizers | 0.23.3 | fastembed | Splits text into the tokens the model reads |
| numpy | 2.5.4 | fastembed, onnxruntime | Stores and calculates with the embedding numbers |
| flatbuffers | 25.12.19 | onnxruntime | Reads an efficient binary data format |
| protobuf | 7.36.2 | onnxruntime | Reads the binary format used by ONNX models |

### Downloading the model

| Package | Version | Needed by | Why it's needed |
|---|---|---|---|
| huggingface_hub | 1.33.0 | fastembed, tokenizers | Downloads models from Hugging Face |
| hf-xet | 1.8.0 | huggingface_hub | Transfers large model files |
| fsspec | 2026.9.0 | huggingface_hub | Provides one way to work with different file locations |
| filelock | 4.2.7 | huggingface_hub | Stops two downloads from writing the same file at once |
| PyYAML | 6.0.3 | huggingface_hub | Reads YAML, a text format used for settings and metadata |
| click | 8.5.0 | huggingface_hub | Builds Hugging Face's command-line tools |
| tqdm | 4.70.1 | fastembed, huggingface_hub | Shows progress bars |

### Network connections

| Package | Version | Needed by | Why it's needed |
|---|---|---|---|
| requests | 2.34.2 | fastembed | Makes web requests |
| urllib3 | 2.8.0 | requests | Handles the connections behind `requests` |
| httpx | 0.28.1 | huggingface_hub | Makes web requests |
| httpcore | 1.0.9 | httpx | Handles the connections behind `httpx` |
| h11 | 0.16.0 | httpcore | Reads and writes HTTP/1.1 messages |
| anyio | 4.16.0 | httpx | Runs asynchronous network code, similar in spirit to Kotlin coroutines |
| certifi | 2026.10.23 | requests, httpx, httpcore | Provides the trusted certificates used to verify HTTPS sites |
| idna | 3.20 | requests, httpx, anyio | Handles international domain names |
| charset-normalizer | 3.5.2 | requests | Detects how downloaded text is encoded |

### Required by fastembed, but not used by our search

fastembed supports more than our text search, so it installs these too. They still run on your machine and still need security updates.

| Package | Version | Why fastembed includes it |
|---|---|---|
| pillow | 11.3.0 | Processes images for image embedding models |
| mmh3 | 5.3.1 | Provides fast hashing for sparse text models |
| py_rust_stemmers | 0.1.8 | Reduces words to their root form for sparse text models |
| loguru | 0.7.3 | Writes log messages |

### Shared helpers

| Package | Version | Needed by | Why it's needed |
|---|---|---|---|
| packaging | 26.3 | huggingface_hub, onnxruntime | Reads and compares version numbers |
| typing_extensions | 4.16.0 | huggingface_hub, anyio | Adds newer Python type features |

### Tooling

| Package | Version | Why it's here |
|---|---|---|
| pip | 26.1.2 | Installs Python packages. It comes with every virtual environment |
