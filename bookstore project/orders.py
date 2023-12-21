from books import get_all_books, get_book_by_id, create_book, update_book, delete_book
from users import get_all_users, get_user_by_id, create_user, update_user, delete_user

orders = []

def place_order(book_id, user_id, quantity):
    book = get_book_by_id(book_id)
    user = get_user_by_id(user_id)

    if book and book["availability"] and user:
        order = {
            "order_id": len(orders) + 1,
            "book_id": book_id,
            "user_id": user_id,
            "email": user["email"],
            "title": book["title"],
            "author": book["author"],
            "price": book["price"],
            "quantity": quantity,
            "total_price": quantity * book["price"]
        }
        orders.append(order)
        book["availability"] = False  # Update availability after placing an order
        return order
    return {"message": "Book not available or not found."}

def get_all_orders():
    return orders

def get_order_by_id(order_id):
    for order in orders:
        if order["order_id"] == int(order_id):
            return order
    return None

def update_order(order_id, data):
    for order in orders:
        if order["order_id"] == int(order_id):
            order["quantity"] = data["quantity"]
            order["total_price"] = order["quantity"] * order["price"]
            return order
    return None

def delete_order(order_id):
    for index, order in enumerate(orders):
        if order["order_id"] == int(order_id):
            orders.pop(index)
            return True
    return False