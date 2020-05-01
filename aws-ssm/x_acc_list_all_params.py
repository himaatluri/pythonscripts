import sys
import boto3

########
# Inputs
#########
# resource_name = sys.argv[1]
# environment = sys.argv[2]
ASSUME_ROLE_ARN = "The full arn of the role goes in here"

# assuming a role in a different account
# setting up sts client
sts = boto3.client('sts')
# assume role object
assumed_credentials = sts.assume_role(
    RoleArn=ASSUME_ROLE_ARN,
    RoleSessionName='boto3-list-ssm'
)

# setting up the destination accounts
# ssm client using the assumed_credentials
ssm = boto3.client(
    'ssm',
    aws_access_key_id=assumed_credentials['Credentials']['AccessKeyId'],
    aws_secret_access_key=assumed_credentials['Credentials']['SecretAccessKey'],
    aws_session_token=assumed_credentials['Credentials']['SessionToken'],
)

parameters_list = []
# a function to list all parameters
def list_all_parameters():
    """
    List the parameters that are in a given path

    E.g:

    If the parameters are saved in `/oracle`
    path, then the output will be:

    /oracle/dev/password
    /oracle/dev/username
    """
    response =  ssm.get_parameters_by_path(
        # inputs shouold be refernce here
        Path='/oracle',
        Recursive=True,
        # Make it true, all the params will
        # listed with thier values exposed
        WithDecryption=False
    )
    for i in response['Parameters']:
        parameters_list.append(i['Name'])
    
    return

if __name__ == "__main__":
    list_all_parameters()
    for i in parameters_list:
        print(i)
    pass
