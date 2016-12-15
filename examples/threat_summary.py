#!/usr/bin/env python
__author__ = 'Jacolon Walker'
__email__ = 'jacolon.walker@collectivehealth.com'

from sentinel_core import *

auth_token = login(req_auth=AUTH)

results = threats_summary(headers=auth_token)

active = results.json()['active']
mitigated = results.json()['mitigated']
suspect = results.json()['suspicious']
blocked = results.json()['blocked']

print("Active threats with out mitigation policies: %d" %(active))
print("Threats that have been mitigated and need resolving: %d" %(mitigated))
print("Suspicious threats: %d" %(suspect))
print("Blocked threats: %d" %(blocked))
