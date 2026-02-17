from database.db_connection import get_connection

def monthly_summary(user_id,month,year):
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

    print("\nMonthly Expense Summary")
    for category,total in results:
        print(f"{category}:{total}")


def show_balance(user_id):
    conn=get_connection()
    cursor=conn.cursor()

    query="""
        SELECT
        SUM(CASE WHEN transaction_type='income' THEN amount ELSE 0 END) -
        SUM(CASE WHEN transaction_type='expense' THEN amount ELSE 0 END)
        FROM transactions
        WHERE user_id=%s
    """

    cursor.execute(query,(user_id))
    balance=cursor.fetchone()[0]
    conn.close()

    print(f"\nCurrent Balance: {balance}")
