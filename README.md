## Synopsis

This repository contains what we have developed to be a core SDK for
[SentinelOne's](https://sentinelone.com/) API. This SDK has been developed
based on SentinelOne's 1.8 API documentation which was beta at the time of this
development. The SDK is backwards compatiable with their older API. The purpose
of this SDK should help IT administrators and security teams help automate
management of their Sentinelone fleet. Examples can range from policy creation,
rapid incident mitigation and escalation or auditing.

## Code Example

```
from sentinel_core import *
auth_token = login(req_auth=AUTH)
results = count_agents(headers=auth_token)
count = results.json()['count']
print("There are %s registered endpoints" %(count))
```

## Motivation

We created this SDK to help speed up the automation of incident response (IR)
while notification can be consumed through each step of the IR process. This
has also help alleviate some of the manual effort of remediation and reporting.

## Installation

Open config.ini.example and drop in the right creds and domain. Then rename the
config to config.ini. Once completed pip install the requirements.txt.
```
pip install -r requirements.txt
```
You are now ready to management your SentinelOne agents with 'ease'


## API Reference

The SentinelOne Web API documentation can be retrieve through their customer
support portal.

## Contributors

If you would like to get involved in contributing to this project, pull
requests will be a great start, along with following any possible issues that
might appear in the repository queue.

## License

self.note: licensing choices and a brief description (MIT, Apache, etc..)
