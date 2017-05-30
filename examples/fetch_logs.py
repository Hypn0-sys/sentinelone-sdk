#!/usr/bin/env python
__author__ = 'Jacolon Walker'
__email__ = 'jacolon.walker@collectivehealth.com'

import pprint
import sentinelone
from ConfigParser import SafeConfigParser

parser = SafeConfigParser()
parser.read('config.ini')

user = parser.get('creds', 'user')
passwd = parser.get('creds', 'passwd')
console = parser.get('endpoints', 'prod_domain')

pp = pprint.PrettyPrinter(indent=4)

# Init
client = sentinelone.SMgmt(user, passwd, console)
client.auth()

# Fetch logs from a system. Replace 'hostname' with a system of interest
logs = client.fetch_logs('hostname')
print "Results: https://your-subdomain.sentinelone.net/#/activity"
pp.pprint(logs)

