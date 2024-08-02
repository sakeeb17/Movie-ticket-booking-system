import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", password="", database="final_movie")
c = mydb.cursor()


def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS USERS(User_ID TEXT, First_name TEXT, Last_Name TEXT, Email_ID TEXT, Age TEXT, Phone_Number TEXT)')


def add_data(User_ID, First_Name, Last_Name, Email_ID, Age, Phone_Number):
    c.execute('INSERT INTO USERS(User_ID, First_Name, Last_Name, Email_ID, Age, Phone_Number) '
              'VALUES (%s,%s,%s,%s,%s,%s)',
              (User_ID, First_Name, Last_Name, Email_ID, Age, Phone_Number))
    mydb.commit()

def get_movies():
    c.execute('SELECT Movie_ID, Name FROM Movie')
    data = c.fetchall()
    return data

def get_showtimes():
    c.execute('SELECT Show_ID, Show_Time, Show_Date FROM Shows',)
    data = c.fetchall()
    return data

def get_theatre_details():
    c.execute('SELECT * FROM Theatre')
    data = c.fetchall()
    return data

def book_movie(Booking_ID, User_ID, Show_ID, No_of_Tickets, Total_Cost):
    c.execute('INSERT INTO BOOKINGS(Booking_ID, User_ID, Show_ID, No_of_Tickets, Total_Cost) '
              'VALUES (%s, %s, %s, %s, %s)',
              (Booking_ID, User_ID, Show_ID, No_of_Tickets, Total_Cost))
    mydb.commit()
# Function to retrieve screen details
def get_screen_details():
    c.execute('SELECT * FROM Screen')
    data = c.fetchall()
    return data

def view_all_data():
    c.execute('SELECT * FROM USERS')
    data = c.fetchall()
    return data

def get_bookings():
    
    c.execute('SELECT * FROM Booking')

    data = c.fetchall()
    return data




def view_only_users_names():
    c.execute('SELECT User_ID FROM USERS')
    data = c.fetchall()
    return data


def get_users(User_ID):
    c.execute('SELECT * FROM USERS WHERE User_ID="{}"'.format(User_ID))
    data = c.fetchall()
    return data


def edit_user_data(new_User_ID, new_First_Name, new_Last_Name, new_Email_ID, new_Age, new_Phone_Number,
                    User_ID, First_Name, Last_Name, Email_ID, Age, Phone_Number):
    c.execute("UPDATE USERS SET User_ID=%s, First_Name=%s, Last_Name=%s, Email_ID=%s, Age=%s, Phone_Number=%s "
              "WHERE User_ID=%s and First_Name=%s and Last_Name=%s and Email_ID=%s and Age=%s and Phone_Number=%s",
               (new_User_ID, new_First_Name, new_Last_Name, new_Email_ID, new_Age, new_Phone_Number,
               User_ID, First_Name, Last_Name, Email_ID, Age, Phone_Number))
    mydb.commit()
    #data = c.fetchall()
    #return data



def delete_data(User_ID):
    c.execute('DELETE FROM USERS WHERE User_ID="{}"'.format(User_ID))


def get_sql(statement):
    c.execute(statement)
    data = c.fetchall()
    return data

def get_movie_details():
    c.execute('SELECT * FROM Movie')
    data = c.fetchall()
    return data

def get_total_users():
    c.execute("SELECT CalculateTotalUsers()")
    data = c.fetchone()
    if data:
        return data[0]
    else:
        return 0

def get_total_movies():
    total_movies = 0  # Initialize to 0
    result = c.callproc('CalculateTotalMoviesNow', [total_movies])
    total_movies = result[0]
    return total_movies


def get_ticket_details(ticket_id):
    c.execute('SELECT * FROM Ticket WHERE Ticket_ID = %s', (ticket_id,))
    data = c.fetchone()
    return data

def get_users_with_bookings():
    c.execute('SELECT DISTINCT b.Booking_ID, b.Name_on_card, t.Ticket_ID FROM Booking b JOIN Ticket t ON b.Booking_ID = t.Booking_ID')
    data = c.fetchall()
    return data

def get_total_bookings():
    c.execute("SELECT CalculateTotalBooking()")
    data = c.fetchone()
    if data:
        return data[0]
    else:
        return 0
    

import uuid  # For generating unique IDs

def book_movie(No_of_Tickets, Total_Cost, Card_Number, Name_on_card, User_ID, Show_ID):
   # Generate a unique Booking_ID using UUID
   Booking_ID = str(uuid.uuid4())  # Generates a random UUID (unique identifier)
   
   # Insert the booking details into the Booking table
   c.execute('INSERT INTO Booking(Booking_ID, No_of_Tickets, Total_Cost, Card_Number, Name_on_card, User_ID, Show_ID) '
             'VALUES (%s, %s, %s, %s, %s, %s, %s)',
             (Booking_ID, No_of_Tickets, Total_Cost, Card_Number, Name_on_card, User_ID, Show_ID))
   mydb.commit()




def add_booking(booking_id, no_of_tickets, total_cost, card_number, name_on_card, user_id, show_id):

    cost_per_ticket = 400
    total_cost = no_of_tickets * cost_per_ticket
    c.execute('INSERT INTO Booking (Booking_ID, No_of_Tickets, Total_Cost, Card_Number, Name_on_card, User_ID, Show_ID) '
              'VALUES (%s, %s, %s, %s, %s, %s, %s)',
              (booking_id, no_of_tickets, total_cost, card_number, name_on_card, user_id, show_id))
    mydb.commit()

def get_user_details():
    c.execute('SELECT User_ID FROM USERS')
    data = c.fetchall()
    user_ids = [item[0] for item in data]
    return user_ids

def get_show_details():
    c.execute('SELECT Show_ID FROM Shows')
    data = c.fetchall()
    show_ids = [item[0] for item in data]
    return show_ids


def get_show_details_movie():
    c.execute('SELECT s.Show_ID,  m.Name AS Movie_Name,s.Show_Date,s.Show_Time,  s.screen_ID FROM Shows s JOIN Movie m ON s.Movie_ID = m.Movie_ID')
    data = c.fetchall()
    return data


