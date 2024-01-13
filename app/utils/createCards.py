import streamlit as st
import datetime
from datetime import timedelta, date, datetime
from utils.getDatabase import DatabaseConnection
from streamlit_tags import st_tags


connection = DatabaseConnection()

class Cards():
    def sort_cards(self, task:dict, desired_status):
        list_tasks = []
        for item in task:
            if item['status'] == desired_status:
                list_tasks.append(item)
        return list_tasks

    def create_task(self):
        with st.form(key='todo', clear_on_submit=True):
            task = st.text_input("Insert your To-do here:")
            tags = st.multiselect("Add tags to your task:", ['Urgent', 'Important', 'Study'])
            date_range = st.date_input(
                "Select period of the task",
                value= (datetime.now(), datetime.now() + timedelta(days=7)),
                min_value= datetime.now(),
                max_value=None,
                format="DD.MM.YYYY",
            )
            todo = {
                "user_id": st.session_state['user_id'],
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

    def create_card(self, task:list, user_id):
        task_display = st.container(border=True)
        task_display.subheader(task['text'])
        options = ["To Do","Doing", "Done"]

        if datetime.now() > datetime.strptime(task['end_date'],"%Y-%m-%d") and task['status'] != "Done":
            due_date_countdown = datetime.strptime(task['end_date'], "%Y-%m-%d") - datetime.now()
            if due_date_countdown.days < 0:
                task_display.markdown(f"_This task is late by {due_date_countdown.days*(-1)} days_")
            else:
                task_display.markdown(f"_This task is due in {due_date_countdown.days} days_")

        new_status = task_display.selectbox("Status", options, key=task['_id'], index=options.index(task['status']))
        if new_status != task['status']:
            connection.update_todo(task['_id'], "status", new_status)
            connection.get_data(user_id)
        
        tag_id = "_tag_multiselect_" + str(task['_id'])
        task_tags = task_display.multiselect("Tags", ['Development', 'Frontend'], task['tags'], key=tag_id, placeholder="Add a tag")
        if sorted(task_tags) != sorted(task['tags']):
            connection.update_todo(task['_id'], "tags", task_tags)
        
        button_id = "_button_" + str(task['_id'])
        delete = task_display.button("✖ ", key=button_id, help="This button will delete your task")
        if delete:
            connection.delete_task(task['_id'])


    def create_display_tasks(self, status, tasks, color, user_id):
        title, count = st.columns(2)
        with title:
            st.title(f":{color}[{status}]")
        with count:
            st.title(connection.count_tasks(status, user_id))
        list_tasks = self.sort_cards(tasks, status)
        for task in list_tasks:
            card = self.create_card(task, user_id)
            if card != None:
                st.write(card)
