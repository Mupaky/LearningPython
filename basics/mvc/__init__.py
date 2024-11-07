def add_expense(expenses):
    amount = float(input("Enter expense amount: "))
    expenses.append(amount)


def total_expenses(expenses):
    return sum(expenses)


def main():
    expenses = []
    while True:
        add_expense(expenses)
        if input("Add another expense? (y/n): " != 'y'):
            break
    print(f"Total expenses: ${total_expenses(expenses):.2f}")


main()
