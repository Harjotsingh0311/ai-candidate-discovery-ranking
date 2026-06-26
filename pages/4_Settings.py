import streamlit as st

st.set_page_config(

    page_title="Settings",

    page_icon="⚙️",

    layout="wide"

)

st.title("⚙️ Application Settings")

st.markdown("---")

st.subheader("Pipeline Information")

st.info("""

### AI Candidate Discovery & Ranking System

Backend:

- BGE Embeddings
- ChromaDB
- Hybrid Ranking
- Groq LLM Validation

Frontend:

- Streamlit
- Plotly
- Pandas

Ranking Strategy:

Semantic Score

↓

Skill Score

↓

Behaviour Score

↓

Experience Score

↓

Career Score

↓

Hybrid Score

↓

Groq Validation

↓

Final Score

""")

st.markdown("---")

st.subheader("Developer")

st.write("Harjot Singh")

st.write("B.Tech AIML")

st.write("Thapar Institute of Engineering & Technology")

st.markdown("---")

st.subheader("Project Statistics")

st.code("""

Dataset Size        : 100,000 Candidates

Filtered            : 24,154

Retrieved           : 2,000

Hybrid Ranked       : 100

Groq Validated      : 20

Embedding Model     : BAAI/bge-base-en-v1.5

Vector Database     : ChromaDB

LLM                 : Groq Llama

""")

st.success("System Ready ✅")