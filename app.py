import json
from pathlib import Path

import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="AI Candidate Discovery",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Candidate Discovery & Ranking System")

st.caption(
    "Semantic Search • ChromaDB • BGE Embeddings • Groq AI"
)

rank_file = Path("artifacts/final_ranked.json")

if not rank_file.exists():

    st.warning("Run the ranking pipeline first.")

    st.stop()

with open(rank_file,"r",encoding="utf-8") as f:

    candidates=json.load(f)

df=pd.DataFrame(candidates)

# --------------------------------------------------

c1,c2,c3,c4=st.columns(4)

c1.metric(
    "Candidates Ranked",
    len(df)
)

c2.metric(
    "Top Score",
    round(df["final_score"].max(),2)
)

c3.metric(
    "Average Score",
    round(df["final_score"].mean(),2)
)

c4.metric(
    "Average Experience",
    round(
        df["profile"].apply(
            lambda x:x["years_of_experience"]
        ).mean(),
        1
    )
)

st.divider()

st.subheader("🏆 Top 10 Candidates")

show=[]

for candidate in candidates[:10]:

    show.append({

        "Rank":

        len(show)+1,

        "Candidate":

        candidate["candidate_id"],

        "Current Role":

        candidate["profile"]["current_title"],

        "Experience":

        candidate["profile"]["years_of_experience"],

        "Score":

        candidate["final_score"]

    })

st.dataframe(

    pd.DataFrame(show),

    use_container_width=True,

    hide_index=True

)

st.divider()

st.success("Pipeline Completed Successfully ✅")