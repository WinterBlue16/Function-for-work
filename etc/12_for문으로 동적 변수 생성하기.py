# for문으로 동적 변수 생성하기
# dataframe을 어떠한 기준에 따라 분리하거나, 한 경로에 든 파일들을 나눠야 할 때 사용할 수 있다.
# 한 변수에 계속 덮어씌워지는 게 아닌 서로 다른 변수를 코드에서 생성하여 따로 저장할 수 있다.

# 라이브러리 불러오기
import sys

# for 문
mod = sys.modules[__name__]

for i in range(10):
    setattr(mod, 'var_{}'.format(i), i) # 변수명, 변수에 들어갈 데이터

# 데이터 확인
var_0
var_1
var_2


# 참고 : https://medium.com/@unfinishedgod/%EB%8F%99%EC%A0%81%EC%9C%BC%EB%A1%9C-%EB%B3%80%EC%88%98-%EC%83%9D%EC%84%B1-%ED%95%98%EA%B8%B0-r-python-7c1d8dbc56e3
