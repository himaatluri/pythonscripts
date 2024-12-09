"""
Script:
-------
Script to clean-up objects in s3 based on the size

Version:
--------
0.0.1 - Cleanup for s3

Future:
-------
* Add exception handling
* Cleanup feature for Versioning enabled buckets

Author:
-------
Hima Atluri

Instructions:
-------------

For Help:
python3 low_byte_cleanup.py -h

Execution:
python3 low_byte_cleanup.py --bucket-name "mybucket"

Permissions required for the execution role
s3:ListObjects
s3:DeleteObjects
"""
import boto3
import argparse

parser = argparse.ArgumentParser(
    prog="low-byte-s3-cleanup",
    description="Script to clean up dummy 0 Byte Objects"
)

# BucketName Argument
parser.add_argument(
    "--bucket-name",
    type=str,
    help="Provide the bucket name that you want to cleanup",
    required=True
)

# BucketName Argument
parser.add_argument(
    "--object-size",
    type=int,
    default=0,
    help="Provide the object size that you want to cleanup",
    required=False
)

args = parser.parse_args()
# vars
BUCKTNAME=args.bucket_name
OBJECTSIZE=args.object_size

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
        {
            'Key': '24/testfile.txt', 
            'LastModified': datetime.datetime(2021, 1, 6, 22, 43, 2, tzinfo=tzutc()), 
            'ETag': '"redacted-ddd-ahasdlhjkkjfffffffff"', 
            'Size': 0,
            'StorageClass': 'STANDARD'
        }
        We extract the `Size` attribute and then compare to the 
        required size and make a list out of it
        """
        if k['Size'] == OBJECTSIZE:
            ObjectsList.append(k['Key'])
        else:
            pass

def delete_selected_objects():
    DelteObjectsList = []
    """
    Function to delte given objects list
    """
    for obj in ObjectsList:
        DelteObjectsList.append(dict(Key=obj))

    response=s3.delete_objects(
        Bucket=BUCKTNAME,
        Delete={
            'Objects': DelteObjectsList
        }
    )
    return response

if ObjectsList != []:
    print("Objects with the requested size: ", OBJECTSIZE)
    for i in ObjectsList:
        print("Object Name: ", i)
    ConfirmationPrompt=input("Enter 'yes' to delete or 'no' to skip: \n")
    if ConfirmationPrompt == "yes":
        print("Deleting the objects.. ")
        delete_selected_objects()
    else:
        print("Skipping the Delete operation..\
        \nNo Objects were deleted..")
else:
=======
"""
Script:
-------
Script to clean-up objects in s3 based on the size

Version:
--------
0.0.1 - Cleanup for s3

Future:
-------
* Add exception handling
* Cleanup feature for Versioning enabled buckets

Author:
-------
Hima Atluri

Instructions:
-------------

For Help:
python3 low_byte_cleanup.py -h

Execution:
python3 low_byte_cleanup.py --bucket-name "mybucket"

Permissions required for the execution role
s3:ListObjects
s3:DeleteObjects
"""
import boto3
import argparse

parser = argparse.ArgumentParser(
    prog="low-byte-s3-cleanup",
    description="Script to clean up dummy 0 Byte Objects"
)

# BucketName Argument
parser.add_argument(
    "--bucket-name",
    type=str,
    help="Provide the bucket name that you want to cleanup",
    required=True
)

# BucketName Argument
parser.add_argument(
    "--object-size",
    type=int,
    default=0,
    help="Provide the object size that you want to cleanup",
    required=False
)

args = parser.parse_args()
# vars
BUCKTNAME=args.bucket_name
OBJECTSIZE=args.object_size

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
        {
            'Key': '24/testfile.txt', 
            'LastModified': datetime.datetime(2021, 1, 6, 22, 43, 2, tzinfo=tzutc()), 
            'ETag': '"redacted-ddd-ahasdlhjkkjfffffffff"', 
            'Size': 0,
            'StorageClass': 'STANDARD'
        }
        We extract the `Size` attribute and then compare to the 
        required size and make a list out of it
        """
        if k['Size'] == OBJECTSIZE:
            ObjectsList.append(k['Key'])
        else:
            pass

def delete_selected_objects():
    DelteObjectsList = []
    """
    Function to delte given objects list
    """
    for obj in ObjectsList:
        DelteObjectsList.append(dict(Key=obj))

    response=s3.delete_objects(
        Bucket=BUCKTNAME,
        Delete={
            'Objects': DelteObjectsList
        }
    )
    return response

if ObjectsList != []:
    print("Objects with the requested size: ", OBJECTSIZE)
    for i in ObjectsList:
        print("Object Name: ", i)
    ConfirmationPrompt=input("Enter 'yes' to delete or 'no' to skip: \n")
    if ConfirmationPrompt == "yes":
        print("Deleting the objects.. ")
        delete_selected_objects()
    else:
        print("Skipping the Delete operation..\
        \nNo Objects were deleted..")
else:
    print("No Objects are found with the provided size. Size: ", OBJECTSIZE)