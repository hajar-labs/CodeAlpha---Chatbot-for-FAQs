"""
nlp/vectorizer.py — TF-IDF Model
===================================
Builds and exposes the scikit-learn TF-IDF vectorizer
fitted on the FAQ question corpus.
"""

from sklearn.feature_extraction.text import TfidfVectorizer
from nlp.pipeline import preprocess


def build_vectorizer(faq_db: list[dict]):
    """
    Fit a TF-IDF vectorizer on all FAQ questions.

    Returns:
        vectorizer   — fitted TfidfVectorizer
        tfidf_matrix — sparse matrix of FAQ question vectors
    """
    vectorizer = TfidfVectorizer(
        tokenizer=preprocess,
        ngram_range=(1, 2),   # Unigrams + bigrams for better matching
        min_df=1,
        sublinear_tf=True,    # Apply sublinear TF scaling
        token_pattern=None,   # Use custom tokenizer
    )

    questions = [faq["question"] for faq in faq_db]
    tfidf_matrix = vectorizer.fit_transform(questions)

    print(
        f"✅ TF-IDF matrix built: "
        f"{tfidf_matrix.shape[0]} FAQs × {tfidf_matrix.shape[1]} features"
    )
    return vectorizer, tfidf_matrix