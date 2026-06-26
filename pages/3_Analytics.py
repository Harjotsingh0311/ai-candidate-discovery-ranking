import json
from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="Analytics",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Recruitment Analytics Dashboard")

FILE = Path("artifacts/final_ranked.json")

if not FILE.exists():
    st.error("Run the ranking pipeline first.")
    st.stop()

with open(FILE, "r", encoding="utf-8") as f:
    candidates = json.load(f)

# --------------------------------------------
# Build DataFrame
# --------------------------------------------

rows = []

for c in candidates:

    rows.append({

        "Candidate":
            c["candidate_id"],

        "Experience":
            c["profile"]["years_of_experience"],

        "Industry":
            c["profile"]["current_industry"],

        "Role":
            c["profile"]["current_title"],

        "Score":
            c["final_score"],

        "Hybrid":
            c["hybrid_score"],

        "Github":
            c["redrob_signals"]["github_activity_score"],

        "Recruiter Response":
            c["redrob_signals"]["recruiter_response_rate"]*100,

        "Work Mode":
            c["redrob_signals"]["preferred_work_mode"]

    })

df = pd.DataFrame(rows)

# --------------------------------------------
# Metrics
# --------------------------------------------

m1,m2,m3,m4 = st.columns(4)

m1.metric("Candidates",len(df))

m2.metric("Average Score",round(df["Score"].mean(),2))

m3.metric("Average Experience",round(df["Experience"].mean(),1))

m4.metric("Max Score",round(df["Score"].max(),2))

st.divider()

# --------------------------------------------
# Score Distribution
# --------------------------------------------

c1,c2 = st.columns(2)

with c1:

    fig = px.histogram(

        df,

        x="Score",

        nbins=20,

        title="Score Distribution"

    )

    st.plotly_chart(fig,use_container_width=True)

with c2:

    fig = px.histogram(

        df,

        x="Experience",

        nbins=15,

        title="Experience Distribution"

    )

    st.plotly_chart(fig,use_container_width=True)

st.divider()

# --------------------------------------------
# Industry
# --------------------------------------------

c1,c2 = st.columns(2)

with c1:

    industry = (

        df["Industry"]

        .value_counts()

        .head(10)

        .reset_index()

    )

    industry.columns=["Industry","Count"]

    fig=px.bar(

        industry,

        x="Industry",

        y="Count",

        title="Top Industries"

    )

    st.plotly_chart(fig,use_container_width=True)

with c2:

    work=df["Work Mode"].value_counts().reset_index()

    work.columns=["Mode","Count"]

    fig=px.pie(

        work,

        names="Mode",

        values="Count",

        title="Preferred Work Mode"

    )

    st.plotly_chart(fig,use_container_width=True)

st.divider()

# --------------------------------------------
# Scatter Plot
# --------------------------------------------

fig=px.scatter(

    df,

    x="Experience",

    y="Score",

    color="Industry",

    hover_data=["Candidate"],

    title="Experience vs Final Score"

)

st.plotly_chart(fig,use_container_width=True)

st.divider()

# --------------------------------------------
# Top Skills
# --------------------------------------------

skills=[]

for c in candidates:

    for s in c["skills"]:

        skills.append(s["name"])

skill_df=(

    pd.Series(skills)

    .value_counts()

    .head(20)

    .reset_index()

)

skill_df.columns=["Skill","Frequency"]

fig=px.bar(

    skill_df,

    x="Skill",

    y="Frequency",

    color="Frequency",

    title="Top Skills"

)

st.plotly_chart(fig,use_container_width=True)

st.success("Analytics Generated Successfully")