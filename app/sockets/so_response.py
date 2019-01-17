from app import celery


class ResponseSocket:
    def __init__(self, task_id):
        self.task_id = task_id

    def respond(self, command, cmd_type, cmd_input, output, magic_type):
        if cmd_type == 'text/plain':
            result = {'task_id':self.task_id, 'command':command, 'data':output, 'magic':magic_type}
        else:
            result = {'task_id':self.task_id, 'command':command, 'magic':magic_type}
 
        print(result)
        send_result = celery.send_task('api.result', retry=True, args=(result,))
        print('sent re sult')
        return {'result':'success', 'data':str(send_result)}