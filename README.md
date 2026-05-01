# 🧠 Slay the Spire Deck Analyzer

A backend-driven tool to analyze decks and suggest optimal card choices based on heuristics and (later) AI.

---

## 🚀 Project Overview

This project aims to build a decision-support system for deck-building games.

It provides:

* Deck analysis (composition, stats)
* Card scoring (absolute + contextual)
* Recommendations based on synergy and needs
* (Future) AI-powered explanations

---

## 🏗️ Tech Stack

* **Backend**: FastAPI
* **Frontend**: Streamlit
* **Language**: Python
* **Data**: JSON (initially), SQLite/PostgreSQL (later)

---

## 📦 Features (Current & Planned)

### ✅ Current

* Basic FastAPI setup
* API endpoints
* Project structure
* Interactive UI with Streamlit

### 🚧 In Progress

* Deck analyzer (stats extraction)
* Card model & dataset
* Scoring system (V1)
* Inermediate scoring (synergies, playability)

### 🔮 Future

* Advanced scoring (advanced synergies, scaling)
* AI explanations (LLM)
* Deck optimization suggestions

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/slay-ai.git
cd slay-ai
```

### 2. Create virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the project

### Start FastAPI server

```bash
uvicorn app.main:app --reload
```

### Access API

* API root: http://127.0.0.1:8000
* Docs (Swagger): http://127.0.0.1:8000/docs

---

## 🧪 Example API Usage

### Analyze a deck

```json
POST /analyze

["Strike", "Defend", "Bash"]
```

Response:

```json
{
  "size": 3
}
```
### Start Streamlit app



```bash
export PYTHONPATH=.
streamlit run streamlit_app/app.py
```

### Access

* Local URL: http://localhost:8501
* Network URL: http://172.27.75.137:8501

---

## 🧠 Architecture

```
Deck → Analyzer → Stats → Scoring → (AI) → UI
```

---

## 📁 Project Structure

```
slay-ai/
 ├── app/
 │   ├── main.py
 │   ├── api/
 │   ├── services/
 │   ├── models/
 │   └── data/
 ├── streamlit_app/
 ├── tests/
 ├── requirements.txt
 └── README.md
```

---

## 🎯 Goals

* Build a clean backend architecture
* Apply heuristic-based decision systems
* Integrate AI for explainability
* Create a portfolio-ready project

---

## 💡 Why this project?

This project combines:

* Backend engineering
* Game mechanics modeling
* Applied mathematics (optimization, heuristics)
* AI integration

---

## 📌 Roadmap

* [ ] Card dataset (JSON)
* [ ] Deck analyzer
* [ ] Scoring V1 (absolute)
* [ ] Scoring V2 (synergies)
* [ ] Streamlit UI
* [ ] AI explanations

---

## 🤝 Contributing

This is a personal learning project, but suggestions are welcome.

---

## 📜 License

MIT License
