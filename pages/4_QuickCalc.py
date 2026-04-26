import streamlit as st


if "expression" not in st.session_state:
    st.session_state.expression = ""
if "history" not in st.session_state:
    st.session_state.history = []

st.header("QuickCalc🧮")

st.write("---")

st.text_input("Display", st.session_state.expression, disabled=True)


def press(val):
    st.session_state.expression += str(val)


def clear():
    st.session_state.expression = ""


def calculate():
    try:
        result = str(eval(st.session_state.expression))
        st.session_state.history.append(f"{st.session_state.expression} = {result}"
                                        )
        st.session_state.expression = result
    except:
        st.session_state.expression = "Error"


rows = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", "C", "=", "+"]
]

for row in rows:
    cols = st.columns(4)

    for i, val in enumerate(row):
        with cols[i]:
            if val == "C":
                st.button(val, on_click=clear)
            elif val == "=":
                st.button(val, on_click=calculate)
            else:
                st.button(val, on_click=press, args=(val, ))

st.subheader("History")
if st.button("Clear History"):
    st.session_state.history = ""
for item in st.session_state.history[::-1]:
    st.write(item)
