import os, sys
import logging
import json
import boto3
from datetime import date, datetime

iam = boto3.client('iam')
User=sys.argv[1]

def _listMfa():
    response = iam.list_mfa_devices(
        UserName=User
    )
    return response

MFA_DEVICE_ARN = _listMfa()

print MFA_DEVICE_ARN['MFADevices']