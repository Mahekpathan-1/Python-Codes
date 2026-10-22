
import streamlit as st

st.title("Student Result Calculator")

name = st.text_input("Enter Student Name")

st.subheader("Enter Marks (Out of 100)")

m1 = st.number_input("Subject 1 Marks", min_value=0, max_value=100)
m2 = st.number_input("Subject 2 Marks", min_value=0, max_value=100)
m3 = st.number_input("Subject 3 Marks", min_value=0, max_value=100)

if st.button("Calculate Result"):
    if name.strip() == "":
        st.error("Please enter the student's name.")
    else:
        total = m1 + m2 + m3
        percentage = (total / 300) * 100

        st.write("Student Name:", name)
        st.write("Total Marks:", total, "/ 300")
        st.write(f"Percentage: {percentage:.2f}%")

        if m1 >= 40 and m2 >= 40 and m3 >= 40:
            st.success("Result: PASS")
        else:
            st.error("Result: FAIL")
