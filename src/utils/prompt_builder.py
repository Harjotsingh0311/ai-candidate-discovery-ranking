import json


def summarize_behavior(signals):

    return {
        "github": signals.get("github_activity_score", -1),
        "response_rate": signals.get("recruiter_response_rate", 0),
        "profile_complete": signals.get("profile_completeness_score", 0),
        "interview_completion": signals.get("interview_completion_rate", 0),
        "open_to_work": signals.get("open_to_work_flag", False),
        "saved_by_recruiters": signals.get("saved_by_recruiters_30d", 0),
        "search_appearances": signals.get("search_appearance_30d", 0)
    }


def summarize_career(history):

    summary = []

    for job in history[-3:]:

        summary.append({
            "title": job["title"],
            "company": job["company"],
            "industry": job["industry"]
        })

    return summary


def build_prompt(job, candidate):

    skills = sorted([
        skill["name"]
        for skill in candidate["skills"]
    ])[:12]

    behaviour = summarize_behavior(
        candidate["redrob_signals"]
    )

    career = summarize_career(
        candidate["career_history"]
    )

    prompt = f"""
You are an expert Senior Technical Recruiter.

Evaluate ONE candidate for ONE job.

Return ONLY JSON.

Job Summary
-----------
Role:
Senior AI Engineer

Must Have Skills:
Embeddings
Retrieval
Ranking
Hybrid Search
Vector Databases
Python
Evaluation Metrics
LLMs
Fine-tuning

Preferred Experience:
5-9 years

Candidate
---------

Headline:
{candidate["profile"]["headline"]}

Current Role:
{candidate["profile"]["current_title"]}

Experience:
{candidate["profile"]["years_of_experience"]} years

Skills:
{", ".join(skills)}

Recent Career:
{json.dumps(career, indent=2)}

Behaviour:
{json.dumps(behaviour, indent=2)}

Hybrid Score:
{round(candidate["hybrid_score"],3)}

Respond ONLY with

{{
"technical_match":95,
"product_fit":90,
"startup_fit":92,
"overall_score":93,
"reasoning":"Maximum 25 words."
}}
"""

    return prompt