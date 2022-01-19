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

# Eicar and a unknown variant
iocs = [
    'cff14e5536e86e086b12a2271d7b15c29aa1d2ae',
    '3395856ce81f2b7382dee72602f798b642f14140',
    '506db7cc75304c29459061ebf9d1d3305aa5b798',
]

# Blacklist hashes
def block_ioc(iocs):
    for item in iocs:
        print("Blocking IOC: %s" %(item))

        ops = client.post_hash(
                ioc=item,
                os='windows',
                is_black=True,
                desc='Eicar Test and assoicated bad DLL'
                )

        hash_id = ops['id']
        delete_ioc(hash_id)


# Remove hashes from SentinelOne
def delete_ioc(hash_id):
    print("Deleting IOC by hash: %s" %(hash_id))
    ops = client.delete_hash(ioc=hash_id)


block_ioc(iocs)
