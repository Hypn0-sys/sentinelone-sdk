#!/usr/bin/env python
__author__ = 'Jacolon Walker'
__email__ = 'jacolon.walker@collectivehealth.com'
__forked__ = 'Hypn0sys'

import sentinelone


# Init
client = sentinelone.SMgmt()
client.auth()

results = client.agents_count()

count = results['data']['total']

print("There are %s registered endpoints" %(count))
