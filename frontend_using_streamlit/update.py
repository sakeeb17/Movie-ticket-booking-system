import pandas as pd
import streamlit as st
from database import view_all_data, view_only_users_names, get_users, edit_user_data


def update():
    result = view_all_data()
    df = pd.DataFrame(result, columns=['User_ID', 'First_Name', 'Last_Name', 'Email_ID', 'Age', 'Phone_Number'])
    with st.expander("Current Users:"):
        st.dataframe(df)
    list_of_dealers = [i[0] for i in view_only_users_names()]
    selected_users = st.selectbox("Train to Edit", list_of_dealers)
    selected_result = get_users(selected_users)
    if selected_result:
        User_ID = selected_result[0][0]
        First_Name = selected_result[0][1]
        Last_Name = selected_result[0][2]
        Email_ID = selected_result[0][3]
        Age = selected_result[0][4]
        Phone_Number = selected_result[0][5]
        col1, col2 = st.columns(2)
        with col1:
            new_User_ID = st.text_input("User_ID:", User_ID )
            new_First_Name = st.text_input("First_Name:", First_Name)
            new_Last_Name = st.text_input("Last_Name:", Last_Name)
        with col2:
            new_Email_ID = st.text_input("Email_ID:", Email_ID )
            new_Age = st.text_input("Age:", Age )
            new_Phone_Number = st.text_input("Phone_Number:", Phone_Number )
        if st.button("Update User"):
            edit_user_data(new_User_ID, new_First_Name, new_Last_Name,new_Email_ID, new_Age, new_Phone_Number,
                            User_ID, First_Name, Last_Name, Email_ID, Age, Phone_Number)
        st.success("Successfully updated:: {}".format(new_User_ID))
        result2 = view_all_data()
        df2 = pd.DataFrame(result2, columns=['User_ID', 'First_Name', 'Last_Name', 'Email_ID', 'Age', 'Phone_Number'])
        with st.expander("Updated Users"):
            st.dataframe(df2)
