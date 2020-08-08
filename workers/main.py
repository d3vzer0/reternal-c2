from celery import Celery
from workers.environment import config
import os
import logging
import redis

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))
rediscache = redis.Redis.from_url(config['CELERY_BACKEND'])
app = Celery('c2', backend=config['CELERY_BACKEND'], broker=config['CELERY_BROKER'])
app.conf.task_routes = {
    'c2.*': { 'queue': 'c2' },
    'api.*': { 'queue': 'api' }    
}
