# scripts/bootstrap_structure.py
from __future__ import annotations
import os
from pathlib import Path
from textwrap import dedent

ROOT = Path(__file__).resolve().parents[1]  # repo root
mk = lambda p: (ROOT / p).mkdir(parents=True, exist_ok=True)

# --- 0. create directories ---
dirs = [
    "apps/api/src/ragbot_api/routers",
    "apps/api/src/ragbot_api/schemas",
    "apps/api/src/ragbot_api/services",
    "apps/ui/public",
    "services/ingester/src/ingester/sources",
    "services/parser/src/parser",
    "services/indexer/src/indexer",
    "libs/common",
    "data/raw",
    "data/processed",
    "data/goldset",
    "ops/docker",
    "ops/k8s",
    "ops/sql",
    "configs",
    "scripts",
    "notebooks",
]
for d in dirs:
    mk(d)

# --- 1. helper to write a file if missing ---
def write_if_absent(rel, content):
    path = ROOT / rel
    if not path.exists():
        path.write_text(dedent(content).lstrip(), encoding="utf-8")
        print("created:", rel)
    else:
        print("skip (exists):", rel)

# --- 2. python package __init__.py files ---
for pkg in [
    "apps/api/src/ragbot_api",
    "apps/api/src/ragbot_api/routers",
    "apps/api/src/ragbot_api/schemas",
    "apps/api/src/ragbot_api/services",
    "services/ingester/src/ingester",
    "services/ingester/src/ingester/sources",
    "services/parser/src/parser",
    "services/indexer/src/indexer",
    "libs/common",
]:
    write_if_absent(f"{pkg}/__init__.py", "# package\n")

# --- 3. API stub (FastAPI) ---
write_if_absent(
    "apps/api/src/ragbot_api/main.py",
    """
    from fastapi import FastAPI

    app = FastAPI(title="RAGBot API", version="0.1.0")

    @app.get("/health")
    def health():
        return {"status": "ok"}
    """
)

# --- 4. UI stub (Streamlit) ---
write_if_absent(
    "apps/ui/streamlit_app.py",
    """
    import streamlit as st

    st.set_page_config(page_title="RAGBot", page_icon="🤖", layout="wide")
    st.title("RAGBot — MVP")
    st.write("Hello! UI will come after backend is ready.")
    """
)

# --- 5. Ingester daemon stub ---
write_if_absent(
    "services/ingester/src/ingester/main.py",
    """
    import time
    def run():
        print("Ingester daemon placeholder — folder watcher will go here.")
        while False:
            time.sleep(1)

    if __name__ == "__main__":
        run()
    """
)

# --- 6. Parser stub (we'll move notebook funcs here later) ---
write_if_absent(
    "services/parser/src/parser/chunker.py",
    """
    # placeholder for clean_text, chunk_text, parse_pdf_to_chunks functions
    """
)

# --- 7. Indexer stub ---
write_if_absent(
    "services/indexer/src/indexer/embedder.py",
    """
    # placeholder for embedding & vector DB writers
    """
)

# --- 8. shared config/logging ---
write_if_absent(
    "libs/common/config.py",
    """
    from pydantic import BaseModel
    class Settings(BaseModel):
        data_dir: str = "./data"
    settings = Settings()
    """
)
write_if_absent(
    "libs/common/logging.py",
    """
    import logging
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    logger = logging.getLogger("ragbot")
    """
)

# --- 9. sources.yml sample ---
write_if_absent(
    "configs/sources.yml",
    """
    # MVP registry of sources
    local_folders:
      - path: data/raw
        recursive: false

    url_lists:
      - file: configs/urls.txt  # create this file if you want URLs
    """
)

# --- 10. .env.example ---
write_if_absent(
    ".env.example",
    """
    RAG_ENV=dev
    DATA_DIR=./data
    EMBED_MODEL=sentence-transformers/all-MiniLM-L6-v2
    """
)

# --- 11. README stub ---
write_if_absent(
    "README.md",
    """
    # RAGBot
    End-to-end Retrieval-Augmented Generation chatbot.

    ## Dev quickstart
    - Create env: `mamba env create -f environment.yml && mamba activate ragbot`
    - Put a PDF in `data/raw/`
    - Run micro-ingest notebook or cells to create JSONL chunks & embeddings
    """
)

print("Done.")
