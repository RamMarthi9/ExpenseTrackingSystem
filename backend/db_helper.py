# DB Helper to perform CRUD Operations in expense tracking system
# CRUD
# Create # Retrieve # Update # Delete

import mysql.connector
from contextlib import contextmanager
from logging_setup import setup_logger

logger = setup_logger("db_helper")

@contextmanager
def get_db_cursor(commit=False):
    connection = mysql.connector.connect(
                            host="localhost",
                            user="root",
                            password="root",
                            database="expense_manager")

    if connection.is_connected():
        print("Connection Successful!!")
    else:
        print("Connection Failed!!")

    cursor = connection.cursor(dictionary=True)
    yield cursor

    if commit:
        connection.commit()

    cursor.close()
    connection.close()


def fetch_all_records():
    with get_db_cursor() as cursor:
        logger.info(f"Fetch all records from expenses")
        cursor.execute("select * from expenses;")
        expenses = cursor.fetchall()
        for expense in expenses:
            print(expense)


def fetch_expenses_for_date(expense_date):
    logger.info(f"Fetch all expenses for date {expense_date}")
    with get_db_cursor() as cursor:  #
        cursor.execute(
            "select * from expenses where expense_date = %s",
            (expense_date,)
        )
        expenses = cursor.fetchall()
        return expenses

def insert_expense(expense_date, amount, category, notes):
    logger.info(f"Insert expenses called with {expense_date}{amount} {category} {notes}")
    with get_db_cursor(commit=True) as cursor:
        cursor.execute(
            "INSERT INTO expenses(expense_date,amount,category, notes) VALUES(%s,%s,%s,%s)",
            (expense_date, amount, category, notes)
        )

def delete_expenses_for_date(expense_date):
    logger.info(f"Delete expenses for date {expense_date}")
    with get_db_cursor(commit=True) as cursor:
        cursor.execute("DELETE FROM expenses WHERE expense_date = %s", (expense_date,))
        return cursor.rowcount

def fetch_expense_summary(start_date, end_date):
    '''Select category, Sum(amount) from expense_manager.expenses
    where expense_date between "2024-08-01" and "2024-08-05"
    Group by category;'''
    logger.info(f"Fetch expense summary for {start_date} to {end_date}")
    with get_db_cursor() as cursor:
        cursor.execute(
            "SELECT category, Sum(amount) as total FROM expenses WHERE expense_date between %s and %s GROUP BY category",
            (start_date, end_date)
        )
        data = cursor.fetchall()
        return data

if __name__ == "__main__":
    # fetch_expenses_for_date("2024-08-01")
    # insert_expense("2024-08-25", "40", "Food", "Bonda")
    delete_expenses_for_date("2024-08-10")
    # print(fetch_expenses_for_date("2024-08-15"))
    # fetch_expense_summary("2024-01-01","2024-12-31")
    # for expense in summary:
    # print(expense)