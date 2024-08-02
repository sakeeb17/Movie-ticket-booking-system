import streamlit as st
from database import get_ticket_details

def display_ticket_details():
    st.title("Ticket Details")
    ticket_id = st.text_input("Enter Ticket ID:")
    
    if st.button("View Ticket Details"):
        if not ticket_id:
            st.warning("Please enter a Ticket ID.")
        else:
            ticket_data = get_ticket_details(ticket_id)
            if ticket_data:
                st.write("Ticket Details:")
                st.write(f"Ticket ID: {ticket_data[0]}")
                st.write(f"User ID: {ticket_data[1]}")
                st.write(f"Show Class: {ticket_data[2]}")
                
            else:
                st.warning("Ticket not found.")