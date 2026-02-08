from database.db_connection import get_connection
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def try_to_create_users_table(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        user_id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(100) UNIQUE NOT NULL,
        password VARCHAR(256) NOT NULL
    )
    """)


def register_user():
    username=input("Enter username: ")
    password=input("Enter password: ")

    hashed_password=hash_password(password)

    conn=get_connection(password)
    cursor=conn.cursor()

    try:
        try_to_create_users_table(cursor)
        query="INSERT INTO users (username,password) VALUE (%s,%s)"
        cursor.execute(query,(username,hashed_password))
        conn.commit()
        print("User registered successfully")
    except:
        print("Username already exists")
    conn.close()

register_user()