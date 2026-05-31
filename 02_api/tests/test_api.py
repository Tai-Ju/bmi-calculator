import pytest
from fastapi.testclient import TestClient
from src.api.main import app

client = TestClient(app)

def test_api_e2e_success():
    # Test height in cm
    response = client.post("/calculate", json={"height": 175, "weight": 70})
    assert response.status_code == 200
    data = response.json()
    assert data["bmi"] == 22.86
    assert "category" in data
    assert "suggestion" in data

    # Test height in m
    response = client.post("/calculate", json={"height": 1.75, "weight": 70})
    assert response.status_code == 200
    assert response.json()["bmi"] == 22.86

def test_api_e2e_invalid_input():
    # Negative height
    response = client.post("/calculate", json={"height": -170, "weight": 70})
    assert response.status_code == 400
    assert "Height must be greater than zero" in response.json()["detail"]

def test_api_openapi_compliance():
    response = client.post("/calculate", json={"height": 175, "weight": 70})
    data = response.json()
    # Check keys match OPENAPI.yaml
    assert set(data.keys()) == {"bmi", "category", "suggestion"}
    assert isinstance(data["bmi"], float)
    assert isinstance(data["category"], str)
    assert isinstance(data["suggestion"], str)
