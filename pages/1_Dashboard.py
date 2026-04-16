import streamlit as st
from database_connect import connect_db, view_value
from Aureus_Application import show_sidebar
import pandas as pd
from datetime import datetime
now = datetime.now()


st.title("🖥️ Dashboard")
show_sidebar()
st.write("Overview of your expenses will go here.")


data = view_value()

df = pd.DataFrame(
    data,
    columns=["ID", "Category", "Amount", "Date", "Note", "del"]
)
df_chart = df.groupby("Category", as_index=False)["Amount"].sum()
df_chart = df_chart.set_index("Category")

st.bar_chart(df_chart)
