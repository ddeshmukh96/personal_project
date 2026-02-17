from database.db_connection import get_connection
from datetime import date

def add_income(user_id):
    amount=float(input("Enter income amount: "))
    description=input("Description: ")

    conn=get_connection
    cursor=conn.cursor()

    query="""
        INSERT INTO transactions
        (user_id,amount,transaction_type,transaction_date,description)
        VALUES
    """

    cursor.execute(query,(user_id,amount,date.today(),description))
    conn.commit()
    conn.close()

    print("Income added successfully")

def add_expense(user_id):
    amount=float(input("Enter expense amount: "))
    category_id=int(input("Enter category id: "))
    description=input("Description: ")

    conn=get_connection
    cursor=conn.cursor()

    query="""
        INSERT INTO transactions
        (user_id,category_id,amount,transaction_type,transaction_date,description)
        VALUES
    """

    cursor.execute(query,(user_id,category_id,amount,date.today(),description))
    conn.commit()
    conn.close()

    print("Expense added successfully")