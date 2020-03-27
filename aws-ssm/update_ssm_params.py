import os
import sys
import boto3

# Instructions #
# Execution: python update_ssm_params.py parameters_list.txt
# line(43) KMS_KEY_ID: hard code the kms key-id that you use to encrypt all the paramters
# 
# Permissions required for you
# kms:Decrypt
# ssm:PutParameter

# create the clients
ssm = boto3.client('ssm')

# Inputs, file name in which you have the paramter paths in the list
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
for path in list_of_params.split('\n'):
    INPUT_VALUE = input("Enter the new password for the parameter "+path+": \n")
    KMS_KEY_ID = ""
    update_parameter_value(path, INPUT_VALUE, KMS_KEY_ID)
