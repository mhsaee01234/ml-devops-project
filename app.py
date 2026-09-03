from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Load trained model
model = joblib.load("model.pkl")


@app.route("/")
def home():
    return "ML Model API is running!"


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    prediction = model.predict([data["features"]])

    return jsonify({
        "prediction": int(prediction[0])
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
    