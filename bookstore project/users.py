from database import fetchall, fetchone, execute

def create_user(data):
    try:
        cur = execute("CALL create_user(%s, %s, %s, %s)",
                      (data["name"], data["email"], data["username"], data["password"]))
        row = cur.fetchone()
        data["id"] = row["id"]
        return data
    except Exception as e:
        print(f"Error creating user: {e}")
        return None

def get_all_users():
    try:
        return fetchall("SELECT * FROM users_view")
    except Exception as e:
        print(f"Error getting all users: {e}")
        return None

def get_user_by_id(user_id):
    try:
        return fetchone("SELECT * FROM users_view WHERE id = %s", (user_id,))
    except Exception as e:
        print(f"Error getting user by ID: {e}")
        return None

def update_user(user_id, data):
    try:
        cur = execute("CALL update_user(%s, %s, %s, %s, %s)",
                      (user_id, data["name"], data["email"], data["username"], data["password"]))
        row = cur.fetchone()
        data["id"] = row["id"]
        return data
    except Exception as e:
        print(f"Error updating user: {e}")
        return None

def delete_user(user_id):
    try:
        cur = execute("CALL delete_user(%s)", (user_id,))
        row = cur.fetchone()
        if row is None:
            return True
        return False
    except Exception as e:
        print(f"Error deleting user: {e}")
        return None
