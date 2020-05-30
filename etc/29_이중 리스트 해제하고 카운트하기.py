# 데이터를 처리하다 보면 리스트 안에 리스트가 존재하는 경우가 있다.
# 이 경우 리스트 안의 item들을 검색하거나 카운트하는데 어려움을 겪게 된다.
# 이러한 상황을 해결하고 싶을 때 사용한다

# 라이브러리 불러오기
import itertools
from collections import Counter

# 샘플 리스트 만들기
sample_li = [[1], [2], [2], [3], [5]]

# 리스트 item 확인해보기
for li in sample_li:
    print(li) # 타입 list

# 리스트 갯수 카운트해보기(실패)
count_li = Counter(sample_li)
print(count_li)
>> TypeError: unhashable type: 'list' 발생

# 이중 리스트 해제하기
li2_to_li1 = list(itertools.chain(*sample_li))
for i in li2_to_li1:
    print(i) # 타입이 int로 바뀌었다!

# 다시 리스트 item 카운트
count_newli = Counter(li2_to_li1)
print(count_newli)
