import streamlit as st
from datetime import datetime
import requests

API_URL = "http://localhost:8000"

def add_update_tab():
    # Date selection
    date_obj = st.date_input(
        "Enter Date:",
        datetime(2024, 8, 1),
        label_visibility="collapsed"
    )
    selected_date = date_obj.strftime("%Y-%m-%d")

    # Fetch data
    response = requests.get(f"{API_URL}/expenses/{selected_date}")
    existing_expenses = response.json() if response.status_code == 200 else []

    categories = ["Rent", "Food", "Shopping", "Entertainment", "Other"]

    # 🔹 RESET FORM STATE WHEN DATE CHANGES
    if "last_selected_date" not in st.session_state:
        st.session_state.last_selected_date = selected_date

    if st.session_state.last_selected_date != selected_date:
        for i in range(5):
            st.session_state.pop(f"Amount_{i}", None)
            st.session_state.pop(f"Category_{i}", None)
            st.session_state.pop(f"Notes_{i}", None)
        st.session_state.last_selected_date = selected_date

    # HEADERS
    h1, h2, h3 = st.columns(3)
    h1.markdown("**Amount (₹)**")
    h2.markdown("**Category**")
    h3.markdown("**Notes**")

    # ✅ FORM KEY DEPENDS ON DATE
    with st.form(key=f"expense_form_{selected_date}"):
        expenses = []
        for i in range(5):
            if i < len(existing_expenses):
                amount = existing_expenses[i]["amount"]
                category = existing_expenses[i]["category"]
                notes = existing_expenses[i]["notes"]
            else:
                amount = 0.0
                category = "Shopping"
                notes = ""

            c1, c2, c3 = st.columns(3)

            with c1:
                amount_input = st.number_input(
                    label="Amount",
                    min_value=0.0,
                    step=1.0,
                    value=float(amount),
                    key=f"Amount_{i}_{selected_date}",
                    label_visibility="collapsed"
                )

            with c2:
                category_input = st.selectbox(
                    label="Category",
                    options=categories,
                    index=categories.index(category),
                    key=f"Category_{i}_{selected_date}",
                    label_visibility="collapsed"
                )

            with c3:
                notes_input = st.text_input(
                    label="Notes",
                    value=notes,
                    key=f"Notes_{i}_{selected_date}",
                    label_visibility="collapsed"
                )

            expenses.append(
                {
                    "amount": amount_input,
                    "category": category_input,
                    "notes": notes_input
                }
            )

        submit_button = st.form_submit_button()
        filtered_expenses = [expense for expense in expenses if expense["amount"] > 0.0]

        requests.post(f"{API_URL}/expenses/{selected_date}", json=filtered_expenses)