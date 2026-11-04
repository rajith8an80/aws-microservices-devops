from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/products", methods=["GET"])
def get_products():
    return jsonify([
        {"id": 101, "name": "Laptop", "price": 50000},
        {"id": 102, "name": "Mobile", "price": 20000}
    ])

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "healthy", "service": "product"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)