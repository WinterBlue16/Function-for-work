"""
함수 결과 return 시 tuple이나 string, int가 아닌 json 형태로 반환합니다.
"""
import json


def convert_json(data):

    language = "Python"
    data = data
    error_code = 0

    value = {
        "language": language,
        "data": data,
        "error_code": error_code
    }

    return json.dumps(value)
