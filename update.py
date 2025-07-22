import datetime

import pandas as pd
import streamlit as st
from databas import view_criminal,view_only_crime_ids, get_details, edit_details


def update():
    result = view_criminal()
    df = pd.DataFrame(result, columns=["crime_id", "criminal_id", "criminal_name", "past_crimes","jail_name"])
    with st.expander("Current Criminals"):
        st.dataframe(df)
    list_of_crimes = [i[0] for i in view_only_crime_ids()]
    selected_crime = st.selectbox("Select the crime_id to change Criminal Info:", list_of_crimes)
    selected_result = get_details(selected_crime)
    # st.write(selected_result)
    if selected_result:
        crime_id = selected_result[0][0]
        criminal_id = selected_result[0][1]
        criminal_name = selected_result[0][2]
        past_crimes = selected_result[0][3]
        jail_name = selected_result[0][4]


        # Layout of Create

        col1, col2 = st.columns(2)
        with col1:
            new_crime_id = st.text_input("crime id:", crime_id)
            new_criminal_name = st.text_input("criminal_name:", criminal_name)
            new_jail_name=st.text_input("Jail name:",jail_name)
        with col2:
            new_criminal_id = st.number_input("Criminal Id:",criminal_id)
            new_past_crimes=st.text_input("Past crimes",past_crimes)
        

        if st.button("Update criminal info"):
            edit_details(new_crime_id,new_criminal_id,new_criminal_name,new_past_crimes,new_jail_name ,crime_id,criminal_id,criminal_name,past_crimes,jail_name)
            st.success("Successfully updated")

       
        with st.expander("Updated data"):
            result2 = view_criminal()
            df2 = pd.DataFrame(result2, columns=["crime_id", "criminal_id", "criminal_name", "past_crimes","jail_name"])
            st.dataframe(df2)


