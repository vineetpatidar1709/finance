from expense import Expense
from file_manager import save_expense, load_expenses, backup_data, restore_data
from validators import validate_amount, validate_date, validate_category, validate_description
from reports import total_expense, print_report

def show_menu():
    print("\n===== Personal Finance Manager =====")
    print("1️⃣  Add Expense")
    print("2️⃣  View Total Expense")
    print("3️⃣  Generate Expense Report")
    print("4️⃣  Backup Data")
    print("5️⃣  Restore Data")
    print("6️⃣  Exit")

def add_expense():
    try:
        amount = validate_amount(input("Enter amount: "))
        category = validate_category(input("Enter category: "))
        date = validate_date(input("Enter date (YYYY-MM-DD): "))
        description = validate_description(input("Enter description: "))

        expense = Expense(amount, category, date, description)
        save_expense(expense)
        print("✅ Expense added successfully!")

    except ValueError as e:
        print("❌ Error:", e)

def main():
    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            expenses = load_expenses()
            print("💰 Total Expense:", total_expense(expenses))

        elif choice == "3":
            expenses = load_expenses()
            if not expenses:
                print("No expenses recorded yet.")
            else:
                print_report(expenses)

        elif choice == "4":
            backup_data()

        elif choice == "5":
            restore_data()

        elif choice == "6":
            print("👋 Exiting program...")
            break

        else:
            print("❌ Invalid choice, try again.")

if __name__ == "__main__":
    main()
