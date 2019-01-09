# Import AWS Python SDK
import boto3
from botocore.client import Config

bucket_name = 'minio-test-bucket' # Name of the mounted Qumulo folder
object_name = 'training-data.csv' # Name of the file you want to read inside your Qumulo folder

# Configure S3 Connection
s3 = boto3.resource('s3',  
  aws_access_key_id = 'YOUR-ACCESS-KEY-HERE',
  aws_secret_access_key = 'YOUR-SECRET-KEY-HERE',                                                                                                         
  endpoint_url = 'YOUR-SERVER-URL-HERE',
  config=Config(signature_version='s3v4'))

# List all buckets
for bucket in s3.buckets.all():
  print(bucket.name)

input('Press Enter to continue...\n')

# Read File
object = s3.Object(bucket_name, object_name)
body = object.get()['Body']
print(body.read())
print('File Read')
input('Press Enter to continue...\n')

# Stream File - Useful for Larger Files
object = s3.Object(bucket_name, object_name)
body = object.get()['Body']
with io.FileIO('/tmp/sample.txt', 'w') as tmp_file:
  while file.write(body.read(amt=512)):
    pass

print('File Streamed @ /tmp/sample.txt')
input('Press Enter to continue...\n')

# Write File
s3.Object(bucket_name, 'aws-write-test.txt').put(Body=open('./aws-write-test.txt', 'rb'))
print('File Written')
input('Press Enter to continue...\n')

# Delete File
s3.Object(bucket_name, 'aws_write_test.txt').delete()
print('File Deleted')
input('Press Enter to continue...\n')

# Stream Write File

# Create Bucket
s3.create_bucket(Bucket='new-bucket')
print('Bucket Created')
input('Press Enter to continue...\n')

# Delete Bucket
bucket_to_delete = s3.Bucket('new-bucket')
for key in bucket_to_delete.objects.all():
  key.delete()

bucket_to_delete.delete()

print('Bucket Deleted')
input('Press Enter to continue...\n')
