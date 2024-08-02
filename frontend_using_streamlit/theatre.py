import pandas as pd
import streamlit as st
from database import get_theatre_details, get_screen_details


def read_theatres_and_screens():
    # Retrieve theatre details
    theatre_result = get_theatre_details()
    if theatre_result:
        # Create a DataFrame to display the theatre details
        theatre_df = pd.DataFrame(theatre_result, columns=['Theatre_ID', 'Name_of_Theatre', 'No_of_Screens', 'Area'])

        # Use st.dataframe to display the theatre details
        with st.expander("Theatre Details"):
            st.dataframe(theatre_df)
    else:
        st.warning("No theatre details found.")

    # Retrieve screen details
    screen_result = get_screen_details()
    if screen_result:
        # Create a DataFrame to display the screen details
        screen_df = pd.DataFrame(screen_result, columns=['Screen_ID', 'No_of_Seats_Gold', 'No_of_Seats_Silver', 'Theatre_ID'])

        # Use st.dataframe to display the screen details
        with st.expander("Screen Details"):
            st.dataframe(screen_df)
    else:
        st.warning("No screen details found.")
