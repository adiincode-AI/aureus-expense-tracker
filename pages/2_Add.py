import streamlit as st
from database_connect import connect_db, insert_value
from datetime import datetime
from Aureus_Application import show_sidebar


st.title("➕ Add Expense")
show_sidebar()
category = st.selectbox(
    "Category",
    [
        "🍔 Food",
        "🚗 Travel",
        "🛒 Shopping",
        "💡 Bills",
        "💊 Health",
        "📚 Education",
        "📦 Other"
    ]
)
amount = st.number_input(
    "Amount (₹)", min_value=0, step=1, value=0)
date = st.date_input("Date")
note = st.text_input("Note (optional)")

if st.button("Save"):
    if amount <= 0:
        st.error("Amount must be greater than 0")
    else:
        insert_value(category, amount, date, note)
        st.success("Expense Saved!")
