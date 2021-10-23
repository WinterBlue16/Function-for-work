import boto3
from datetime import datetime


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
