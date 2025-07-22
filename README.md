
# DBMS PROJECT
# PROJECT TITLE:

CRIME DATA MANAGEMENT SYSTEM

# DESCRIPTION OF PROJECT:

The project has five tables
- Usertable
- crime
- criminal
- fir
- fir_backup

Usertable stores the username and password.


crime table contains the crime_id,crime_type,crime_date and crime_place.


criminal table contains crime_id,criminal_id,past_crimes,jail_name,criminal_name.


fir table contains fir_id,crime_id,fir_writer,fir_description,date_of_fir.


fir_backup is same as fir that stores the fir information as backup if we delete it.


# INSTALLATION AND RUNNING 

XAMPP AND STREAMLIT HAS TO BE INSTALLED 


APACHE ND MYSQL SHOULD BE RUNNING BEFORE IMPLEMENTATION

First a database `crime_db` has to be created 

Code to start the Application

`streamlit run app.py` or `streamlit run path(app.py)`

`app.py` is the home page


After running the application Home page will be displayed.

Select the login option from the select queue and then Do as indicated in the functionalities.



The Project has 
`
Login page
`

After logging in succesfully,
if Profiles category is choosen,it shows the usernames of the people that has logged in.

We have to chose the category as cop to 


`
Add crime Details`

`
View crime Details
`

`
Update Crime Details
`

`Delete crime Details
`
- TRIGGERS , FUNCTIONS AND PROCEDURES should be executed in mysql server to implement in the project


# FUNCTIONALITIES OF THE PROJECT


Add crime details
- We can add crime , criminal and fir details individually

View crime details
- In this section the input data is represented and we can check the delay between the crime date and date of fir by selecting the crime id of the case 
- If the fir is entered before the crime has been comitted , warning message will be shown else the delay of fir is shown
- check category button will classify the case based on input crime id selected.

Update Crime details
- we can update the criminal details here and the changes can be seen below the Update button

Delete Crime details
- Fir with the selected crime id can be deleted 
- The deleted fir is stored in the fir_backup table by using trigger

### TRIGGER

Adds the fir data which has been deleted into fir _backup table


`
DELIMITER $$
CREATE TRIGGER fir_trigger BEFORE DELETE ON fir
FOR EACH ROW
BEGIN
IF EXISTS (SELECT * FROM fir WHERE crime_id=OLD.crime_id)
THEN INSERT INTO fir_backup SELECT * FROM fir WHERE crime_id=OLD.crime_id;
END IF;
END$$
DELIMITER;
`

### PROCEDURE AND FUNCTIONS

Procedure `rai` gives the output as No if date_of_fir is older than crime_date which doesnot make sense(fir is entered before crime commited) else gives Yes as output


`
DELIMITER $$
CREATE PROCEDURE rai(IN id int,OUT des varchar(10))
BEGIN
DECLARE d1,d2 DATE;
select crime_date INTO d1 from crime where crime_id=id;
select date_of_fir INTO d2 from fir where crime_id=id;
if datediff(d1,d2)>0 then 
set des="No";
else
set des="yes";
END IF;
END $$
DELIMITER ;
`


The `catogery` procedure classify the Crime based on crime id given.



`
DELIMITER $$
CREATE PROCEDURE catogery(IN id int,OUT cat varchar(20))
BEGIN
DECLARE c1 varchar(10);
select crime_type INTO c1 from crime where crime_id=id;
if c1="MURDER" then
set cat="CBI";
else
set cat="police";
END IF;
END $$
DELIMITER ;
`

Function `find_delay_fir` gives the delay between crime_date and date_of_fir (like 30 days..15 days...)


`
DELIMITER $
CREATE FUNCTION find_delay_fir(id int)
RETURNS int
BEGIN
DECLARE d1,d2 DATE;
select date_of_fir into d2 from fir where crime_id=id;
select crime_date into d1 from crime where crime_id=id;
RETURN (day(d1)-day(d2) + 30*(MONTH(d1)-MONTH(d2))+365*(YEAR(d1)-YEAR(d2)));
END$
DELIMITER ;
`


