from celery import Celery
from flask import Flask
from flask_restful import Api, Resource
from app.tasks.task_celery import FlaskCelery

#Initialize Flask Instance
app = Flask(__name__)
api = Api(app)

# Initialize DB and load models and views
from  app.configs import *
celery = FlaskCelery(app).make()

# Import views
from app import api_pulse
