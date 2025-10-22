# FastAPI Calculator

A simple calculator web application built using **FastAPI**. This app supports basic arithmetic operations via a REST API and includes full test coverage (unit, integration, and end-to-end tests). It also uses GitHub Actions for automated testing (CI).

---

##  Features

-  Four arithmetic operations: Add, Subtract, Multiply, Divide
-  FastAPI backend
-  Logging to file (`logs/app.log`)
-  Unit tests for all functions
-  Integration tests for all API routes
-  End-to-End (E2E) test using Playwright
-  Continuous Integration with GitHub Actions

---


---

## 🚀 How to Run the App

### 1. Clone the Repo

```bash
git clone https://github.com/Mikev2002/fastapi-calculator.git
cd fastapi-calculator


2. Create and Activate Virtual Environment
python -m venv venv
.\venv\Scripts\activate     # Windows
# Or:
source venv/bin/activate    # macOS/Linux

3. Install Dependencies
pip install -r requirements.txt
playwright install


4. Start the Server
uvicorn main:app --reload

Visit the app at:
📎 http://localhost:8000
Swagger docs at:
📎 http://localhost:8000/docs

5. Running Tests Unit & Integration Tests
pytest

6. End-to-End Tests (Make sure server is running)
pytest e2e/


Author

Name: Mike Villagomez 

Assignment: Module 8 – FastAPI Calculator App


