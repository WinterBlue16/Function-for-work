import json


def string_json_to_json(string_json):
    convert_json = json.loads(string_json)
    return convert_json


def print_json_indent(string_json):
    convert_json = json.loads(string_json)
    pretty_json = json.dumps(convert_json, indent=4)
    print(pretty_json)
    return pretty_json


sample = '{"sample": "apple", "sample2":"strawberry"}'
print(string_json_to_json(sample))
print(type(string_json_to_json(sample)))
print(print_json_indent(sample))
