

# Flask API for Product Management

## Overview
This project is a **Flask-based API** for managing a list of products. It includes features for retrieving an initial product list from a public API and supports both fetching and adding products via HTTP methods. The application is designed to handle errors gracefully and ensures proper data validation for incoming requests.

---

## Features
- **Initial Data Load**: Fetches products from the Dummy JSON API (`https://dummyjson.com/products`) on application startup.
- **GET `/products`**: Retrieves the current list of products.
- **POST `/products`**: Adds a new product to the in-memory storage with validation for required fields.
- **Error Handling**: Handles server errors and invalid input with appropriate status codes and messages.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/flask-product-api.git
   cd flask-product-api
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask application:
   ```bash
   python app.py
   ```

4. Access the API at:
   ```
   http://127.0.0.1:5000
   ```

---

## API Endpoints

### 1. GET `/products`
- **Description**: Fetches the list of products.
- **Response**:
  - **200 OK**: Returns the current product list.
- **Example Response**:
  ```json
  [
      {
          "id": 1,
          "title": "iPhone 9",
          "price": 549,
          "category": "smartphones"
      },
      ...
  ]
  ```

---

### 2. POST `/products`
- **Description**: Adds a new product to the in-memory storage.
- **Request Body**:
  - JSON format with required fields: `title`, `price`, and `category`.
- **Response**:
  - **201 Created**: Returns the updated product list.
  - **400 Bad Request**: Returns an error message if required fields are missing.
- **Example Request**:
  ```json
  {
      "title": "New Product",
      "price": 100,
      "category": "gadgets"
  }
  ```
- **Example Response**:
  ```json
  [
      {
          "id": 1,
          "title": "iPhone 9",
          "price": 549,
          "category": "smartphones"
      },
      {
          "title": "New Product",
          "price": 100,
          "category": "gadgets"
      }
  ]
  ```

---

## Error Handling
- **500 Internal Server Error**: Triggered if there are issues connecting to the Dummy JSON API or other server-related errors.
  - Example Response:
    ```json
    {
        "error": "Internal server error."
    }
    ```
- **400 Bad Request**: Triggered when required fields are missing during a POST request.
  - Example Response:
    ```json
    {
        "error": "Invalid product data. 'title', 'price', and 'category' are required."
    }
    ```

---

## Usage with Postman

1. **GET `/products`**:
   - Method: GET
   - URL: `http://127.0.0.1:5000/products`
   - Response: List of products.

2. **POST `/products`**:
   - Method: POST
   - URL: `http://127.0.0.1:5000/products`
   - Body: JSON
     ```json
     {
         "title": "Sample Product",
         "price": 150,
         "category": "electronics"
     }
     ```
   - Response: Updated product list.

---
