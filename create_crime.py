import streamlit as st
from databas import add_crime_data
from databas import create_table
from databas import add_criminal_data
from databas import add_fir_data

def create():
    st.title("Add Crime Data ")
    

    create_table()
    menu = ["Add Crime Details", "Add Criminal Details", "Add FIR Details"]
    choice = st.selectbox("Menu", menu)
    st.subheader("Enter Crime Details:")

    if choice == "Add Crime Details":
        st.subheader(choice)

        col1, col2 = st.columns(2)
        with col1:
            crime_id = st.number_input("Crime id:")
            crime_type = st.text_input("Crime Type:")
       
        with col2:
            crime_date=st.date_input("Date of Crime:")
            crime_place=st.text_input("Place of crime:")

        if st.button("Add Crime Details"):
            add_crime_data(crime_id, crime_type,crime_place,crime_date)
            st.success("Successfully added the Crime Details: {}".format(crime_id))
    if choice == "Add Criminal Details":
        st.subheader("Enter Criminal Details:")
        col1, col2 = st.columns(2)
        with col1:
            crime_id = st.number_input("Crime id:")
            criminal_name = st.text_input("Criminal name:")
            past_crimes=st.text_input("Past Crimes (if any)")
       
        with col2:
            criminal_id=st.number_input("Criminal id:")
            jail_name=st.text_input("Jail the accused been put(if):")

        if st.button("Add criminal Details"):
            add_criminal_data(crime_id, criminal_id,criminal_name,past_crimes,jail_name)
            st.success("Successfully added the Crime Details: {}".format(criminal_name))
    if choice == "Add FIR Details":
        st.subheader("Add FIR Details")
        col1,col2=st.columns(2)
        with col1:
            crime_id=st.number_input("Enter crime id:")
            fir_writer=st.text_input("Enter Fir writer name:")
            fir_statement=st.text_input("Enter FIR Description:")
        with col2:
            fir_id=st.number_input("enter FIR id:")
            date_of_fir=st.date_input("Enter the Date on which the FIR has filled")
        if st.button("Add FIR Details"):
            add_fir_data(crime_id,fir_id,fir_statement,fir_writer,date_of_fir)
            st.success("Successfully added the FIR Details by: {}".format(fir_writer))
