from workers import app
from yaml import Loader
import yaml

available_workers = []
with open('workers/config.yaml') as config_file:
    available_workers = yaml.load(config_file.read(), Loader=Loader)
    
@app.task(name='c2.system.workers')
def get_workers():
    return available_workers


@app.task(name='c2.system.state')
def get_states(worker_name):
    if not worker_name in available_workers: return { 'states':{ } }
    return available_workers


@app.task(name='c2.system.agents')
def get_agents(worker_name):
    if not worker_name in available_workers: return { 'get': None, 'set' :None }
    return {'get': available_workers[worker_name]['agents']['get'],
        'set': available_workers[worker_name]['agents']['set']}
 

@app.task(name='c2.system.listeners')
def get_listeners(worker_name):
    if not worker_name in available_workers: return { 'listeners': { } }
    get_listeners = app.send_task(available_workers[worker_name]['listeners']['get'])
    return get_listeners