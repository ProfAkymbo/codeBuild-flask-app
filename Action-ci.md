# 🚀 Flask App CI with GitHub Actions

This repository includes a **Continuous Integration (CI) workflow** powered by **GitHub Actions**.  
The workflow automatically builds, installs dependencies, and runs tests on the Flask application whenever changes are pushed to the repository.

---

## 📌 Why CI?

Think of CI (Continuous Integration) like a **mechanic that checks your car every time you drive it**:
- If something is broken, you find out immediately (instead of later in production).
- It saves you from “it works on my machine” problems.
- It ensures the app is stable before deployment.

---

## ⚙️ Workflow Setup

The workflow file lives in:  
`.github/workflows/ci.yml`

It is triggered on every **push** to the repository.

### 🔑 Key Steps in the Workflow

1. **Checkout code**
   ```yaml
   - uses: actions/checkout@v4
   ```
   Brings your repository files into the workflow runner.

2. **Set up Python**
   ```yaml
   - uses: actions/setup-python@v4
     with:
       python-version: '3.10'
   ```
   Installs Python 3.10 so the Flask app can run.

3. **Install dependencies**
   ```yaml
   - run: pip install -r requirements.txt
   ```
   Installs Flask, pytest, and any other required packages.

4. **Run tests**
   ```yaml
   - run: pytest
   ```
   Executes your test suite (for example, checking `/` returns a `200 OK`).

---

## 🧪 Example Test (test_app.py)

```python
from app import app

def test_homepage():
    response = app.test_client().get('/')
    assert response.status_code == 200
```

This test confirms that the Flask app’s root endpoint (`/`) is working correctly.

---

## ✅ What This Workflow Achieves

- Automates builds and test runs on **every push**  
- Ensures the Flask app starts correctly and critical endpoints are tested  
- Provides immediate feedback if code changes break the app  

---

## 📖 Next Steps

- Add more tests for endpoints like `/time`, `/reverse`, and `/env`  
- Optionally add a **deploy job** that runs only if the tests pass  
- Track code coverage with tools like `coverage.py`  

---
