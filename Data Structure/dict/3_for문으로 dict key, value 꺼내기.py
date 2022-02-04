"""
python에서는 for loop를 통해 dict의 key, value 값을 모두 꺼낼 수 있다.
"""

sample_dict = {}
sample_dict[1] = 'a'
sample_dict[2] = 'b'
sample_dict[3] = 'c'

print(sample_dict)

for k, v in sample_dict.items():
    print(k, v)
