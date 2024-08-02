import pandas as pd
import streamlit as st
from database import view_all_data

def read():
    result = view_all_data()
    df = pd.DataFrame(result, columns=['User_ID', 'First_Name', 'Last_Name', 'Email_ID', 'Age', 'Phone_Number'])
    with st.expander("View all Users"):
        st.dataframe(df)