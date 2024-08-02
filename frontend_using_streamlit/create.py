import streamlit as st
from database import add_data
def create():
    col1, col2 = st.columns(2)
    with col1:
        User_ID = st.text_input("User_ID:")
        First_Name = st.text_input("First_Name:")
        Last_Name = st.text_input("Last_Name:")

    with col2:
        Email_ID = st.text_input("Email_ID:")
        Age = st.text_input("Age:")
        Phone_Number = st.text_input("Phone_Number:")


    if st.button("Add User Record"):
        add_data(User_ID, First_Name, Last_Name, Email_ID, Age, Phone_Number)
    st.success("Successfully added User record: {}".format(First_Name))
