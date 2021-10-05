"""
csv 파일 등 특정 파일의 encoding을 확인하고 싶을 때 사용할 수 있다.
"""
import chardet


def check_file_encoding(file_path):
    data = open(file_path, 'rb').read()
    result = chardet.detect(data)
    dataenc = result['encoding']
    return dataenc
