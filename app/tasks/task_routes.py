celery_routes = {
    'agent.*': {
        'queue': 'agent'
    },
    'api.*': {
        'queue':'api'
    }
}