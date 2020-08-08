from workers.empire2.api.empire import Empire
from workers.empire2.schema import AgentSchema
from workers.empire2 import Fields
from workers import app

@app.task(name='c2.agents.empire2.get')
def get_agents(agent_id: str = None):
    ''' Get active agents from Empire '''
    http_response = Empire(f'agent/{agent_id}').get() if agent_id else Empire('agents').get()
    if http_response['status'] == 200:
        http_response['response'] = AgentSchema().load(http_response['response']['agents'], many=True)
    return http_response

@app.task(name='c2.agents.empire2.stop')
def get_agents(agent_id: str = None):
    ''' Stop active agent '''
    http_response = Empire(f'agents/{agent_id}/kill').get()
    return http_response

@app.task(name='c2.agents.empire2.delete')
def get_agents(agent_id: str = None):
    ''' Stop active agent '''
    http_response = Empire(f'agents/{agent_id}').delete()
    return http_response

