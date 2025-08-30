from flask import Flask, request, jsonify
from pymongo import MongoClient
import os

app = Flask(__name__)
MONGO_URI = os.getenv("MONGO_URI")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")
client = MongoClient(MONGO_URI)
db = client["luarmor_free_panel"]
keys_collection = db["keys"]

@app.route("/validate", methods=["GET"])
def validate():
    key = request.args.get("key")
    if keys_collection.find_one({"key": key}):
        return jsonify({"status": "valid"})
    return jsonify({"status": "invalid"}), 404

@app.route("/stats", methods=["GET"])
def stats():
    total = keys_collection.count_documents({})
    return jsonify({"total_keys": total})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
