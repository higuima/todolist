from app.utils.getDatabase import DatabaseConnection
from datetime import datetime

connection = DatabaseConnection()
client = connection.init_connection()
todo = {
            "name": "Helena",
            "text": 'task',
            "status": "To Do",
            "tags": 'tags',
            "creation_date": datetime.strftime(datetime.now(),"%Y-%m-%d"),
            "end_date": datetime.strftime(datetime.now(),"%Y-%m-%d")
            }
        
connection.insert_todo(todo)