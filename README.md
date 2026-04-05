# 🚀 AI Resume Analyzer – NLP-Based CV Matching System

## 🧠 Overview

This project is an **AI-powered Resume Analyzer API** that evaluates how well a CV matches a given job description using Natural Language Processing (NLP).

It provides:
- 🔍 Semantic similarity scoring (SBERT)
- 🧾 Keyword-based similarity (TF-IDF)
- 📊 Skill gap analysis (matched vs missing skills)
- ⚖️ Bias detection in job descriptions
- 💡 Explainable feedback for improvement

---

## 🎓 Course Context

This project was developed as part of:

**IBM AI Workflow Specialization (Coursera)**

---

## 📚 What I Learned

Through this project and the course, I applied and strengthened the following skills:

### 🤖 Machine Learning & NLP
- Semantic similarity using SBERT  
- Text vectorization using TF-IDF  
- Feature engineering for text data  
- Combining multiple models into a unified scoring system  

### 🧩 AI Workflow & Modeling
- Comparing models (SBERT vs TF-IDF)  
- Designing ensemble-like scoring logic  
- Understanding trade-offs between semantic and keyword-based approaches  

### ⚙️ Backend & API Development
- Building APIs using FastAPI  
- Handling file uploads (PDF processing)  
- Structuring modular backend applications  

### 🔄 MLOps Fundamentals
- Writing unit tests (API, model, logging)  
- Automating tests using `run_tests.sh`  
- Logging inference time  
- Ensuring reproducibility  

### 🐳 Deployment & Tools
- Using Swagger UI for API testing  
- Containerizing the application with Docker  
- Managing dependencies and environments  

---

## ⚙️ How It Works

### 📥 Input:
- CV (PDF file)
- Job Description (text)

### 🔄 Pipeline:
1. Extract text from PDF  
2. Clean and preprocess text  
3. Compute:
   - SBERT similarity  
   - TF-IDF similarity  
4. Perform semantic skill matching  
5. Detect:
   - ✅ Matched skills  
   - ❌ Missing skills  
6. Compute advanced score  
7. Detect bias  
8. Generate explanation  

---

## 📊 Example Output

```json
{
  "sbert_score": 0.61,
  "tfidf_score": 0.33,
  "advanced_score": 0.58,
  "matched_skills": ["python", "machine learning"],
  "missing_skills": ["docker", "kubernetes"],
  "bias": {
    "male_bias": 0,
    "female_bias": 0,
    "dominant": "neutral"
  },
  "explanation": "Skills match well, but overall alignment can be improved."
}
