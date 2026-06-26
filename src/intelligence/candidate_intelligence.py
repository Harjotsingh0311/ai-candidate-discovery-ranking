import json
from tqdm import tqdm

INPUT="artifacts/top2000_candidates.json"

OUTPUT="artifacts/candidate_features.json"

KEYWORDS={

"retrieval",

"ranking",

"recommendation",

"llm",

"embedding",

"vector",

"search",

"rag"

}

results=[]

with open(INPUT,"r",encoding="utf-8") as f:

    candidates=json.load(f)

for candidate in tqdm(candidates):

    skills={

        s["name"].lower()

        for s in candidate["skills"]

    }

    tech=sum(

        1

        for keyword in KEYWORDS

        if any(keyword in skill for skill in skills)

    )

    technical_score=tech/len(KEYWORDS)

    titles=" ".join(

        job["title"].lower()

        for job in candidate["career_history"]

    )

    startup_fit=0.5

    if "lead" in titles:

        startup_fit+=0.1

    if "senior" in titles:

        startup_fit+=0.1

    if "manager" in titles:

        startup_fit+=0.1

    results.append({

        "candidate_id":

        candidate["candidate_id"],

        "technical_score":

        technical_score,

        "startup_fit":

        startup_fit

    })

with open(

    OUTPUT,

    "w"

) as f:

    json.dump(results,f,indent=4)

print("Candidate Intelligence Built")