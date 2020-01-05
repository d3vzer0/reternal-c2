from workers.empire.api import Empire

class Agents:
    def __init__(self, endpoint='agents'):
        self._endpoint = endpoint

    def get(self):
        return Empire(self._endpoint).get()

class Agent:
    def __init__(self, agent_id, endpoint='agent'):
        self._path = f'{endpoint}/{agent_id}'

    def get(self):
        return Empire(f'{self._path}').get()

    def change(self, data):
        return Empire(f'{self._path}').post(data)

    def delete(self):
        return Empire(f'{self._path}').delete()
