import pandas as pd
import streamlit as st
from databas import crime_in_fir,delete_data,view_fir,backup


def delete():
    result = view_fir()
    df = pd.DataFrame(result, columns=["crime_id", "fir_id", "fir_statement", "fir_writer","date_of_fir"])
    with st.expander("Current data"):
        st.dataframe(df)

    list_of_crimes = [i[0] for i in crime_in_fir()]
    selected_crime = st.selectbox("crime to Delete", list_of_crimes)
    st.warning("Do you want to delete ::{}".format(selected_crime))
    if st.button("Delete crime"):
        delete_data(selected_crime)
        st.success("crime has been deleted successfully")
    
    with st.expander("Updated data"):
        new_result = view_fir()
        df2 = pd.DataFrame(new_result, columns=["crime_id", "fir_id", "fir_statement", "fir_writer","date_of_fir"])
        st.dataframe(df2)
    with st.expander("Backup Fir Data"):
        res=backup()
        df3=pd.DataFrame(res,columns=["crime_id","fir_id","fir_statement","fir_writer","date_of_fir"])
        st.dataframe(df3)
    

'''st.subheader("Delete")
        with st.beta_expander("View Data"):
            result = view_all_data()
            # st.write(result)
            clean_df = pd.DataFrame(result,columns=["Task","Status","Date"])
            st.dataframe(clean_df)

        unique_list = [i[0] for i in view_all_task_names()]
        delete_by_task_name =  st.selectbox("Select Task",unique_list)
        if st.button("Delete"):
            delete_data(delete_by_task_name)
            st.warning("Deleted: '{}'".format(delete_by_task_name))

        with st.beta_expander("Updated Data"):
            result = view_all_data()
            # st.write(result)
            clean_df = pd.DataFrame(result,columns=["Task","Status","Date"])
            st.dataframe(clean_df)'''