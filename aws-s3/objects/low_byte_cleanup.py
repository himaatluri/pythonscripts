import boto3

# vars
BUCKTNAME=""
OBJECTSIZE=""

# Clients
s3 = boto3.client('s3')

BucketName="himaops-athena-dev"
BucketContents = {}

def get_objects(BucketName):
    resp=s3.list_objects_v2(
        Bucket=BucketName
    )
    for k in resp['Contents']:
        obj = k['Key']
        BucketContents[BucketName] = obj

if __name__ == "__main__":
    print(BucketContents)
    pass