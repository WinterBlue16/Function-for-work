# dict의 value를 통해 key를 얻어낸다.
sample_dict = {'a': 1, 'b': 2, 'c': 3}

# dict keys
print(sample_dict.keys())

# dict values
print(sample_dict.values())

# get value by key
print(sample_dict.get('a'))  # 1
print(sample_dict.get('b'))  # 2

# get keys by values
print([k for k, v in sample_dict.items()])

# get key by value
print([k for k, v in sample_dict.items() if v == 3])  # 'c'
print([k for k, v in sample_dict.items() if v == 1])  # 'a'
