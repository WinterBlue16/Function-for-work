'''
여러 개의 길이가 같은 리스트가 존재할 때, 같은 INDEX를 가진 값들만 더해 리스트를 생성한다
'''

# 리스트가 따로따로 존재할 때
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]

sumindexlist = [sum(item) for item in zip(list1, list2, list3)]
print(sumindexlist)

# 리스트가 리스트 안에 존재할 때
listinlist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
sumindexlist = [sum(item) for item in zip(*listinlist)]
print(sumindexlist)
