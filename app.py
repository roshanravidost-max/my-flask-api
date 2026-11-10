
from flask import Flask, jsonify
import os

app = Flask(__name__)

# Base URL
@app.route("/")
def home():
    return jsonify({
        "status": "success",
        "message": "API is running!",
        "base_url": "/"
    })

# API endpoint
@app.route("/api")
def api():
    return jsonify({
        "status": "success",
        "message": "Hello from Python Flask API"
    })

# Health check
@app.route("/health")
def health():
    return jsonify({
        "status": "online"
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
  
