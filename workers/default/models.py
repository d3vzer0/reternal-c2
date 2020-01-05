from marshmallow import Schema, fields

class RequestSchema(Schema):
    beacon_id = fields.Str(required=True)
    username = fields.Str(required=True)
    hostname = fields.Str(required=True)
    platform = fields.Str(required=True, choices=('windows', 'darwin', 'linux'))
    data = fields.Dict(required=True)
    timer = fields.Int(required=True)
    working_dir = fields.Str(required=True)

class ResultSchema(Schema):
    beacon_id = fields.Str(required=True)
    task_id = fields.Str(required=True)
    command = fields.Str(required=True)
    input = fields.Str(required=True)
    type = fields.Str(required=True)
    output = fields.Str(required=True)
    