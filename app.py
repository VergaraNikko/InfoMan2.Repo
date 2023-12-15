from flask import Flask, request, jsonify
from users import get_all_users, get_user_by_id, create_user, update_user, delete_user
from database import set_database

app = Flask(__name__)

app.config["MYSQL_DATABASE_HOST"] = "localhost"
app.config["MYSQL_DATABASE_PORT"] = 3306
app.config["MYSQL_DATABASE_USER"] = "root"
app.config["MYSQL_DATABASE_PASSWORD"] = ""
#app.config["MYSQL_DATABASE_DB"] = ""

@app.route('/')
def home():
    return "<h1>Hello, CSIT327!</h1>"

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


if __name__ == '__main__':
    app.run(debug=True)
