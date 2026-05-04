# Number Analyzer App - BCS601-4MW23CS084

This project is developed for **Project Based Learning on Cloud Platform (App Engine / Database)**.

## Title
Number Analyzer Web Application using Cloud Deployment

## Problem Statement
To design and develop a web-based application that accepts a number from the user and performs multiple mathematical analyses such as checking whether the number is prime, determining if it is even or odd, calculating the sum of its digits, and computing its factorial. The application will be deployed on a cloud platform for public access.

## Tech Stack
- Frontend: HTML
- Backend: Python (Flask)
- IDE: Visual Studio Code
- Version Control: GitHub
- Cloud: Google Cloud Platform (App Engine)
- Database: SQLite (local) / PostgreSQL via `DATABASE_URL` (cloud-ready)

## Project Structure
```text
BCS601-4MW23CS084/
|- app.py
|- app.yaml
|- requirements.txt
|- README.md
|- REPORT.md
|- templates/
|  |- index.html
|- static/
|  |- style.css
```

## Run Locally
1. Create and activate virtual environment:
   - Windows PowerShell:
     ```powershell
     python -m venv venv
     .\venv\Scripts\activate
     ```
2. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```
3. Start the app:
   ```powershell
   python app.py
   ```
4. Open browser:
   - http://localhost:8080

## Input/Output Example
- Input: `Number = 5`
- Output:
  - Prime: Yes
  - Even/Odd: Odd
  - Sum of digits: 5
  - Factorial: 120

## Small Enhancement Implemented
- Error handling for invalid input and negative numbers
- Factorial limit added (`max = 20`) to avoid very large computations
- Basic UI styling for better readability

## Deploy to Google App Engine
1. Install and initialize Google Cloud SDK:
   ```powershell
   gcloud init
   ```
2. Set your project:
   ```powershell
   gcloud config set project YOUR_PROJECT_ID
   ```
3. Deploy:
   ```powershell
   gcloud app deploy
   ```
4. Open deployed app:
   ```powershell
   gcloud app browse
   ```

## Deployed URL
Update this section after deployment:

- **Live URL:** `PASTE_YOUR_DEPLOYED_URL_HERE`

## GitHub Repository Name (as per instruction)
- `bcs601_4mw23cs084`
