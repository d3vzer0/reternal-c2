from celery import Celery
from workers.environment import config

app = Celery('c2', backend=config['CELERY_BACKEND'], broker=config['CELERY_BACKEND'])
app.autodiscover_tasks([
    'workers.empire',
    'workers.system'
])

app.conf.beat_schedule = {
    'check-running-scenarios': {
        'task': 'c2.system.scheduler',
        'schedule': config['CELERY_TIMER'],
    }
}