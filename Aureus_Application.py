import streamlit as st
from database_connect import create_table
from datetime import datetime


now = datetime.now()
create_table()

st.set_page_config(page_title="Aureus", layout="centered")

st.title("💵Welcome to :rainbow[AUREUS]💵")
st.subheader("Track. Control. Grow your wealth")
st.write(now.strftime(":rainbow[Date:] %d-%m-%Y :rainbow[Time:] %H:%M:%S"))

st.write("""Track every expense with ease and clarity.
Stay informed about your spending in real time.""")

st.write("---")
st.subheader("Quick Navigation-")
st.write("---")

col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button("➕Add Expense"):
        st.switch_page("pages/2_Add.py")
with col2:
    if st.button("🔍View Expense"):
        st.switch_page("pages/3_View.py")
with col3:        
    if st.button("📊View Dashboard"):
        st.switch_page("pages/1_Dashboard.py")
with col4:
    if st.button("🧮Open Calculator"):
        st.switch_page("pages/4_QuickCalc.py")
st.write("---")
st.sidebar.markdown("### Version 1.1")
st.sidebar.caption("Added QuickCalc")

st.write("---")
st.markdown("What's New in v1.1")
st.error("""
        - Added QuickCalc-Personal_buildin_Calculator.
        - Supports basic arethemetic operations.
        - Improve user interface.
     """)
