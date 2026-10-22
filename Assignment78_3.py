
import streamlit as st

st.title("Simple Interest Calculator")

p = st.number_input("Enter Principal Amount", min_value=0.0)
r = st.number_input("Enter Rate of Interest (%)", min_value=0.0)
t = st.number_input("Enter Time Period (Years)", min_value=0.0)

if st.button("Calculate"):
    si = (p * r * t) / 100

    st.success(f"Simple Interest = {si:.2f}")

