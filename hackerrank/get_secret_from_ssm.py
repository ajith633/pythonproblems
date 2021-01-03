import boto3
import json
from botocore.exceptions import ClientError

session=boto3.session.Session()
client=session.client(service_name='secretsmanager', region_name='us-west-1')
try:
    secret_response=client.get_secret_value(SecretId='phani_secret')
    print(secret_response)
    secret=secret_response['SecretString']
    print(json.loads(secret))
except ClientError as e:
    print(e)



