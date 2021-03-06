from workers.empire3.api.empire import Empire
from workers.empire3.schema import AgentSchema
from workers.empire3 import Fields
from workers import app

@app.task(name='c2.agents.empire3.get')
def get_agents(agent_id: str = None):
    ''' Get active agents from Empire '''
    http_response = Empire(f'agent/{agent_id}').get() if agent_id else Empire('agents').get()
    print(http_response)
    if http_response['status'] == 200:
        http_response['response'] = AgentSchema().load(http_response['response']['agents'], many=True)
    return http_response

