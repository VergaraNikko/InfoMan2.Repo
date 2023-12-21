from database import fetchall, fetchone, execute

def create_book(data):
    try:
        cur = execute("""CALL create_book(%s, %s, %s, %s)""", (data["title"], data["author"], data["price"], data["availability"]))
        # Assuming create_book stored procedure returns the ID
        row = cur.fetchone()
        data["id"] = row["id"]
        return data
    except Exception as e:
        # Handle the exception appropriately (e.g., log the error)
        print(f"Error creating book: {e}")
        return None

def get_all_books():
    try:
        return fetchall("""SELECT * FROM books_view""")
    except Exception as e:
        print(f"Error fetching all books: {e}")
        return None

def get_book_by_id(book_id):
    try:
        return fetchone("""SELECT * FROM books_view WHERE id = %s""", (book_id,))
    except Exception as e:
        print(f"Error fetching book by ID: {e}")
        return None

def update_book(book_id, data):
    try:
        cur = execute("""CALL update_book(%s, %s, %s, %s, %s)""", (book_id, data["title"], data["author"], data["price"], data["availability"]))
        row = cur.fetchone()
        data["id"] = row["id"]
        return data
    except Exception as e:
        print(f"Error updating book: {e}")
        return None

def delete_book(book_id):
    try:
        cur = execute("""CALL delete_book(%s)""", (book_id,))
        row = cur.fetchone()
        if row is None:
            return True
        return False
    except Exception as e:
        print(f"Error deleting book: {e}")
        return False
