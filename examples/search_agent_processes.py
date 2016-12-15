#!/usr/bin/env python
__author__ = 'Jacolon Walker'
__email__ = 'jacolon.walker@collectivehealth.com'

import pprint
from sentinel_core import *

pp = pprint.PrettyPrinter(indent=4)

auth_token = login(req_auth=AUTH)

# replace 'system' with something you are search for
target_agent = search_agents(headers=auth_token, query="system")
# Store agent id for process searc
for item in target_agent.json():
    agent_id = item['id']

    results = agent_process_list(headers=auth_token, agent_id=agent_id)
    pp.pprint(results.json())
