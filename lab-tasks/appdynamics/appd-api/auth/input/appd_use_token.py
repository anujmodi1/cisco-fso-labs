#!/usr/bin/env python
import json, re, sys, os, json, subprocess, time, logging, requests, urllib3
from subprocess import call, check_output
from requests.structures import CaseInsensitiveDict
urllib3.disable_warnings()

#import the env vars and logon to vault to get the secret and then use it to run this command and write the output to the vault
APPD_OATH_TOKEN = os.getenv('APPD_OATH_TOKEN')
STR_APPD_OATH_TOKEN=str(APPD_OATH_TOKEN)

#get the appd oath bearer token from the vault
#May run into a problem if everyone is usin the secret from the same account - fsolab4 and resetting the token every time.
#Ensure to set up pipeline or task so that for each branch - it will write to that branch example concourse/cisco-fso-labs/us-east-2a-appd secret=

#import from the env var or call the vault command using subprocess - lots of ways to skin this cat.
#has to logon to vault first.

url="https://cisco-apipartnertraininglab.saas.appdynamics.com/zero/v1beta/install/agentVersions?latest=true"

payload={}
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Authorization': 'Bearer ' + STR_APPD_OATH_TOKEN
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
print(response.json)





