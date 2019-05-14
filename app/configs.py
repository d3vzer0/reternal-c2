from app import app
import os

app.config['SECRET_KEY'] = os.getenv('C2_SECRET', None)
app.config['C2_PORT'] = int(os.getenv('C2_PORT', 9000))
app.config['CELERY_BACKEND'] = os.getenv('CELERY_BACKEND', 'redis://localhost:6379')
app.config['CELERY_BROKER'] = os.getenv('CELERY_BROKER', 'redis://localhost:6379')
app.config['C2_ENDPOINT'] = os.getenv('C2_ENDPOINT', '/api/v1/ping')