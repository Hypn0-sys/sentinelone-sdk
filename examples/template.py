#!/usr/bin/env python
""" This template is here to give an example of initializing based on a
config.ini file. You can alternatively embed username, password and domain
in the code if you so wish. That will cut down your line count. """

__author__ = 'Jacolon Walker'
__email__ = 'jacolon.walker@collectivehealth.com'

import pprint
import sentinelone
from ConfigParser import SafeConfigParser

parser = SafeConfigParser()
parser.read('config.ini')

# Pull credentials from a config file
user = parser.get('creds', 'user')
passwd = parser.get('creds', 'passwd')
console = parser.get('endpoints', 'prod_domain')

# For debugging
pp = pprint.PrettyPrinter(indent=4)

# Init Client and Auth
client = sentinelone.SMgmt(user, passwd, console)
client.auth()
