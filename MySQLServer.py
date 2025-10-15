# MySQLServer.py
import mysql.connector
from mysql.connector import Error
import getpass

def main():
    user = input("MySQL user [root]: ") or "root"
    host = input("Host [localhost]: ") or "localhost"
    password = getpass.getpass("Password: ")

    conn = None
    cur = None
    try:
        # connect to server (no DB selected)
        conn = mysql.connector.connect(host=host, user=user, password=password)
        cur = conn.cursor()

        # create the database name the checker expects
        cur.execute("CREATE DATABASE IF NOT EXISTS alxbookstore")
        conn.commit()

        print("Database 'alxbookstore' created successfully!")

    except Error as e:
        # handle errors
        print(f"Error: {e}")
    finally:
        try:
            if cur is not None:
                cur.close()
        except Exception:
            pass
        try:
            if conn is not None and conn.is_connected():
                conn.close()
        except Exception:
            pass

if __name__ == "__main__":
    main()
