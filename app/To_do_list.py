import streamlit as st
import datetime
from datetime import timedelta, date, datetime
from pymongo import MongoClient
from bson.objectid import ObjectId
from utils.getDatabase import DatabaseConnection
from utils.createCards import Cards

st.set_page_config(
    page_icon="✏️",
    layout="wide",
    initial_sidebar_state="expanded"
)

connection = DatabaseConnection()

cards = Cards()

col1, col2 = st.columns(2, gap="large")

with col1:
    st.header("Create your To Do here", divider="rainbow")
    cards.create_task()

with st.sidebar:
    st.header("If you liked this project, here are my contacts")
    # icons, info = st.columns(2,gap="small")
    # with icons:
    #     st.image('app/assets/gmail.png')
    #     st.image('app/assets/linkedin.png')
    # with info:
    st.markdown("[E-mail](higuima13@gmail.com)")
    st.markdown("[Linkedin](https://www.linkedin.com/in/helena-g-702b31a3/)")


tasks = connection.get_data()

col4, col5, col6 = st.columns(3)

with col4:
    cards.create_display_tasks("To Do", tasks, "red")
with col5:
    cards.create_display_tasks("Doing", tasks, "orange")
with col6:
    cards.create_display_tasks("Done", tasks, "green")
