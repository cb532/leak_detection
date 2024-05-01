import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import os

# Function to get a database connection using SQLAlchemy
def get_connection():
    user = os.getenv("DB_USER")
    passwd = os.getenv("DB_PASS")
    host = os.getenv("DB_HOST")
    db = os.getenv("DB_NAME")
    connection_string = f"mysql+pymysql://{user}:{passwd}@{host}/{db}"
    engine = create_engine(connection_string)
    return engine

# Function to load the last 10 entries from the database
def load_recent_data():
    engine = get_connection()
    # Consistent order: newest entries at the top
    query = "SELECT * FROM sensor_data ORDER BY timestamp DESC LIMIT 10"  # Adjust 'timestamp' as per your column name
    return pd.read_sql(query, engine.connect())

# Function to load data based on a specific date, with consistent ordering
def load_data_by_date(date):
    engine = get_connection()
    # Consistent order: newest entries at the top
    query = f"SELECT * FROM sensor_data WHERE DATE(timestamp) = '{date}' ORDER BY timestamp DESC"
    return pd.read_sql(query, engine.connect())

# Main app function
def main():
    st.title('Leak Detection')

    # Sidebar for date input and buttons
    date_to_filter = st.sidebar.date_input("Choose a date to filter data")
    show_date = st.sidebar.button("Show Data for Selected Date")
    show_latest = st.sidebar.button("Show Latest 10 Entries")

    if show_date:
        data = load_data_by_date(date_to_filter)
        st.write("Data for Selected Date (newest at top):")
        st.dataframe(data)
    
    if show_latest:
        data = load_recent_data()
        st.write("Latest 10 Entries (newest at top):")
        st.dataframe(data)

    if not show_date and not show_latest:
        # Optional: Show some default text or data when no button has been clicked
        st.write("Please select an option to view data.")

# Run the main function
if __name__ == "__main__":
    main()
