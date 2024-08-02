create database final_movie;
use final_movie;

CREATE Table users(
User_ID varchar(5),
First_Name varchar(15), 
Last_Name varchar(20),
Email_ID varchar(30),
Age int,
Phone_Number varchar(10) NOT NULL, 
Primary Key(User_ID));





Create Table Theatre(
Theatre_ID varchar(5),
Name_of_Theatre varchar(30) NOT NULL,
No_of_Screens int,
Area varchar(30),
Primary Key(Theatre_ID));




CREATE TABLE Screen(
Screen_ID varchar(5),
No_of_Seats_Gold int NOT NULL,
No_of_Seats_Silver int NOT NULL,
Theatre_ID varchar(5),
Primary Key(Screen_ID),
Foreign Key(Theatre_ID) REFERENCES Theatre(Theatre_ID) ON DELETE CASCADE ON UPDATE CASCADE);





Create Table Movie(
Movie_ID varchar(5),
Name varchar(30) NOT NULL,
Language varchar(10),
Genre varchar(20),
Target_Audience varchar(5),
Primary Key(Movie_ID));






CREATE Table Shows(				
Show_ID varchar(10),
Show_Time time NOT NULL,
Show_Date date NOT NULL,				
Seats_Remaining_Gold int NOT NULL CHECK (Seats_Remaining_Gold >= 0),
Seats_Remaining_Silver int NOT NULL CHECK (Seats_Remaining_Silver >= 0),
Class_Cost_Gold int NOT NULL,
Class_Cost_Silver int NOT NULL,
Screen_ID varchar(5) NOT NULL,
Movie_ID varchar(5) NOT NULL,
Primary Key(Show_ID),
Foreign Key (Screen_ID) REFERENCES Screen(Screen_ID) ON DELETE CASCADE ON UPDATE CASCADE,
Foreign Key (Movie_ID) REFERENCES Movie(Movie_ID) ON DELETE CASCADE ON UPDATE CASCADE);







CREATE Table Booking(
Booking_ID varchar(10),
No_of_Tickets int NOT NULL,
Total_Cost int NOT NULL,                                           
Card_Number varchar(19),
Name_on_card varchar(21),
User_ID varchar(5),
Show_ID varchar(10),
Foreign Key (User_ID) REFERENCES users (User_ID) ON DELETE CASCADE ON UPDATE CASCADE,
Foreign Key (Show_ID) REFERENCES Shows(Show_ID) ON DELETE CASCADE ON UPDATE CASCADE,
Primary Key(Booking_ID));









CREATE Table Ticket(
Ticket_ID varchar(20),
Booking_ID varchar(10),
Class varchar(3) NOT NULL,
Price int NOT NULL,
Primary Key(Ticket_ID),
Foreign Key(Booking_ID) REFERENCES Booking(Booking_ID)ON DELETE CASCADE);

Insert into users values
('1000', 'Sakeeb', 'G', 'sakeeb123@gmail.com', 22, '9682568456'),
('1001', 'Shraddha', 'Advani', 'shraddha_advani6248@gmail.com', 26, '9632798647'),
('1002', 'Rahul', 'Kulkarni', 'rahul.kulkarni8648@gmail.com', 48, '9635472848'),
('1003', 'Preran', 'Goswami', 'prerangoswami1186@gmail.com', 16, '8635262747'),
('1004', 'Prithvi', 'Rao', 'prithviroa8864@gmail.com', 24, '6852796434'),
('1005', 'Shreya', 'Raj', 'shreyaraj6518@gmail.com', 22, '8624125186'),
('1006', 'Rahul', 'Aggarwal', 'prithviroa8864@gmail.com', 17, '8643521789'),
('1007', 'Hardhik', 'Sharma', 'shreyaraj6518@gmail.com', 35, '6842164678'),
('1008', 'Rohit', 'A', 'rohit48@gmail.com', 28, '8412536748'),
('1009', 'kishan', 'G', 'kishan68@gmail.com', 29, '9721465368');











Insert into Theatre values
('TH1', 'INOX Movies', 3, 'Jayanagar, Bengaluru South'),
('TH2', 'PVR Cinemas', 2, 'JP nagar , Bengaluru South'),
('TH3', 'Cinepolis', 2, 'Yeswanthpur, Bengaluru North'),
('TH4', 'Inox Lido', 20, 'Bannerghattha, Bengaluru South'), -- Adjusted 'Area' value
('TH5', 'Cinepolis1', 3, 'Yelahankha, Bengaluru North');













Insert into Screen values
('TH11', 40, 60, 'TH1'), 
('TH12', 40, 60, 'TH1'),
('TH13', 40, 60, 'TH1'), 
('TH21', 36, 64, 'TH2'), 
('TH22', 36, 64, 'TH2'), 
('TH31', 50, 50, 'TH3'), 
('TH32', 50, 50, 'TH3'),
('TH41', 40, 60, 'TH4'), 
('TH42', 40, 60, 'TH4'),
('TH51', 50, 50, 'TH5'), 
('TH52', 50, 50, 'TH5'),
('TH53', 50, 50, 'TH5');














Insert into Movie values
('001', 'movie1', 'English','Fantasy/Adventure', 'U/A'),
('002', 'movie2',  'English','Fantasy/SciFi', 'U/A'),
('003', 'movie3','Kannada', 'Fantasy/Action', 'U/A'),
('004', 'movie4', 'Telugu','Drama/Comedy', 'U/A'),
('005', 'movie5', 'Hindi','Romance','R'),
('006', 'movie6','English','Horror' ,'A');













Insert into Shows values
('SHTH110001', '09:00:00', '2022-08-18', 40, 60, 400, 350, 'TH11', '001'),
('SHTH110002', '16:00:00', '2022-08-18', 38, 60, 400, 350, 'TH11', '002'),
('SHTH120001', '09:00:00', '2022-08-18', 40, 60, 400, 350, 'TH12', '003'),
('SHTH130001', '09:00:00', '2022-08-18', 40, 60, 400, 350, 'TH13', '004'),
('SHTH210001', '09:00:00', '2022-08-18', 36, 64, 415, 375, 'TH21', '003'),
('SHTH220001', '16:00:00', '2022-08-18', 36, 64, 415, 375, 'TH22', '002'),
('SHTH310001', '09:00:00', '2022-08-18', 50, 50, 480, 380, 'TH31', '002'),
('SHTH310002', '16:00:00', '2022-08-20', 50, 50, 480, 380, 'TH31', '004'),
('SHTH320001', '09:00:00', '2022-08-18', 50, 46, 480, 380, 'TH32', '005'),
('SHTH320002', '16:00:00', '2022-08-20', 50, 50, 480, 380, 'TH32', '006'),
('SHTH410001', '09:00:00', '2022-08-20', 40, 60, 415, 375, 'TH41', '001'),
('SHTH420001', '09:00:00', '2022-08-20', 40, 60, 415, 375, 'TH42', '004'),
('SHTH510001', '09:00:00', '2022-08-20', 50, 50, 480, 380, 'TH51', '002'),
('SHTH520001', '09:00:00', '2022-08-20', 50, 50, 480, 380, 'TH52', '003'),
('SHTH530001', '09:00:00', '2022-08-20', 50, 50, 480, 380, 'TH53', '005');

















INSERT into Booking values('BOOK0001', 2, 800, '8249621092163126', 'Sakeeb G', 1000,'SHTH110002');
INSERT into Ticket values('TIDBOOK0001001', 'BOOK0001', 'GLD',  400);
INSERT into Ticket values('TIDBOOK0001002', 'BOOK0001', 'GLD',  400);

INSERT into Booking values('BOOK0002', 4, 1520, '9261738271340646', 'Shraddha Advani', 1001, 'SHTH320001');
INSERT into Ticket values('TIDBOOK0002001', 'BOOK0002', 'SLV',  380);
INSERT into Ticket values('TIDBOOK0002002', 'BOOK0002', 'SLV',  380);
INSERT into Ticket values('TIDBOOK0002003', 'BOOK0002', 'SLV',  380);
INSERT into Ticket values('TIDBOOK0002004', 'BOOK0002', 'SLV',  380);

INSERT into Booking values('BOOK0003', 4, 1660, '9864821890538268', 'Hardhik Sharma', 1007, 'SHTH410001');
INSERT into Ticket values('TIDBOOK0003001', 'BOOK0003', 'GLD',  415);
INSERT into Ticket values('TIDBOOK0003002', 'BOOK0003', 'GLD',  415);
INSERT into Ticket values('TIDBOOK0003003', 'BOOK0003', 'GLD',  415);
INSERT into Ticket values('TIDBOOK0003004', 'BOOK0003', 'GLD',  415);

INSERT into Booking values('BOOK0004', 2, 960, '8261723854786968', 'Rohit A', 1008, 'SHTH520001');
INSERT into Ticket values('TIDBOOK0004001', 'BOOK0004', 'GLD',  480);
INSERT into Ticket values('TIDBOOK0004002', 'BOOK0004', 'GLD',  480);

INSERT into Booking values('BOOK0005', 2, 960, '6826145790463578', 'kishan G', 1009, 'SHTH530001');
INSERT into Ticket values('TIDBOOK0005001', 'BOOK0005', 'GLD',  480);
INSERT into Ticket values('TIDBOOK0005002', 'BOOK0005', 'GLD',  480);



DELIMITER $$

CREATE FUNCTION CalculateTotalUsers()
RETURNS INT
DETERMINISTIC
READS SQL DATA
BEGIN
  DECLARE totalUsers INT;
  SELECT COUNT(User_ID) INTO totalUsers FROM USERS;
  RETURN totalUsers;
END $$

DELIMITER ;








DELIMITER //
CREATE PROCEDURE CalculateTotalMoviesNow(OUT total_movies INT)
BEGIN
  SELECT COUNT(*) INTO total_movies FROM Movie;
END;
//
DELIMITER ;










DELIMITER $$

CREATE FUNCTION CalculateTotalBooking()
RETURNS INT
DETERMINISTIC
READS SQL DATA
BEGIN
  DECLARE totalbooks INT;
  SELECT COUNT(Booking_ID) INTO totalbooks FROM booking;
  RETURN totalbooks;
END $$

DELIMITER ;