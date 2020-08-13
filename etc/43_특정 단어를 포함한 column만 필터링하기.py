# 데이터프레임을 다룰 때, 특정 문자나 단어만을 포함하고 있는 열만 뽑아내고 싶을 때 사용한다.

# 라이브러리 불러오기
import pandas as pd

# 데이터프레임 만들기
sample_df = pd.DataFrame(data={'test1':[50, 30, 98], 'test2':[70, 84, 65], 'score1':['D', 'F', 'A'], 'score2':['C', 'B', 'D']})
sample_df

# column명에 test가 포함되는 열만 골라내기
test_col = sample_df.filter(like='test', axis=1)

# column명에 score가 포함되는 열만 골라내기
score_col = sample_df.filter(like='score', axis=1)
