from workers.empire import Listener, Listeners, Agents, Fields
from workers.empire.schema import AgentSchema, ListenersSchema
from workers.utils.fields import SchemaFields
from workers import app

listeners = {
    'http': 'Starts a http[s] listener (PowerShell or Python) that uses a GET/POST approach.',
    'meterpreter': 'Starts a foreign http[s] Meterpreter listener.',
    'redirector': 'Internal redirector listener. Active agent required. Listener options will be copied from another existing agent. Requires the active agent to be in an elevated context.'
}

@app.task(name='c2.stagers.empire2.get')
def get_stagers():
    get_stagers = Fields().stagers()
    return get_stagers

@app.task(name='c2.listeners.empire2.delete')
def delete_listener(listener_name):
    delete_listener = Listener(listener_name).delete()
    return delete_listener

@app.task(name='c2.listeners.empire2.create')
def create_listener(listener_type, data):
    create_listener = Listeners().create(listener_type, data)
    return create_listener

@app.task(name='c2.listeners.empire2.get')
def get_listeners(listener_id=None):
    listener_state = Listener(listener_id).get() if listener_id else Listeners().get()
    format_listeners = ListenersSchema().dump(listener_state['listeners'], many=True)
    return format_listeners

@app.task(name='c2.listeners.empire2.options')
def get_listener_options():
    all_listeners = {listener: {'description': description, 'options': Fields().listeners(listener)}
        for listener, description in listeners.items()}
    return all_listeners

@app.task(name='c2.agents.empire2.get')
def get_agents():
    agents = Agents().get()
    validate_agents = AgentSchema().load(agents['agents'], many=True)
    return validate_agents

