# MySQLServer.py
import mysql.connector
from mysql.connector import errorcode

def create_database():
    try:
        cnx = mysql.connector.connect(user='root', password='yourpassword', host='127.0.0.1')
        cursor = cnx.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        cnx.close()

if __name__ == "__main__":
    create_database()
