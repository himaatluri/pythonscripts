"""
Script:
-------
Script to clean-up objects based on the size

Version:
--------
0.0.1

Author:
-------
Hima Atluri

Instructions:
-------------

Execution: python low_byte_cleanup.py <bucket-name>

Permissions required for the execution role
s3:ListObjects
s3:DeleteObjects
"""
import boto3

# vars
BUCKTNAME="himaops-athena-dev"
OBJECTSIZE=0

# Clients
s3 = boto3.client('s3')

ObjectsList = []

paginator = s3.get_paginator('list_objects_v2')
page_iterator = paginator.paginate(Bucket=BUCKTNAME)

for page in page_iterator:
    ObjectsResponse=page['Contents']
    for k in ObjectsResponse:
        """
        The `k` object looks like this:
        {'Key': '24/testfile.txt', 'LastModified':
        datetime.datetime(2021, 1, 6, 22, 43, 2, tzinfo=tzutc()), 
        'ETag': '"d41d8cd98f00b204e9800998ecf8427e"', 'Size': 0,
        'StorageClass': 'STANDARD'}
        We try to extract the `Size` attribute and then compare to the 
        required size and make a list out of it
        """
        if k['Size'] == OBJECTSIZE:
            ObjectsList.append(k['Key'])
        else:
            pass

print(ObjectsList)