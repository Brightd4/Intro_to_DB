# CreateTables.py
import mysql.connector
from mysql.connector import errorcode
import getpass

def main():
    print("This script will create the required tables in the alx_book_store database.")
    user = input("MySQL user [root]: ") or "root"
    host = input("Host [localhost]: ") or "localhost"
    password = getpass.getpass("Password: ")

    conn = None
    cursor = None
    try:
        # Connect without selecting a DB first, then ensure DB exists and USE it
        conn = mysql.connector.connect(host=host, user=user, password=password)
        cursor = conn.cursor()

        # Ensure the database exists
        cursor.execute(
            "CREATE DATABASE IF NOT EXISTS alx_book_store "
            "CHARACTER SET UTF8MB4 COLLATE UTF8MB4_UNICODE_CI"
        )
        cursor.execute("USE alx_book_store")

        # AUTHORS
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS authors (
            author_id INT NOT NULL AUTO_INCREMENT,
            author_name VARCHAR(215) NOT NULL,
            PRIMARY KEY (author_id)
        ) ENGINE=INNODB DEFAULT CHARSET=UTF8MB4
        """)
        print("Table AUTHORS ready")

        # CUSTOMERS
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            customer_id INT NOT NULL AUTO_INCREMENT,
            customer_name VARCHAR(215) NOT NULL,
            email VARCHAR(215) NOT NULL,
            address TEXT,
            PRIMARY KEY (customer_id),
            UNIQUE KEY uq_customers_email (email)
        ) ENGINE=INNODB DEFAULT CHARSET=UTF8MB4
        """)
        print("Table CUSTOMERS ready")

        # BOOKS
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
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
        ) ENGINE=INNODB DEFAULT CHARSET=UTF8MB4
        """)
        print("Table BOOKS ready")

        # ORDERS
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
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
        ) ENGINE=INNODB DEFAULT CHARSET=UTF8MB4
        """)
        print("Table ORDERS ready")

        # ORDER_DETAILS
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS order_details (
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
        ) ENGINE=INNODB DEFAULT CHARSET=UTF8MB4
        """)
        print("Table ORDER_DETAILS ready")

        conn.commit()
        print("All tables created successfully in database 'alx_book_store'")

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error: ACCESS DENIED. CHECK USERNAME OR PASSWORD")
        elif err.errno == errorcode.ER_CANNOT_ADD_FOREIGN:
            print("Error: CANNOT ADD FOREIGN KEY. CHECK TABLE ORDER OR TYPES")
        else:
            print(f"Error: {err}")
    finally:
        try:
            if cursor is not None:
                cursor.close()
        except Exception:
            pass
        try:
            if conn is not None and conn.is_connected():
                conn.close()
        except Exception:
            pass

if __name__ == "__main__":
    main()
