# 데이터 전처리 시 어떤 column을 기준으로 데이터프레임을 재배열(열을 나열)하고 싶을 때가 있다.
# 그 과정에서 사용하는 기본적인 코드는 이하와 같다.

# 라이브러리 불러오기
import pandas as pd

# 데이터프레임 만들기
sample_df = pd.DataFrame(data={'col_1':[1, 2, 3, 4, 5], 'col_2': [6, 4, 8, 5, 9], 'col_3':[10, 25, 15, 20, 35]})
sample_df # 데이터 확인

# 'col_2'기분으로 데이터프레임 재배열(오름차순)
sort_df = sample_df.sort_values(by='col_2')

# 'col_2'기분으로 데이터프레임 재배열(내림차순)
sort_df = sample_df.sort_values(by='col_2', ascending=False)
