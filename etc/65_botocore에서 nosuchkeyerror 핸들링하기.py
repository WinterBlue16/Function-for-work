# django에서 aws s3 bucket을 활용할 때 사용하는 라이브러리 boto3, botocore에서 Nosuchkey 에러를 핸들링한다.
# 아래의 함수는 s3 bucket에서 json 파일을 가져오고, 해당 파일이 경로에 존재하지 않을 경우 발생하는 nosuchkey에러를 핸들링한다.

import json
import boto3
from boto3.session import Session


session = boto3.Session()


def get_json_file_from_s3(file_path, file_type, bucket_name):
    s3 = session.client('s3')

    try:
        s3_object = s3.get_object(Bucket=bucket_name, Key=file_path+file_type)
        s3_file = s3_object['Body'].read().decode('utf-8')
        json_file = json.loads(s3_file)
        return json_file

    except s3.exceptions.NoSuchKey as e:
        return None
