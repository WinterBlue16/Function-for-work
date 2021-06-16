# column 내 특정 단어가 들어간 행들만 필터링하고,
# 그 열들을 숫자로 전처리하고 싶을 때 사용하는 코드

# 라이브러리 불러오기
import pandas as pd
import numpy as np

# 필터링 기준 설정
condition_li=[
    (sample_df['대상이 될 column 명'].str.contains('column 내 값들 중 필터링하고 싶은 단어 1')),
    (sample_df['대상이 될 column 명'].str.contains('column 내 값들 중 필터링하고 싶은 단어 2')),
    (sample_df['대상이 될 column 명'].str.contains('column 내 값들 중 필터링하고 싶은 단어 3'))
]

# 필터링 조건에 해당하는 열들을 변환할 값 지정
value_li=[1, 2, 3]

# 새로운 열 생성
sample_df['새로 생성될 column 명']=np.select(condition_li,value_li)
