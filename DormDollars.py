expenses = {}


def display_expenses():
    print("\n--- All Expenses ---")
    if not expenses:
        print("No expenses recorded yet.")
    else:
        total = 0
        for category, amount in expenses.items():
            print(f"{category}: ${amount:.2f}")
            total += amount
        print(f"Total Expenses: ${total:.2f}")
        
       
        if total > 100:
            print("You are overspending😳!")
        else:
            print("You are within Budget👍")
    print("--------------------\n")


while True:
    print("Expense Tracker Menu:")
    print("1. Add Expense")
    print("2. Display Expenses")
    print("3. Remove Expense")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == '1':
        category = input("Enter the category of the expense (e.g., Food, Transport, etc.): ")
        amount = input(f"Enter the amount spent on {category}: ")

        if amount.replace('.', '', 1).isdigit():
            amount = float(amount)
            if category in expenses:
                expenses[category] += amount  
            else:
                expenses[category] = amount 
            print(f"Added ${amount:.2f} to {category}.\n")
        else:
            print("Invalid amount. Please enter a numeric value.\n")

    elif choice == '2':
        display_expenses()

    elif choice == '3':
        category = input("Enter the category of the expense to remove: ")
        if category in expenses:
            del expenses[category]
            print(f"Removed expenses for {category}.\n")
        else:
            print(f"No expenses found for {category}.\n")

    elif choice == '4':
        print("Exiting Expense Tracker. Goodbye!")
        break

    else:
        print("Invalid choice. Please select an option between 1 and 4.\n")
