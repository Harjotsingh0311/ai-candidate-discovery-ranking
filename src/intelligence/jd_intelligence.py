import json
import re
from pathlib import Path

INPUT="artifacts/job_profile.json"

OUTPUT="artifacts/jd_analysis.json"

with open(INPUT,"r",encoding="utf-8") as f:
    jd=json.load(f)

text=jd["job_text"].lower()

skills=[]

skill_bank=[

"python",
"llm",
"retrieval",
"ranking",
"embedding",
"embeddings",
"vector database",
"faiss",
"pinecone",
"qdrant",
"milvus",
"hybrid search",
"langchain",
"evaluation",
"ndcg",
"mrr",
"map",
"fine-tuning",
"lora",
"qlora",
"peft",
"xgboost",
"recommendation"

]

for skill in skill_bank:

    if skill in text:

        skills.append(skill)

experience=re.search(r"(\d+)\s*-\s*(\d+)\s*years",text)

if experience:

    min_exp=int(experience.group(1))
    max_exp=int(experience.group(2))

else:

    min_exp=0
    max_exp=50

anti=[]

bad_words=[

"consulting",

"research",

"robotics",

"speech",

"computer vision"

]

for word in bad_words:

    if word in text:

        anti.append(word)

analysis={

"required_skills":skills,

"minimum_experience":min_exp,

"maximum_experience":max_exp,

"anti_patterns":anti

}

with open(OUTPUT,"w") as f:

    json.dump(analysis,f,indent=4)

print("JD Intelligence Built")