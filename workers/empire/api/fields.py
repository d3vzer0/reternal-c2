from workers.empire import Stagers, Listeners
from marshmallow import fields

class Fields:
    def to_field(self, attribute):
        dest_type = { 'str': 'String', 'int': 'Integer', 'float': 'Float' }
        source_type = type(attribute['Value']).__name__
        field_object = { 'required': attribute['Required'], 'default': attribute['Value'],
            'description': attribute['Description'] }
        return field_object

    def listeners(self, listener_type):
        get_options = Listeners().options(listener_type)
        field_options = { listener: self.to_field(attribute) for listener, attribute in get_options['listeneroptions'].items()}      
        return field_options

    def stagers(self):
        stagers = { 'Windows': { }, 'macOS': { }, 'Linux': { } }
        mapping = { 'windows': 'Windows', 'osx': 'macOS',
                'multi': 'Linux' }

        for stager in Stagers().get()['stagers']:
            platform = stager['Name'].split('/')[0]
            stager_options = { option: self.to_field(attributes)
                for option, attributes in stager['options'].items()}
            stagers[mapping[platform]][stager['Name']] = stager_options
        stagers['macOS'].update(stagers['Linux'])
        return stagers