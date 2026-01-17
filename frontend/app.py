import streamlit as st
from datetime import datetime
import requests
from analytics_ui2 import analytics_tab
from add_update_ui import add_update_tab

API_URL = "http://localhost:8000"

st.title("Expense Management System")
tab1, tab2 = st.tabs(["Add/Update", "Analytics"])

with tab1:
    add_update_tab()
with tab2:
    analytics_tab()