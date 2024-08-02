import pandas as pd
import streamlit as st
from database import get_movie_details


def read_movies():
    result = get_movie_details()
    if result:
        # Create a DataFrame to display the movie details
        df = pd.DataFrame(result, columns=['Movie_ID', 'Name', 'Language', 'Genre', 'Target_Audience'])

        # Use st.dataframe to display the movie details
        with st.expander("Movie Details"):
            st.dataframe(df)
    else:
        st.warning("No movie details found.")
