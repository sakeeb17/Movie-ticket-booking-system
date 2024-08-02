import streamlit as st
from database import get_users_with_bookings

def display_users_with_bookings():
    st.title("Users with Bookings")
    
    # Get the list of users with bookings from the database
    users_with_bookings = get_users_with_bookings()
    
    if not users_with_bookings:
        st.warning("No users with bookings found.")
    else:
        st.write("Users with Bookings:")
        for user in users_with_bookings:
            st.write(f"Booking ID: {user[0]},  Name: {user[1]}, Ticket Id: {user[2]}")
