from database import get_total_users
import streamlit as st

def calculate_total_users():
    total_users = get_total_users()
    st.write(f"Total registered users: {total_users}")
    
