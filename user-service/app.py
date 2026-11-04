from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/users", methods=["GET"])
def get_users():
    return jsonify([
        {"id": 1, "name": "Raj"},
        {"id": 2, "name": "Kiran"}
    ])

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "healthy", "service": "user"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)