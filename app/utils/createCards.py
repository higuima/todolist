import streamlit as st
import datetime
from datetime import timedelta, date, datetime
from utils.getDatabase import DatabaseConnection


connection = DatabaseConnection()

class Cards():
    def sort_cards(self, task:dict, desired_status):
        list_tasks = []
        for item in task:
            if item['status'] == desired_status:
                list_tasks.append(item)
        return list_tasks

    def create_card(self, task:list):
        if task['text'] != "":
            task_display = st.container(border=True)
            task_display.subheader(task['text'])
            options = ["To Do","Doing", "Done"]

            new_status = task_display.selectbox("Status", options, key=task['_id'], index=options.index(task['status']))
            if new_status != task['status']:
                connection.update_todo(task['_id'], "status", new_status)
                connection.get_data()
            if datetime.now() > datetime.strptime(task['end_date'],"%Y-%m-%d") and task['status'] != "Done":
                task_display.warning("Task is behind schedule!")
            tag_id = str(task['_id']) + task['text']
            if task['tags']:
                task_tags = task_display.multiselect("Tags", ['Development', 'Frontend'], task['tags'], key=tag_id)
                # st.write(task_tags != len(task['tags']))
                # if task_tags != len(task['tags']):
                #     connection.update_todo(task['_id'], "tags", task_tags)