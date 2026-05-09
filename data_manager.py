def update_expense_amount_in_data(expense_id: int, new_amount: float) -> bool:
    """Updates the amount of a specified expense by ID and saves the data."""
    if new_amount <= 0:
        print("Error: New amount must be positive.")
        return False
    
    expenses = load_expenses()
    
    updated_expenses = []
    found = False
    
    for expense in expenses:
        if expense['id'] == expense_id:
            expense['amount'] = round(new_amount, 2)
            found = True
            print(f"Expense ID {expense_id} updated successfully.")
        updated_expenses.append(expense)
    
    if not found:
        print(f"Error: Expense with ID {expense_id} not found. No changes made.")
        return False

    if save_expenses(updated_expenses):
        return True
    else:
        return False