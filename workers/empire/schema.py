from marshmallow import Schema, fields, INCLUDE, EXCLUDE, post_load, post_dump, pre_dump
from workers.empire import ListenerFields

class ListenerSchema(Schema):
    http = fields.Nested(ListenerFields('http').create(),
        description='Starts a http[s] listener (PowerShell or Python) that uses a GET/POST approach.')
    meterpeter = fields.Nested(ListenerFields('meterpreter').create(),
        description='Starts a foreign http[s] Meterpreter listener.')
    redirector = fields.Nested(ListenerFields('redirector').create(),
        description='Internal redirector listener. Active agent required. Listener options will be copied from another existing agent. Requires the active agent to be in an elevated context.')


class AgentSchema(Schema):
    class Meta:
        unknown = INCLUDE

    id = fields.Int(data_key='ID', required=True)
    last_checkin = fields.String(data_key='checkin_time', required=True)
    beacon_interval = fields.Int(data_key='delay', required=True)
    operating_system = fields.String(data_key='os_details', required=True)
    pid = fields.String(data_key='process_id', required=True)

    @post_load
    def extract_os(self, data, many, **kwargs):
        data['integration'] = 'empire2'
        data['operating_system'] = data['operating_system'].split(',')[0]
        return data


class ListenersSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    id = fields.Int(attribute='ID', required=True)
    listener_type = fields.String(attribute='module', required=True)
    name = fields.String(attribute='name', required=True)
    options = fields.Method("get_listener_options")
    integration = fields.String(default='empire2', dump_only=True)

    def get_listener_options(self, data):
        listener_options = {item: options['Value'] for item, options in data['options'].items()}
        return listener_options
