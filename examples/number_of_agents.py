#!/usr/bin/env python
__author__ = 'Jacolon Walker'
__email__ = 'jacolon.walker@collectivehealth.com'

from sentinel_core import *

auth_token = login(req_auth=AUTH)

results = count_agents(headers=auth_token)

count = results.json()['count']

print("There are %s registered endpoints" %(count))
