import json
from pathlib import Path
from tqdm import tqdm

INPUT_FILE = Path(
    "data/India_runs_data_and_ai_challenge/candidates.jsonl"
)

OUTPUT_FILE = Path(
    "artifacts/features.json"
)

CONSULTING = {
    "TCS",
    "Infosys",
    "Wipro",
    "Accenture",
    "Cognizant",
    "Capgemini",
    "HCL"
}

features = []

with open(INPUT_FILE, "r", encoding="utf-8") as f:

    for line in tqdm(f):

        candidate = json.loads(line)

        profile = candidate["profile"]
        signals = candidate["redrob_signals"]

        companies = [
            job["company"]
            for job in candidate["career_history"]
        ]

        consulting_count = sum(
            company in CONSULTING
            for company in companies
        )

        job_hops = len(candidate["career_history"])

        github_score = signals.get(
            "github_activity_score",
            0
        )

        recruiter_response = signals.get(
            "recruiter_response_rate",
            0
        )

        interview_rate = signals.get(
            "interview_completion_rate",
            0
        )

        open_to_work = int(
            signals.get(
                "open_to_work_flag",
                False
            )
        )

        profile_score = signals.get(
            "profile_completeness_score",
            0
        )

        features.append({

            "candidate_id":
            candidate["candidate_id"],

            "years_exp":
            profile["years_of_experience"],

            "job_hops":
            job_hops,

            "consulting_count":
            consulting_count,

            "github_score":
            github_score,

            "recruiter_response":
            recruiter_response,

            "interview_rate":
            interview_rate,

            "open_to_work":
            open_to_work,

            "profile_score":
            profile_score
        })

with open(
    OUTPUT_FILE,
    "w",
    encoding="utf-8"
) as f:

    json.dump(features, f)

print("Feature extraction complete")