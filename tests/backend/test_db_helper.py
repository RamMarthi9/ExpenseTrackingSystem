from backend import db_helper
from datetime import date

def test_fetch_expenses_for_date():
    expenses = db_helper.fetch_expenses_for_date("2024-08-15")
    assert len(expenses) == 1
    assert float(expenses[0]['amount']) == 10.0
    assert expenses[0]['expense_date'] == date(2024, 8, 15)
    assert expenses[0]['category'] == "Shopping"
    assert expenses[0]['notes'] == "Bought potatoes"

def test_fetch_expenses_for_invalid_date():
    expenses = db_helper.fetch_expenses_for_date("9999-04-11")
    assert len(expenses) == 0

def test_fetch_expense_for_invalid_date_range():
    summary = db_helper.fetch_expense_summary("2029-01-01","2029-12-31")
    assert len(summary) == 0
