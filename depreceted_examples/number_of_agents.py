#!/usr/bin/env python
__author__ = 'Jacolon Walker'
__email__ = 'jacolon.walker@collectivehealth.com'

import sentinelone


# Init
client = sentinelone.SMgmt()
client.auth()

results = client.agents_count()

count = results['count']

print("There are %s registered endpoints" %(count))
