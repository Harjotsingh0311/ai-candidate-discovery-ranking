from typing import List

REQUIRED_SKILLS = {
    "embeddings",
    "retrieval",
    "ranking",
    "vector database",
    "hybrid search",
    "python",
    "llm",
    "fine-tuning",
    "evaluation",
    "ndcg",
    "mrr",
    "map"
}


def calculate_skill_score(candidate_skills: List[dict]):

    skills = {
        skill["name"].lower()
        for skill in candidate_skills
    }

    matches = 0

    for req in REQUIRED_SKILLS:

        for skill in skills:

            if req in skill or skill in req:
                matches += 1
                break

    return matches / len(REQUIRED_SKILLS)