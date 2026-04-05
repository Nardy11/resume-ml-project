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
```

---

## 🏗️ Project Structure

```
app/
  main.py
  model.py
  ingestion.py
  preprocessing.py
  logger.py

tests/
  test_api.py
  test_model.py
  test_logging.py
  sample_cv.pdf

logs/
  app.log

run_tests.sh
Dockerfile
requirements.txt
README.md
```

---

## 🧪 Testing

### ▶ Run all tests (Linux / Mac)

```
./run_tests.sh
```

### ▶ Run all tests (Windows)

```
python -m pytest
```

> ⚠️ We use `python -m pytest` instead of `pytest` to avoid import/path issues.

---

## ✅ What is Tested

- API endpoint (`/analyze`)  
- Model outputs (SBERT, TF-IDF, advanced score)  
- Logging system  
- Full pipeline integration  

---

## 📄 Sample Testing Files

Included for easy testing:

- ✅ `tests/sample_cv.pdf`  
- ✅ predefined job descriptions  

---

## 🧪 Example Test Scenarios

### 🟢 Strong Match (~70–80%)
Machine learning engineer with experience in Python, TensorFlow, deep learning, and computer vision.

### 🟡 Moderate Match (~50–65%)
Software engineer with knowledge of APIs, databases, and some machine learning concepts.

### 🔴 Low Match (<40%)
Frontend developer with experience in HTML, CSS, JavaScript, and UI design.

---

## ⚙️ Installation & Running

### 1️⃣ Install dependencies
```
pip install -r requirements.txt
```

### 2️⃣ Run tests
```
python -m pytest
```

### 3️⃣ Run API
```
uvicorn app.main:app --reload
```

### 4️⃣ Open Swagger UI
```
http://127.0.0.1:8000/docs
```

---

## 🐳 Docker Usage

### 🔧 Build image
```
docker build -t resume_ml_project .
```

### ▶ Run container
```
docker run -p 8000:8000 resume-analyzer
```

### 🌐 Access API
```
http://localhost:8000/docs
```

---

## 📸 Screenshots

### 📌 Swagger UI
<img width="1600" height="848" alt="image" src="https://github.com/user-attachments/assets/e4611805-3e22-4e4e-aa0c-1352e942ccc0" />

### 📌 Sample API Response
<img width="1282" height="878" alt="image" src="https://github.com/user-attachments/assets/b180df37-55f0-4f08-a9ed-be2a6579047e" />

### 📌 Docker Running Container
<img width="1734" height="729" alt="image" src="https://github.com/user-attachments/assets/1e4d9b97-5a9d-43a8-8b6b-7e50cfc1d1fc" />

---

## ✨ Key Features

- 🧠 Semantic understanding (SBERT)  
- 🔍 Keyword matching (TF-IDF)  
- 📊 Skill gap detection  
- 💡 Explainable results  
- ⚖️ Bias detection  
- 🧪 Fully tested (pytest)  
- 🐳 Dockerized  
- ⚡ FastAPI-based API  

---

## ⚠️ Limitations

- Skill detection depends on predefined skill list  
- Semantic similarity is approximate  
- Not fine-tuned for specific domains  

---

## 🚀 Future Improvements

- ✍️ CV rewriting suggestions  
- 🖥️ UI dashboard  
- 📚 Improved skill ontology  
- ⚖️ Advanced bias detection  

---

## 👨‍💻 Author

Developed as part of an AI/ML learning journey focusing on:

- Machine Learning Engineering  
- NLP Systems  
- Backend API Development  
- MLOps Fundamentals  
