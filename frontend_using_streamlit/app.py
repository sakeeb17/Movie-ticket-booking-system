import streamlit as st
from create import create
from database import create_table
from delete import delete
from read import read
from update import update
from sql_stat import stat
from database import get_movie_details
from movies import read_movies
from theatre import read_theatres_and_screens
from book import view_bookings
from function import calculate_total_users
from tmovies import display_total_movies
from ticket import display_ticket_details
from bookedticket import display_users_with_bookings
from totalbooks import calculate_total_bookings
from booking import book_ticket
from show import read_shows



def main():
    st.title("Movie_Booking_System")
    menu = ["Add User", "View Users", "Edit Users","View Movies","View Theatres and Screens","ShowIDs for Movies","Book Movie Tickets","View Bookings","Total Users","Total Movies","Total Bookings","Remove"]
    choice = st.sidebar.selectbox("Menu", menu)
    create_table()
    if choice == "Add User":
        st.subheader("Enter User Details:")
        create()
    elif choice == "View Users":
        st.subheader("View created Users")
        read()
    elif choice == "Edit Users":
        st.subheader("Update created Users")
        update()
    elif choice == "View Movies":
        st.subheader("View Movie Details")
        read_movies()
    elif choice == "View Theatres and Screens":
        st.subheader("View Theatre and Screen Details")
        read_theatres_and_screens()

    elif choice == "ShowIDs for Movies":
        st.subheader("View Show Details")
        read_shows()


    elif choice == "Book Movie Tickets":
        st.subheader("Book a Movie Ticket Here")
        book_ticket()
    
    
    elif choice=="View Bookings":
        st.subheader("show booked details")
        view_bookings()

    elif choice == "Total Users":
        st.subheader("Show the total Users")
        calculate_total_users()
        
    elif choice == "Total Movies":
        display_total_movies()
    
    
    

    elif choice == "Total Bookings":
        st.header("The total number of bookings")
        calculate_total_bookings()

    elif choice == "Remove":
        st.subheader("Delete created Users")
        delete()

        
  
    else:
        st.subheader("About Users")


if __name__ == main():
    main()
