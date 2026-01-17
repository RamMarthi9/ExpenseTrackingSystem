import streamlit as st
import requests
import pandas as pd

API_URL = "http://localhost:8000"

def monthly_analytics_tab():
    st.subheader("Monthly Expense Analytics")

    response = requests.get(f"{API_URL}/analytics/monthly")

    if response.status_code != 200:
        st.error("Failed to fetch monthly analytics")
        return

    data = response.json()

    if not data:
        st.warning("No monthly data available")
        return

    df = pd.DataFrame(
        list(data.items()),
        columns=["Month", "Total Expense"]
    )

    df["Month"] = pd.to_datetime(df["Month"])
    df = df.sort_values("Month")

    st.bar_chart(
        df.set_index("Month"),
        use_container_width=True
    )

    df["Month"] = df["Month"].dt.strftime("%Y-%m")
    df["Total Expense"] = df["Total Expense"].map("₹{:,.2f}".format)

    st.dataframe(df, use_container_width=True, hide_index=True)
