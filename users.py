users = [
    {
        "id": 1,
        "name": "John",
        "email": "john@doe.com",
        "password": "123456"
    },
    {
        "id": 2,
        "name": "Jane",
        "email": "jane@doe.com",
        "password": "654321"
    },
    {
    "id": 3,
        "name": "Joe",
        "email": "joe@doe.com",
        "password": "123456"
    }
    ]

def create_user(data):
    data["id"] = users[-1]["id"] + 1
    users.append(data) # @TODO - replace this with a databawse call INSERT
    return data

def get_all_users():
    # @TODO - replace this with a databawse call SELECT
    return users

def get_user_by_id(id):
    # @TODO - replace this with a databawse call SELECT
    for user in users:
        if user["id"] == int(id):
            return user
    return None

def update_user(id, data):
    # @TODO - replace this with a databawse call UPDATE
    for user in users:
        if user["id"] == int(id):
            user["name"] = data["name"]
            user["email"] = data["email"]
            user["password"] = data["password"]
            return user
    return None

def delete_user(id):
    # @TODO - replace this with a databawse call DELETE
    for index, user in enumerate(users):
        if user["id"] == int(id):
            users.pop(index)
            return True
    return False