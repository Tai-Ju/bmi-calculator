from fastapi.testclient import TestClient
from src.api.main import app

client = TestClient(app)

def test_api_endpoints():
    # Test Case 1: Successful calculation (cm)
    response = client.post("/calculate", json={"height": 175, "weight": 70})
    assert response.status_code == 200
    data = response.json()
    assert data["bmi"] == 22.86
    assert data["category"] == "Normal weight"
    print("✓ POST /calculate (cm) passed")

    # Test Case 2: Successful calculation (m)
    response = client.post("/calculate", json={"height": 1.75, "weight": 70})
    assert response.status_code == 200
    data = response.json()
    assert data["bmi"] == 22.86
    print("✓ POST /calculate (m) passed")

    # Test Case 3: Invalid Input (negative height) -> Should trigger ValueError in service -> 400 in API
    response = client.post("/calculate", json={"height": -175, "weight": 70})
    assert response.status_code == 400
    assert "Height must be greater than zero" in response.json()["detail"]
    print("✓ API error handling (400) passed")

    # Test Case 4: Invalid Payload (missing field) -> FastAPI automatic 422
    response = client.post("/calculate", json={"height": 175})
    assert response.status_code == 422
    print("✓ API automatic validation (422) passed")

if __name__ == "__main__":
    try:
        test_api_endpoints()
        print("ALL PHASE 4 API TESTS PASSED")
    except Exception as e:
        print(f"TEST FAILED: {e}")
        exit(1)
