from workers.empire.api import Empire
from marshmallow import fields

class Stagers:
    def __init__(self, endpoint='stagers'):
        self._endpoint = endpoint

    def get(self):
        return Empire(self._endpoint).get()

    def create(self, data):
        return Empire(self._endpoint).post(data)
