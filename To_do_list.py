import streamlit as st
from pymongo import MongoClient
from bson.objectid import ObjectId
import datetime

print(pymongo.version)

database = 'test'
cluster = f"mongodb+srv://{username}:{passworwd}@cluster0.bhf5gnj.mongodb.net/{database}?retryWrites=true&w=majority"
client = MongoClient(cluster)

db = client
print(db)


# todo = {
#     "name": "Helena",
#     "text": "My first todo!",
#     "status": "open",
#     "tags": ["python", "coding"],
#     "date": datetime.datetime.utcnow()
# }

# todo2 = {
#     "name": "Patrick",
#     "text": "My Second todo!",
#     "status": "open",
#     "tags": ["python", "coding", "learning"],
#     "date": datetime.datetime.utcnow()
# }

# todos_list = [todo, todo2]

# todos = db.todos

# insert_one = todos.insert_one(todo)
# insert_many = todos.insert_many(todos_list)

# return_one = todos.find_one({"tags": "coding", "_id": ObjectId('6597f55ad938326df85c24d4')})
# return_all = todos.find({"tags": "coding"})
# for result in return_all:
#     print(result)

# print(todos.count_documents("name": "Patrick"))

# remove_one = todos.delete_one({"_id": ObjectId('6597f55ad938326df85c24d4')})
# remove_many = todos.delete_many([{"_id": ObjectId('6597f55ad938326df85c24d4')}])


# update_one = todos.update_one({"tags": "coding"}, {"$set": {"status": "done"}})
# update_many = todos.update_many({"tags": "coding"}, {"$set": {"status": "doing"}})