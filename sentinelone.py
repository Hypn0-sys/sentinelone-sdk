#!/usr/bin/env python
""" Core python SDK for SentinelOne Platform """
__author__ = 'Jacolon Walker'
__email__ = 'jacolon.walker@collectivehealth.com'
__version__ = 'v1.0'
__forked__ = 'Hypn0sys'
# SDK Built from SentinelOne's 1.8 API

# pylint: disable=C0103
# pylint: disable=R0913
# pylint: disable=E1121

# The basic imports
from configparser import SafeConfigParser
import requests

class SMgmt(object):
    """ Core functions based on SentinelOne's API Docs
    https://your-subdomain.sentinelone.net/apidoc """

    def __init__(self):
        """ Defining the basic for API interaction """

        # Assigning variables from config.ini to code global variables
        self.domain = None
        self.token = None

    def auth(self):
        """ Authentication to SentinelOne Management Console """

        parser = SafeConfigParser()
        parser.read('config.ini')
        self.token = parser.get('creds', 'apitoken')
        self.domain = parser.get('endpoints', 'prod_domain')

        self.header = {
            'Authorization': 'ApiToken %s' %(self.token),
            'Content-Type': 'application/json',
            }


    def get(self, endpoint):
        """ HTTP GET method because it will be used often """

        r = requests.get(self.domain + endpoint, headers=self.header)
        resp = r.json()

        return resp


    def post(self, endpoint):
        """ HTTP POST method because it will be used often """

        r = requests.post(self.domain + endpoint, headers=self.header)
        resp = r.json()

        return resp


    def post_body(self, endpoint, body):
        """ HTTP POST method with BODY """

        r = requests.post(
            self.domain + endpoint,
            json=body,
            headers=self.header)
        resp = r.json()

        return resp


    def put_body(self, endpoint, body):
        """ HTTP PUT method with BODY """

        r = requests.post(
            self.domain + endpoint,
            json=body,
            headers=self.header)
        resp = r.json()

        return resp


    def delete(self, endpoint):
        """ HTTP DELETE method """

        r = requests.delete(self.domain + endpoint, headers=self.header)
        if isinstance(r, dict):
            resp = r.json()
        else:
            resp = r.text

        return resp


    def ad_list(self, query=None):
        """ Active_Directory - List """

        # Bug: {u'status': 400, u'message': u'Host/Port can not be empty',
        # u'error': u'BadRequest'}
        endpoint = '/active-directory?query=%s' %(query)
        results = self.get(endpoint)

        return results


    def activities_list(self):
        """ Activities - List """

        endpoint = '/activities/types'
        results = self.get(endpoint)

        return results


    def agents_apps(self, app_name=None):
        """ Agent - Applications List By Name """

        endpoint = '/agents/applications?name=%s' %(app_name)
        results = self.get(endpoint)

        return results


    def apps_by_agent_id(self, agent_id=None):
        """ Agent - Applications """

        endpoint = '/agents/%s/applications' %(agent_id)
        results = self.get(endpoint)

        return results


    def agents_count_by_filter(self, query=None):
        """ Count by filters: uri: /apidoc/#api-Agent-AgentsCountByFilter """

        if query != None:
            endpoint = '/agents/count-by-filters?%s' %(query)
            results = self.get(endpoint)

            return results
        else:
            endpoint = '/agents/count-by-filters'
            results = self.get(endpoint)

            return results


    def agents_count(self, query=None):
        """ Get counts of agents, supports filters
        uri: /apidoc/#api-Agent-CountAgents """

        if query != None:
            endpoint = '/agents/count?%s' %(query)
            results = self.get(endpoint)
        else:
            endpoint = '/agents/count'
            results = self.get(endpoint)

        return results


    def decom_agent(self, agent_id=None):
        """ Decommission agent """

        endpoint = '/agents/%s/decommission' %(agent_id)
        results = self.post(endpoint)

        return results


    def disconnect_agent(self, agent_id=None):
        """ This will disconnect the agent from the network. Think isolation
        """

        endpoint = '/agents/%s/disconnect' %(agent_id)
        results = self.post(endpoint)

        return results


    def agent_info(self, agent_id=None):
        """ Get agent information by agent_id """

        endpoint = '/agents/%s' %(agent_id)
        results = self.get(endpoint)

        return results


    def agents_search(self, query=None):
        """ List and search agents by filters
        uri: /apidoc/#api-Agent-ListAgents """

        if query != None:
            endpoint = '/agents?query=%s' %(query)
            results = self.get(endpoint)

            return results
        else:
            endpoint = '/agents'
            results = self.get(endpoint)

            return results


    def agent_pslist(self, agent_id=None):
        """ Print agent process list by agent_id """

        endpoint = '/agents/%s/processes' %(agent_id)
        results = self.get(endpoint)

        return results


    def recom_agent(self, agent_id=None):
        """ Recommissions agent by agent id. Should return HTTP 204 """

        endpoint = '/agents/%s/recommission' %(agent_id)
        results = self.post(endpoint)

        return results


    def reconnect_agent(self, agent_id=None):
        """ Reconnects an agent back to the network by agent_id"""

        endpoint = '/agents/%s/connect' %(agent_id)
        results = self.post(endpoint)

        return results


    def shutdown_agent(self, agent_id=None):
        """ Shutdown agent. This actually shutdowns the system """

        endpoint = '/agents/%s/shutdown' %(agent_id)
        results = self.post(endpoint)

        return results


    def uninstall_agent(self, agent_id=None):
        """ Uninstall SentinelOne Agent from host """

        endpoint = '/agents/%s/uninstall' %(agent_id)
        results = self.post(endpoint)

        return results

    # The below methods are Agent actions across the fleet
    # USE WITH CAUTION
    # https://your-subdomain.sentinelone.net/apidoc/#api-Agents_Actions
    def broadcast_msg(self, msg=None, query=None):
        """ Broadcast message to agents.
        uri: /apidoc/#api-Agents_Actions-BroadcastAgents """

        message = {
            'message': msg,
            }

        if query != None:
            endpoint = '/agents/broadcast?%s' %(query)
            r = requests.post(
                self.domain + endpoint,
                json=message,
                headers=self.header)
            resp = r.json()

            return resp
        else:
            endpoint = '/agents/broadcast'
            r = requests.post(
                self.domain + endpoint,
                json=message,
                headers=self.header)
            resp = r.json()

            return resp


    def agents_connect(self, query=None):
        """ Agents_Actions - Connect To Network
        uri: /apidoc/#api-Agents_Actions-UnQuarantine """

        if query != None:
            endpoint = '/agents/connect?%s' %(query)
            results = self.post(endpoint)

            return results
        else:
            endpoint = '/agents/connect'
            results = self.get(endpoint)

            return results


    def agents_decomm(self, query=None):
        """ Agents_Actions - Decommission
        uri: /apidoc/#api-Agents_Actions-DecommissionAgents """

        if query != None:
            endpoint = '/agents/decommission?%s' %(query)
            results = self.post(endpoint)

            return results
        else:
            endpoint = '/agents/decomission'
            results = self.get(endpoint)

            return results


    def agents_disconn(self, query=None):
        """ Agents_Actions - Disconnect From Network
        uri: /apidoc/#api-Agents_Actions-Quarantine """

        if query != None:
            endpoint = '/agents/disconnect?%s' %(query)
            results = self.post(endpoint)

            return results
        else:
            endpoint = '/agents/disconnect'
            results = self.post(endpoint)

            return results


    def fetch_logs(self, query=None):
        """ Fetch system and agent logs
        uri: /apidoc/#api-Agents_Actions-FetchLogsAgents """

        if query != None:
            endpoint = '/agents/fetch-logs?query=%s' %(query)
            results = self.post(endpoint)

            return results
        else:
            endpoint = '/agents/fetch-logs'
            results = self.post(endpoint)

            return results


    def agents_shutdown(self, query=None):
        """ Agents_Actions - Shutdown
        uri: /apidoc/#api-Agents_Actions-ShutdownAgents """

        if query != None:
            endpoint = '/agents/shutdown?%s' %(query)
            results = self.post(endpoint)

            return results
        else:
            endpoint = '/agents/shutdown'
            results = self.post(endpoint)

            return results


    def agents_uninstall(self, query=None):
        """ Agents_Actions - Uninstall
        uri: /apidoc/#api-Agents_Actions-UninstallAgents """

        if query != None:
            endpoint = '/agents/uninstall?%s' %(query)
            results = self.post(endpoint)

            return results
        else:
            endpoint = '/agents/uninstall'
            results = self.post(endpoint)

            return results


    def agents_upgrade(self, recent=bool, pkg_name=None, os=None, query=None):
        """ Agents_Actions - Upgrade agents software uri:
        /apidoc/#api-Agents_Actions-Upgrade recent, pkg_name and os are
        required """

        upgrade = {
            'use_recent': recent,
            'package_name': pkg_name,
            'os_type': os,
            }

        if query != None:
            endpoint = '/agents/update-software?%s' %(query)
            results = self.post_body(endpoint, upgrade)

            return results
        else:
            endpoint = '/agents/update-software'
            results = self.post_body(endpoint, upgrade)

            return results


    # Exclusion APIs
    # https://your-subdomain.sentinelone.net/apidoc/#api-Exclusion
    def exclusion_list(self):
        """ Exclusion List """
        endpoint = '/exclusion-lists'
        results = self.get(endpoint)

        return results


    def exclude_list_by_id(self, list_id=None):
        """ GET exclusion list by id """
        endpoint = '/exclusion-lists/%s' %(list_id)
        results = self.get(endpoint)

        return results


    def del_exclude_by_list_id(self, list_id=None):
        """ Delete exclusion list by id """

        endpoint = '/exclusion-lists/%s' %(list_id)
        results = self.delete(endpoint)

        return results


    def create_exclusion_list(self, list_name=None):
        """ Creates an exclusion list name """

        body = {
            'name': list_name,
            }

        endpoint = '/exclusion-lists'
        results = self.post_body(endpoint, body)

        return results


    def update_exclusion_list(self, list_id=None, list_name=None):
        """ Updates an already existing list
        BUG: SentinelOne API doesn't allow for PUT. Conflicts with there API
        docs. uri: /apidoc/#api-Exclusion_List-ListExclusionList"""

        body = {
            'name': list_name,
            }

        endpoint = '/exclusion-lists/%s' %(list_id)
        results = self.put_body(endpoint, body)

        return results


    def create_exclusion_item(
            self,
            list_id=None,
            folder_path=None,
            desc=None,
            os=None,
            inject=bool,
            exclude_type=None):
        """ Creates an object to exclude e.g. files, folders, subfolders
        uri: /apidoc/#api-Exclusions """

        body = {
            'folder_path': folder_path,
            'description': desc,
            'os_family': os,
            'inject': inject,
            'exclusion_type': exclude_type,
            }

        endpoint = '/exclusion-lists/%s/folders' %(list_id)
        results = self.post_body(endpoint, body)

        return results


    def delete_folders(self, list_ids=None):
        """ Deletes Exclusion folders by list IDs. Exclusions folders is the
        Name of your exclusion with a group of whitelisted items. Separate IDs
        by commas e.g 59225184346a1634c2c5505b,59225184346a1634c2c12345 """

        endpoint = '/folders?id__in=%s' %(list_ids)
        results = self.delete(endpoint)

        return results


    def get_exclusion_items(self, list_id=None, folder_id=None):
        """ Gets the contents of the exclusion items """

        endpoint = '/exclusion-lists/%s/folders/%s' %(list_id, folder_id)
        results = self.get(endpoint)

        return results


    def update_exclusion_items(
            self,
            list_id=None,
            folder_id=None,
            folder_path=None,
            desc=None,
            os=None,
            inject=None,
            exclude_type=None):
        """ Update the exclusion list contents """

        body = {
            'folder_path': folder_path,
            'description': desc,
            'os_family': os,
            'inject': inject,
            'exclusion_type': exclude_type,
        }

        endpoint = '/exclusion-lists/%s/folders/%s' %(list_id, folder_id)
        results = self.put_body(endpoint, body)

        return results

    # Hash API
    # https://your-subdomain.sentinelone.net/apidoc/#api-Hash
    def post_hash(self, ioc=None, os=None, is_black=bool, desc=None):
        """ POST SHA1 HASH of Indicator of Compromise (IOC) """

        body = {
            'description': desc,
            'os_family': os,
            'is_black': is_black,
            'hash': ioc,
        }

        endpoint = '/hashes'
        results = self.post_body(endpoint, body)

        return results


    def delete_hash(self, ioc=None):
        """ Delete an existing hash in the Black/White listed hashes. This
        should return HTTP 204 if successful """

        endpoint = '/hashes/%s' %(ioc)
        results = self.delete(endpoint)

        return results


    def hash_rep(self, hash_id=None):
        """ Retrieves HASH reputation using hash id """

        endpoint = '/hashes/%s/reputation' %(hash_id)
        results = self.get(endpoint)

        return results


    def get_hash(self, hash_id=None):
        """ Get HASH SentinelOne meta information """

        endpoint = '/hashes/%s' %(hash_id)
        results = self.get(endpoint)

        return results


    def list_hashes(self, query=None):
        """ List of submitted hashes stored on SentinelOne Management Console
        """

        if query != None:
            endpoint = '/hashes/%s' %(query)
            results = self.get(endpoint)
        else:
            endpoint = '/hashes'
            results = self.get(endpoint)

        return results


    def update_hash(self, ioc=None, os=None, is_black=bool, desc=None):
        """ Update existing hashes. BUG: API docs says it supports PUT but
        returns { u'message': u'The method is not allowed for the requested
        URL.'} """

        body = {
            'description': desc,
            'os_family': os,
            'is_black': is_black,
        }

        endpoint = '/hashes/%s' %(ioc)
        results = self.put_body(endpoint, body)

        return results


    # System Status API
    # https://your-subdomain.sentinelone.net/apidoc/#api-Info
    def system_status(self):
        """ Retrieve system status """

        endpoint = '/status'
        results = self.get(endpoint)

        return results


    def system_ver(self):
        """ Retrieve system version """

        endpoint = '/info'
        results = self.get(endpoint)

        return results


    # Policy API
    # https://your-subdomain.sentinelone.net/apidoc/#api-Policy
    def list_policies(self):
        """ Retrieves the list of policies """

        endpoint = '/policies'
        results = self.get(endpoint)

        return results


    def create_policy(
            self,
            name=None,
            cloud_val=bool,
            auto_mitigate=None,
            network_quaratine=bool,
            auto_immune=bool,
            auto_decomm=bool,
            decomm_days=int,
            research=bool,
            show_suspect=bool):
        """ Create a new policy """

        body = {
            'name': name,
            'cloud_validation_on': cloud_val,
            'auto_mitigation_action': auto_mitigate,
            'network_quarantine_on': network_quaratine,
            'auto_immune_on': auto_immune,
            'auto_decommission_on': auto_decomm,
            'auto_decommission_days': decomm_days,
            'research_on': research,
            'show_suspicious_on': show_suspect,
        }

        endpoint = '/policies'
        results = self.post_body(endpoint, body)

        return results


    def get_policy(self, policy_id=None):
        """ Get information about a policy """

        endpoint = '/policies/%s' %(policy_id)
        results = self.get(endpoint)

        return results


    def update_policy(
            self,
            policy_id=None,
            name=None,
            cloud_val=bool,
            auto_mitigate=None,
            network_quaratine=bool,
            auto_immune=bool,
            auto_decomm=bool,
            decomm_days=int,
            research=bool,
            show_suspect=bool):
        """ Update an exisiting policy. BUG: 'The method is not allowed for the
        requested URL.'"""

        body = {
            'name': name,
            'cloud_validation_on': cloud_val,
            'auto_mitigation_action': auto_mitigate,
            'network_quarantine_on': network_quaratine,
            'auto_immune_on': auto_immune,
            'auto_decommission_on': auto_decomm,
            'auto_decommission_days': decomm_days,
            'research_on': research,
            'show_suspicious_on': show_suspect,
        }

        endpoint = '/policies/%s' %(policy_id)
        results = self.put_body(endpoint, body)

        return results


    def delete_policy(self, policy_id=None):
        """ Delete a policy by policy by id """

        endpoint = '/policies/%s' %(policy_id)
        results = self.delete(endpoint)

        return results


    # Reports API
    # https://your-subdomain.sentinelone.net/apidoc/#api-Reports
    def schedule_report(
            self,
            report_name=None,
            types=list,
            attach_type=list,
            recp=list,
            is_manual=bool,
            days_period=int,
            repeat_day=int):
        """ Create a scheduled report """

        body = {
            'report_name': report_name,
            'types': types,
            'attachment_types': attach_type,
            'recipients': recp,
            'is_manual': is_manual,
            'days_period': days_period,
            'repeat_day': repeat_day,
        }

        endpoint = '/report-tasks'
        results = self.post_body(endpoint, body)

        return results


    def generate_report(
            self,
            report_name=None,
            types=list,
            attach_type=list,
            recp=list,
            is_manual=bool,
            days_period=int,
            repeat_day=int,
            fdate=int,
            tdate=int):
        """ Create a one time report """

        body = {
            'report_name': report_name,
            'types': types,
            'attachment_types': attach_type,
            'recipients': recp,
            'is_manual': is_manual,
            'days_period': days_period,
            'repeat_day': repeat_day,
            'from_date': fdate,
            'to_date': tdate,
        }

        endpoint = '/report-tasks'
        results = self.post_body(endpoint, body)

        return results


    def list_reports(self):
        """ List scheduled reports """

        endpoint = '/report-tasks'
        results = self.get(endpoint)

        return results


    def get_report(self, report_id=None):
        """ Get report by report id """

        endpoint = '/report-tasks/%s' %(report_id)
        results = self.get(endpoint)

        return results


    def download_report(self, report_id=None, report_type=None):
        """ Download report by report id. Type: pdf or html """

        endpoint = '/reports/%s/%s' %(report_id, report_type)
        r = requests.get(self.domain + endpoint, headers=self.header)
        results = r.text

        return results


    def delete_report(self, report_id=None):
        """ Delete report by report id """

        endpoint = '/report-tasks/%s' %(report_id)
        results = self.delete(endpoint)

        return results


    # System Configuration API
    # https://your-subdomain.sentinelone.net/apidoc/#api-System_Configuration
    def syslog_setup(self, host=None, port=int, ssl=bool, syslog_format=None):
        """ Setup Syslog: Syslog format: ioc, cef, or stix """

        body = {
            'host': host,
            'port': port,
            'ssl': ssl,
            'syslog_format': syslog_format,
        }

        endpoint = '/settings/active-directory/test'
        results = self.post_body(endpoint, body)

        return results


    def get_ad_settings(self):
        """ Get Active Directory settings """

        endpoint = '/settings/active-directory'
        results = self.get(endpoint)

        return results


    def get_server_settings(self):
        """ Get server settings """

        endpoint = '/server-settings'
        results = self.get(endpoint)

        return results


    def get_syslog(self):
        """ Get syslog settings """

        endpoint = '/settings/syslog'
        results = self.get(endpoint)

        return results


    def test_ad(
            self,
            host=None,
            port=int,
            user=None,
            passwd=None,
            ssl=bool,
            root_dn=None,
            req_cert=bool,
            cert=None):
        """ Test the AD server """

        body = {
            'host': host,
            'port': port,
            'username': user,
            'password': passwd,
            'ssl': ssl,
            'root_dn': root_dn,
            'require_cert': req_cert,
            'cert': cert,
        }

        endpoint = '/settings/active-directory/test'
        results = self.post_body(endpoint, body)

        return results


    def test_smtp(
            self,
            host=None,
            port=int,
            user=None,
            passwd=None,
            no_reply=None,
            ssl=bool,
            tls=bool):
        """ Testing SMTP """

        body = {
            'host': host,
            'port': port,
            'username': user,
            'password': passwd,
            'no_reply_email': no_reply,
            'ssl': ssl,
            'tls': tls,
        }

        endpoint = '/settings/smtp/test'
        results = self.post_body(endpoint, body)

        return results


    def update_ad(
            self,
            host=None,
            port=int,
            user=None,
            passwd=None,
            root_dn=None,
            ssl=bool,
            req_cert=bool,
            cert=None,
            enabled=bool):
        """ Update AD settings """

        body = {
            'host': host,
            'port': port,
            'username': user,
            'password': passwd,
            'root_dn': root_dn,
            'ssl': ssl,
            'require_cert': req_cert,
            'cert': cert,
            'enabled': enabled,
        }

        endpoint = '/settings/active-directory'
        results = self.put_body(endpoint, body)

        return results


    def sys_update(self, cloud_intel=bool, global_mfa=bool, remember_me=int):
        """ Update global configuration around clout intelligence, two factor
        login and remember me length for logins """

        body = {
            'cloud_intelligence_on': cloud_intel,
            'global_two_fa_enabled': global_mfa,
            'remember_me_length': remember_me,
        }

        endpoint = '/settings/agents/mode/options'
        results = self.put_body(endpoint, body)

        return results


    def list_threats(self, query=None):
        """ List threats without parameters default """

        if query != None:
            endpoint = '/threats?%s' %(query)
            results = self.get(endpoint)
        else:
            endpoint = '/threats'
            results = self.get(endpoint)

        return results


    def threat_sum(self):
        """ Output a summary of current threats in the system grouped by
        mitigation level. """

        endpoint = '/threats/summary'
        results = self.get(endpoint)

        return results


    def get_threat(self, threat_id):
        """ Get threat by threat id """

        endpoint = '/threats/%s' %(threat_id)
        results = self.get(endpoint)

        return results


    def mark_threat_benign(self, threat_id=None):
        """ Mark Threat as benign """

        endpoint = '/threats/%s/mark-as-benign' %(threat_id)
        results = self.post(endpoint)

        return results


    def mark_as_threat(self, threat_id=None):
        """ Mark as threat """

        endpoint = '/threats/%s/mark-as-threat' %(threat_id)
        results = self.post(endpoint)

        return results


    def mitigate_threat(self, threat_id=None, action=None):
        """ Mitigate threat by threat id with actions. Allowed values: "kill",
        "quarantine", "un-quarantine", "remediate", "rollback-remediation" """

        endpoint = '/threats/%s/mitigate/%s' %(threat_id, action)
        results = self.post(endpoint)

        return results


    def resolve_threat(self, threat_id=None):
        """ Resolve threat by threat id """

        endpoint = '/threats/%s/resolve' %(threat_id)
        results = self.post(endpoint)

        return results


    # Global threats action
    def mark_threats_benign(self, query=None):
        """ Mark Multiple threats as benign """

        if query != None:
            endpoint = '/threats/mark-as-benign?%s' %(query)
            results = self.post(endpoint)
        else:
            results = 'Specify a parameter'

        return results


    def mark_as_threats(self, query=None):
        """ Mark multiple IOCs as threats """

        if query != None:
            endpoint = '/threats/mark-as-threat?%s' %(query)
            results = self.post(endpoint)
        else:
            results = 'Specify a parameter'

        return results


    def mitigate_threats(self, action=None, query=None):
        """ Mitigate multiple threats. Allowed values: "kill", "quarantine",
        "remediate", "rollback-remediation" """

        endpoint = '/threats/mitigate/%s?%s' %(action, query)
        results = self.post(endpoint)

        return results


    def resolve_threats(self, query=None):
        """ Resolve multiple threats """

        if query != None:
            endpoint = '/threats/resolve?%s' %(query)
            results = self.post(endpoint)
        else:
            results = 'Specify a parameter'

        return results


    # USER API
    # https://your-subdomain.sentinelone.net/apidoc/#api-User
    def change_password(
            self,
            user_id=None,
            cur_passwd=None,
            new_passwd=None,
            confirm_passwd=None):
        """ Change a user password """

        body = {
            'current_password': cur_passwd,
            'new_password': new_passwd,
            'confirm_new_password': confirm_passwd,
        }

        endpoint = '/users/%s/change-password' %(user_id)
        results = self.post(endpoint, body)

        return results


    def create_user(
            self,
            user=None,
            name=None,
            email=None,
            passwd=None,
            groups=list):
        """ Create a user """

        body = {
            'username': user,
            'full_name': name,
            'email': email,
            'password': passwd,
            'groups': groups,
        }

        endpoint = '/users'
        results = self.post(endpoint, body)

        return results


    def delete_user(self, user_id=None):
        """ Delete user by user id """

        endpoint = '/users/%s' %(user_id)
        results = self.delete(endpoint)

        return results


    def api_token_info(self, user_id=None):
        """ Get information about a user's generated API token. """

        endpoint = '/users/%s/api-token-details' %(user_id)
        results = self.get(endpoint)
        return results


    def user_info(self, user_id=None):
        """ Get information about a SentinelOne management user """

        endpoint = '/users/%s' %(user_id)
        results = self.get(endpoint)

        return results


    def list_users(self):
        """ List users registered in the SentinelOne Management console """

        endpoint = '/users'
        results = self.get(endpoint)

        return results


    def revoke_api_token(self, user_id=None):
        """ Revoke a user's api token by user id """

        endpoint = '/users/%s/revoke-api-token'%(user_id)
        results = self.post(endpoint)

        return results


    def update_user(self, user_id=None, name=None, email=None, groups=None):
        """ Update user """

        body = {
            'full_name': name,
            'email': email,
            'groups': groups,
        }

        endpoint = '/users/%s' %(user_id)
        results = self.put_body(endpoint, body)

        return results
