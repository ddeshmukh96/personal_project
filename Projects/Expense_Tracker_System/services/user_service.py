from database.db_connection import get_connection
import hashlib

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()


def register_user():
    username=input("Enter username: ")
    password=input("Enter password: ")

    hashed_password=hash_password(password)

    conn=get_connection()
    cursor=conn.cursor()

    try:
        query="""
        INSERT INTO users (username,password)
        VALUES (%s,%s)
        """
        cursor.execute(query,(username,hashed_password))
        conn.commit()
        print("User registered successfully")
    except Exception as e:
        print("Registration failed:", e)
    finally:
        conn.close()


def login_user():
    username=input("Enter username: ")
    password=input("Enter password: ")

    hashed_password=hash_password(password)

    conn=get_connection()
    cursor=conn.cursor()

    query="""
    SELECT user_id FROM users
    WHERE username=%s AND password=%s
    """

    cursor.execute(query,(username,hashed_password))
    user=cursor.fetchone()
    conn.close()

    if user:
        print("Login successful.")
        return user[0]  #user_id
    else:
        print("Invalid username or password.")
        return None

# standalone testing

# if __name__=="__main__":
#     print("1. Register")
#     print("2. Login")
#     choice=input("Choose: ")

#     if choice=="1":
#         register_user()
#     elif choice=="2":
#         uid=login_user()
#         print("Returned user_id:",uid)