# 하나의 리스트를 홀수 index, 짝수 index별로 나누어 두 개의 리스트를 만든다.

sample_list = [i for i in range(100)]
odd_list, even_list = sample_list[::2], sample_list[1::2]

print(odd_list)
print(even_list)
