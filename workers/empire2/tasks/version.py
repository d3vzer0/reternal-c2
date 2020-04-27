from workers.empire2.api.empire import Empire
from workers import app

@app.task(name='c2.version.empire2.get')
def delete_listener() -> dict:
    ''' Get running empire version '''
    get_version = Empire('version').get()
    return get_version
