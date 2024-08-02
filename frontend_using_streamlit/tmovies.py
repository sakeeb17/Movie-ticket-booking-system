import streamlit as st
from database import get_total_movies

def display_total_movies():
    total_movies = get_total_movies()
    st.title("Total Movies")
    st.write(f"Total movies available: {total_movies}")

