from collections import defaultdict

def total_expense(expenses):
    return sum(float(exp.amount) for exp in expenses)

def average_expense(expenses):
    if len(expenses) == 0:
        return 0
    return total_expense(expenses) / len(expenses)

def category_breakdown(expenses):
    categories = defaultdict(float)
    for exp in expenses:
        categories[exp.category] += float(exp.amount)
    return categories

def print_report(expenses):
    print("\n===== Expense Report =====")
    print(f"{'Category':<15}{'Amount':>10}")
    print("-" * 25)

    categories = category_breakdown(expenses)
    total = 0
    for cat, amt in categories.items():
        print(f"{cat:<15}${amt:>9.2f}")
        total += amt

    print("-" * 25)
    print(f"{'Total':<15}${total:>9.2f}")
    print(f"{'Average':<15}${average_expense(expenses):>9.2f}")

