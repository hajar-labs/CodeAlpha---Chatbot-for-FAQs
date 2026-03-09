"""
nlp/pipeline.py — Text Preprocessing Pipeline
================================================
Handles tokenization, stop-word removal, and stemming.
Used by the TF-IDF vectorizer as a custom tokenizer.
"""

import re

# Extended stop words (NLTK-style, no download needed)
STOP_WORDS = {
    'a','an','the','is','it','in','on','of','to','and','or','but','for',
    'with','my','i','me','we','you','he','she','they','this','that','these',
    'those','be','are','was','were','am','do','does','did','have','has','had',
    'will','would','could','should','may','might','shall','can','about','how',
    'what','when','where','why','who','which','any','all','some','more','most',
    'also','as','at','by','from','up','out','if','so','no','not','there',
    'their','then','than','into','over','after','your','our','get','want',
    'need','its','been','being','just','very','too','much','many','well',
    'now','here','use','using','used','make','made','let','like','know',
    'go','going','come','coming','take','taking','see','find','give','tell'
}

# Porter-inspired stemming rules (pattern → replacement)
STEM_RULES = [
    (r'ational$', 'ate'), (r'tional$', 'tion'), (r'enci$', 'ence'),
    (r'anci$', 'ance'), (r'izer$', 'ize'), (r'ising$', 'ise'),
    (r'izing$', 'ize'), (r'ised$', 'ise'), (r'ized$', 'ize'),
    (r'fulness$', 'ful'), (r'ousness$', 'ous'), (r'iveness$', 'ive'),
    (r'ation$', 'ate'), (r'ator$', 'ate'), (r'alism$', 'al'),
    (r'nesses$', ''), (r'ness$', ''), (r'ments$', ''), (r'ment$', ''),
    (r'ies$', 'y'), (r'ied$', 'y'), (r'ing$', ''), (r'ed$', ''),
    (r'ers$', ''), (r'er$', ''), (r'ly$', ''), (r'ful$', ''),
    (r'able$', ''), (r'ible$', ''), (r'ous$', ''), (r'ive$', ''),
    (r'ize$', ''), (r'ise$', ''), (r'ings$', ''), (r's$', ''),
]


def tokenize(text: str) -> list[str]:
    """Split text into word tokens, removing punctuation."""
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', ' ', text)
    return text.split()


def remove_stopwords(tokens: list[str]) -> list[str]:
    """Remove common stop words and single-character tokens."""
    return [t for t in tokens if t not in STOP_WORDS and len(t) > 1]


def stem(word: str) -> str:
    """
    Lightweight rule-based stemmer (Porter-inspired).
    Handles common English suffixes without requiring NLTK.
    """
    if len(word) <= 3:
        return word
    for pattern, replacement in STEM_RULES:
        if re.search(pattern, word):
            stemmed = re.sub(pattern, replacement, word)
            if len(stemmed) >= 3:
                return stemmed
    return word


def preprocess(text: str) -> list[str]:
    """Full NLP pipeline: tokenize → remove stop words → stem."""
    tokens = tokenize(text)
    tokens = remove_stopwords(tokens)
    return [stem(t) for t in tokens]


def get_pipeline_steps(text: str) -> dict:
    """
    Return each preprocessing stage for transparency / debugging.
    Used by the /api/nlp/analyze endpoint.
    """
    raw_tokens = tokenize(text)
    no_stop = remove_stopwords(raw_tokens)
    stemmed = [stem(t) for t in no_stop]
    return {
        "original": text,
        "tokenized": raw_tokens,
        "after_stopword_removal": no_stop,
        "after_stemming": stemmed,
    }