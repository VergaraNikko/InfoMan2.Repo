from users import get_all_users, get_user_by_id, create_user, update_user, delete_user

books = [
    {
        "id": 1,
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "price": 15.99,
        "availability": True  # Initially in stock
    },
    {
        "id": 2,
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "price": 12.99,
        "availability": True
    },
    {
        "id": 3,
        "title": "1984",
        "author": "George Orwell",
        "price": 10.99,
        "availability": False  # Initially out of stock
    }
]

def create_book(data):
    data["id"] = books[-1]["id"] + 1
    data["availability"] = True  # By default, a newly added book is considered in stock
    books.append(data)
    return data

def get_all_books():
    return books

def get_book_by_id(book_id):
    for book in books:
        if book["id"] == int(book_id):
            return book
    return None

def update_book(book_id, data):
    for book in books:
        if book["id"] == int(book_id):
            book["title"] = data["title"]
            book["author"] = data["author"]
            book["price"] = data["price"]
            return book
    return None

def delete_book(book_id):
    for index, book in enumerate(books):
        if book["id"] == int(book_id):
            books.pop(index)
            return True
    return False


