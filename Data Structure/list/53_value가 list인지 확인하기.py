'''
list가 값(value)로 포함된 데이터에서 해당 값이 list인지 아닌지를 구분할 수 있다.
'''

sample_dict = {'a': 1, 'b': 2, 'c': [3, 4, 5]}
values = list(sample_dict.values())

for i in range(len(sample_dict)):
    if isinstance(values[i], list):
        print('리스트입니다.')
    else:
        print('리스트가 아닙니다.')
