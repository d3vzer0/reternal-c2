from workers.covenant.api import Covenant
from workers import app


@app.task(name='c2.payloads.covenant')
def get_payloads():
    url = f'{config['base_url']}launchers'
    request = request.get(url, headers={''})
    print(jewat)
