import csv
import shutil
import os
from expense import Expense

# ----------------------------
# File & Folder Setup
# ----------------------------
DATA_FOLDER = "data"
FILE_PATH = os.path.join(DATA_FOLDER, "expenses.csv")
BACKUP_PATH = os.path.join(DATA_FOLDER, "backup_expenses.csv")

# Create folder if it doesn't exist
if not os.path.exists(DATA_FOLDER):
    os.makedirs(DATA_FOLDER)

# Create CSV file if it doesn't exist
if not os.path.exists(FILE_PATH):
    with open(FILE_PATH, "w", newline="") as f:
        pass

# ----------------------------
# Expense File Operations
# ----------------------------
def save_expense(expense):
    with open(FILE_PATH, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(expense.to_list())

def load_expenses():
    expenses = []
    try:
        with open(FILE_PATH, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                expense = Expense(row[0], row[1], row[2], row[3])
                expenses.append(expense)
    except Exception as e:
        print(" Error loading expenses:", e)
    return expenses

# ----------------------------
# Backup & Restore Functions
# ----------------------------
def backup_data():
    try:
        shutil.copy(FILE_PATH, BACKUP_PATH)
        print(" Backup created successfully!")
    except Exception as e:
        print(" Backup failed:", e)

def restore_data():
    try:
        shutil.copy(BACKUP_PATH, FILE_PATH)
        print(" Data restored successfully!")
    except FileNotFoundError:
        print(" Backup file not found!")
    except Exception as e:
        print(" Restore failed:", e)
