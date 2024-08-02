import pandas as pd
import streamlit as st
from database import get_show_details_movie

def read_shows():
    result = get_show_details_movie()
    if not result:
        st.warning("Nothing found.")
    else:
        st.write("Shows with shows:")
        for user in result:
            st.write(f"Show ID: {user[0]},  Movie Name: {user[1]},Show Date: {user[2]},Show Time: {user[3]},Screen ID: {user[4]}")