import streamlit as st
from database_connect import connect_db, view_value
import pandas as pd
from datetime import datetime
now = datetime.now()


st.title("🖥️ Dashboard")
st.write("Overview of your expenses will go here.")


data = view_value()

df = pd.DataFrame(
    data,
    columns=["ID", "Category", "Amount", "Date", "Note",]
)
df_chart = df.groupby("Category", as_index=False)["Amount"].sum()
df_chart = df_chart.set_index("Category")

st.bar_chart(df_chart)
st.write("---")

if st.button("Add Expenses"):
    st.switch_page("pages/2_Add.py")
if st.button("View Expenses"):
    st.switch_page("pages/3_View.py")

