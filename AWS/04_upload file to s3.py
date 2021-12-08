import boto3
import json
from datetime import datetime

from boto3 import session


def upload_txt_file_to_s3(bucket_name, text_file, path, file_name):
    """
    s3 bucket에 텍스트 파일을 업로드하는 함수입니다.
    """
    s3 = boto3.resource('s3')
    date = datetime.now().strftime('%y%m%d')

    key = path+file_name+'.txt'
    object = s3.Object(bucket_name, key)
    object.put(Body=text_file)
    print('txt file uploaded successfully!!')

    return key


def upload_json_file(dictionary, file_name, file_path, file_type, bucket_name):
    """
    Upload json file to s3 bucket.
    """
    try:
        s3 = boto3.resource('s3')
        object = s3.Object(bucket_name, file_path+file_name+file_type)
        object.put(
            BucketKeyEnabled=True,
            Body=(bytes(json.dumps(dictionary, ensure_ascii=False).encode('UTF-8')))
        )
        print('파일 업로드에 성공했습니다.')

    except Exception as e:
        print('파일 업로드에 실패하였습니다.')
