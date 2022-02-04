'''
주어진 리스트의 n번째 값들만 리스트로 만들기
'''

sample_list = [i for i in range(100)]
print(sample_list)

# 간격이 3 # 리스트의 첫 값으로 만들고 싶은 index를 가장 앞에 넣어준다.
list1 = sample_list[::3]
list2 = sample_list[1::3]
list3 = sample_list[2::3]

print(list3)
