# json의 list를 json 형태로 저장한다.
import json

sample_json_list = [{
    'id': 1,
    'name': 'Alice'
},
    {
    'id': 2,
    'name': 'Ben',
},
    {
    'id': 3,
    'name': 'Sam'
}]

# save
with open('{}.json'.format('sampled_json_list'), 'w') as json_list:
    json.dump(sample_json_list, json_list)

# read
with open(r"{}".format('sample_json_list'), 'r') as read_json_list:
    data = json.load(read_json_list)
