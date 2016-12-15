#!/usr/bin/env python
""" Core python SDK for SentinelOne Platform """
__author__ = 'Jacolon Walker'
__email__ = 'jacolon.walker@collectivehealth.com'
__version__ = 'v0.1'
__mo_song__ = 'https://www.youtube.com/watch?v=kCWZ-qKzjyQ'
__my_quote__ = 'Give back what you can and dont be afraid to try'
# SDK Built from SentinelOne's 1.8 API
# Bugs: Self generated API tokens are broken via SentinelOne's UI
# one must use inspect / dev mode if you want to grab that token
# via network resources

# pylint: disable=C0103

# The basic
from ConfigParser import SafeConfigParser
import requests

# Lets use the defined configuration from config.ini
parser = SafeConfigParser()
parser.read('config.ini')

# Assigning variables from config.ini to code global variables
DOMAIN = parser.get('endpoints', 'prod_domain')
USER = parser.get('creds', 'user')
PASSWD = parser.get('creds', 'passwd')

# Used for SentinelOne Auth
AUTH = {
    'username': USER,
    'password': PASSWD,
}

HEADER = None


def login(base_url=DOMAIN, req_auth=None):
    """ Authenticate to S1 and retrieve short lived operational token """

    ep_api = "/users/login"
    url = base_url + ep_api

    r = requests.post(url, json=req_auth)

    API_TOKEN = r.json()['token']

    HEADER = {
        'Authorization': 'Token %s' %(API_TOKEN)
    }

    return HEADER


def list_activites(base_url=DOMAIN, headers=None):
    """ Get a list of activities from SentinelOne """

    ep_api = "/activites"
    url = base_url + ep_api

    r = requests.get(url, headers=headers)

    return r


def search_agents(base_url=DOMAIN, headers=None, query=""):
    """ Get a list of agents from SentinelOne. Optional fields refer
    to SentinelOne's  API documentation """

    ep_api = "/agents?query=%s" %(query)
    url = base_url + ep_api

    r = requests.get(url, headers=headers)

    return r


def decomm_agent(base_url=DOMAIN, headers=None, query=""):
    """ Decommission agent by id"""

    ep_api = "/agents/%s/decommission" %(query)
    url = base_url + ep_api

    r = requests.get(url, headers=headers)

    return r


def get_agent(base_url=DOMAIN, headers=None, query=""):
    """ Get agent by agent_id """

    ep_api = "/agents/%s" %(query)
    url = base_url + ep_api

    r = requests.get(url, headers=headers)

    return r


def agent_process_list(base_url=DOMAIN, headers=None, agent_id=None):
    """ List the processes of an agent """

    ep_api = "/agents/%s/processes" %(agent_id)
    url = base_url + ep_api

    r = requests.get(url, headers=headers)

    return r


def disconnect_agent(base_url=DOMAIN, headers=None, query=""):
    """ Disconnect or Quarantine agent from the network """

    ep_api = "/agents/%s/disconnect" %(query)
    url = base_url + ep_api

    r = requests.get(url, headers=headers)

    return r


def agent_recomm(base_url=DOMAIN, headers=None, query=""):
    """ Recommission SentinelOne agent """

    ep_api = "/agents/%s/recommission" %(query)
    url = base_url + ep_api

    r = requests.get(url, headers=headers)

    return r


def shutdown_agent(base_url=DOMAIN, headers=None, query=""):
    """ Shutdown SentinelOne agent (system) """

    ep_api = "/agents/%s/shutdown" %(query)
    url = base_url + ep_api

    r = requests.get(url, headers=headers)

    return r


def connect_agent(base_url=DOMAIN, headers=None, query=""):
    """ Reconnect SentinelOne agent. (UnQuarantine agent from network) """

    ep_api = "/agents/%s/connect" %(query)
    url = base_url + ep_api

    r = requests.get(url, headers=headers)

    return r


def uninstall_agent(base_url=DOMAIN, headers=None, query=""):
    """ Uninstall SentinelOne from system """

    ep_api = "/agents/%s/uninstall" %(query)
    url = base_url + ep_api

    r = requests.post(url, headers=headers)

    return r


def message_agent(base_url=DOMAIN, headers=None, msg="", query=""):
    """ Broadcast a message to specified SentinelOne agent """

    ep_api = "/agents/broadcast?query=%s" %(query)
    url = base_url + ep_api
    message = {"message": msg}

    r = requests.post(url, json=message, headers=headers)

    return r


def count_agents(base_url=DOMAIN, headers=None):
    """ Count of agents registered to SentinelOne. There are query parameters
    but not clear in SentinelOne API docs how the request is formatted """

    ep_api = "/agents/count"
    url = base_url + ep_api

    r = requests.get(url, headers=headers)

    return r


def fetch_agent_logs(base_url=DOMAIN, headers=None, query=""):
    """ Fetch agent logs """

    ep_api = "/agents/fetch-logs?query=%s" %(query)
    url = base_url + ep_api

    r = requests.post(url, headers=headers)

    return r


def upgrade_agent(base_url=DOMAIN, headers=None, query=""):
    """ Currently 404: Upgrade agent(s) to newest release """

    ep_api = "/agents/upgrade?query=%s" %(query)
    url = base_url + ep_api

    r = requests.post(url, headers=headers)

    return r


def list_applications(base_url=DOMAIN, headers=None):
    """ TBD: SentinelOne has this API endpoint in beta with no docs"""

    ep_api = "/applications"
    url = base_url + ep_api

    r = requests.get(url, headers=headers)

    return r


def create_filter(base_url=DOMAIN, headers=None, body=None):
    """ TBD: Create a filter for easily searchable agents """

    ep_api = "/filters"
    url = base_url + ep_api

    payload = body

    r = requests.post(url, json=payload, headers=headers)

    return r


def delete_filter(base_url=DOMAIN, headers=None, fid=""):
    """ Delete filter by filter_id"""

    ep_api = "/filters/%s" %(fid)
    url = base_url + ep_api

    r = requests.delete(url, headers=headers)

    return r


def get_filter(base_url=DOMAIN, headers=None, fid=""):
    """ Get filter by filter_id """
    ep_api = "/filters/%s" %(fid)
    url = base_url + ep_api

    r = requests.get(url, headers=headers)

    return r


def list_filters(base_url=DOMAIN, headers=None):
    """ List active filters """

    ep_api = "/filters"
    url = base_url + ep_api

    r = requests.get(url, headers=headers)

    return r


def update_filter(base_url=DOMAIN, headers=None, fid="", query=None):
    """ Update existing filters """

    ep_api = "/filters/%s" %(fid)
    url = base_url + ep_api

    payload = query

    r = requests.put(url, json=payload, headers=headers)

    return r


def get_groups(base_url=DOMAIN, headers=None):
    """ Get Groups """

    ep_api = "/groups"
    url = base_url + ep_api

    r = requests.get(url, headers=headers)

    return r


def create_groups(base_url=DOMAIN, headers=None, group=None):
    """ Create group """

    ep_api = "/groups"
    url = base_url + ep_api

    payload = group

    r = requests.post(url, json=payload, headers=headers)

    return r


def update_group(base_url=DOMAIN, headers=None, group=""):
    """ Update existing group by group_id """

    ep_api = "/groups/%s" %(group['group_id'])
    url = base_url + ep_api
    # Accept modified changes to group
    payload = group

    r = requests.put(url, json=payload, headers=headers)

    return r


def delete_group(base_url=DOMAIN, headers=None, query=""):
    """ Delete an exsiting group. Systems in this group will default back
    to the Default group """

    ep_api = "/groups/%s" %(query)
    url = base_url + ep_api

    r = requests.delete(url, headers=headers)

    return r


def blacklist_hash(base_url=DOMAIN, headers=None, ioc=None):
    """ Blacklist a item by hash md5, sha1, sha256 supported? """

    ep_api = "/hashes"
    url = base_url + ep_api

    payload = ioc

    r = requests.post(url, json=payload, headers=headers)

    return r


def delete_hash(base_url=DOMAIN, headers=None, hash_id=""):
    """ Remove a blacklisted hash from SentinelOne """

    ep_api = "/hashes/%s" %(hash_id)
    url = base_url + ep_api

    r = requests.delete(url, headers=headers)

    return r


def list_hashes(base_url=DOMAIN, headers=None, query=""):
    """ Get the list of known (seen) hashes Refer to SentinelOne API Guide for
    fields """

    ep_api = "/hashes?%s" %(query)
    url = base_url + ep_api

    r = requests.get(url, headers=headers)

    return r


def update_hash(base_url=DOMAIN, headers=None, query=""):
    """ Update hash """

    ep_api = "/hashes/%s" %(query['hash'])
    url = base_url + ep_api

    payload = {
        'os_family': query['os_family'],
        'is_black': query['is_black'],
        'description': query['description']
    }

    r = requests.get(url, json=payload, headers=headers)

    return r


def list_policies(base_url=DOMAIN, headers=None):
    """ List Policies """

    ep_api = "/policies"
    url = base_url + ep_api

    r = requests.get(url, headers=headers)

    return r


def create_policy(base_url=DOMAIN, headers=None, body=None):
    """ Create policy for new groups """

    ep_api = "/policies"
    url = base_url + ep_api

    payload = body

    r = requests.post(url, json=payload, headers=headers)

    return r


def update_policy(base_url=DOMAIN, headers=None, pol_id="", body=None):
    """ Update existing policy by policy_id """

    ep_api = "/policies/%s" %(pol_id)
    url = base_url + ep_api

    payload = body

    r = requests.put(url, json=payload, headers=headers)

    return r


def delete_policy(base_url=DOMAIN, headers=None, pol_id=""):
    """ Delete an existing policy """

    ep_api = "/policies/%s" %(pol_id)
    url = base_url + ep_api

    r = requests.delete(url, headers=headers)

    return r


def list_threats(base_url=DOMAIN, headers=None, query=""):
    """ List threats reported to SentinelOne console
    Refer to SentinelOne API Guide for fields """

    ep_api = "/threats?%s" %(query)
    url = base_url + ep_api

    r = requests.get(url, headers=headers)

    return r


def threats_summary(base_url=DOMAIN, headers=None):
    """ Output a summary of current threats in the system grouped by mitigation
    level """

    ep_api = "/threats/summary"
    url = base_url + ep_api

    r = requests.get(url, headers=headers)

    return r


def mark_threat_id(base_url=DOMAIN, headers=None, threat_id=""):
    """ TBD: Beta mark suspicious threat via by threat_id as threat """

    ep_api = "/threats/%s/mark-as-threat" %(threat_id)
    url = base_url + ep_api

    r = requests.get(url, headers=headers)

    return r


def mitigate_threat(base_url=DOMAIN, headers=None, action=None):
    """ Mitigate probably threat.

    Actions allowed for "action" parameter:
    "kill", "quaratine", "un-quarantine", "remediate", "rollback-remediation"
    """

    ep_api = "/threats/%s/mitgate/%s" %(action['threat_id'], action['action'])
    url = base_url + ep_api

    r = requests.post(url, headers=headers)

    return r


def resolve_threat(base_url=DOMAIN, headers=None, action=None):
    """ Resolved existing threats after they have been mitifated or
    investigated """

    ep_api = "/threats/%s/resolve" %(action['threat_id'])
    url = base_url + ep_api

    r = requests.post(url, headers=headers)

    return r


def mark_indicator(base_url=DOMAIN, headers=None, query=""):
    """ Mark threats based on other indicators. Refer to SentinelOne API Guide
    for fields """

    ep_api = "/threats/mark-as-threat?%s" %(query)
    url = base_url + ep_api

    r = requests.post(url, headers=headers)

    return r


def mitigate_indicator(base_url=DOMAIN, headers=None, action="", query=""):
    """ Mitigate threats based on other indicators. Refer to SentinelOne API
    Guide for fields. Actions allowed for "action" parameter:
    "kill", "quaratine", "un-quarantine", "remediate", "rollback-remediation"
    """

    ep_api = "/threats/mitigate/%s?%s" %(action, query)
    url = base_url + ep_api

    r = requests.post(url, headers=headers)

    return r


def resolve_indicators(base_url=DOMAIN, headers=None, query=""):
    """ Resolve threats based on advanced query parameters. Refer to
    SentinelOne API Guide for fields """

    ep_api = "/threats/resolve?%s" %(query)
    url = base_url + ep_api

    r = requests.post(url, headers=headers)

    return r
