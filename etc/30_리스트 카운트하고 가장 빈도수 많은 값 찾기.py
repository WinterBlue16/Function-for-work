# list 안의 item을 종류별로 카운트하고 싶을 때가 있다.
# 특히 빈도수를 체크할 때, 가장 많이 존재하는 item과 가장 적게 존재하는 item을 찾고 싶을 때도 유용하게 쓸 수 있다.

# 0. 라이브러리 불러오기
from collections import Counter

# 1. 샘플 리스트 만들기
sample_li = ['사과', '배', '수박', '딸기', '배', '배', '사과']

# 2. item 카운트
count_item = Counter(sample_li)
print(count_item)
>> Counter({'배': 3, '사과': 2, '수박': 1, '딸기': 1})

# 3. 가장 수가 많은 item 찾기
max_item = count_item.most_common(n=1) # n은 찾을 item 종류의 수를 의미한다. n=2일 경우 가장 수가 많은 item, 그 다음으로 수가 많은 item 두 개를 반환
print(max_item)
>> [('배', 3)]
