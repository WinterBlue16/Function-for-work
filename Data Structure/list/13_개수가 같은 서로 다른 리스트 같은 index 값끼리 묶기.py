# 길이가 같은 n개의 리스트를 index가 같은 items들끼리 묶어 새로운 리스트를 생성하는 방법을 알아본다.

sample_list1 = [1, 2, 3]
sample_list2 = ['가', '나', '다']
sample_list3 = ['a', 'b', 'c']

same_index_list = [list(t)
                   for t in zip(sample_list1, sample_list2, sample_list3)]
print(same_index_list)
