# Setting variables
from app import app
import os
import datetime

# Todo - set MongoDB username and Password as variables for DB
app.config['SECRET_KEY'] = os.environ["C2_SECRET"]
app.config['MONGODB_SETTINGS'] = {
    'db': os.environ["MONGO_DB"],
    'host': os.environ["MONGO_IP"],
    'port': int(os.environ["MONGO_PORT"])
}

