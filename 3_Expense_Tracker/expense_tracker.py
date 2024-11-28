# Adds a new expense to the list of expenses
def add_expense(expenses, amount, category):
    expenses.append({'amount': amount, 'category': category})

# Prints all expenses in a formatted way
def print_expenses(expenses):
    for expense in expenses:
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')
    
# Calculates the total amount of all expenses
def total_expenses(expenses):
    return sum(map(lambda expense: expense['amount'], expenses))

# Filters expenses by a given category and returns an iterable of matching expenses
def filter_expenses_by_category(expenses, category):
    return filter(lambda expense: expense['category'] == category, expenses)
    
# Main function to manage the expense tracker program
def main():
    expenses = []  # Initialize an empty list to store expenses
    while True:  # Continuous loop until the user chooses to exit
        # Display menu options
        print('\nExpense Tracker')
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Exit')
       
        choice = input('Enter your choice: ')  # Get user input for menu choice

        if choice == '1':  # Add a new expense
            amount = float(input('Enter amount: '))  # Get the amount as a float
            category = input('Enter category: ')  # Get the category as a string
            add_expense(expenses, amount, category)

        elif choice == '2':  # List all expenses
            print('\nAll Expenses:')
            print_expenses(expenses)
    
        elif choice == '3':  # Display the total of all expenses
            print('\nTotal Expenses: ', total_expenses(expenses))
    
        elif choice == '4':  # Filter and display expenses by category
            category = input('Enter category to filter: ')  # Get the category to filter
            print(f'\nExpenses for {category}:')
            expenses_from_category = filter_expenses_by_category(expenses, category)
            print_expenses(expenses_from_category)  # Display the filtered expenses
    
        elif choice == '5':  # Exit the program
            print('Exiting the program.')
            break  # Break the loop to exit

main()  # Call the main function to start the program