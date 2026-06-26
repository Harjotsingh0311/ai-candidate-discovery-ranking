import json
import os
import sys
import time
from pathlib import Path

from dotenv import load_dotenv
from groq import Groq

# -------------------------------------------------------
# Fix Imports
# -------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[2]

sys.path.append(str(PROJECT_ROOT))

from src.utils.prompt_builder import build_prompt

# -------------------------------------------------------
# Environment
# -------------------------------------------------------

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

MODEL = "llama-3.1-8b-instant"

# -------------------------------------------------------
# Files
# -------------------------------------------------------

TOP100_FILE = PROJECT_ROOT / "artifacts" / "top100_candidates.json"

OUTPUT_FILE = PROJECT_ROOT / "artifacts" / "final_ranked.json"

CHECKPOINT_FILE = PROJECT_ROOT / "artifacts" / "groq_checkpoint.json"

# -------------------------------------------------------
# Load Candidates
# -------------------------------------------------------

with open(TOP100_FILE, "r", encoding="utf-8") as f:
    candidates = json.load(f)

# -------------------------------------------------------
# Only rerank Top 20
# -------------------------------------------------------

TOP_K = 20

top_candidates = candidates[:TOP_K]

remaining_candidates = candidates[TOP_K:]

# -------------------------------------------------------
# Resume Support
# -------------------------------------------------------

completed = {}

if CHECKPOINT_FILE.exists():

    with open(CHECKPOINT_FILE, "r") as f:

        completed = json.load(f)

print(f"\nLoaded {len(completed)} completed candidates.\n")

# -------------------------------------------------------
# Load JD
# -------------------------------------------------------

with open(
    PROJECT_ROOT / "artifacts" / "job_profile.json",
    "r",
    encoding="utf-8"
) as f:

    job = json.load(f)

results = []

# -------------------------------------------------------
# Evaluate
# -------------------------------------------------------

for index, candidate in enumerate(top_candidates):

    cid = candidate["candidate_id"]

    if cid in completed:

        print(f"Skipping {cid}")

        results.append(completed[cid])

        continue

    print(f"\n[{index+1}/{TOP_K}] {cid}")

    prompt = build_prompt(job, candidate)

    try:

        response = client.chat.completions.create(

            model=MODEL,

            temperature=0,

            response_format={
                "type": "json_object"
            },

            messages=[

                {
                    "role":"system",
                    "content":"You are a senior AI recruiter."
                },

                {
                    "role":"user",
                    "content":prompt
                }

            ]

        )

        answer = json.loads(
            response.choices[0].message.content
        )

        llm_score = float(
            answer.get(
                "overall_score",
                candidate["hybrid_score"] * 100
            )
        )

        reasoning = answer.get(
            "reasoning",
            "No reasoning."
        )

    except Exception as e:

        print("\nGroq Error")

        print(e)

        llm_score = candidate["hybrid_score"] * 100

        reasoning = "Fallback to hybrid score."

    candidate["llm_score"] = round(llm_score, 2)

    candidate["reasoning"] = reasoning

    candidate["final_score"] = round(

        candidate["hybrid_score"] * 60 +

        llm_score * 0.40,

        2

    )

    results.append(candidate)

    completed[cid] = candidate

    with open(

        CHECKPOINT_FILE,

        "w",

        encoding="utf-8"

    ) as f:

        json.dump(

            completed,

            f,

            indent=4

        )

    time.sleep(1)

# -------------------------------------------------------
# Merge Remaining Candidates
# -------------------------------------------------------

for candidate in remaining_candidates:

    candidate["llm_score"] = None

    candidate["reasoning"] = "Ranked using Hybrid AI Recruiter."

    candidate["final_score"] = round(

        candidate["hybrid_score"] * 100,

        2

    )

    results.append(candidate)

# -------------------------------------------------------
# Final Sort
# -------------------------------------------------------

results = sorted(

    results,

    key=lambda x: x["final_score"],

    reverse=True

)

with open(

    OUTPUT_FILE,

    "w",

    encoding="utf-8"

) as f:

    json.dump(

        results,

        f,

        indent=4

    )

print("\n===================================")

print("Groq Validation Complete")

print(f"Candidates Evaluated : {TOP_K}")

print("Saved : artifacts/final_ranked.json")

print("===================================")