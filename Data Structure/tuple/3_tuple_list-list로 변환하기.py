# tuple list를 이중 리스트로 변환한다.

sample_tuple_list = [(1, 2), (3, 4)]

# solution 1
sample_list = [list(t) for t in sample_tuple_list]
print(sample_list)

# solution 2
sample_list = list(map(list, sample_list))
print(sample_list)

# 반대의 경우도 가능
sample_tuple_list = [tuple(l) for l in sample_list]
print(sample_tuple_list)

sample_tuple_list = list(map(tuple, sample_list))
print(sample_tuple_list)
