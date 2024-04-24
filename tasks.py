from celery import Celery
from pymongo import MongoClient

app = Celery('tasks', broker='redis://redis:6379/0')
app.config_from_object('celery_config')

@app.task
def store_last_login(username):
    try:
        client = MongoClient('mongodb://db:27017/')
        db = client['scaffolding']
        collection = db['login_history']
        collection.insert_one({"username": username})
    except Exception as e:
        print(f"Error storing last login: {str(e)}")
