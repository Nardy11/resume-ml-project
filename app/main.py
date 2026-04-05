from fastapi import FastAPI, UploadFile, File, Form
from app.ingestion import extract_text_from_pdf
from app.model import sbert_similarity,tfidf_similarity,semantic_skill_match,advanced_score,explain_result

from app.logger import log_inference_time
from app.preprocessing import clean_text
import time

app = FastAPI()


@app.post("/analyze")
async def analyze(cv: UploadFile = File(...), job_description: str = Form(...)):
    start = time.time()
    cv_text = extract_text_from_pdf(await cv.read())
    cv_text = clean_text(cv_text)
    job_description = clean_text(job_description)

    sbert_score = sbert_similarity(cv_text, job_description)
    tfidf_score = tfidf_similarity(cv_text, job_description)

    cv_skills = semantic_skill_match(cv_text)
    job_skills = semantic_skill_match(job_description)

    matched_skills = cv_skills & job_skills
    missing_skills = job_skills - cv_skills

    adv_score = advanced_score(cv_text, job_description, sbert_score)
    explanation = explain_result(cv_text, job_description)

    male_words = {"he", "his", "man"}
    female_words = {"she", "her", "woman"}

    male_bias = sum(word in job_description for word in male_words)
    female_bias = sum(word in job_description for word in female_words)

    if male_bias > female_bias:
        dominant = "male"
    elif female_bias > male_bias:
        dominant = "female"
    else:
        dominant = "neutral"

    bias = {
        "male_bias": male_bias,
        "female_bias": female_bias,
        "dominant": dominant
    }

    end = time.time()
    log_inference_time(end - start)

    return {
        "sbert_score": sbert_score,
        "tfidf_score": tfidf_score,
        "advanced_score": adv_score,
        "matched_skills": list(matched_skills),
        "missing_skills": list(missing_skills),
        "bias": bias,
        "explanation": explanation
    }