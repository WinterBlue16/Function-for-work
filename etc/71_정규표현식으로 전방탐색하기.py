"""
특정 string을 정규표현식으로 필터링하는 방법을 설명합니다.    
"""
import re

# '원' 앞의 string filtering
sample_string = ['1000원', '2000원', '3000원', '4000원']
str_filter = re.compile('.+(?=원)')

for t in sample_string:
    filtered_str = str_filter.search(t).group()
    print(filtered_str)

# 'mb' 앞의 string filtering
sample_string = '1000mb 2000mb 3000mb 4000mb'
sample_string = sample_string.split()

for t in sample_string:
    str_filter = re.compile('.+(?=mb)')
    filtered_str = str_filter.search(t).group()
    print(filtered_str)
