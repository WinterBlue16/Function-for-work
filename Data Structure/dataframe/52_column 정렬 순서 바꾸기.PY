"""
데이터 프레임 열의 순서를 바꾸는 데 사용한다.
df는 기존에 데이터프레임이 존재한다고 가정했을 때, 데이터이다.
"""
import pandas as pd

# 모든 열의 순서를 리스트로
cols = df.columns.tolist()

# 바꾸고 싶은 열의 순서에 따라 변경 가능
cols = cols[-1:] + cols[:-1]

# 열 순서 변경
df = df[cols]
