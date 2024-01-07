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

    def get_data(self):
        client = self.init_connection()
        db = client.todolistdb
        items = db.todos.find()
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

    def delete_all_data(self):
        client = self.init_connection()
        db = client.todolistdb
        db.todos.delete_many({"name": "Helena"})
        

