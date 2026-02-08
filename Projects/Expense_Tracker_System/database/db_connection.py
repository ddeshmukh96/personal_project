import mysql.connector

def get_connection(password):
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password=password,
        database="expense_tracker"
    )