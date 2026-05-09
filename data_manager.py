import json
import os
from datetime import datetime

DATA_FILE = "expenses.json"

def _initialize_data_file():
    """Ensures the data file exists and contains a valid empty list if it's missing."""
    if not os.path.exists(DATA_FILE):
        print(f"Data file '{DATA_FILE}' not found. Creating it with an empty list.")
        with open(DATA_FILE, 'w') as f:
            json.dump([], f)

def load_expenses():
    """Loads all expenses from the JSON file."""
    _initialize_data_file()
    try:
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        # Handle case where file exists but is empty or corrupted
        print("Warning: Data file is corrupted or empty. Starting with an empty expense list.")
        return []
    except IOError as e:
        print(f"Error reading data file: {e}")
        return []

def save_expenses(expenses):
    """Saves the expense list back to the JSON file."""
    try:
        with open(DATA_FILE, 'w') as f:
            json.dump(expenses, f, indent=4)
        return True
    except Exception as e:
        print(f"Error saving data file: {e}")
        return False

def add_expense_to_data(amount: float, category: str, description: str) -> dict or None:
    """Adds a new expense, assigns an ID, and saves the data."""
    if amount <= 0:
        print("Error: Amount must be positive.")
        return None
    
    expenses = load_expenses()
    
    # Generate a unique ID (simple sequential ID)
    new_id = len(expenses) + 1 if expenses else 1
    
    new_expense = {
        "id": new_id,
        "date": datetime.now().strftime("%Y-%m-%d"),
        "amount": round(amount, 2),
        "category": category,
        "description": description
    }
    
    expenses.append(new_expense)
    
    if save_expenses(expenses):
        print(f"Successfully added expense ID {new_id}.")
        return new_expense
    else:
        return None

def get_all_expenses():
    """Returns a copy of all loaded expenses."""
    return load_expenses()

def delete_expense_from_data(expense_id: int) -> bool:
    """Deletes an expense by ID."""
    expenses = load_expenses()
    
    initial_count = len(expenses)
    
    # Filter out the expense with the matching ID
    updated_expenses = [e for e in expenses if e['id'] != expense_id]
    
    if len(updated_expenses) == initial_count:
        print(f"Error: Expense with ID {expense_id} not found.")
        return False

    if save_expenses(updated_expenses):
        print(f"Successfully deleted expense ID {expense_id}.")
        return True

def print_expenses(expenses: list):
    """Prints the list of expenses in a structured table format."""
    if not expenses:
        print("\n--- No expenses recorded yet. ---")
        return

    # Simple formatting using markdown table structure for visual clarity
    print("\n--- Expense Report ---")
    header = "{:<5} {:<12} {:<10} {:<15} {:<50}".format("ID", "Date", "Amount", "Category", "Description")
    print(header)
    print("-" * (5 + 12 + 10 + 15 + 50 + 4)) # Adjusting length for separator
    
    for expense in expenses:
        line = "{:<5} {:<12} ${:<9.2f} {:<15} {:<50}".format(
            expense['id'], 
            expense['date'], 
            expense['amount'], 
            expense['category'], 
            expense['description']
        )
        print(line)
    print("--------------------------\n")