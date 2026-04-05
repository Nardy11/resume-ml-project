from sentence_transformers import SentenceTransformer, util
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

# Load model once
model = SentenceTransformer("all-MiniLM-L6-v2")

def sbert_similarity(text1, text2):
    emb = model.encode([text1, text2])
    score = float(cosine_similarity([emb[0]], [emb[1]])[0][0])
    return score

def tfidf_similarity(text1, text2):
    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform([text1, text2])
    score = float(cosine_similarity(tfidf[0], tfidf[1])[0][0])
    return score

SKILLS = {
    "python", "docker", "api", "ml", "machine learning",
    "deep learning", "nlp", "sql", "tensorflow", "pytorch",
    "computer vision", "data analysis", "pandas",
    "scikit-learn", "kubernetes", "ci/cd"
}

def semantic_skill_match(text, skills=SKILLS, threshold=0.4):
    text_emb = model.encode(text, convert_to_tensor=True)
    matched = set()

    for skill in skills:
        skill_emb = model.encode(skill, convert_to_tensor=True)
        score = util.cos_sim(text_emb, skill_emb).item()
        if score > threshold:
            matched.add(skill)

    return matched

def advanced_score(cv_text, job_description, sbert_score):
    tfidf_score = tfidf_similarity(cv_text, job_description)

    cv_skills = semantic_skill_match(cv_text)
    job_skills = semantic_skill_match(job_description)

    matched = cv_skills & job_skills
    missing = job_skills - cv_skills

    skill_score = len(matched) / (len(matched) + len(missing) + 1e-5)

    final_score = 0.5 * sbert_score + 0.2 * tfidf_score + 0.3 * skill_score

    return final_score


def explain_result(cv_text, job_description):
    cv_skills = semantic_skill_match(cv_text)
    job_skills = semantic_skill_match(job_description)

    matched = cv_skills & job_skills
    missing = job_skills - cv_skills

    if len(missing) == 0:
        return "Your CV covers all major required skills."
    elif len(matched) > len(missing):
        return "You match most requirements but can improve in some areas."
    else:
        return "Your CV is missing several key skills for this role."