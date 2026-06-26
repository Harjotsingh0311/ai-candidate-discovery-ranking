import json
from pathlib import Path

import pandas as pd
import streamlit as st
from st_aggrid import AgGrid, GridOptionsBuilder

st.set_page_config(
    page_title="Leaderboard",
    page_icon="🏆",
    layout="wide"
)

st.title("🏆 AI Candidate Leaderboard")

# ---------------------------------------------------------
# Load Data
# ---------------------------------------------------------

FILE = Path("artifacts/final_ranked.json")

if not FILE.exists():
    st.error("❌ Run the ranking pipeline first.")
    st.stop()

with open(FILE, "r", encoding="utf-8") as f:
    candidates = json.load(f)

rows = []

for rank, candidate in enumerate(candidates, start=1):

    rows.append({

        "Rank": rank,

        "Candidate ID":
            candidate["candidate_id"],

        "Current Role":
            candidate["profile"]["current_title"],

        "Experience":
            candidate["profile"]["years_of_experience"],

        "Hybrid Score":
            round(candidate["hybrid_score"], 3),

        "LLM Score":
            candidate.get("llm_score", "-"),

        "Final Score":
            round(candidate["final_score"], 2)

    })

df = pd.DataFrame(rows)

# ---------------------------------------------------------
# Sidebar
# ---------------------------------------------------------

st.sidebar.header("Filters")

min_score = st.sidebar.slider(
    "Minimum Final Score",
    float(df["Final Score"].min()),
    float(df["Final Score"].max()),
    float(df["Final Score"].min())
)

experience = st.sidebar.slider(
    "Minimum Experience",
    0.0,
    float(df["Experience"].max()),
    0.0
)

filtered = df[
    (df["Final Score"] >= min_score)
    &
    (df["Experience"] >= experience)
]

st.sidebar.metric(
    "Candidates",
    len(filtered)
)

# ---------------------------------------------------------
# Table
# ---------------------------------------------------------

gb = GridOptionsBuilder.from_dataframe(filtered)

gb.configure_default_column(
    sortable=True,
    filter=True,
    resizable=True
)

gb.configure_pagination(
    paginationAutoPageSize=False,
    paginationPageSize=15
)

gb.configure_selection(
    selection_mode="single"
)

response = AgGrid(

    filtered,

    gridOptions=gb.build(),

    fit_columns_on_grid_load=True,

    height=650,

    update_mode="SELECTION_CHANGED"

)

# ---------------------------------------------------------
# Selected Candidate
# ---------------------------------------------------------

selected = response.get("selected_rows")

if selected is None:
    selected = []

# If DataFrame
if isinstance(selected, pd.DataFrame):

    if not selected.empty:

        row = selected.iloc[0]

        st.success(
            f"Selected Candidate : {row['Candidate ID']}"
        )

# If List
elif isinstance(selected, list):

    if len(selected) > 0:

        row = selected[0]

        st.success(
            f"Selected Candidate : {row['Candidate ID']}"
        )

# ---------------------------------------------------------
# Download
# ---------------------------------------------------------

st.divider()

csv = filtered.to_csv(index=False).encode("utf-8")

st.download_button(

    "📥 Download Leaderboard",

    csv,

    "leaderboard.csv",

    "text/csv"

)