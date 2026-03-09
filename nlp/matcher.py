"""
nlp/matcher.py — FAQ Matching
================================
Finds the best FAQ match for a user query using
cosine similarity against the TF-IDF matrix.
"""

import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from nlp.pipeline import get_pipeline_steps

# Minimum scores for a result to be included
MATCH_THRESHOLD = 0.15
ALT_THRESHOLD = 0.05


def find_best_match(
    user_query: str,
    faq_db: list[dict],
    vectorizer,
    tfidf_matrix,
    top_k: int = 3,
) -> dict:
    """
    Find the best matching FAQ for a user query.

    Returns a dict containing:
        - query         : original query string
        - nlp_steps     : pipeline breakdown for transparency
        - vocabulary_size
        - top_score     : highest cosine similarity score
        - matched       : best FAQ match (or None if below threshold)
        - alternatives  : runner-up matches above ALT_THRESHOLD
    """
    query_vec = vectorizer.transform([user_query])
    similarities = cosine_similarity(query_vec, tfidf_matrix).flatten()
    top_indices = np.argsort(similarities)[::-1][:top_k]

    top_idx = top_indices[0]
    top_score = float(similarities[top_idx])

    result = {
        "query": user_query,
        "nlp_steps": get_pipeline_steps(user_query),
        "vocabulary_size": len(vectorizer.vocabulary_),
        "top_score": round(top_score, 4),
        "matched": None,
        "alternatives": [],
    }

    if top_score >= MATCH_THRESHOLD:
        result["matched"] = {
            **faq_db[top_idx],
            "score": round(top_score, 4),
            "score_pct": round(top_score * 100, 1),
        }

        for idx in top_indices[1:]:
            alt_score = float(similarities[idx])
            if alt_score >= ALT_THRESHOLD:
                result["alternatives"].append({
                    "question": faq_db[idx]["question"],
                    "topic": faq_db[idx]["topic"],
                    "score": round(alt_score, 4),
                    "score_pct": round(alt_score * 100, 1),
                    "id": faq_db[idx]["id"],
                })

    return result