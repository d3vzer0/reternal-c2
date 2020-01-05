from celery import Celery

app = Celery('c2', backend='redis://localhost:6379', broker='redis://localhost:6379')
app.autodiscover_tasks([
    'workers.empire',
    'workers.system'
])
