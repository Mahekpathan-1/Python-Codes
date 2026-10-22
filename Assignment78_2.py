
import streamlit as st

st.title("Even or Odd Number")

num = st.number_input(
    "Enter an integer",
    value=0,
    step=1
)

if st.button("Check"):
    if num % 2 == 0:
        st.success(f"{num} is an Even Number")
    else:
        st.success(f"{num} is an Odd Number")
