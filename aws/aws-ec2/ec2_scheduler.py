import boto3
import json

ec2 = boto3.client('ec2')


def start_instance():
    start = ec2.describe_instances()
    #print start.InstanceId()
    jsonout=json.dumps(start, indent=4, sort_keys=True, default=str)
    response=json.loads(jsonout)
    #jsonout = json.dumps(start, indent=4, cls=awspice.ClsEncoder)
    print response
    print response['Reservations'][0]['Instances'][0]['InstanceId']

start_instance()    
