import streamlit as st
import mysql.connector
from create_crime import create
from read_data import read
from update import update
from remove import delete

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    
)
c = mydb.cursor()
c.execute("CREATE DATABASE IF NOT EXISTS CRIME;")


def crud():
    
    menu = ["Add Crime Details", "View Crime Details", "Edit Crime Details", "Remove Crime Details"]
    choice = st.sidebar.selectbox("Menu", menu)

    
    if choice == "Add Crime Details":
        st.subheader("Enter Crime Details:")
        create()

    elif choice == "View Crime Details":
        st.subheader("View Crime Details:")
        read()
        

    elif choice == "Edit Crime Details":
        st.subheader("Edited crime Details:")
        update()
        

    elif choice == "Remove Crime Details":
        st.subheader("Delete crime:")
        delete()
        

    else:
        st.subheader("About crime")


'''if __name__ == '__main__':
    main()'''