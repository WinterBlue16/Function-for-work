import boto3
from boto3.session import Session
from botocore.exceptions import ClientError


def check_file_exised_in_s3(key, bucket_name='bucket 이름'):
    """
    s3 bucket에 해당 파일이 존재하는지 확인합니다. 
    """
    session = boto3.Session()
    try:
        s3_client = session.client('s3')
        response = s3_client.get_object(Bucket=bucket_name, Key=key)
        return key
    except ClientError as e:
        if e.response['Error']['Code'] == 'NoSuchKey':
            return None
