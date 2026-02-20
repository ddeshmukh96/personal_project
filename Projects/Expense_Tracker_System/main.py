from services.user_service import register_user, login_user
from services.transaction_service import(
    add_income,
    add_expense,
    list_transactions
)
from services.report_service import(
    monthly_summary,
    category_expense_summary,
    show_balance
)

def user_menu(user_id: int):
    while True:
        print("\n====== Expense Tracker Menu ======")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. List Transactions")
        print("4. Monthly Financial Summary (Income vs Expense)")
        print("5. Category-wise Expense Report")
        print("6. Show Balance")
        print("7. Logout")
        print("0. Exit")

        choice=input("Choose an option: ").strip()

        if choice=="1":
            add_income(user_id)
        elif choice=="2":
            add_expense(user_id)
        elif choice=="3":
            list_transactions(user_id)
        elif choice=="4":
            month=int(input("Enter month (1-12): "))
            year=int(input("Enter year (YYYY): "))
            monthly_summary(user_id,month,year)
        elif choice=="5":
            month=int(input("Enter month (1-12): "))
            year=int(input("Enter year (YYYY): "))
            category_expense_summary(user_id,month,year)
        elif choice=="6":
            show_balance(user_id)
        elif choice=="7":
            print("Logged out.")
            break
        elif choice=="0":
            print("Existing application.")
            exit(0)
        else:
            print("Invalid option. Try again.")


def main():
    while True:
        print("\n====== Welcome to Expense Tracker System ======")
        print("1. Register")
        print("2. Login")
        print("0. Exit")

        choice=input("Choose an option: ").strip()

        if choice=="1":
            register_user()
        elif choice=="2":
            user_id=login_user()
            if user_id:
                user_menu(user_id)
        elif choice=="0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again")

if __name__=="__main__":
    main()