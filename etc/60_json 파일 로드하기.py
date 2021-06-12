# 저장된 json 파일을 로드한다.
import json

file_path = 'json 파일 저장 경로'

with open(file_path, 'r') as json_file:
    json_to_dict = json.load(json_file)  # json이 dict로 바뀌어 로드된다.
