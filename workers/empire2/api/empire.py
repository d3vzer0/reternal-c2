from workers.environment import config
from workers.main import rediscache
from workers.empire2.api import empirelog
from workers.empire2.api.get_token import get_token
import requests
import functools

# Empire does not return JSON when an error occurs
# overwrite default response when status is not 200

def check_response(func):
    ''' Generic wrapper to catch Empire API failures '''
    @functools.wraps(func)
    def wrapper_check_response(*args, **kwargs):
        response_object = func(*args, **kwargs)
        if response_object.status_code == 200:
            result = {'response': response_object.json(), 'status': 200 }
        else:
            result = {'status': response_object.status_code,
                'response': {'message': response_object.text} }
        return result
    return wrapper_check_response

# Generic EMPIRE API class
class Empire:
    def __init__(self, endpoint, base_url=config['EMPIRE_PATH']):
        self.base_url = base_url
        self.endpoint = endpoint

        # Check redis if token exists else initiate login
        token = rediscache.get('cache-empiretoken')
        self.token = token if token else get_token()

    @check_response
    def get(self):
        ''' Get object via Empire API '''
        url = f'{self.base_url}{self.endpoint}'
        get_object = requests.get(url, verify=False, params={'token':self.token})
        return get_object

    @check_response
    def post(self, data=None):
        ''' Create od mofidy object via Empire API '''
        url = f'{self.base_url}{self.endpoint}'
        set_object = requests.post(url, json=data, verify=False, params={'token':self.token})
        return set_object

    @check_response
    def delete(self):
        ''' Delete object via Empire API '''
        url = f'{self.base_url}{self.endpoint}'
        delete_object = requests.delete(url, verify=False, params={'token':self.token})
        return delete_object