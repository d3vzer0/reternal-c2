from workers.empire.api.empire import Empire
from workers.empire import Fields
from workers import app

mapping = { 'windows': 'Windows', 'osx': 'macOS', 'multi': 'Linux' }

def parse_stagers(all_stagers: list) -> dict:
    ''' Reformat the stager format '''
    stagers = { 'Windows': { }, 'macOS': { }, 'Linux': { } }
    for stager in all_stagers:
        platform = stager['Name'].split('/')[0]
        stager_options = { option: Fields(attributes).to_string()
            for option, attributes in stager['options'].items()}
    
        stagers[mapping[platform]][stager['Name']] = {'description': stager['Description'],
            'options':stager_options }

    stagers['macOS'].update(stagers['Linux'])
    return stagers

@app.task(name='c2.stagers.empire2.get')
def get_stagers() -> dict:
    ''' Get available stagers from Empire '''
    http_response = Empire('stagers').get()
    if http_response['status'] == 200:
        http_response['response'] = parse_stagers(http_response['response']['stagers'])
    return http_response

@app.task(name='c2.stagers.empire2.create')
def create_stager(data: dict) -> dict:
    ''' Create a specific stager '''
    http_response = Empire('stagers').post(data)
    if http_response['status'] == 200:
        http_response['response'] = {'type':'text',
            'content':http_response['response'][data['StagerName']]['Output']}
    return http_response
