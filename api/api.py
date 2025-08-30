from flask import Flask, request, jsonify
from pymongo import MongoClient
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Enable Cross-Origin requests

# Load Mongo URI from environment variables
MONGO_URI = os.getenv("MONGO_URI")

# Connect to MongoDB
try:
    client = MongoClient(MONGO_URI)
    db = client["luarmor"]  # database name
    keys_collection = db["keys"]  # collection name
except Exception as e:
    print("Error connecting to MongoDB:", e)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"status": "API is running 🚀"})

@app.route("/validate", methods=["GET"])
def validate():
    try:
        key = request.args.get("key")
        if not key:
            return jsonify({"error": "Key parameter is missing"}), 400

        # Check if key exists in DB
        if keys_collection.find_one({"key": key}):
            return jsonify({"status": "valid"}), 200
        else:
            return jsonify({"status": "invalid"}), 404

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
