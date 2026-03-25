from flask import Flask, jsonify, request
import json
import os

app = Flask(__name__)

DATA_FILE = os.path.join(os.path.dirname(__file__), "data", "customers.json")

# Load data from JSON file
def load_customers():
    with open(DATA_FILE, "r") as f:
        return json.load(f)


@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200


@app.route("/api/customers", methods=["GET"])
def get_customers():
    try:
        customers = load_customers()

        # Pagination params
        page = int(request.args.get("page", 1))
        limit = int(request.args.get("limit", 10))

        start = (page - 1) * limit
        end = start + limit

        paginated_data = customers[start:end]

        return jsonify({
            "data": paginated_data,
            "total": len(customers),
            "page": page,
            "limit": limit
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/customers/<customer_id>", methods=["GET"])
def get_customer(customer_id):
    try:
        customers = load_customers()

        for customer in customers:
            if customer["customer_id"] == customer_id:
                return jsonify(customer), 200

        return jsonify({"error": "Customer not found"}), 404

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)