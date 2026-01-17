import streamlit as st
from datetime import datetime
import requests
import pandas as pd
import plotly.express as px

API_URL = "http://localhost:8000"

def analytics_tab():
    st.subheader("Expense Analytics")

    # ── Date filters ───────────────────────────────
    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input("Start Date", datetime(2024, 8, 1))
    with col2:
        end_date = st.date_input("End Date", datetime(2024, 8, 5))

    # ── Fetch analytics ────────────────────────────
    if st.button("Get Analytics", type="primary"):
        payload = {
            "start_date": start_date.strftime("%Y-%m-%d"),
            "end_date": end_date.strftime("%Y-%m-%d")
        }

        response = requests.post(f"{API_URL}/analytics/", json=payload)

        if response.status_code != 200:
            st.error("Failed to fetch analytics data")
            return

        response = response.json()

        if not response:
            st.warning("No data available for the selected date range")
            return

        # ── Transform data ──────────────────────────
        data = {
            "Category": list(response.keys()),
            "Total": [response[c]["total"] for c in response],
            "Percentage": [response[c]["percentage"] for c in response]
        }

        df = pd.DataFrame(data)
        df_sorted = df.sort_values("Percentage", ascending=False)

        # ── Layout: Pie chart + Table ───────────────
        col_chart, col_table = st.columns([2, 1])

        # 🎨 PIE CHART
        with col_chart:
            fig = px.pie(
                df_sorted,
                names="Category",
                values="Percentage",
                title="Expense Distribution (%)",
                color_discrete_sequence=px.colors.qualitative.Set3,
                hole=0.35
            )

            fig.update_traces(
                textinfo="label+percent",
                pull=[0.05] * len(df_sorted)
            )

            fig.update_layout(
                legend_title="Category",
                title_x=0.5
            )

            st.plotly_chart(fig, use_container_width=True)

        # 📋 TABLE
        with col_table:
            st.markdown("### Category Summary")

            df_display = df_sorted.copy()
            df_display["Total"] = df_display["Total"].map("₹{:,.2f}".format)
            df_display["Percentage"] = df_display["Percentage"].map("{:.2f}%".format)

            st.dataframe(
                df_display,
                use_container_width=True,
                hide_index=True
            )
