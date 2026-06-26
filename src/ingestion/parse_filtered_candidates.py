import json
from pathlib import Path
from tqdm import tqdm

INPUT_FILE = Path(
    "artifacts/filtered_candidates.json"
)

OUTPUT_FILE = Path(
    "artifacts/processed/filtered_processed.json"
)

with open(INPUT_FILE, "r", encoding="utf-8") as f:
    candidates = json.load(f)

processed = []

for candidate in tqdm(candidates):

    profile = candidate["profile"]

    skills = "\n".join([
        f"{s['name']} ({s['proficiency']})"
        for s in candidate["skills"]
    ])

    career = "\n".join([
        f"{job['title']} at {job['company']}. {job['description']}"
        for job in candidate["career_history"]
    ])

    text = f"""
Headline:
{profile['headline']}

Summary:
{profile['summary']}

Current Title:
{profile['current_title']}

Experience:
{profile['years_of_experience']}

Skills:
{skills}

Career:
{career}
"""

    processed.append({

        "candidate_id":
        candidate["candidate_id"],

        "text":
        text,

        "years_exp":
        profile["years_of_experience"]

    })

with open(
    OUTPUT_FILE,
    "w",
    encoding="utf-8"
) as f:

    json.dump(processed, f)

print(
    f"Processed: {len(processed)}"
)