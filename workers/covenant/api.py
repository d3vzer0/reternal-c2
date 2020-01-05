import requests

class Covenant:
    def __init__(self, token, base_url='https://localhost:7443/api/'):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({'Authorization': f'Bearer {token}'})

    def payloads(self):
        url = f'{self.base_url}launchers'
        get_payloads = self.session.get(url, verify=False)
        return get_payloads.json()

