# 한 열을 기준으로 다른 열과의 상관관계 구하기

# 라이브러리 불러오기
import pandas as pd

# 샘플 데이터프레임 만들기
sample_df = pd.DataFrame(data={'언어':[88, 76, 45, 95, 82], '수리':[35, 89, 77, 56, 84], '외국어':[100, 97, 80, 95, 73], '사회탐구':[50, 45, 32, 27, 46]})

# 언어 column을 기준으로 외국어 column이 가지는 상관계수 구하기
sample_df['언어'].corr(sample_df['외국어'])
