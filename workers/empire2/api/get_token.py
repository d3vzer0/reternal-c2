from workers.environment import config
from workers.main import rediscache
from workers.empire2.api import empirelog
import requests

def get_token():
    # Login to empire using user/pass
    login_empire = requests.post(f'{config["EMPIRE_PATH"]}admin/login',
        json={'username': config['EMPIRE_USERNAME'], 'password': config['EMPIRE_PASSWORD']},
        verify=False)

    # If login is succesfull get an API token
    if login_empire.status_code == 200:
        empire_token = login_empire.json()['token']
        rediscache.set('cache-empiretoken',
            ex=3600,
            value=empire_token
        )
        return empire_token
    else:
        empirelog.error('Invalid Empire credentials')
        return None