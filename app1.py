"""
SmartHelp FAQ Chatbot — Entry Point
====================================
Run:  python app.py
"""

from flask import Flask
from api.routes import register_routes
from nlp.vectorizer import build_vectorizer
from data.faqs import FAQ_DB

app = Flask(__name__, static_folder="static")

# Build TF-IDF model on startup
vectorizer, tfidf_matrix = build_vectorizer(FAQ_DB)

# Register all API + frontend routes
register_routes(app, FAQ_DB, vectorizer, tfidf_matrix)

if __name__ == "__main__":
    print("\n" + "═" * 55)
    print("  🤖 SmartHelp FAQ Chatbot — Python NLP Backend")
    print("═" * 55)
    print(f"  📚 FAQ entries loaded  : {len(FAQ_DB)}")
    print(f"  🧠 TF-IDF vocab size   : {len(vectorizer.vocabulary_)} features")
    print(f"  🔗 Serving at          : http://127.0.0.1:5000")
    print("═" * 55)
    print("  API Endpoints:")
    print("    POST /api/chat         ← send a user query")
    print("    GET  /api/faqs         ← list all FAQs")
    print("    GET  /api/faq/<id>     ← get FAQ by ID")
    print("    POST /api/nlp/analyze  ← inspect NLP pipeline")
    print("═" * 55 + "\n")
    app.run(debug=False, port=5000)