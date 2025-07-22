CREATE TABLE crime(crime_id int NOT NULL, crime_type varchar(100),crime_place varchar(100),crime_date DATE NOT NULL,PRIMARY KEY(crime_id));
CREATE TABLE fir(crime_id int not null,fir_id int not null,fir_statement varchar(200),fir_writer varchar(200),date_of_fir DATE NOT NULL,PRIMARY KEY(fir_id),FOREIGN KEY(crime_id) REFERENCES crime(crime_id));
CREATE TABLE criminal(crime_id int not null,criminal_id int not null,criminal_name varchar(100),past_crimes varchar(200) DEFAULT "None",jail_name varchar(100) DEFAULT "NONE",FOREIGN KEY(crime_id) REFERENCES crime(crime_id));
CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)
CREATE TABLE fir_backup(crime_id int not null,fir_id int not null,fir_statement varchar(200),fir_writer varchar(200),date_of_fir DATE NOT NULL,PRIMARY KEY(fir_id),FOREIGN KEY(crime_id) REFERENCES crime(crime_id));

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

DELIMITER $$
CREATE TRIGGER fir_trigger BEFORE DELETE ON fir
FOR EACH ROW
BEGIN
IF EXISTS (SELECT * FROM fir WHERE crime_id=OLD.crime_id)
THEN INSERT INTO fir_backup SELECT * FROM fir WHERE crime_id=OLD.crime_id;
END IF;
END$$
DELIMITER;

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
