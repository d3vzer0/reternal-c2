from workers.empire.api.empire import Empire
from workers.empire.schema import ListenersSchema
from workers.empire import Fields
from workers import app

listeners = {
    'http': 'Starts a http[s] listener (PowerShell or Python) that uses a GET/POST approach.',
    'meterpreter': 'Starts a foreign http[s] Meterpreter listener.',
    'redirector': 'Internal redirector listener. Active agent required. Listener options will be copied from another existing agent. Requires the active agent to be in an elevated context.'
}

def parse_options(listener_type) -> dict:
    ''' Get available listeners and the available parameters '''
    get_options = Empire(f'listeners/options/{listener_type}').get()
    print(get_options)
    field_options = { listener: Fields(attribute).to_string() for listener, attribute in get_options['response']['listeneroptions'].items()}      
    return field_options

@app.task(name='c2.listeners.empire3.delete')
def delete_listener(listener_name: str) -> dict:
    ''' Disable active listener '''
    delete_listener = Empire(f'listeners/{listener_name}').delete()
    return delete_listener

@app.task(name='c2.listeners.empire3.create')
def create_listener(listener_type: str, data: str) -> dict:
    ''' Enable Empire listener '''
    create_listener = Empire(f'listeners/{listener_type}').post(data)
    return create_listener

@app.task(name='c2.listeners.empire3.get')
def get_listeners(listener_id: str = None) -> dict:
    ''' Configuration of selected (active) listener '''
    listener_state =  Empire(f'listeners/{listener_id}').get() if listener_id else Empire('listeners').get()
    if listener_state['status'] == 200:
        listener_state['response'] = ListenersSchema().dump(listener_state['response']['listeners'], many=True)
    return listener_state

@app.task(name='c2.listeners.empire3.options')
def get_listener_options() -> dict:
    ''' Get available listeners and the available parameters '''
    all_listeners = {listener: {'description': description, 'options': parse_options(listener)}
        for listener, description in listeners.items()}
    return {'code': 200, 'response': all_listeners }
