import json

from skill_score import calculate_skill_score
from experience_score import calculate_experience_score
from behavior_score import calculate_behavior_score
from company_score import calculate_company_score
from career_score import calculate_career_score

INPUT = "artifacts/top2000_candidates.json"

OUTPUT = "artifacts/top100_candidates.json"

with open(INPUT,"r",encoding="utf-8") as f:

    candidates=json.load(f)

results=[]

for candidate in candidates:

    semantic=candidate["semantic_score"]

    skill=calculate_skill_score(
        candidate["skills"]
    )

    experience=calculate_experience_score(
        candidate["profile"]["years_of_experience"]
    )

    behaviour=calculate_behavior_score(
        candidate["redrob_signals"]
    )

    company=calculate_company_score(
        candidate["career_history"]
    )

    career=calculate_career_score(
        candidate["career_history"]
    )

    final=(

        semantic*0.35+

        skill*0.20+

        experience*0.15+

        behaviour*0.20+

        company*0.05+

        career*0.05

    )

    candidate["hybrid_score"]=round(final,4)

    results.append(candidate)

results=sorted(

    results,

    key=lambda x:x["hybrid_score"],

    reverse=True

)

results=results[:100]

with open(

    OUTPUT,

    "w",

    encoding="utf-8"

) as f:

    json.dump(results,f,indent=4)

print("Hybrid Ranking Complete")

print(f"Top Candidates : {len(results)}")