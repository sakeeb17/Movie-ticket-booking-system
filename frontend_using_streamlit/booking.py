import streamlit as st
import uuid  # For generating a unique Booking ID
from database import add_booking, get_user_details, get_show_details

def book_ticket():
    st.title("Book Ticket")
    
    # Create a form to collect user input
    with st.form("ticket_booking_form"):
        st.write("Please provide the following details:")
        booking_id = str(uuid.uuid4())[:8]  # Generate a unique Booking ID
        no_of_tickets = st.number_input("Number of Tickets", min_value=1, value=1)
        total_cost = st.number_input("Total Cost", min_value=0, step=1)
        card_number = st.text_input("Card Number", max_chars=19)
        name_on_card = st.text_input("Name on Card", max_chars=21)

        # Select User ID from a dropdown
        user_id = st.selectbox("Select User ID", get_user_details())

        # Select Show ID from a dropdown
        show_id = st.selectbox("Select Show ID", get_show_details())

        if st.form_submit_button("Book Ticket"):
            add_booking(booking_id, no_of_tickets, total_cost, card_number, name_on_card, user_id, show_id)
            st.success("Ticket booked successfully!")

