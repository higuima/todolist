import streamlit as st
import datetime
from pymongo import MongoClient
from bson.objectid import ObjectId


class DatabaseConnection:
    def __init__(self):
        self.database = 'todolistdb'
        self.cluster = f"mongodb+srv://{st.secrets.mongo.username}:{st.secrets.mongo.password}@cluster0.lpjfcwv.mongodb.net/{self.database}?retryWrites=true&w=majority"

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

    def update_todo_status(self, id, new_status):
        client = self.init_connection()
        db = client.todolistdb
        db.todos.update_one({"_id": "$id"}, {"$set": {"status": "$new_status"}})

    def delete_all_data(self):
        client = self.init_connection()
        db = client.todolistdb
        db.todos.delete_many({"name": "Helena"})
        

