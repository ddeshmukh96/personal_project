import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="expense_user",
        password="StrongPass@123",
        database="expense_tracker"
    )