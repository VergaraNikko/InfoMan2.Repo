from flask import Flask, request, jsonify
from users import get_all_users, get_user_by_id, create_user, update_user, delete_user
from books import get_all_books, get_book_by_id, create_book, update_book, delete_book
from orders import place_order, get_all_orders, get_order_by_id, update_order, delete_order
from flask_mysqldb import MySQL
from bookstore.database import set_database
from dotenv import load_dotenv
from os import getenv

app = Flask(__name__)

load_dotenv()

app.config["MYSQL_HOST"] = getenv("MYSQL_HOST")
#app.config["MYSQL_PORT"] = int(getenv("MYSQL_PORT"))
app.config["MYSQL_USER"] = getenv("MYSQL_USER")
app.config["MYSQL_PASSWORD"] = getenv("MYSQL_PASSWORD")
app.config["MYSQL_DB"] = getenv("MYSQL_DB")
# to return results as dictionaries and not an array
app.config["MYSQL_CURSORCLASS"] = getenv("MYSQL_CURSORCLASS")
app.config["MYSQL_AUTOCOMMIT"] = True if getenv("MYSQL_AUTOCOMMIT") == "True" else False

mysql = MySQL(app)
set_database(mysql)

@app.route('/')
def home():
    return "<h1>Welcome to the Online Bookstore!</h1>"

@app.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == "POST":
        try:
            data = request.get_json()
            result = create_user(data)
            return jsonify(result), 201  # HTTP 201 Created
        except Exception as e:
            return jsonify({"error": str(e)}), 400  # HTTP 400 Bad Request
    else:
        result = get_all_users()
        return jsonify(result)

@app.route('/users/<id>', methods=['GET', 'PUT', 'DELETE'])
def users_by_id(id):
    try:
        if request.method == "PUT":
            data = request.get_json()
            result = update_user(id, data)
        elif request.method == "DELETE":
            result = delete_user(id)
        else:
            result = get_user_by_id(id)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # HTTP 500 Internal Server Error


@app.route('/books', methods=['GET', 'POST'])
def manage_books():
    if request.method == "POST":
        try:
            data = request.get_json()
            result = create_book(data)
            return jsonify(result), 201 
        except Exception as e:
            return jsonify({"error": str(e)}), 400
    else:
        result = get_all_books()
    return jsonify(result)


@app.route('/books/<book_id>', methods=['GET', 'PUT', 'DELETE'])
def manage_book_by_id(book_id):
    try:
        if request.method == "PUT":
            data = request.get_json()
            result = update_book(book_id, data)
        elif request.method == "DELETE":
            result = delete_book(book_id)
        else:
            result = get_book_by_id(book_id)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

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
