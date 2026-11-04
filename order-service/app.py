from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/orders", methods=["GET"])
def get_orders():
    return jsonify([
        {"order_id": 1001, "user_id": 1, "product_id": 101},
        {"order_id": 1002, "user_id": 2, "product_id": 102}
    ])

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "healthy", "service": "order"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003)