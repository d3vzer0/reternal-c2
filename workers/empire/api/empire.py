import requests

class Empire:
    def __init__(self, endpoint, base_url='https://localhost:1337/api/'):
        self.base_url = base_url
        self.endpoint = endpoint
        self.token = config['token']

    def get(self):
        url = f'{self.base_url}{self.endpoint}'
        get_object = requests.get(url, verify=False, params={'token':self.token})
        return get_object.json()

    def post(self, data=None):
        url = f'{self.base_url}{self.endpoint}'
        set_object = requests.post(url, json=data, verify=False, params={'token':self.token})
        return set_object.json()

    def delete(self):
        url = f'{self.base_url}{self.endpoint}'
        delete_object = requests.delete(url, verify=False, params={'token':self.token})
        return delete_object.json()