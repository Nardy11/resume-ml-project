from app.model import sbert_similarity ,tfidf_similarity

def test_sbert_similarity1():
    score = sbert_similarity("machine learning developer", "machine learning developer")
    assert score > 0.8

def test_sbert_similarity2():
    score = sbert_similarity("machine learning", "machine learning developer")
    assert score > 0.5

def test_tfidf_similarity1():
    score = tfidf_similarity("machine learning developer", "machine learning developer")
    assert score > 0.5    

def test_tfidf_similarity2():
    score = tfidf_similarity("machine learning", "machine learning developer")
    assert score > 0.5    