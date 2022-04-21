import os
import json
import boto3
from matplotlib.pyplot import get


def call_lambda(data):
    lambda_client = boto3.client('lambda',
                                 region_name=os.environ.get('AWS 리전'),
                                 aws_access_key_id=os.environ.get(
                                     'AWS ACCESS KEY ID'),
                                 aws_secret_access_key=os.os.environ.get('AWS SECRET ACCESS KEY'))

    response = lambda_client.invoke(
        FunctionName='lambda 함수 이름',
        InvocationType='Event',
        Payload=data
    )
