from flask import Flask, request, jsonify
import requests

app = Flask(__name__)  # Corrected __name__

# In-memory storage for products
products = []

# Fetch initial product list from Dummy JSON API
def fetch_initial_products():
    global products
    try:
        response = requests.get("https://dummyjson.com/products")
        response.raise_for_status()
        products = response.json().get("products", [])
    except requests.exceptions.RequestException as e:
        products = []
        print(f"Error fetching data from Dummy JSON API: {e}")

# Load products on startup
fetch_initial_products()

@app.route('/products', methods=['GET', 'POST'])
def handle_products():
    if request.method == 'GET':
        # Return the list of products
        return jsonify(products), 200

    if request.method == 'POST':
        # Validate the incoming product data
        new_product = request.get_json()
        if not new_product or not all(key in new_product for key in ["title", "price", "category"]):
            return jsonify({"error": "Invalid product data. 'title', 'price', and 'category' are required."}), 400

        # Add the new product to the list
        products.append(new_product)
        return jsonify(products), 201

# Error handler for Dummy JSON API unreachability
@app.errorhandler(500)
def internal_server_error(e):
    return jsonify({"error": "Internal server error."}), 500

if __name__ == '__main__':
    app.run(debug=True)
