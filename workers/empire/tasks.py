from workers.empire import Listener, Listeners, Agents, ListenerFields
from workers.empire.schema import AgentSchema, ListenerSchema, ListenersSchema
from workers.utils.fields import SchemaFields
from workers import app


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
    listener_options = SchemaFields(ListenerSchema(), True).get()
    return listener_options

@app.task(name='c2.agents.empire2.get')
def get_agents():
    agents = Agents().get()
    validate_agents = AgentSchema().load(agents['agents'], many=True)
    return validate_agents

