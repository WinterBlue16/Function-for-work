"""
데이터 프레임 열의 순서를 바꾸는 데 사용한다.
df는 기존에 데이터프레임이 존재한다고 가정했을 때, 데이터이다.
"""
import pandas as pd

# 방법 1
# 모든 열의 순서를 리스트로
cols = df.columns.tolist()

# 바꾸고 싶은 열의 순서에 따라 변경 가능
# list 형태로 더하는 것만 가능 # cols[3]+cols[2] 이런 식으로 더할 수는 없다.
cols = cols[-1:] + cols[:-1]

# 열 순서 변경
df = df[cols]


# 방법 2
# 바꾸고 싶은 순서대로 열 이름을 배열한 리스트 만들기
cols_list = [cols1, cols3, cols2...]

# 열 순서 변경
df_update = df[cols]
