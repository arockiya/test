import argparse
import data_manager

def add_expense(args):
    """Handles the 'add' command: adds a new expense."""
    data_manager.add_expense_to_data(
        amount=args.amount,
        category=args.category,
        description=args.description
    )

def view_expenses(args):
    """Handles the 'view' command: displays all recorded expenses."""
    expenses = data_manager.get_all_expenses()
    data_manager.print_expenses(expenses)

def delete_expense(args):
    """Handles the 'delete' command: deletes an expense by ID."""
    try:
        expense_id = int(args.id)
        data_manager.delete_expense_from_data(expense_id)
    except ValueError:
        print("Error: Expense ID must be an integer.")

def main():
    """Main function to parse arguments and run the CLI application."""
    parser = argparse.ArgumentParser(
        description="A simple CLI expense tracker."
    )
    subparsers = parser.add_subparsers(dest="command")

    # View command
    parser_view = subparsers.add_parser("view", help="View all recorded expenses.")
    parser_view.set_defaults(func=view_expenses)

    # Add command
    parser_add = subparsers.add_parser("add", help="Add a new expense.")
    parser_add.add_argument("amount", type=float, help="The monetary amount of the expense.")
    parser_add.add_argument("category", help="The category of the expense (e.g., Food, Travel).")
    parser_add.add_argument("description", help="A brief description of the expense.")
    parser_add.set_defaults(func=add_expense)
    
    # Delete command
    parser_delete = subparsers.add_parser("delete", help="Delete an expense by ID.")
    parser_delete.add_argument("id", type=str, help="The ID of the expense to delete.")
    parser_delete.set_defaults(func=delete_expense)

    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()