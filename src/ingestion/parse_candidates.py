# src/ingestion/parse_candidates.py

import json
from pathlib import Path
from tqdm import tqdm

DATA_FILE = Path(
    "data/India_runs_data_and_ai_challenge/candidates.jsonl"
)

OUTPUT_FILE = Path(
    "artifacts/processed/candidates_processed.json"
)

processed = []

with open(DATA_FILE, "r", encoding="utf-8") as f:

    for line in tqdm(f):

        candidate = json.loads(line)

        profile = candidate["profile"]

        skills = "\n".join(
            [
                f"{s['name']} ({s['proficiency']})"
                for s in candidate["skills"]
            ]
        )

        career = "\n".join(
            [
                f"{job['title']} at {job['company']}: {job['description']}"
                for job in candidate["career_history"]
            ]
        )

        education = "\n".join(
            [
                f"{e['degree']} in {e['field_of_study']} from {e['institution']}"
                for e in candidate["education"]
            ]
        )

        text = f"""
Candidate ID: {candidate['candidate_id']}

Headline:
{profile['headline']}

Summary:
{profile['summary']}

Experience:
{profile['years_of_experience']} years

Current Title:
{profile['current_title']}

Current Company:
{profile['current_company']}

Current Industry:
{profile['current_industry']}

Skills:
{skills}

Career History:
{career}

Education:
{education}
"""

        processed.append(
            {
                "candidate_id": candidate["candidate_id"],
                "text": text,
                "years_experience":
                profile["years_of_experience"]
            }
        )

with open(
    OUTPUT_FILE,
    "w",
    encoding="utf-8"
) as f:

    json.dump(processed, f)

print("Done")
print(len(processed))