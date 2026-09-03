from app import app


def test_home():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert response.data == b"ML Model API is running!"


def test_predict():
    client = app.test_client()

    response = client.post(
        "/predict",
        json={"features": [5.1, 3.5, 1.4, 0.2]}
    )

    assert response.status_code == 200
    assert "prediction" in response.json


def test_predict_without_features():
    client = app.test_client()

    response = client.post(
        "/predict",
        json={}
    )

    assert response.status_code == 400
    assert response.json["error"] == "Please provide 'features' in the request."


def test_predict_with_wrong_number_of_features():
    client = app.test_client()

    response = client.post(
        "/predict",
        json={"features": [5.1, 3.5]}
    )

    assert response.status_code == 400
    assert response.json["error"] == "Exactly 4 features are required."