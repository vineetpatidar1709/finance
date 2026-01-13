from datetime import datetime

def validate_amount(amount):
    try:
        value = float(amount)
        if value <= 0:
            raise ValueError("Amount must be positive")
        return value
    except ValueError:
        raise ValueError("Invalid amount. Enter a number greater than 0.")

def validate_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return date_str
    except ValueError:
        raise ValueError("Date must be in YYYY-MM-DD format")

def validate_category(category):
    if not category.strip():
        raise ValueError("Category cannot be empty")
    return category.strip()

def validate_description(description):
    if not description.strip():
        raise ValueError("Description cannot be empty")
    return description.strip()
