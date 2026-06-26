import json
from pathlib import Path

import chromadb
from sentence_transformers import SentenceTransformer
from tqdm import tqdm

# ==========================================================
# PATHS
# ==========================================================

CHROMA_PATH = "artifacts/chroma_db"

JOB_FILE = Path("artifacts/job_profile.json")

CANDIDATE_FILE = Path(
    "artifacts/filtered_candidates.json"
)

OUTPUT_FILE = Path(
    "artifacts/top2000_candidates.json"
)

# ==========================================================
# LOAD CHROMADB
# ==========================================================

print("Loading ChromaDB...")

client = chromadb.PersistentClient(path=CHROMA_PATH)

collection = client.get_collection(
    "candidate_profiles"
)

# ==========================================================
# LOAD EMBEDDING MODEL
# ==========================================================

print("Loading BGE model...")

model = SentenceTransformer(
    "BAAI/bge-base-en-v1.5"
)

# ==========================================================
# LOAD JOB DESCRIPTION
# ==========================================================

with open(JOB_FILE, "r", encoding="utf-8") as f:
    job = json.load(f)

query = job["job_text"]

print("Generating query embedding...")

query_embedding = model.encode(
    query,
    normalize_embeddings=True,
    convert_to_numpy=True
)

# ==========================================================
# RETRIEVE TOP 2000
# ==========================================================

print("Searching ChromaDB...")

results = collection.query(
    query_embeddings=[query_embedding.tolist()],
    n_results=2000
)

retrieved_ids = results["ids"][0]
retrieved_distances = results["distances"][0]

semantic_scores = {}

for cid, distance in zip(retrieved_ids, retrieved_distances):

    semantic_scores[cid] = 1 - distance

# ==========================================================
# LOAD FILTERED CANDIDATES
# ==========================================================

print("Loading candidate database...")

with open(
    CANDIDATE_FILE,
    "r",
    encoding="utf-8"
) as f:

    candidates = json.load(f)

candidate_lookup = {
    c["candidate_id"]: c
    for c in candidates
}

# ==========================================================
# BUILD TOP2000 DATASET
# ==========================================================

top_candidates = []

print("Preparing retrieved candidates...")

for cid in tqdm(retrieved_ids):

    if cid not in candidate_lookup:
        continue

    candidate = candidate_lookup[cid]

    candidate["semantic_score"] = semantic_scores[cid]

    top_candidates.append(candidate)

# ==========================================================
# SAVE
# ==========================================================

with open(
    OUTPUT_FILE,
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        top_candidates,
        f,
        indent=4
    )

print("\nDone!")

print(f"Retrieved Candidates : {len(top_candidates)}")

print(f"Saved to : {OUTPUT_FILE}")