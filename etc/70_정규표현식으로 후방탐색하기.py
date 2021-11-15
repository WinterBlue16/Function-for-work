"""
특정 string을 정규표현식으로 필터링하는 방법을 설명합니다.    
"""
import re

# ':' 뒤의 string filtering
sample_test = 'name: test test test test'
str_filter = re.compile('(?<=:).+')
filtered_str = str_filter.search(sample_test).group()
print(filtered_str)

# '/' 뒤의 string filtering
sample_test = 'name/ test2 test2 test2 test2'
str_filter = re.compile('(?<=/).+')
filtered_str = str_filter.search(sample_test).group()
print(filtered_str)

# '=' 뒤의 string filtering
sample_test = 'name= test3 test3 test3 test3'
str_filter = re.compile('(?<==).+')
filtered_str = str_filter.search(sample_test).group()
print(filtered_str)
