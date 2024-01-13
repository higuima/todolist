import streamlit as st
import datetime
import hmac
from pymongo import MongoClient
from bson.objectid import ObjectId
from utils.getDatabase import DatabaseConnection

database = DatabaseConnection()

class UsersConnection:
    def user_email_exists(self, email):
        client = database.init_connection()
        db = client.todolistdb
        user_info = db.users.find_one({'email':email})
        if user_info:
            st.error('Email is already registered')
            return True
        else:
            return False

    def insert_user(self, user):
        client = database.init_connection()
        db = client.todolistdb
        db.users.insert_one(user)
