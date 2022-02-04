'''
주어진 배열을 가능한 동일한 크기를 가진 N개의 덩어리로 분할한다.
'''

import numpy as np

sample_array = np.array([i for i in range(10)])

# 2개 덩어리로 분할
array_divide_2 = np.array_split(sample_array, 2)
print(array_divide_2)

# 3개 덩어리로 분할
array_divide_3 = np.array_split(sample_array, 3)
print(array_divide_3)

# 5개 덩어리로 분할
array_divide_5 = np.array_split(sample_array, 5)
print(array_divide_5)
