from workers.empire.api.empire import Empire
from workers.empire.api.fields import Fields
from workers.empire.schema import RunModuleIn
from workers.empire import Fields
from workers import app

def parse_modules(module):
    ''' Reformat empire modules '''
    mapping = { 'python': ['macOS', 'Linux'], 'powershell':['Windows'] }
    modules = {'description': module['Description'],
        'operating_system': mapping[module.get('Language', 'powershell').lower()],
        'options': {option: Fields(attribute).to_string() for option,
        attribute in module['options'].items()}}
    return modules

@app.task(name='c2.modules.empire2.get')
def get_modules() -> dict:
    ''' Get available Empire modules '''
    http_response = Empire('modules').get()
    if http_response['status'] == 200:
        http_response['response'] = {module['Name']: parse_modules(module)
        for module in http_response['response']['modules']}
    return http_response

@app.task(name='c2.modules.empire2.run')
def run_module(input_data: RunModuleIn) -> dict:
    ''' Run an Empire modules or shell command'''
    http_response = Empire(f'modules/{input_data["module"]}').post({'Agent': input_data['agent'],
        **input_data['input']}) if input_data['module'] != 'exec_shell' else \
        Empire(f'agents/{input_data["agent"]}/shell').post(input_data['input'])
    if http_response['status'] == 200:
        http_response['response'] = {'external_id': str(http_response['response']['taskID'])}
    return http_response
