from workers.empire.api import Empire
from marshmallow import fields

class ListenerFields:
    def __init__(self, listener_type=None):
        self.listener_type = listener_type

    def to_field(self, attribute):
        dest_type = { 'str': fields.String, 'int': fields.Int, 'float': fields.Float }
        source_type = type(attribute['Value']).__name__
        field_object = dest_type[source_type](required=attribute['Required'],
                default=attribute['Value'], description=attribute['Description'])
        return field_object

    def create(self):
        get_options = Listeners().options(self.listener_type)
        field_options = { listener: self.to_field(attribute) for listener, attribute in get_options['listeneroptions'].items()}      
        return field_options

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
