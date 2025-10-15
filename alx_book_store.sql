-- CREATE DATABASE AND SELECT IT
DROP DATABASE IF EXISTS alx_book_store;
CREATE DATABASE alx_book_store CHARACTER SET UTF8MB4 COLLATE UTF8MB4_UNICODE_CI;
USE alx_book_store;

-- CREATE TABLE: AUTHORS
CREATE TABLE authors (
    author_id INT NOT NULL AUTO_INCREMENT,
    author_name VARCHAR(215) NOT NULL,
    PRIMARY KEY (author_id)
) ENGINE=INNODB DEFAULT CHARSET=UTF8MB4;

-- CREATE TABLE: CUSTOMERS
CREATE TABLE customers (
    customer_id INT NOT NULL AUTO_INCREMENT,
    customer_name VARCHAR(215) NOT NULL,
    email VARCHAR(215) NOT NULL,
    address TEXT,
    PRIMARY KEY (customer_id),
    UNIQUE KEY uq_customers_email (email)
) ENGINE=INNODB DEFAULT CHARSET=UTF8MB4;

-- CREATE TABLE: BOOKS
CREATE TABLE books (
    book_id INT NOT NULL AUTO_INCREMENT,
    title VARCHAR(130) NOT NULL,
    author_id INT NOT NULL,
    price DOUBLE NOT NULL,
    publication_date DATE,
    PRIMARY KEY (book_id),
    KEY idx_books_author_id (author_id),
    CONSTRAINT fk_books_author
        FOREIGN KEY (author_id)
        REFERENCES authors (author_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
) ENGINE=INNODB DEFAULT CHARSET=UTF8MB4;

-- CREATE TABLE: ORDERS
CREATE TABLE orders (
    order_id INT NOT NULL AUTO_INCREMENT,
    customer_id INT NOT NULL,
    order_date DATE NOT NULL,
    PRIMARY KEY (order_id),
    KEY idx_orders_customer_id (customer_id),
    CONSTRAINT fk_orders_customer
        FOREIGN KEY (customer_id)
        REFERENCES customers (customer_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
) ENGINE=INNODB DEFAULT CHARSET=UTF8MB4;

-- CREATE TABLE: ORDER_DETAILS
CREATE TABLE order_details (
    orderdetailid INT NOT NULL AUTO_INCREMENT,
    order_id INT NOT NULL,
    book_id INT NOT NULL,
    quantity DOUBLE NOT NULL,
    PRIMARY KEY (orderdetailid),
    KEY idx_order_details_order_id (order_id),
    KEY idx_order_details_book_id (book_id),
    CONSTRAINT fk_order_details_order
        FOREIGN KEY (order_id)
        REFERENCES orders (order_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT fk_order_details_book
        FOREIGN KEY (book_id)
        REFERENCES books (book_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
) ENGINE=INNODB DEFAULT CHARSET=UTF8MB4;
