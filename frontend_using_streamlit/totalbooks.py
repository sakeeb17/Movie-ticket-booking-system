from database import get_total_bookings
import streamlit as st

def calculate_total_bookings():
    total_booked = get_total_bookings()
    st.write(f"Total registered users: {total_booked}")
    