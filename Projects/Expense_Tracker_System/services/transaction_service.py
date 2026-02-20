from database.db_connection import get_connection
from datetime import date

def add_income(user_id: int):
    amount=float(input("Enter income amount: "))
    description=input("Description: ")

    conn=get_connection()
    cursor=conn.cursor()

    query="""
        INSERT INTO transactions
        (user_id,amount,transaction_type,transaction_date,description)
        VALUES (%s,%s,'income',%s,%s)
    """

    cursor.execute(query,(user_id,amount,date.today(),description))
    conn.commit()
    conn.close()

    print("Income added successfully")

def add_expense(user_id: int):
    amount=float(input("Enter expense amount: "))
    description=input("Description: ")

    conn=get_connection()
    cursor=conn.cursor()

    # Fetch categories dynamically
    cursor.execute("SELECT category_id,category_name FROM categories ORDER BY category_id")
    categories=cursor.fetchall()

    if not categories:
        print("No categories found. Please add categories first.")
        conn.close()
        return
    
    print("\nSelect Category:")
    for c_id,c_name in categories:
        print(f"{c_id}. {c_name}")
    
    try:
        selected_id=int(input("Choose category number: "))
    except ValueError:
        print("Invalid input.")
        conn.close()
        return
    
    category_ids=[c_id for c_id, _ in categories]

    if selected_id not in category_ids:
        print("Invalid category selection.")
        conn.close()
        return

    query="""
        INSERT INTO transactions
        (user_id,category_id,amount,transaction_type,transaction_date,description)
        VALUES (%s,%s,%s,'expense',%s,%s)
    """

    cursor.execute(query,(user_id,selected_id,amount,date.today(),description))
    conn.commit()
    conn.close()

    print("Expense added successfully.")

def list_transactions(user_id: int):
    conn=get_connection()
    cursor=conn.cursor()

    query="""
    SELECT
        t.transaction_id,
        t.amount,
        t.transaction_type,
        c.category_name,
        t.transaction_date,
        t.description
    FROM transactions t
    LEFT JOIN categories c ON t.category_id=c.category_id
    WHERE t.user_id=%s
    ORDER BY t.transaction_date DESC
    """

    cursor.execute(query, (user_id,))
    results=cursor.fetchall()
    conn.close()

    if not results:
        print("No transactions found.")
        return
    
    print("\n--- Transactions ---")
    for result in results:
        print(result)