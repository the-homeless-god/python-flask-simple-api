from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import requests
import os

app = Flask(__name__)
CORS(app)

WEBHOOK_URL = os.getenv("WEBHOOK_URL", "")


@app.route("/api/answers", methods=["POST"])
def submit_answer():
    data = request.get_json()
    print(WEBHOOK_URL)
    print(data)

    requests.post(WEBHOOK_URL, json=data)
    return jsonify("OK"), 200


@app.route("/api/health", methods=["GET"])
def health_check():
    return jsonify({"status": "ok"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
