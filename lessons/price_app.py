import streamlit as st

st.title("Product prices")
name = st.text_input("Product name", "Pen")
prices = {"Pen": 1.5, "Notebook": 3.0, "Pencil": 0.8}
if name in prices:
    st.write(name, "costs", prices[name])
else:
    st.write("I do not have it.")
