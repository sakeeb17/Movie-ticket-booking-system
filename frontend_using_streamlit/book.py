import streamlit as st
from database import get_bookings

def view_bookings():
    st.title("View Bookings")
    
    # Fetch the bookings data from the database
    bookings_data = get_bookings()
    
    if not bookings_data:
        st.warning("No bookings found in the database.")
    else:
        st.write("All Bookings")
        st.dataframe(bookings_data)


