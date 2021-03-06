from workers.empire3.api.empire import Empire
from workers import app

@app.task(name='c2.version.empire3.get')
def delete_listener() -> dict:
    ''' Get running empire version '''
    get_version = Empire('version').get()
    return get_version
