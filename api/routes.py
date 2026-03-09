"""
api/routes.py — Flask Route Definitions
=========================================
All REST API endpoints and the frontend serving route.
"""

import numpy as np
from flask import request, jsonify, Response, send_from_directory
from nlp.matcher import find_best_match
from nlp.pipeline import get_pipeline_steps


def register_routes(app, faq_db, vectorizer, tfidf_matrix):
    """Attach all routes to the Flask app instance."""

    # ── Chat ─────────────────────────────────────────────────────────────────

    @app.route("/api/chat", methods=["POST"])
    def chat():
        """Receive a user query and return the best FAQ match."""
        data = request.get_json()
        if not data or "query" not in data:
            return jsonify({"error": "Missing 'query' field"}), 400

        query = data["query"].strip()
        if not query:
            return jsonify({"error": "Empty query"}), 400

        result = find_best_match(query, faq_db, vectorizer, tfidf_matrix)
        return jsonify(result)

    # ── FAQs ─────────────────────────────────────────────────────────────────

    @app.route("/api/faqs", methods=["GET"])
    def get_faqs():
        """Return all FAQs grouped by topic."""
        topics: dict[str, list] = {}
        for faq in faq_db:
            topics.setdefault(faq["topic"], []).append(
                {"id": faq["id"], "question": faq["question"]}
            )
        return jsonify({"topics": topics, "total": len(faq_db)})

    @app.route("/api/faq/<int:faq_id>", methods=["GET"])
    def get_faq(faq_id):
        """Return a single FAQ by ID."""
        faq = next((f for f in faq_db if f["id"] == faq_id), None)
        if not faq:
            return jsonify({"error": "FAQ not found"}), 404
        return jsonify(faq)

    # ── NLP Analysis ─────────────────────────────────────────────────────────

    @app.route("/api/nlp/analyze", methods=["POST"])
    def analyze():
        """Inspect the NLP pipeline for a given text (debug/education)."""
        data = request.get_json()
        if not data or "text" not in data:
            return jsonify({"error": "Missing 'text' field"}), 400

        steps = get_pipeline_steps(data["text"])

        query_vec = vectorizer.transform([data["text"]])
        feature_names = vectorizer.get_feature_names_out()
        scores = query_vec.toarray()[0]
        top_terms = sorted(
            [
                (feature_names[i], round(float(scores[i]), 4))
                for i in np.argsort(scores)[::-1][:10]
                if scores[i] > 0
            ],
            key=lambda x: x[1],
            reverse=True,
        )

        steps["top_tfidf_terms"] = top_terms
        steps["vocabulary_size"] = len(vectorizer.vocabulary_)
        return jsonify(steps)

    # ── Frontend ─────────────────────────────────────────────────────────────

    @app.route("/")
    def index():
        """Serve the chat UI."""
        return send_from_directory("static", "index.html")