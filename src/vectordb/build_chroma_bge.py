import json
import shutil
from pathlib import Path

import chromadb
from tqdm import tqdm
from sentence_transformers import SentenceTransformer

# ==================================================
# CONFIG
# ==================================================

INPUT_FILE = Path(
    "artifacts/processed/filtered_processed.json"
)

CHROMA_PATH = Path(
    "artifacts/chroma_db"
)

COLLECTION_NAME = "candidate_profiles"

BATCH_SIZE = 128

# ==================================================
# CLEAN OLD CHROMA DB
# ==================================================

if CHROMA_PATH.exists():
    print("Removing old ChromaDB...")
    shutil.rmtree(CHROMA_PATH)

# ==================================================
# CREATE FRESH CHROMA
# ==================================================

client = chromadb.PersistentClient(
    path=str(CHROMA_PATH)
)

collection = client.create_collection(
    name=COLLECTION_NAME
)

# ==================================================
# LOAD MODEL
# ==================================================

print("Loading BGE model...")

model = SentenceTransformer(
    "BAAI/bge-base-en-v1.5"
)

# ==================================================
# LOAD CANDIDATES
# ==================================================

with open(
    INPUT_FILE,
    "r",
    encoding="utf-8"
) as f:

    candidates = json.load(f)

print(f"\nCandidates Loaded: {len(candidates):,}")

# ==================================================
# BUILD VECTOR STORE
# ==================================================

for i in tqdm(
    range(0, len(candidates), BATCH_SIZE),
    desc="Embedding Candidates"
):

    batch = candidates[i:i + BATCH_SIZE]

    docs = [
        c["text"]
        for c in batch
    ]

    ids = [
        c["candidate_id"]
        for c in batch
    ]

    metadatas = [
        {
            "years_exp": float(
                c["years_exp"]
            )
        }
        for c in batch
    ]

    embeddings = model.encode(
        docs,
        batch_size=64,
        normalize_embeddings=True,
        convert_to_numpy=True,
        show_progress_bar=False
    )

    collection.add(
        ids=ids,
        documents=docs,
        embeddings=embeddings.tolist(),
        metadatas=metadatas
    )

print("\nChromaDB Build Complete!")

print(
    f"Collection: {COLLECTION_NAME}"
)

print(
    f"Total Candidates: {len(candidates):,}"
)