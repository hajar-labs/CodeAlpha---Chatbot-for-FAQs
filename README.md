# 🤖 SmartHelp — FAQ Chatbot with Python NLP Backend

> **CodeAlpha AI Internship — Task 2: Chatbot for FAQs**

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.1.0-000000?style=for-the-badge&logo=flask&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.6.1-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-2.2.3-013243?style=for-the-badge&logo=numpy&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-CSS3-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![License](https://img.shields.io/badge/License-Educational-green?style=for-the-badge)
![Internship](https://img.shields.io/badge/CodeAlpha-Internship-blueviolet?style=for-the-badge)

A full-stack FAQ chatbot powered by a **Python NLP pipeline** (tokenization → stop-word removal → stemming → TF-IDF vectorization → cosine similarity). Includes a REST API built with Flask and a polished chat UI with live NLP pipeline transparency.

---

## ✨ Features

- 🧠 **Custom NLP pipeline** — tokenization, stop-word removal, Porter-inspired stemmer (no NLTK needed)
- 📐 **TF-IDF + Cosine Similarity** — powered by scikit-learn with bigram support and sublinear TF scaling
- 🔬 **NLP Transparency panel** — every response shows a collapsible breakdown of the pipeline steps
- 📊 **Confidence meter** — color-coded match score (green / yellow / red)
- 💡 **Alternative suggestions** — runner-up FAQ matches displayed as clickable chips
- 🗂️ **Topic sidebar** — all FAQs grouped by topic, clickable to pre-fill the query
- 🌐 **REST API** — clean Flask endpoints for chat, FAQ listing, and NLP analysis
- 📦 **Zero frontend dependencies** — pure HTML/CSS/JS, no framework needed

---

## 🏗️ Project Structure

```
CodeAlpha_FAQChatbot/
├── api/
│   └── routes.py          # Flask REST API endpoints
├── data/
│   └── faqs.py            # FAQ database (18 entries, 6 topics)
├── nlp/
│   ├── pipeline.py        # Tokenizer → stop-word removal → stemmer
│   ├── vectorizer.py      # TF-IDF model builder (scikit-learn)
│   └── matcher.py         # Cosine similarity matching logic
├── static/
│   ├── index.html         # Chat UI
│   ├── style.css          # Dark-theme styles
│   └── chat.js            # Frontend logic
├── app.py                 # Flask entry point
├── requirements.txt
└── README.md
```

---

## 🧠 How It Works

```
User Query
    │
    ▼
① Tokenization        "How do I reset my password?"
                       → ["how", "do", "i", "reset", "my", "password"]
    │
    ▼
② Stop-word Removal   → ["reset", "password"]
    │
    ▼
③ Stemming            → ["reset", "password"]   (Porter-inspired rules)
    │
    ▼
④ TF-IDF Vectorization  → sparse vector (sklearn, unigrams + bigrams)
    │
    ▼
⑤ Cosine Similarity   → compare against all FAQ vectors
    │
    ▼
⑥ Best Match          → return top result + alternatives + pipeline steps
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/CodeAlpha_FAQChatbot.git
cd CodeAlpha_FAQChatbot
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Flask server

```bash
python app.py
```

### 4. Open the chat UI

Visit **http://127.0.0.1:5000** in your browser.

---

## 🔌 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/api/chat` | Send a user query, get best FAQ match |
| `GET` | `/api/faqs` | List all FAQs grouped by topic |
| `GET` | `/api/faq/<id>` | Get a single FAQ by ID |
| `POST` | `/api/nlp/analyze` | Inspect NLP pipeline for any text |

### Example — `/api/chat`

**Request:**
```json
POST /api/chat
{ "query": "How do I reset my password?" }
```

**Response:**
```json
{
  "query": "How do I reset my password?",
  "top_score": 0.8921,
  "matched": {
    "id": 1,
    "topic": "Account",
    "question": "How do I reset my password?",
    "answer": "To reset your password, click 'Forgot Password'...",
    "score": 0.8921,
    "score_pct": 89.2
  },
  "alternatives": [...],
  "nlp_steps": {
    "original": "How do I reset my password?",
    "tokenized": ["how", "do", "i", "reset", "my", "password"],
    "after_stopword_removal": ["reset", "password"],
    "after_stemming": ["reset", "password"]
  },
  "vocabulary_size": 312
}
```

---

## 📚 FAQ Topics Covered

| Topic | # of FAQs |
|-------|-----------|
| Account | 3 |
| Billing | 5 |
| Security | 3 |
| Support | 2 |
| Getting Started | 3 |
| Teams & Integrations | 2 |

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python 3.10+, Flask |
| NLP | Custom pipeline + scikit-learn TF-IDF |
| Similarity | Cosine similarity (sklearn) |
| Frontend | HTML5, CSS3, Vanilla JavaScript |
| Fonts | Google Fonts (DM Serif Display, DM Mono, Instrument Sans) |

---

## 📦 Dependencies

```
flask==3.1.0
scikit-learn==1.6.1
numpy==2.2.3
```

Install with:
```bash
pip install -r requirements.txt
```

---

## 🎓 Internship

This project was built as part of the **CodeAlpha AI Internship Program**.

- 🏢 Company: [CodeAlpha](https://www.codealpha.tech)
- 📋 Task: Task 2 — Chatbot for FAQs
- 🔗 Submission: via CodeAlpha internship portal

---

## 📄 License

This project is intended for educational purposes as part of an internship program.
