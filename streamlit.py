import streamlit as st
import snowflake.connector
import pandas as pd

st.sidebar.title("my streamlit app")
account = st.sidebar.text_input("Snowflake Account Name")
warehouse = st.sidebar.text_input("Snowflake Warehouse")
username = st.sidebar.text_input("Username")
password = st.sidebar.text_input("password", type="password")
query = st.sidebar.text_area("SQL Query")

#Create a button to execute the query
if st.sidebar.button("Run Query"):
    st.spinner(text='text is running')
    #Connect to snowflake
    conn = snowflake.connector.connect(
        user=username,
        password=password,
        warehouse=warehouse,
        account=account
    )

    # Execute the query
    cur = conn.cursor()
    cur.execute(query)
    # Fetch column names
    column_names = [desc[0] for desc in cur.description]
    # Fetch results and display them
    results = cur.fetchall()
    # Convert results to pandas DataFrame
    df = pd.DataFrame(results, columns=column_names)

    # Display the DataFrames
    st.dataframe(df)

    # Close the cursor and connection 
    cur.close()
    conn.close()

    