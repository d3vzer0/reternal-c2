from workers.empire.api import Empire
from marshmallow import fields


class Listeners:
    def __init__(self, endpoint='listeners'):
          self._endpoint = endpoint

    def get(self):
        return Empire(self._endpoint).get()

    def create(self, listener_type, data):
        self._endpoint += f'/{listener_type}'
        return Empire(self._endpoint).post(data)

    def options(self, listener_id):
        self._endpoint += f'/options/{listener_id}'
        return Empire(self._endpoint).get()


class Listener:
    def __init__(self, listener_id, endpoint='listeners'):
          self._path = f'{endpoint}/{listener_id}'

    def get(self):
        return Empire(f'{self._path}').get()

    def change(self, data):
        return Empire(f'{self._path}').post(data)

    def delete(self):
        return Empire(f'{self._path}').delete()
