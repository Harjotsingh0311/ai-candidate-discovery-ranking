import json
from pathlib import Path

import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[2]

INPUT_FILE = PROJECT_ROOT / "artifacts" / "final_ranked.json"
OUTPUT_FILE = PROJECT_ROOT / "submission.csv"

# -------------------------------------------------------
# Load ranked candidates
# -------------------------------------------------------

with open(INPUT_FILE, "r", encoding="utf-8") as f:
    candidates = json.load(f)

print(f"Loaded {len(candidates)} ranked candidates.")

# -------------------------------------------------------
# Remove duplicate candidate IDs
# -------------------------------------------------------

unique_candidates = []
seen = set()

for candidate in candidates:

    cid = candidate["candidate_id"]

    if cid in seen:
        continue

    seen.add(cid)
    unique_candidates.append(candidate)

print(f"Unique candidates: {len(unique_candidates)}")

# -------------------------------------------------------
# Sort by score
# -------------------------------------------------------

unique_candidates = sorted(
    unique_candidates,
    key=lambda x: (
        -float(x.get("final_score", 0)),
        x["candidate_id"]
    )
)

# -------------------------------------------------------
# Build submission rows
# -------------------------------------------------------

rows = []

for rank, candidate in enumerate(unique_candidates, start=1):

    score = round(
        float(candidate.get("final_score", 0)),
        2
    )

    reasoning = candidate.get(
        "reasoning",
        "Hybrid AI ranking."
    )

    rows.append(
        {
            "candidate_id": candidate["candidate_id"],
            "rank": rank,
            "score": score,
            "reasoning": reasoning[:200]
        }
    )

df = pd.DataFrame(rows)

# -------------------------------------------------------
# Save CSV
# -------------------------------------------------------

df.to_csv(
    OUTPUT_FILE,
    index=False
)

print("\nSubmission generated successfully!")

print(f"Saved to: {OUTPUT_FILE}")

print("\nTop 10 Candidates\n")

print(df.head(10))

print("\nSubmission Shape:", df.shape)