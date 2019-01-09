# Import AWS Python SDK
import boto3
from botocore.client import Config

bucket_name = 'minio-test-bucket'
object_name = 'training-data.csv'

# Configure S3 Connection
s3 = boto3.resource('s3',  
  aws_access_key_id = 'access_key',                                                                                                                                              
  aws_secret_access_key = 'secret_key',                                                                                                                                       
  endpoint_url = 'http://localhost:9000',
  config=Config(signature_version='s3v4'))

# Configure GCP Connection
