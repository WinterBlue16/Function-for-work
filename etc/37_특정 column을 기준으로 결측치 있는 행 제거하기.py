# 특정 column을 기준으로 결측치 제거하기

# 라이브러리 불러오기
import pandas as pd

# 데이터 만들기
df = pd.DataFrame(data={'name':['apple', 'samsung', 'Sony'], 'country':['US', 'KO', 'JA'], 'code':[1, None, 3]}) # 결측치를 만들기 위해서는 None을 넣으면 된다.
df

# 결측치가 있는 행만 지우기
df = df[df['code'].notnull()]
df

# 참고 : https://c10106.tistory.com/4134
