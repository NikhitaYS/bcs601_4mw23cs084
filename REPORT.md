# Opening Page

**Title:** Number Analyzer Web Application using Cloud Deployment  
**Project Name:** BCS601-4MW23CS084  
**Student USN:** 4MW23CS084  
**Course:** Cloud Computing (BCS601)  
**Submission Date:** 06-May-2026  

---

# Introduction

**Problem Statement:**  
To design and develop a web-based application that accepts a number from the user and performs multiple mathematical analyses such as checking whether the number is prime, determining if it is even or odd, calculating the sum of its digits, and computing its factorial. The application will be deployed on a cloud platform for public access.

The **Number Analyzer App** performs:
- Prime number check
- Even/Odd check
- Sum of digits
- Factorial calculation

The project demonstrates:
- Application development using Python Flask
- Database integration to store analysis history
- Deployment readiness for cloud platforms (Google App Engine)

---

# Code

The source code is available in the project repository. Main files:
- `app.py` - Backend logic, routing, database model, and analysis functions
- `templates/index.html` - Frontend user interface
- `static/style.css` - Styling
- `app.yaml` - Google App Engine configuration
- `requirements.txt` - Python dependencies

Functional modules implemented:
1. **Input module** - takes integer from user.
2. **Prime module** - checks whether input is prime.
3. **Parity module** - identifies number as even or odd.
4. **Digit sum module** - computes sum of digits.
5. **Factorial module** - computes factorial.
6. **Validation module** - handles invalid, negative, and out-of-range values.
7. **Database module** - stores recent analysis records.

Example output:
- Input: Number = 5
- Output:
  - Prime: Yes
  - Even/Odd: Odd
  - Sum of digits: 5
  - Factorial: 120

---

# Steps

## 1) Project setup
1. Created project folder `BCS601-4MW23CS084`.
2. Initialized Python virtual environment.
3. Installed dependencies from `requirements.txt`.

## 2) Development
1. Built Flask app with a single route (`/`) for GET and POST.
2. Implemented number analysis functions in backend.
3. Designed frontend form and result sections in HTML.
4. Added validations:
   - Non-integer input handling
   - Negative number rejection
   - Factorial limit `max = 20`
5. Added CSS styling for better readability.

## 3) Database integration
1. Added SQLAlchemy model `AnalysisHistory`.
2. Configured local SQLite for development.
3. Added cloud-ready database URL support using `DATABASE_URL`.
4. Stored each analysis output into database table.

## 4) Cloud deployment
1. Added `app.yaml` for Google App Engine.
2. Added `gunicorn` entrypoint for production runtime.
3. Deployed using:
   - `gcloud app deploy`
   - `gcloud app browse`

## 5) Documentation
1. Prepared `README.md` with setup and deployment instructions.
2. Added deployed URL section in README.
3. Prepared this report as per given format.

---

# Summary

The Number Analyzer Web Application successfully implements all required outputs: prime check, even/odd check, sum of digits, and factorial computation.  
It also includes small enhancement features for extra quality: validation, negative input handling, factorial upper limit (`20`), and better UI styling.  
The project is cloud-deployment ready on Google App Engine and fulfills both implementation and report requirements.

---

# Annexure with Reference Links

1. Flask Official Documentation  
   [https://flask.palletsprojects.com/](https://flask.palletsprojects.com/)

2. Flask-SQLAlchemy Documentation  
   [https://flask-sqlalchemy.palletsprojects.com/](https://flask-sqlalchemy.palletsprojects.com/)

3. Google App Engine Python Standard Environment  
   [https://cloud.google.com/appengine/docs/standard/python3](https://cloud.google.com/appengine/docs/standard/python3)

4. Google Cloud SDK  
   [https://cloud.google.com/sdk/docs](https://cloud.google.com/sdk/docs)

5. Gunicorn Documentation  
   [https://docs.gunicorn.org/](https://docs.gunicorn.org/)
