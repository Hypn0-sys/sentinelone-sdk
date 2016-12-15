#!/usr/bin/env python
__author__ = 'Jacolon Walker'
__email__ = 'jacolon.walker@collectivehealth.com'

import pprint
from sentinel_core import *

pp = pprint.PrettyPrinter(indent=4)

auth_token = login(req_auth=AUTH)

# replace 'system' with something you are searching for
target_agent = fetch_agent_logs(headers=auth_token, query="system")

pp.pprint(target_agent.json())
