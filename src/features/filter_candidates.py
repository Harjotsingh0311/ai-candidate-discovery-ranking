import json
from pathlib import Path
from tqdm import tqdm

INPUT_FILE = Path(
    "data/India_runs_data_and_ai_challenge/candidates.jsonl"
)

OUTPUT_FILE = Path(
    "artifacts/filtered_candidates.json"
)

AI_KEYWORDS = {

    "llm",
    "rag",
    "retrieval",
    "ranking",
    "search",
    "recommendation",
    "recommendations",
    "nlp",
    "transformer",
    "transformers",
    "embedding",
    "embeddings",
    "fine-tuning",
    "fine tuning",
    "vector",
    "langchain",
    "machine learning",
    "deep learning",
    "generative ai",
    "genai",
    "pytorch",
    "tensorflow"
}

filtered = []

with open(INPUT_FILE, "r", encoding="utf-8") as f:

    for line in tqdm(f):

        candidate = json.loads(line)

        profile = candidate["profile"]

        years_exp = profile["years_of_experience"]

        if years_exp < 4:
            continue

        if years_exp > 12:
            continue

        candidate_text = ""

        candidate_text += profile.get(
            "headline", ""
        ).lower()

        candidate_text += " "

        candidate_text += profile.get(
            "summary", ""
        ).lower()

        for skill in candidate["skills"]:

            candidate_text += (
                " " +
                skill["name"].lower()
            )

        match = any(
            keyword in candidate_text
            for keyword in AI_KEYWORDS
        )

        if match:
            filtered.append(candidate)

with open(
    OUTPUT_FILE,
    "w",
    encoding="utf-8"
) as f:

    json.dump(filtered, f)

print(
    f"Filtered Candidates: {len(filtered)}"
)