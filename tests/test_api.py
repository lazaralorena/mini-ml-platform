"""Tests for the prediction endpoint of the ML Model API."""

from fastapi.testclient import TestClient
from serve.app import app

client = TestClient(app)


def test_predict_class_0():
    """Test prediction for class 0."""
    response = client.post("/predict", json={"features": [5.1, 3.5, 1.4, 0.2]})
    assert response.status_code == 200
    assert response.json()["prediction"] == 0


def test_predict_class_1():
    """Test prediction for class 1."""
    response = client.post("/predict", json={"features": [6.0, 2.2, 4.0, 1.0]})
    assert response.status_code == 200
    assert response.json()["prediction"] == 1


def test_predict_class_2():
    """Test prediction for class 2."""
    response = client.post("/predict", json={"features": [6.9, 3.1, 5.4, 2.1]})
    assert response.status_code == 200
    assert response.json()["prediction"] == 2


def test_invalid_input():
    """Test prediction with invalid input (too few features)."""
    response = client.post("/predict", json={"features": [1.0, 2.0]})
    assert response.status_code == 400
