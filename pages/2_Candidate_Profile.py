import json
from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="Candidate Explorer",
    page_icon="👤",
    layout="wide"
)

st.title("👤 Candidate Explorer")

FILE = Path("artifacts/final_ranked.json")

if not FILE.exists():
    st.error("Run the ranking pipeline first.")
    st.stop()

with open(FILE, "r", encoding="utf-8") as f:
    candidates = json.load(f)

candidate_map = {
    c["candidate_id"]: c
    for c in candidates
}

selected = st.selectbox(
    "Select Candidate",
    list(candidate_map.keys())
)

candidate = candidate_map[selected]

profile = candidate["profile"]

# --------------------------------------------------------
# Header
# --------------------------------------------------------

col1, col2 = st.columns([3, 1])

with col1:

    st.header(profile["headline"])

    st.write(profile["summary"])

    st.caption(
        f"{profile['current_company']} • {profile['location']}, {profile['country']}"
    )

with col2:

    st.metric("⭐ Final Score", candidate["final_score"])

    st.metric(
        "Hybrid",
        round(candidate["hybrid_score"], 3)
    )

    st.metric(
        "Experience",
        f"{profile['years_of_experience']} yrs"
    )

st.divider()

# --------------------------------------------------------
# Tabs
# --------------------------------------------------------

tab1, tab2, tab3, tab4 = st.tabs([
    "🛠 Skills",
    "💼 Career",
    "📊 Behaviour",
    "🧠 AI Analysis"
])

# --------------------------------------------------------
# Skills
# --------------------------------------------------------

with tab1:

    skills = pd.DataFrame(candidate["skills"])

    st.dataframe(
        skills,
        use_container_width=True,
        hide_index=True
    )

    fig = px.bar(
        skills,
        x="name",
        y="endorsements",
        color="proficiency",
        title="Skill Endorsements"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# --------------------------------------------------------
# Career
# --------------------------------------------------------

with tab2:

    history = pd.DataFrame(candidate["career_history"])

    st.dataframe(
        history,
        use_container_width=True,
        hide_index=True
    )

    timeline = history.copy()

    timeline["duration"] = timeline["duration_months"]

    fig = px.bar(
        timeline,
        x="duration",
        y="company",
        orientation="h",
        color="industry",
        title="Career Timeline"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# --------------------------------------------------------
# Behaviour
# --------------------------------------------------------

with tab3:

    behaviour = candidate["redrob_signals"]

    metrics = pd.DataFrame({

        "Metric":[
            "Github",
            "Recruiter Response",
            "Interview Completion",
            "Profile Complete",
            "Search Appearances",
            "Recruiter Saves"
        ],

        "Value":[
            behaviour["github_activity_score"],
            behaviour["recruiter_response_rate"]*100,
            behaviour["interview_completion_rate"]*100,
            behaviour["profile_completeness_score"],
            behaviour["search_appearance_30d"],
            behaviour["saved_by_recruiters_30d"]
        ]

    })

    fig = px.bar(
        metrics,
        x="Metric",
        y="Value",
        color="Value",
        title="Behaviour Analysis"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# --------------------------------------------------------
# AI Analysis
# --------------------------------------------------------

with tab4:

    st.success(candidate["reasoning"])

    score_df = pd.DataFrame({

        "Score":[
            "Semantic",
            "Hybrid",
            "LLM",
            "Final"
        ],

        "Value":[
            candidate["semantic_score"]*100,
            candidate["hybrid_score"]*100,
            candidate.get("llm_score",0),
            candidate["final_score"]
        ]

    })

    fig = px.bar(
        score_df,
        x="Score",
        y="Value",
        color="Score",
        title="Score Breakdown"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

st.divider()

st.subheader("Education")

education = pd.DataFrame(candidate["education"])

if not education.empty:

    st.dataframe(
        education,
        use_container_width=True,
        hide_index=True
    )

else:

    st.info("No education records available.")