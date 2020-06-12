# tuple 자료형 인덱싱하기
# django를 활용하다 보면 tuple을 사용할 때가 많다.
# 튜플 중 자유자재로 값을 꺼내기 위해서는 인덱싱에 익숙해야 한다.

# 라이브러리 불러오기
from numpy import array


# 튜플 예시
tuple_sample = (0, array([[0.8653636 , 0.01928098, 0.11535539]], dtype=float32))

# array 자료형의 값들을 하나씩 꺼내서 % 단위로 만들고 싶을 떄
a = tuple_sample[1][0][0]*100
b = tuple_sample[1][0][1]*100
c = tuple_sample[1][0][2]*100

# 소수점 두 자리 이하 날라기
a = round(a, 1)
b = round(b, 1)
c = round(c, 1)
