# 주어진 리스트에서 다른 리스트와 겹치는, 특정한 일부만을 잘라내고 싶을 때 사용한다.
# sample_list1에서 sample_list2에 해당하는 부분만 잘라내기

sample_list1 = ['a', 'b', 'c', 'd']
sample_list2 = ['c', 'd']

sample_list3 = [v for v in sample_list1 if v not in sample_list2]
