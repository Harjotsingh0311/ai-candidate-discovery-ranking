from pathlib import Path
from docx import Document
import json
import re

JD_PATH = Path(
    "data/India_runs_data_and_ai_challenge/job_description.docx"
)

OUTPUT_PATH = Path(
    "artifacts/job_profile.json"
)

doc = Document(JD_PATH)

text = "\n".join(
    [p.text for p in doc.paragraphs if p.text.strip()]
)

required_skills = [
    "embeddings",
    "retrieval",
    "ranking",
    "llm",
    "fine-tuning",
    "vector database",
    "hybrid search",
    "evaluation",
    "ndcg",
    "mrr",
    "map",
    "python",
    "a/b testing"
]

preferred_skills = [
    "lora",
    "qlora",
    "peft",
    "learning-to-rank",
    "xgboost",
    "distributed systems",
    "hr-tech",
    "recommendation systems"
]

anti_patterns = [
    "consulting only",
    "pure research",
    "computer vision only",
    "speech only",
    "robotics only"
]

job_profile = {
    "job_text": text,
    "required_skills": required_skills,
    "preferred_skills": preferred_skills,
    "anti_patterns": anti_patterns,
}

OUTPUT_PATH.parent.mkdir(exist_ok=True)

with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    json.dump(job_profile, f, indent=4)

print("Job profile saved.")