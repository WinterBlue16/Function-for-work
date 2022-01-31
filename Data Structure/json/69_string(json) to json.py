import json


def string_json_to_json(string_json):
    convert_json = json.loads(string_json)
    return convert_json


sample = '{"sample": "apple", "sample2":"strawberry"}'
print(string_json_to_json(sample))
print(type(string_json_to_json(sample)))
