import streamlit as st
from database_connect import connect_db, view_value, delete_value
import pandas as pd
from Aureus_Application import show_sidebar

st.title("📊 View Expenses")
st.write("Here is your Expense List.")
data = view_value()
if data:
    df = pd.DataFrame(
        data,
        columns=["ID", "Category", "Amount", "Date", "Note"]
    )

    for index, row in df.iterrows():
        col1, col2, col3, col4, col5, col6 = st.columns(6)

        col1.write(row["ID"])
        col2.write(row["Category"])
        col3.write(row[f"Amount"])
        col4.write(row["Date"])
        col5.write(row["Note"])
        if col6.button("⌫", key=row["ID"]):
            delete_value(row["ID"])
            st.rerun()
else:
    st.info("No Data Found")


st.write("---")

if st.button("View Dashboard"):
    st.switch_page("pages/1_Dashboard.py")
