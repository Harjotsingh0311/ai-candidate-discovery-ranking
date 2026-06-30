# 🤖 AI Candidate Discovery & Ranking System

> **An AI-powered semantic candidate retrieval and ranking platform that understands *who fits the role*, not just *which keywords match*.**

[![Python](https://img.shields.io/badge/Python-3.13-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-red)](https://streamlit.io/)
[![ChromaDB](https://img.shields.io/badge/VectorDB-ChromaDB-success)](https://www.trychroma.com/)
[![LangChain](https://img.shields.io/badge/LangChain-Framework-green)](https://www.langchain.com/)
[![Groq](https://img.shields.io/badge/LLM-Groq-orange)](https://groq.com/)
[![Docker](https://img.shields.io/badge/Deployment-Docker-blue)](https://www.docker.com/)

---

## 📌 Overview

Traditional Applicant Tracking Systems (ATS) rely heavily on keyword matching, often overlooking highly qualified candidates whose profiles don't exactly match a job description.

This project introduces an **AI-powered Candidate Discovery & Ranking System** that combines:

* 🧠 Semantic Search
* 📚 Vector Embeddings
* 🤖 Large Language Models
* 📊 Behavioral Intelligence
* 🎯 Hybrid Ranking

To retrieve and rank candidates similarly to how an experienced recruiter would.

---

# 🚀 Features

### 🔍 Semantic Candidate Retrieval

* BGE Embeddings
* ChromaDB Vector Search
* Context-aware candidate matching

---

### 📄 Intelligent Job Description Understanding

* Parses Job Description
* Extracts important hiring signals
* Understands required experience & skills

---

### 🏆 Hybrid Candidate Ranking

Each candidate receives scores based on:

* Semantic Similarity
* Skills Match
* Experience
* Career Growth
* Company Background
* Behavioral Signals
* LLM Validation

---

### 🤖 AI Recruiter

Uses Groq LLM to:

* Evaluate candidate fit
* Generate recruiter reasoning
* Validate Top Candidates

---

### 📈 Interactive Dashboard

Built with Streamlit.

Includes:

* Dashboard
* Candidate Leaderboard
* Candidate Explorer
* Analytics
* Settings

---

# 🏗️ System Architecture

```text
                     Job Description
                            │
                            ▼
                 JD Intelligence Engine
                            │
                            ▼
              Candidate Feature Extraction
                            │
                            ▼
                   BGE Embedding Model
                            │
                            ▼
                  ChromaDB Vector Search
                            │
                            ▼
                  Top Semantic Candidates
                            │
                            ▼
                Hybrid Ranking Algorithm
                            │
                            ▼
                  Groq AI Validation
                            │
                            ▼
                  Final Candidate Ranking
                            │
                            ▼
                     Streamlit Dashboard
```

---

# 🛠️ Tech Stack

| Category        | Technology            |
| --------------- | --------------------- |
| Language        | Python                |
| Frontend        | Streamlit             |
| LLM             | Groq                  |
| Framework       | LangChain             |
| Vector Database | ChromaDB              |
| Embeddings      | BAAI/bge-base-en-v1.5 |
| ML              | PyTorch               |
| Data Processing | Pandas                |
| Visualization   | Plotly                |
| Deployment      | Docker                |

---

# 📂 Project Structure

```text
HACK_SKILL
│
├── app.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
│
├── data/
├── artifacts/
├── pages/
├── src/
│
├── submission.csv
└── README.md
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/Harjotsingh0311/ai-candidate-discovery-ranking.git

cd HACK_SKILL
```

---

## 2️⃣ Create Virtual Environment

### Using uv (Recommended)

```bash
uv venv

source .venv/bin/activate
```

Windows

```powershell
.venv\Scripts\activate
```

---

## 3️⃣ Install Dependencies

```bash
uv pip install -r requirements.txt
```

or

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Create Environment File

Create a file named:

```text
.env
```

Add:

```env
GROQ_API_KEY=your_groq_api_key_here
```

---

# 📥 Dataset

Place the challenge dataset inside:

```text
data/
└── India_runs_data_and_ai_challenge/
```

---

# 🚀 Running the Pipeline

Run the pipeline in sequence:

```bash
python src/intelligence/jd_intelligence.py

python src/intelligence/candidate_intelligence.py

python src/retrieval/retrieve_candidates.py

python src/ranking/hybrid_ranker.py

python src/ranking/groq_reranker.py

python src/output/generate_submission.py
```

---

# 🌐 Launch Dashboard

```bash
streamlit run app.py
```

Open:

```
http://localhost:8501
```

---

# 🐳 Docker Deployment

Build

```bash
docker compose build
```

Run

```bash
docker compose up
```

Open

```
http://localhost:8501
```

Stop

```bash
docker compose down
```

---

# 📊 Dashboard

The application provides:

* 🏠 Dashboard
* 🏆 Leaderboard
* 👤 Candidate Explorer
* 📊 Analytics
* ⚙️ Settings

---

# 🧠 Ranking Pipeline

```text
Candidate Dataset
       │
       ▼
Feature Engineering
       │
       ▼
BGE Embeddings
       │
       ▼
ChromaDB
       │
       ▼
Semantic Retrieval
       │
       ▼
Hybrid Ranking
       │
       ▼
Groq Validation
       │
       ▼
Final Candidate Ranking
```

---

# 📈 Scoring Strategy

Final ranking is computed using:

* Semantic Similarity
* Skill Match
* Experience Match
* Career Progression
* Company Background
* Behavioral Signals
* LLM Validation

---

# 📜 Output

The system generates:

```
submission.csv
```

containing:

* Candidate ID
* Rank
* Score
* AI Reasoning

---

# 👨‍💻 Author

**Harjot Singh**

B.Tech – Artificial Intelligence & Machine Learning

Thapar Institute of Engineering & Technology

GitHub: https://github.com/Harjotsingh1103

---

# ⭐ Future Improvements

* Hybrid BM25 + Vector Search
* Explainable AI Dashboard
* Multi-Job Comparison
* Resume Upload Support
* Live Recruiter Feedback Loop
* Fine-tuned Ranking Model
* Kubernetes Deployment

---

# 📄 License

This project is developed for educational and hackathon purposes.
