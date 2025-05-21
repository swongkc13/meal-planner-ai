import sys
import os

# Ensure 'backend/' is treated as the root module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_recommend_valid(client):
    response = client.post("/recommend", json={"query": "gluten-free dinner with chicken"})
    assert response.status_code == 200
    data = response.get_json()
    assert "tags" in data and isinstance(data["tags"], list)
    assert "results" in data and isinstance(data["results"], list)

def test_recommend_empty(client):
    response = client.post("/recommend", json={})
    assert response.status_code == 400
    data = response.get_json()
    assert "error" in data
