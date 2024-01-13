import streamlit as st
import datetime
from pymongo import MongoClient
from bson.objectid import ObjectId


class DatabaseConnection:
    def __init__(self):
        self.database = 'todolistdb'
        self.cluster = f"mongodb+srv://{st.secrets.mongo.username}:{st.secrets.mongo.password}@cluster0.lpjfcwv.mongodb.net/{self.database}?retryWrites=true&w=majority"
    
    # @st.cache_resource
    def init_connection(self):
        return MongoClient(self.cluster)

    def get_data(self, user_id):
        client = self.init_connection()
        db = client.todolistdb
        items = db.todos.find({"user_id": ObjectId(user_id)})
        items = list(items)  # make hashable for st.cache_data
        return items

    def insert_todo(self, todo):
        client = self.init_connection()
        db = client.todolistdb
        db.todos.insert_one(todo)

    def insert_many_todos(self, todo:list):
        client = self.init_connection()
        db = client.todolistdb
        db.todos.insert_many(todo)

    def update_todo(self, id, old_value, new_value):
        client = self.init_connection()
        db = client.todolistdb
        db.todos.update_one({"_id": ObjectId(id)}, {"$set": {old_value: new_value}})
        st.rerun()
    
    def count_tasks(self, filter, id):
        client = self.init_connection()
        db = client.todolistdb
        count = db.todos.count_documents({"status": filter, "user_id": ObjectId(id)})
        if count > 1:
            return f":grey[{count} tasks]"
        elif count == 1:
            return f":grey[{count} task]"
        else:
            return ""
    
    def delete_task(self, id):
        client = self.init_connection()
        db = client.todolistdb
        db.todos.delete_one({"_id": ObjectId(id)})
        st.rerun()
