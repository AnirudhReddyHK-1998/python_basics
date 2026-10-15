import streamlit as st

st.title("My First Application")

name = st.text_input("Enter your name")

if st.button("Submit"):
    st.success(f"Welcome, {name}!")
