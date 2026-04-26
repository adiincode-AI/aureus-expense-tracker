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

if st.button("➕ Add Expense"):
    st.switch_page("pages/2_Add.py")
if st.button("🔍 View Your Expense list"):
    st.switch_page("pages/3_View.py")
if st.button("📊 View Your Dashboard"):
    st.switch_page("pages/1_Dashboard.py")
if st.button("🧮 Open Calculator"):
    st.switch_page("pages/4_QuickCalc.py")
