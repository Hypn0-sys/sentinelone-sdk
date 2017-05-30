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

# For debugging
pp = pprint.PrettyPrinter(indent=4)

# Init
client = sentinelone.SMgmt(user, passwd, console)
client.auth()

# replace 'hostname' with something you are searching for
results = client.agents_search("hostname")

pp.pprint(results)
