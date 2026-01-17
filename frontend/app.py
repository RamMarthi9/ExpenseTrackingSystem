import streamlit as st
from datetime import datetime
import requests
from analytics_ui2 import analytics_tab
from add_update_ui import add_update_tab
from analytics_ui_mon import monthly_analytics_tab

API_URL = "http://localhost:8000"

st.title("Expense Management System")
tab1, tab2, tab3 = st.tabs(["Add/Update","Analytics by Category", "Monthly Analytics"])

with tab1:
    add_update_tab()
with tab2:
    analytics_tab()
with tab3:
    monthly_analytics_tab()