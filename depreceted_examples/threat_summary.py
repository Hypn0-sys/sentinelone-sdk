#!/usr/bin/env python
__author__ = 'Jacolon Walker'
__email__ = 'jacolon.walker@collectivehealth.com'

import sentinelone
from ConfigParser import SafeConfigParser

parser = SafeConfigParser()
parser.read('config.ini')

user = parser.get('creds', 'user')
passwd = parser.get('creds', 'passwd')
console = parser.get('endpoints', 'prod_domain')

# Init
client = sentinelone.SMgmt(user, passwd, console)
client.auth()

results = client.threat_sum()

active = results['active']
mitigated = results['mitigated']
suspect = results['suspicious']
blocked = results['blocked']

print("Active threats with out mitigation policies: %d" %(active))
print("Threats that have been mitigated and need resolving: %d" %(mitigated))
print("Suspicious threats: %d" %(suspect))
print("Blocked threats: %d" %(blocked))
