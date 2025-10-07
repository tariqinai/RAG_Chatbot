ragbot/
├─ apps/
│  ├─ api/                      # FastAPI service (retrieve → rerank → generate)
│  │  ├─ src/ragbot_api/
│  │  │  ├─ __init__.py
│  │  │  ├─ main.py             # app entrypoint
│  │  │  ├─ routers/            # /search, /chat, /ingest hooks
│  │  │  ├─ schemas/            # Pydantic models
│  │  │  └─ services/           # retrieval, rerank, llm adapters
│  │  └─ tests/
│  └─ ui/                       # MVP UI (Streamlit) or Next.js later
│     ├─ streamlit_app.py
│     └─ public/                # logos, demo assets
│
├─ services/
│  ├─ ingester/                  # watches folders/urls (Phase 1)
│  │  ├─ src/ingester/
│  │  │  ├─ __init__.py
│  │  │  ├─ main.py             # CLI/daemon
│  │  │  └─ sources/            # handlers: local, http, (Airbyte later)
│  ├─ parser/                    # Unstructured/OCR → clean sections/chunks
│  │  └─ src/parser/
│  └─ indexer/                   # embeddings + Qdrant/OpenSearch writers
│     └─ src/indexer/
│
├─ libs/
│  └─ common/                    # shared utils (logging, config, ids)
│     ├─ __init__.py
│     ├─ config.py
│     └─ logging.py
│
├─ data/
│  ├─ raw/                       # original files (pdf, html)
│  ├─ processed/                 # chunked jsonl (Phase 0/1 output)
│  └─ goldset/                   # eval Q/A & labels
│
├─ ops/
│  ├─ docker/                    # docker-compose.dev.yml + Dockerfiles
│  ├─ k8s/                       # helm charts (later)
│  └─ sql/                       # schema/migrations (SQLite → Postgres later)
│
├─ configs/
│  ├─ sources.yml                # registry of folders/urls to ingest
│  └─ settings.example.toml      # app-level config sample
│
├─ scripts/                      # one-off CLIs (e.g., ingest_pdf.py)
├─ notebooks/                    # experiments/debug
├─ .env.example
├─ .gitignore
├─ pyproject.toml                # (or requirements.txt) package deps
└─ README.md
