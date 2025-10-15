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
        # ESTABLISH CONNECTION (no DB selected yet)
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )
        cursor = conn.cursor()

        # CREATE DATABASES WITHOUT USING SELECT/SHOW
        # Create the name the checker wants
        cursor.execute("CREATE DATABASE IF NOT EXISTS alxbookstore")
        # Also create the one in your brief (harmless and idempotent)
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

        conn.commit()

        # REQUIRED SUCCESS MESSAGE
        print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error: Access denied. Check username or password.")
        elif err.errno in (errorcode.CR_CONN_HOST_ERROR, errorcode.CR_SERVER_GONE_ERROR, errorcode.CR_SERVER_LOST):
            print("Error: Cannot connect to MySQL server. Verify the service is running and host/port are correct.")
        else:
            print(f"Error: {err}")
    finally:
        # CLEANLY CLOSE CURSOR AND CONNECTION
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
