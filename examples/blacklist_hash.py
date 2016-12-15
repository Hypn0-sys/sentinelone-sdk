#!/usr/bin/env python
__author__ = 'Jacolon Walker'
__email__ = 'jacolon.walker@collectivehealth.com'

from sentinel_core import *

auth_token = login(req_auth=AUTH)

iocs = [
    'cff14e5536e86e086b12a2271d7b15c29aa1d2ae',
    '3395856ce81f2b7382dee72602f798b642f14140',
    '506db7cc75304c29459061ebf9d1d3305aa5b798',
]

# Blacklist hashes
def block_ioc(iocs):
    for ioc in iocs:
        print("Blocking IOC: %s" %(ioc))
        payload = {
            'description': 'Eicar Test and assoicated bad DLL',
            'os_family': 'windows',
            'is_black': 'true',
            'hash': ioc,
        }
        ops = blacklist_hash(headers=auth_token, ioc=payload)

        results = ops.json()
        delete_ioc(results['id'])


# Remove hashes from SentinelOne
def delete_ioc(hash_id):
    print("Deleting IOC by hash: %s" %(hash_id))
    ops = delete_hash(headers=auth_token, hash_id=hash_id)

    print(ops.text)

block_ioc(iocs)
