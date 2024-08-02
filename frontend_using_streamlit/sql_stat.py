import pandas as pd
import streamlit as st
from database import get_sql

def stat():
    sta = st.text_input("SQL_Statement:")

    if st.button("Execute SQL Statement:"):
        result = get_sql(sta)
        df = pd.DataFrame(result)
        with st.expander("View The Ouput"):
            st.dataframe(df)