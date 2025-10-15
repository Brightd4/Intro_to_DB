# MySQLServer.py
import mysql.connector
from mysql.connector import errorcode
import getpass

def main():
    user = input("MySQL user [root]: ") or "root"
    host = input("Host [localhost]: ") or "localhost"
    password = getpass.getpass("Password: ")

    conn = None
    cursor = None

    try:
        # connect without selecting a database
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )
        cursor = conn.cursor()
        # create the database if it does not exist
        cursor.execute(
            "CREATE DATABASE IF NOT EXISTS alx_book_store "
            "CHARACTER SET UTF8MB4 COLLATE UTF8MB4_UNICODE_CI"
        )
        # no SELECT or SHOW used
        print("Database 'alx_book_store' created successfully!")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error: Access denied. Check username or password.")
        elif err.errno == errorcode.CR_CONN_HOST_ERROR:
            print("Error: Cannot connect to MySQL server. Verify that the service is running and host is correct.")
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
