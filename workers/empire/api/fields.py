# from workers.empire import Stagers, Listeners
# from workers.empire.api.modules import Modules
from marshmallow import fields

class Fields:
    def __init__(self, attribute):
        self.attribute = attribute

    def to_string(self):
        ''' Reformat Schema typing to strings '''
        #dest_type = { 'str': 'String', 'int': 'Integer', 'float': 'Float' }
        #source_type = type(attribute['Value']).__name__
        field_object = { 'required': self.attribute['Required'], 'default': self.attribute['Value'],
            'description': self.attribute['Description'] }
        return field_object
