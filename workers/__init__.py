from .main import app
from workers.environment import config

app.autodiscover_tasks([
    'workers.empire2',
    'workers.system'
])

app.conf.beat_schedule = {
    'check-running-scenarios': {
        'task': 'c2.system.scheduler',
        'schedule': config['CELERY_TIMER'],
    }
}