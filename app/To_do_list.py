import streamlit as st
import datetime
from datetime import timedelta, date, datetime
from pymongo import MongoClient
from bson.objectid import ObjectId
from utils.getDatabase import DatabaseConnection
from utils.getUserInfo import UsersConnection
from utils.createCards import Cards
from utils.auth import Auth

st.set_page_config(
    page_icon="✏️",
    layout="wide"
)

if 'user' not in st.session_state:
    st.session_state['user'] = ''
if 'username' not in st.session_state:
    st.session_state['username'] = ''
if 'form' not in st.session_state:
       st.session_state.form = 'login_form'
users = UsersConnection()
auth = Auth()

if st.session_state['user']:
    st.sidebar.write(f"You are logged in as {st.session_state['username'].title()}")
    connection = DatabaseConnection()
    cards = Cards()

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.header("Create your To Do here", divider="rainbow")
        cards.create_task()

    with col2:
        st.image("app/assets/contact_me.png")
    
    tasks = connection.get_data(st.session_state['user_id'])

    col4, col5, col6 = st.columns(3)

    with col4:
        cards.create_display_tasks("To Do", tasks, "red", st.session_state['user_id'])
    with col5:
        cards.create_display_tasks("Doing", tasks, "orange", st.session_state['user_id'])
    with col6:
        cards.create_display_tasks("Done", tasks, "green", st.session_state['user_id'])
    
    auth.logout()
    
elif st.session_state.form == 'signup_form' and  st.session_state.username == '':
    auth.form_selection()
    auth.signup_form()

elif st.session_state.username == '':
    auth.form_selection()
    auth.login_form()
                    