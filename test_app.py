#created test_app.py for pytest githubAction workflow
from app import app

def test_homepage():
    response = app.test_client().get('/')
    assert response.status_code == 200
