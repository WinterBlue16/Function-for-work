import json

sample = '[{"sample": 3}]'
print(type(sample))

# json 형식의 string을 json list로 변경
sample_json = json.loads(sample)
print(type(sample_json))  # list
print(sample_json)
print(type(sample_json[0]))  # dict
