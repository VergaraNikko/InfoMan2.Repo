from flask import Flask, request, jsonify
from books import get_all_books, get_book_by_id, create_book, update_book, delete_book
from users import get_all_users, get_user_by_id, create_user, update_user, delete_user
from orders import get_order_by_id, place_order, get_all_orders, update_order, delete_order

app = Flask(__name__)


@app.route('/')
def home():
    return "<h1>Welcome to the Online Bookstore!</h1>"

@app.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == "POST":
        data = request.get_json()
        result = create_user(data)
    else:
        result = get_all_users()
    return jsonify(result)


@app.route('/users/<id>', methods=['GET', 'PUT', 'DELETE'])
def users_by_id(id):
    if request.method == "PUT":
        data = request.get_json()
        result = update_user(id, data)
    elif request.method == "DELETE":
        result = delete_user(id)
    else:
        result = get_user_by_id(id)
    return jsonify(result)

@app.route('/books', methods=['GET', 'POST'])
def manage_books():
    if request.method == "POST":
        data = request.get_json()
        result = create_book(data)
    else:
        result = get_all_books()
    return jsonify(result)


@app.route('/books/<book_id>', methods=['GET', 'PUT', 'DELETE'])
def manage_book_by_id(book_id):
    if request.method == "PUT":
        data = request.get_json()
        result = update_book(book_id, data)
    elif request.method == "DELETE":
        result = delete_book(book_id)
    else:
        result = get_book_by_id(book_id)
    return jsonify(result)

@app.route('/orders/<book_id>/<user_id>', methods=['POST'])
def place_order_for_book(book_id, user_id):
    quantity = request.get_json().get("quantity", 1)
    result = place_order(book_id, user_id, quantity)
    return jsonify(result)

@app.route('/orders', methods=['GET'])
def get_all_orders_endpoint():
    result = get_all_orders()
    return jsonify(result)

@app.route('/orders/<order_id>', methods=['GET', 'PUT', 'DELETE'])
def manage_order_by_id(order_id):
    if request.method == "PUT":
        data = request.get_json()
        result = update_order(order_id, data)
    elif request.method == "DELETE":
        result = delete_order(order_id)
    else:
        result = get_order_by_id(order_id)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
