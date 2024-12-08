import streamlit as st
import pandas as pd
import mysql.connector

# Custom CSS
custom_css = """<style>
    body { font-family: 'Arial', sans-serif; background-color: #f4f4f9; }
    .title { text-align: center; color: #4A4A4A; }
    [data-testid="stSidebar"] { background-color: #FF4C4C; color: #FFF; }
</style>"""
st.markdown(custom_css, unsafe_allow_html=True)

# Initialize session state for sidebar
if 'show_sidebar' not in st.session_state:
    st.session_state.show_sidebar = False

# Load data from MySQL
def load_data(Table):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="sportradar"
    )
    query = f"SELECT * FROM {Table}"
    df = pd.read_sql(query, con=mydb)
    mydb.close()
    return df

# App Title
st.markdown('<h1 class="title">Tennis Data</h1>', unsafe_allow_html=True)

# Sidebar toggle
if st.checkbox("Show Sidebar"):
    st.session_state.show_sidebar = True
else:
    st.session_state.show_sidebar = False

# Sidebar functionality
if st.session_state.show_sidebar:
    st.sidebar.markdown('<h1 class="title">Filter Details</h1>', unsafe_allow_html=True)

    Data_Table = [
        'categories_table', 'competitions_table',
        'competitors_table', 'competitor_rankings_table',
        'complexes_table', 'venues_table'
    ]
    selected_Table = st.sidebar.selectbox('Table Name', Data_Table)

    # Load and filter data
    df = load_data(selected_Table)
    if not df.empty:
        st.dataframe(df.head())  # Display data preview
    else:
        st.sidebar.write("No data available.")
