import streamlit as st
import datetime
from datetime import timedelta, date, datetime
from pymongo import MongoClient
from bson.objectid import ObjectId
from utils.getDatabase import DatabaseConnection
from utils.createCards import Cards

st.set_page_config(
    # page_icon="",
    layout="wide",
    initial_sidebar_state="expanded"
)


connection = DatabaseConnection()

cards = Cards()

col1, col2 = st.columns(2)


with col1:
    st.title("Create your To Do here")
    with st.form(key='todo', clear_on_submit=True):
        task = st.text_input("Insert your To-do here:")
        tags = st.multiselect("Add tags to your task:", ['Development', 'Frontend'])
        date_range = st.date_input(
            "Select period of the task",
            value= (datetime.now(), datetime.now() + timedelta(days=7)),
            min_value= datetime.now(),
            max_value=None,
            format="DD.MM.YYYY",
        )
        todo = {
            "name": "Helena",
            "text": task,
            "status": "To Do",
            "tags": tags,
            "creation_date": datetime.strftime(datetime.now(),"%Y-%m-%d"),
            "start_date": datetime.strftime(date_range[0],"%Y-%m-%d"),
            "end_date": datetime.strftime( date_range[1],"%Y-%m-%d")
            }
        submit_button = st.form_submit_button("Submit")
        if submit_button == True:
            connection.insert_todo(todo)


tasks = connection.get_data()
# delete = st.button("Delete all data from database", on_click=connection.delete_all_data())


col4, col5, col6 = st.columns(3)

with col4:
    st.title(":red[To Do]")
    list_tasks = cards.sort_cards(tasks, "To Do")
    for task in list_tasks:
        card = cards.create_card(task)
        if card != None:
            st.write(card)
with col5:
    st.title(":orange[Doing]")
    list_tasks = cards.sort_cards(tasks, "Doing")
    for task in list_tasks:
        card = cards.create_card(task)
        if card != None:
            st.write(card)
with col6:        
    st.title(":green[Done]")
    list_tasks = cards.sort_cards(tasks, "Done")
    for task in list_tasks:
        card = cards.create_card(task)
        if card != None:
            st.write(card)

# return_one = todos.find_one({"tags": "coding", "_id": ObjectId('6597f55ad938326df85c24d4')})
# return_all = todos.find({"tags": "coding"})

# print(todos.count_documents("name": "Patrick"))

# remove_one = todos.delete_one({"_id": ObjectId('6597f55ad938326df85c24d4')})
# remove_many = todos.delete_many([{"_id": ObjectId('6597f55ad938326df85c24d4')}])


# update_one = todos.update_one({"tags": "coding"}, {"$set": {"status": "done"}})
# update_many = todos.update_many({"status": "open"}, {"$set": {"status": "doing"}})