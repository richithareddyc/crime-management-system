import pandas as pd
import streamlit as st
import plotly.express as px
from databas import view_crime_data,view_criminal_names,get_crimes,crime_in_fir,get_fir_delay,crimeids
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    #password="root",
    database="crime_db"
)
c = mydb.cursor(buffered=True)


def read():
    result = view_crime_data()
    # st.write(result)
    df = pd.DataFrame(result, columns=['crime_id','crime_type','crime_place','crime_date','criminal_id','criminal_name','past_crimes','jail_name','fir_id','fir_statement','fir_writer','date_of_fir'])
    with st.expander("View all crimes"):
        st.dataframe(df)
    list_of_criminals = [i[0] for i in view_criminal_names()]
    selected_criminal = st.selectbox("Select the Criminal name :", list_of_criminals)
    res=get_crimes(selected_criminal)
    df1=pd.DataFrame(res,columns=['criminal_name','count'])
    with st.expander("View No of crimes done by criminal"):
        st.dataframe(df1)
    

    
    crimes_in_fir=[i[0] for i in crime_in_fir()]
    crime_s=st.selectbox("Select the crime id to find the delay in fir:",crimes_in_fir)

    if st.button("Check date"):
        res1=get_fir_delay(crime_s)
        args=[crime_s,0]
        ans= c.callproc("rai",args)
        if ans[1]=="yes":
            st.success("The Dates are vaild and the gap between them is ::{}".format(-1*res1[0][0]))
        elif ans[1]=="No":
            st.warning("Fir is entered before the crime commited")    
    
    crime_ids=[i[0] for i in crimeids()]
    cr=st.selectbox("select crime id to classify:",crime_ids)
    if st.button("check category"):
        args=[cr,0]
        ans=c.callproc("catogery",args)
        if ans[1]=="police":
            st.write("This case is handled by state government:")
        elif ans[1]=="CBI":
            st.write("This case is handled by central government:")     

