from flask import Flask, request, jsonify
import joblib
import os

app = Flask(__name__)

model = joblib.load("model.pkl")


@app.route("/")
def home():
    return "ML Model API is running!"


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    if not data or "features" not in data:
        return jsonify({
            "error": "Please provide 'features' in the request."
        }), 400

    features = data["features"]

    if len(features) != 4:
        return jsonify({
            "error": "Exactly 4 features are required."
        }), 400

    prediction = model.predict([features])

    return jsonify({
        "prediction": int(prediction[0])
    })


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)