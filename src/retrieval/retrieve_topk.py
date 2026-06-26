import json
import chromadb
from sentence_transformers import SentenceTransformer

client = chromadb.PersistentClient(
    path="artifacts/chroma_db"
)

collection = client.get_collection(
    "candidate_profiles"
)

model = SentenceTransformer(
    "BAAI/bge-base-en-v1.5"
)

with open(
    "artifacts/job_profile.json",
    "r",
    encoding="utf-8"
) as f:

    job = json.load(f)

query_embedding = model.encode(
    job["job_text"],
    normalize_embeddings=True
)

results = collection.query(
    query_embeddings=[
        query_embedding.tolist()
    ],
    n_results=2000
)

with open(
    "artifacts/top2000.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(results, f)

print("Top 2000 retrieved")