
/!\ This fork now use Python 3 !

## Synopsis

This repository contains what we have developed to be a core SDK for
[SentinelOne's](https://sentinelone.com/) API. This SDK has been developed
based on SentinelOne's 1.8 API documentation which was beta at the time of this
development. The SDK is backwards compatiable with their older API. The purpose
of this SDK should help IT administrators and security teams help automate
management of their Sentinelone fleet. Examples can range from policy creation,
rapid incident mitigation and escalation or auditing.

This repository is forked based to an original dev from 
__author__ = 'Jacolon Walker'
__email__ = 'jacolon.walker@collectivehealth.com'

/!\ This fork now use Python 3 !

## Motivation

We created this SDK to help speed up the automation of incident response (IR)
while notification can be consumed through each step of the IR process. This
has also help alleviate some of the manual effort of remediation and reporting.

## Installation

Open config.ini.example and drop in the API Token. Then rename the
config to config.ini. Once completed pip install the requirements.txt.
```
pip install -r requirements.txt
```
You are now ready to management your SentinelOne agents with 'ease'


## API Reference

The SentinelOne Web API documentation can be retrieve through their customer
support portal.

## Copyright, License & Disclaimers

Copyright 2017 Collective Health, Inc

This project is available under the Apache version 2.0 License. Please see LICENSE
file.
Apache version 2.0: https://www.apache.org/licenses/LICENSE-2.0.html
