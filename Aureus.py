from database_connect import create_table, insert_value, view_value, edit_value, total_value

# Add expenses function
def add_expenses():
    while True:
        amount = float(input("Enter Amount:"))
        category = input("Enter Category:")
        date = input("Enter Date:")
        insert_value(amount ,category ,date)
        more_entry = input("Do you want to add another Expense(Y/N):")
        if more_entry.lower() != "y":
            break


def view_expenses(expenses):
    for i, data in enumerate(expenses, start=1):
        print(f"{i}. Amount: ₹{data['amount']}")
        print(f"   Category: {data['category']}")
        print(f"   Date: {data['date']}")
        print("------------------------")


def view_total(expenses):
    total_sum = sum(data['amount'] for data in expenses)
    print(f"Total Spending = ₹{total_sum}")

    
create_table()
# add_expenses()
# view_value()
# edit_value()
# total_value()

