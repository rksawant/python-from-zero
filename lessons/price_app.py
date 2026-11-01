import streamlit as st

st.title("Product prices")
name = st.text_input("Product name", "Pen")
prices = {"Pen": 1.5, "Notebook": 3.0, "Pencil": 0.8}
if name in prices:
    st.write(name, "costs", prices[name])
else:
    st.write("I do not have it.")


inp = st.text_input("Enter number to check odd/even")

if inp:
    try:
        num_inp = int(inp)
        st.write(inp, "is even") if num_inp % 2 == 0 else st.write(inp, "is odd")
    except ValueError:
        st.error("Enter a valid integer")