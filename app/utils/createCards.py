import streamlit as st
import datetime
from datetime import timedelta, date, datetime
from utils.getDatabase import DatabaseConnection


connection = DatabaseConnection()

class Cards():
    def create_card(self, task:dict):
        client = connection.init_connection()
        task_display = st.container(border=True)
        task_display.subheader(task['text'])
        new_status = task_display.selectbox("Status", ["To Do","Doing", "Done"], key=task['_id'])
        if new_status != task['status']:
            st.warning("changed status")
            connection.update_todo_status(client, task['_id'], new_status)
        if datetime.now() > datetime.strptime(task['end_date'],"%Y-%m-%d") and task['status'] != "Done":
            task_display.warning("Task is behind schedule!")