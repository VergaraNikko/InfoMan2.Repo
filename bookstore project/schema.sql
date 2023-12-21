CREATE TABLE `persons` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(500) NOT NULL DEFAULT '',
  `email` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB;


CREATE TABLE `users` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `person_id` int NOT NULL,
  `username` varchar(100) NOT NULL DEFAULT '',
  `password` varchar(200) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB ;

CREATE TABLE `books` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `title` varchar(200) NOT NULL DEFAULT '',
  `author` varchar(100) NOT NULL DEFAULT '',
  `price` float(100) NOT NULL DEFAULT '',
  `availability` varchar(100) NOT NULL '',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB ;

CREATE TABLE `orders` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `book_id` int NOT NULL,
  `user_id` int NOT NULL,
  `email` varchar(200) DEFAULT NULL,
  `title` varchar(200) NOT NULL DEFAULT '',
  `author` varchar(100) NOT NULL DEFAULT '',
  `price` float(100) NOT NULL DEFAULT '',
  `quantity` float(100) NOT NULL DEFAULT '',
  `total-price` float(100) NOT NULL '',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB ;

CREATE VIEW users_view AS
  SELECT users.id,
    users.username,
    users.password,
    persons.name,
    persons.email
  FROM users
  INNER JOIN persons ON users.person_id = persons.id;

CREATE VIEW books_view AS
  SELECT books.id,
    users.user_id,
    books.title,
    books.author,
    books.price,
    books.availability
  FROM books
  INNER JOIN users ON books.user_id = users.id;

CREATE VIEW orders_view AS
  SELECT orders.id,
    users.user_id,
    uers.email
    books.book_id,
    books.title,
    books.author,
    books.price,
    order.quantity,
    order.total_price
  FROM orders
  INNER JOIN books ON orders.books_id = books.id;

DELIMITER $$$
CREATE PROCEDURE create_user(
  IN p_name varchar(500),
  IN p_email varchar(200),
  IN p_username varchar(100),
  IN p_password varchar(200)
)
BEGIN
  DECLARE p_person_id INT;
  DECLARE p_user_id INT;
  INSERT INTO persons (name, email)
    VALUES (p_name, p_email);
  SET p_person_id = LAST_INSERT_ID();
  INSERT INTO users (person_id, username, password)
    VALUES (p_person_id, p_username, p_password);
  SET p_user_id = LAST_INSERT_ID();
  SELECT p_user_id AS id;
END$$$
DELIMITER ;


DELIMITER $$$
CREATE PROCEDURE update_user(
  IN p_id INT,
  IN p_name varchar(500),
  IN p_email varchar(200),
  IN p_username varchar(100),
  IN p_password varchar(200)
)
BEGIN
  UPDATE persons
    INNER JOIN users ON persons.id = users.person_id
    SET name = p_name,
      email = p_email
    WHERE users.id = p_id;
  UPDATE users
    SET username = p_username,
      password = p_password
    WHERE id = p_id;
  SELECT p_id AS id;
END$$$
DELIMITER ;


DELIMITER $$$
CREATE PROCEDURE delete_user(
  IN p_id INT
)
BEGIN
  DELETE persons.* FROM persons
  INNER JOIN users ON persons.id = users.person_id
  WHERE users.id = p_id;
  DELETE FROM users
  WHERE id = p_id;
  SELECT id FROM users
  WHERE id = p_id;
END$$$
DELIMITER ;




/* BOOK */
DELIMITER $$$
CREATE PROCEDURE create_book(
  IN p_id INT,
  IN p_title varchar(500),
  IN p_author varchar(200),
  IN p_price float(100),
  IN p_availability varchar(200)
)
BEGIN
  DECLARE p_user_id INT;
  DECLARE p_book_id INT;
  INSERT INTO users (username, email, password)
    VALUES (p_user_id, p_username, p_password);
  SET p_user_id = LAST_INSERT_ID();
  INSERT INTO books (book_id, title, author, price, availability)
    VALUES (p_book_id, p_book_title, p_book_author, p_boook_price, p_book_availability);
  SET p_book_id = LAST_INSERT_ID();
  SELECT p_book_id AS id;
END$$$
DELIMITER ;


DELIMITER $$$
CREATE PROCEDURE update_book(
  IN p_id INT,
  IN p_title varchar(500),
  IN p_author varchar(200),
  IN p_price float(100),
  IN p_availability varchar(200)
)
BEGIN
  UPDATE users
    INNER JOIN books ON users.id = books.user_id
   SET username = p_username,
      password = p_password,
      email = p_email
    WHERE books.id = p_id;
  UPDATE books
    SET title = p_title,
      author = p_author,
      price = p_price,
      availability = p_availability
    WHERE id = p_id;
  SELECT p_id AS id;
END$$$
DELIMITER ;


DELIMITER $$$
CREATE PROCEDURE delete_books(
  IN p_id INT
)
BEGIN
  DELETE users.* FROM users
  INNER JOIN books ON users.id = books.user_id
  WHERE books.id = p_id;
  DELETE FROM books
  WHERE id = p_id;
  SELECT id FROM books
  WHERE id = p_id;
END$$$
DELIMITER ;





/* ORDER */
DELIMITER $$$
CREATE PROCEDURE place_order(
  IN p_book_id INT,
  IN p_user_id INT,
  IN p_email INT,
  IN p_title INT,
  IN p_author INT,
  IN p_price INT,
  IN p_quantity INT,
  IN p_total_price INT,
)
BEGIN
  DECLARE p_book_id INT;
  DECLARE p_order_id INT;
  INSERT INTO books (title, author, price, availability)
    VALUES (p_book_id, p_title, p_author, p_price, p_availability);
  SET p_book_id = LAST_INSERT_ID();
  INSERT INTO order (order_id, book_id, user_id, email, title, author, price, quantity, total_price)
    VALUES (p_order_id,, p_book_id, p_user_id p_user_email, p_book_title, p_book_author, p_boook_price, p_order_quantity, p_order_total-price);
  SET p_order_id = LAST_INSERT_ID();
  SELECT p_order_id AS id;
END$$$
DELIMITER ;


DELIMITER $$$
CREATE PROCEDURE update_order(
  IN p_book_id INT,
  IN p_user_id INT,
  IN p_email INT,
  IN p_title varchar(500),
  IN p_author varchar(200),
  IN p_price float(100),
  IN p_quantity float(100),
  IN p_total_price float(100)
)
BEGIN
  UPDATE orders
    INNER JOIN orders ON books.id = orders.book_id
   SET email = p_email,
      title = p_title,
      author = p_author,
      price = p_price,
      quantity = p_quantity,
      total_price = p_total_price
    WHERE orders.id = p_id;
  UPDATE orders
    SET email = p_email,
      title = p_title,
      author = p_author,
      price = p_price,
      quantity = p_quantity,
      total_price = p_total_price
    WHERE id = p_id;
  SELECT p_id AS id;
END$$$
DELIMITER ;


DELIMITER $$$
CREATE PROCEDURE delete_orders(
  IN p_id INT
)
BEGIN
  DELETE books.* FROM books
  INNER JOIN orders ON books.id = orders.book_id
  WHERE orders.id = p_id;
  DELETE FROM orders
  WHERE id = p_id;
  SELECT id FROM orders
  WHERE id = p_id;
END$$$
DELIMITER ;