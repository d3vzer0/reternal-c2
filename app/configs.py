# Setting variables
from app import app
import os
import datetime

# Todo - set MongoDB username and Password as variables for DB
app.config['SECRET_KEY'] = os.environ['C2_SECRET']
app.config['C2_PORT'] = os.environ['C2_PORT']
app.config['CELERY_BACKEND'] = os.environ['CELERY_BACKEND']
app.config['CELERY_BROKER'] = os.environ['CELERY_BROKER']
app.config['MONGODB_SETTINGS'] = {
    'db': os.environ['MONGO_DB'],
    'host': os.environ['MONGO_IP'],
    'port': int(os.environ['MONGO_PORT'])
}

