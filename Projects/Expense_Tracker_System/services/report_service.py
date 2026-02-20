from database.db_connection import get_connection

# Finalncial summary (income vs expense)
def monthly_summary(user_id: int,month: int,year: int):
    conn=get_connection()
    cursor=conn.cursor()

    query="""
        SELECT transaction_type,SUM(amount)
        FROM transactions
        WHERE user_id=%s
            AND MONTH(transaction_date)=%s
            AND YEAR(transaction_date)=%s
        GROUP BY transaction_type
    """

    cursor.execute(query,(user_id,month,year))
    results=cursor.fetchall()
    conn.close()

    print("\n--- Monthly Financial Summary ---")
    for transaction_type,total in results:
        print(f"{transaction_type}:{total}")


def show_balance(user_id: int):
    conn=get_connection()
    cursor=conn.cursor()

    query="""SELECT SUM(CASE WHEN transaction_type='income' THEN amount ELSE 0 END) - SUM(CASE WHEN transaction_type='expense' THEN amount ELSE 0 END) FROM transactions WHERE user_id=%s"""

    cursor.execute(query,(user_id,))
    balance=cursor.fetchone()[0]
    conn.close()

    print(f"\nCurrent Balance: {balance}")

# Category-wise expense report (monthly)
def category_expense_summary(user_id: int, month: int, year: int):
    conn=get_connection()
    cursor=conn.cursor()

    query="""
        SELECT c.category_name,SUM(t.amount)
        FROM transactions t
        JOIN categories c ON t.category_id=c.category_id
        WHERE t.user_id=%s
            AND t.transaction_type='expense'
            AND MONTH(t.transaction_date)=%s
            AND YEAR(t.transaction_date)=%s
        GROUP BY c.category_name
    """

    cursor.execute(query,(user_id,month,year))
    results=cursor.fetchall()
    conn.close()

    print("\n--- Category-wise Expense Summary ---")

    if not results:
        print("No expense data found for this period.")
        return
    
    for category_name,total in results:
        print(f"{category_name}: {total}")