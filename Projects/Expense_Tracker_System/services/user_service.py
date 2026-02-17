from database.db_connection import get_connection
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def register_user():
    username=input("Enter username: ")
    password=input("Enter password: ")

    hashed_password=hash_password(password)

    conn=get_connection()
    cursor=conn.cursor()

    try:
        query="INSERT INTO users (username,password) VALUE (%s,%s)"
        cursor.execute(query,(username,hashed_password))
        conn.commit()
        print("User registered successfully")
    except:
        print("Username already exists")
    finally:
        conn.close()

def login_user():
    username=input("Enter username: ")
    password=input("Enter password: ")

    hashed_password=hash_password(password)

    conn=get_connection()
    cursor=conn.cursor()

    query="SELECT user_id FROM users WHERE username=%s AND password=%s"
    cursor.execute(query,(username,hashed_password))

    user=cursor.fetchone()
    conn.close()

    if user:
        print("Login successful")
        return user[0]
    else:
        print("Invalid credentials")
        return None