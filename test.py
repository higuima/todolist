from app.utils.getDatabase import DatabaseConnection
from datetime import datetime

connection = DatabaseConnection()
client = connection.init_connection()
todo = [{
            "name": "Helena",
            "text": 'task 1',
            "status": "Done",
            "tags": 'tags',
            "creation_date": datetime.strftime(datetime.now(),"%Y-%m-%d"),
            "end_date": datetime.strftime(datetime.date('2023-01-20'),"%Y-%m-%d")
            },
        {
            "name": "Helena",
            "text": 'task 2',
            "status": "To Do",
            "tags": 'tags',
            "creation_date": datetime.strftime(datetime.now(),"%Y-%m-%d"),
            "end_date": datetime.strftime(datetime.date('2023-01-20'),"%Y-%m-%d")
            },
        {
            "name": "Helena",
            "text": 'task 3',
            "status": "Doing",
            "tags": 'tags',
            "creation_date": datetime.strftime(datetime.now(),"%Y-%m-%d"),
            "end_date": datetime.strftime(datetime.date('2023-01-20'),"%Y-%m-%d")
            },
        {
            "name": "Helena",
            "text": 'task 4',
            "status": "Doing",
            "tags": 'tags',
            "creation_date": datetime.strftime(datetime.now(),"%Y-%m-%d"),
            "end_date": datetime.strftime(datetime.date('2023-01-20'),"%Y-%m-%d")
            },
]
        
connection.insert_many_todos(todo)