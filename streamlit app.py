import streamlit as st
import pandas as pd
import mysql.connector

# Custom CSS
custom_css = """<style>
    body { font-family: 'Arial', sans-serif; background-color: #f4f4f9; }
    .title { text-align: center; color: #f4f4f9; }
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

    Data_Table = ['categories_table', 'competitions_table','competitors_table', 'competitor_rankings_table','complexes_table', 'venues_table']
    selected_Table = st.sidebar.selectbox('Table Name', Data_Table)

    if selected_Table == 'categories_table':
        # store fetched data in the variable
        df =load_data(selected_Table)

        # Columns for Further process 
        # [category_id , category_name]

        # set options for user 
        category_id = ['All'] + list(df['category_id'].unique())
        category_name =['All']+ list(df['category_name'].unique())
        
        # User selection
        st.sidebar.markdown('<p class="filter-title">Category ID</p>', unsafe_allow_html=True)
        category_id = st.sidebar.selectbox('', category_id)
        st.sidebar.markdown('<p class="filter-title">Category Name</p>', unsafe_allow_html=True)
        category_name = st.sidebar.selectbox('',category_name)

        # Filter the DataFrame based on the selected filters
        if 'category_id' in df.columns and 'category_name' in df.columns:
            filtered_data = df.loc[((df['category_id']==category_id)| (category_id == 'All') )& ((df['category_name']==category_name) | (category_name == 'All'))]
            st.dataframe(filtered_data)
        else:
            st.write("Required columns are missing from the table.")

    elif selected_Table == 'competitions_table':
        df = load_data(selected_Table)
        # Columns for Further process
        # [competition_id,competition_name,parent_id,type,gender,category_id]

        # set options for user
        competition_id = ['All'] + list(df['competition_id'].unique())
        competition_name = ['All'] + list(df['competition_name'].unique())
        parent_id = ['All'] + list(df['parent_id'].unique())
        type = ['All'] + list(df['type'].unique())
        gender = ['All'] + list(df['gender'].unique())
        category_id = ['All'] + list(df['category_id'].unique())

        # User selection
        st.sidebar.markdown('<p class="filter-title">Competation ID</p>', unsafe_allow_html=True)
        competition_id = st.sidebar.selectbox('',competition_id)
        st.sidebar.markdown('<p class="filter-title">Competation Name</p>', unsafe_allow_html=True)
        competition_name = st.sidebar.selectbox('',competition_name)
        st.sidebar.markdown('<p class="filter-title">Parent Name</p>', unsafe_allow_html=True)
        parent_id = st.sidebar.selectbox('',parent_id)
        st.sidebar.markdown('<p class="filter-title">Type</p>', unsafe_allow_html=True)
        type =  st.sidebar.selectbox('',type)
        st.sidebar.markdown('<p class="filter-title">Gender</p>', unsafe_allow_html=True)
        gender = st.sidebar.selectbox('',gender)
        st.sidebar.markdown('<p class="filter-title">Category ID</p>', unsafe_allow_html=True)
        category_id = st.sidebar.selectbox('', category_id)

        # Filter the DataFrame based on the selected filters
        if 'competition_id' in df.columns and 'competition_name' in df.columns and 'parent_id' in df.columns and 'type' in df.columns and 'gender' in df.columns and 'category_id' in df.columns:
            filtered_data = df.loc[((df['competition_id']==competition_id)| (competition_id == 'All')) & ((df['competition_name']==competition_name)| (competition_name == 'All')) & ((df['parent_id']==parent_id)| (parent_id == 'All')) & ((df['type']==type)| (type == 'All')) & ((df['gender']==gender)| (gender == 'All')) & ((df['category_id']==category_id)| (category_id == 'All'))]
            st.dataframe(filtered_data)
        else:
            st.write("Required columns are missing from the table.")


    elif selected_Table == 'complexes_table':
        df =load_data(selected_Table)
        # Columns for Further process
        # [complex_id,complex_name]

        # set options for user
        complex_id = ['All'] + list(df['complex_id'].unique())
        complex_name = ['All'] + list(df['complex_name'].unique())

        # User selection
        st.sidebar.markdown('<p class="filter-title">Complex ID</p>', unsafe_allow_html=True)
        complex_id = st.sidebar.selectbox('',complex_id)
        st.sidebar.markdown('<p class="filter-title">Complex Name</p>', unsafe_allow_html=True)
        complex_name = st.sidebar.selectbox('',complex_name)

        # Filter the DataFrame based on the selected filters
        if 'complex_id' in df.columns and 'complex_name' in df.columns:
            filtered_data = df.loc[((df['complex_id']==complex_id)| (complex_id == 'All') )& ((df['complex_name']==complex_name) | (complex_name == 'All'))]
            st.dataframe(filtered_data)
        else:
            st.write("Required columns are missing from the table.")


    elif selected_Table == 'venues_table':
        df = load_data(selected_Table)
        # Columns for Further process
        # [venue_id,venue_name,city_name,country_name,country_code,timezone,complex_id]

        # set options for user
        venue_id = ['All'] + list(df['venue_id'].unique())
        venue_name = ['All'] + list(df['venue_name'].unique())
        city_name = ['All'] + list(df['city_name'].unique())
        country_name = ['All'] + list(df['country_name'].unique())
        country_code = ['All'] + list(df['country_code'].unique())
        timezone = ['All'] + list(df['timezone'].unique())
        complex_id = ['All'] + list(df['complex_id'].unique())

        # User selection
        st.sidebar.markdown('<p class="filter-title">Venue ID</p>', unsafe_allow_html=True)
        venue_id = st.sidebar.selectbox('',venue_id)
        st.sidebar.markdown('<p class="filter-title">Venue Name</p>', unsafe_allow_html=True)
        venue_name = st.sidebar.selectbox('',venue_name)
        st.sidebar.markdown('<p class="filter-title">City Name</p>', unsafe_allow_html=True)
        city_name = st.sidebar.selectbox('',city_name)
        st.sidebar.markdown('<p class="filter-title">Country Name</p>', unsafe_allow_html=True)
        country_name = st.sidebar.selectbox('',country_name)
        st.sidebar.markdown('<p class="filter-title">Country Code</p>', unsafe_allow_html=True)
        country_code = st.sidebar.selectbox('',country_code)
        st.sidebar.markdown('<p class="filter-title">TimeZone</p>', unsafe_allow_html=True)
        timezone = st.sidebar.selectbox('',timezone)
        st.sidebar.markdown('<p class="filter-title">Complex ID</p>', unsafe_allow_html=True)
        complex_id = st.sidebar.selectbox('',complex_id)

        # Filter the DataFrame based on the selected filters
        if 'venue_id' in df.columns and 'venue_name' in df.columns and 'city_name' in df.columns and 'country_name' in df.columns and 'country_code' in df.columns and 'timezone' in df.columns and 'complex_id' :
            filtered_data = df.loc[((df['venue_id']==venue_id)| (venue_id == 'All') ) & ((df['venue_name']==venue_name) | (venue_name == 'All')) & ((df['city_name']==city_name) | (city_name == 'All')) & ((df['country_name']==country_name) | (country_name == 'All')) & ((df['country_code']==country_code) | (country_code == 'All')) & ((df['timezone']==timezone) | (timezone == 'All')) & ((df['complex_id']==complex_id) | (complex_id == 'All'))]
            st.dataframe(filtered_data)
        else:
            st.write("Required columns are missing from the table.")

    elif selected_Table == 'competitor_rankings_table':
        df = load_data(selected_Table)
        # Columns for Further process
        # [rank_id,rank,movement,points,competitions_played,competitor_id]

        # set options for user
        rank_id = ['All'] + list(df['rank_id'].unique())
        rank = ['All'] + list(df['rank'].unique())
        movement = ['All'] + list(df['movement'].unique())
        points = ['All'] + list(df['points'].unique())
        competitions_played = ['All'] + list(df['competitions_played'].unique())
        competitor_id = ['All'] + list(df['competitor_id'].unique())

        # User selection
        st.sidebar.markdown('<p class="filter-title">Rank ID</p>', unsafe_allow_html=True)
        rank_id = st.sidebar.selectbox('',rank_id,key="rank_id_key")
        st.sidebar.markdown('<p class="filter-title">Rank</p>', unsafe_allow_html=True)
        rank = st.sidebar.selectbox('',rank)
        st.sidebar.markdown('<p class="filter-title">Movement</p>', unsafe_allow_html=True)
        movement = st.sidebar.selectbox('',movement)
        st.sidebar.markdown('<p class="filter-title">Points</p>', unsafe_allow_html=True)
        points = st.sidebar.selectbox('',points)
        st.sidebar.markdown('<p class="filter-title">Competitions Played</p>', unsafe_allow_html=True)
        competitions_played = st.sidebar.selectbox('',competitions_played)
        st.sidebar.markdown('<p class="filter-title">Competitior ID</p>', unsafe_allow_html=True)
        competitor_id = st.sidebar.selectbox('',competitor_id)

        # Filter the DataFrame based on the selected filters
        if 'rank_id' in df.columns and 'rank' in df.columns and 'movement' in df.columns and 'points' in df.columns and 'competitions_played' in df.columns and 'competitor_id' in df.columns :
            filtered_data = df.loc[((df['rank_id']==rank_id)| (rank_id == 'All') ) & ((df['rank']== rank) | (rank == 'All')) & ((df['movement']==movement) | (movement == 'All')) & ((df['points']==points) | (points == 'All')) & ((df['competitions_played']==competitions_played) | (competitions_played == 'All')) & ((df['competitor_id']==competitor_id) | (competitor_id == 'All'))]
            st.dataframe(filtered_data)
        else:
            st.write("Required columns are missing from the table.")

    elif selected_Table == 'competitors_table':
        df = load_data(selected_Table)
        # Columns for Further process
        # [competitor_id,name,country,country_code,abbreviation]

        # set options for user
        competitor_id = ['All'] + list(df['competitor_id'].unique())
        name = ['All'] + list(df['name'].unique())
        country = ['All'] + list(df['country'].unique())
        country_code = ['All'] + list(df['country_code'].unique())
        abbreviation = ['All'] + list(df['abbreviation'].unique())

        # User selection
        st.sidebar.markdown('<p class="filter-title">Competitor ID</p>', unsafe_allow_html=True)
        competitor_id = st.sidebar.selectbox('',competitor_id)
        st.sidebar.markdown('<p class="filter-title">Name</p>', unsafe_allow_html=True)
        name = st.sidebar.selectbox('',name)
        st.sidebar.markdown('<p class="filter-title">Country</p>', unsafe_allow_html=True)
        country = st.sidebar.selectbox('',country)
        st.sidebar.markdown('<p class="filter-title">Country Code</p>', unsafe_allow_html=True)
        country_code = st.sidebar.selectbox('',country_code)
        st.sidebar.markdown('<p class="filter-title">Abbrevation</p>', unsafe_allow_html=True)
        abbreviation = st.sidebar.selectbox('',abbreviation)
        

        # Filter the DataFrame based on the selected filters
        if 'competitor_id' in df.columns and 'name' in df.columns and 'country' in df.columns and 'country_code' in df.columns and 'abbreviation' in df.columns:
            filtered_data = df.loc[((df['competitor_id']==competitor_id)| (competitor_id == 'All') ) & ((df['name']== name) | (name == 'All')) & ((df['country']==country) | (country == 'All')) & ((df['country_code']==country_code) | (country_code == 'All')) & ((df['abbreviation']==abbreviation) | (abbreviation == 'All'))]
            st.dataframe(filtered_data)
        else:
            st.write("Required columns are missing from the table.")
    else:
        st.sidebar.write(' no data available')


    
   
