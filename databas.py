import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    #password="root",
    database="crime_db"
)
c = mydb.cursor(buffered=True)



def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS crime(crime_id int NOT NULL, crime_type varchar(100),crime_place varchar(100),crime_date DATE NOT NULL,PRIMARY KEY(crime_id));')


def add_crime_data(crime_id, crime_type,crime_place,crime_date):
    c.execute('INSERT INTO crime (crime_id,crime_type,crime_place,crime_date) VALUES (%s,%s,%s,%s);',
              (crime_id, crime_type,crime_place,crime_date))
    mydb.commit()

def add_criminal_data(crime_id, criminal_id,criminal_name,past_crimes,jail_name):
    c.execute('INSERT INTO criminal (crime_id, criminal_id,criminal_name,past_crimes,jail_name) VALUES (%s,%s,%s,%s,%s);',
              (crime_id, criminal_id,criminal_name,past_crimes,jail_name))
    mydb.commit()

def add_fir_data(crime_id,fir_id,fir_statement,fir_writer,date_of_fir):
    c.execute('INSERT INTO fir(crime_id,fir_id,fir_statement,fir_writer,date_of_fir) VALUES (%s,%s,%s,%s,%s);',
                (crime_id,fir_id,fir_statement,fir_writer,date_of_fir))
    mydb.commit()

def view_crime_data():
    c.execute('SELECT * FROM crime NATURAL JOIN (criminal NATURAL JOIN fir); ')
    data = c.fetchall()
    return data

def edit_details(new_crime_id,new_criminal_id,new_criminal_name,new_past_crimes,new_jail_name ,crime_id,criminal_id,criminal_name,past_crimes,jail_name):
    c.execute("UPDATE criminal SET crime_id=%s, criminal_id=%s, criminal_name=%s, past_crimes=%s,jail_name=%s WHERE crime_id=%s and criminal_id=%s and criminal_name=%s and past_crimes=%s and jail_name=%s", (new_crime_id,new_criminal_id,new_criminal_name,new_past_crimes,new_jail_name ,crime_id,criminal_id,criminal_name,past_crimes,jail_name))
    mydb.commit()


def view_only_crime_ids():
    c.execute('SELECT crime_id FROM criminal')
    data = c.fetchall()
    return data

def crime_in_fir():
    c.execute("select crime_id from fir;")
    data=c.fetchall()
    return data
def get_fir_delay(crime_id):
    c.execute("select find_delay_fir({})".format(crime_id))
    data=c.fetchall()
    return data

def view_only_fir_ids():
    c.execute('SELECT fir_id FROM fir')
    data = c.fetchall()
    return data

def view_crime():
    c.execute('SELECT * FROM crime;')
    data = c.fetchall()
    return data

def view_criminal_names():
    c.execute("SELECT criminal_name FROM criminal ;")
    data = c.fetchall()
    return data

def view_criminal():
    c.execute('SELECT * FROM criminal;')
    data = c.fetchall()
    return data
def get_crimes(criminal_name):
    c.execute('SELECT criminal_name,count(crime_id) FROM criminal WHERE criminal_name="{}"'.format(criminal_name))
    data = c.fetchall()
    return data
def view_fir():
    c.execute('SELECT * FROM fir;')
    data = c.fetchall()
    return data

def get_details(crime_id):
    c.execute('SELECT * FROM criminal WHERE crime_id="{}"'.format(crime_id))
    data = c.fetchall()
    return data

def delete_data(crime_id):
	c.execute('DELETE FROM fir WHERE crime_id="{}"'.format(crime_id))
	mydb.commit()

def backup():
    c.execute("SELECT * FROM fir_backup;")
    data = c.fetchall()
    return data

def crimeids():
    c.execute("select crime_id from crime;")
    data = c.fetchall()
    return data


