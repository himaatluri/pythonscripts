import os
import sys
import boto3

# create the clients
ssm = boto3.client('ssm')

# Inputs
file_path=sys.argv[1]

# funtion to update the given parameter:
def update_parameter_value(PARAMETER_NAME, INPUT_VALUE, KMS_KEY_ID):
    resp=ssm.put_parameter(
        Name=PARAMETER_NAME,
        Value=INPUT_VALUE,
        KeyId=KMS_KEY_ID,
        Type='SecureString',
        Overwrite=True
    )

    if resp['Version']:
        status_of_update="SUCCESS"
    else:
        status_of_update="FAILED"

    return status_of_update

# Read the list of the parameters from the file given
file=open(file_path, "r")
list_of_params=file.read()

# input the parameters new value
for i in list_of_params:
    print(i)