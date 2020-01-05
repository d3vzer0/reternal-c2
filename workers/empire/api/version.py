from workers.empire.api import Empire

class Version:
    def __init__(self, endpoint='version'):
        self._endpoint = endpoint

    def get(self):
        return Empire(self._endpoint).get()
  