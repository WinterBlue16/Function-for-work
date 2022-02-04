# 이미 존재하는 dataframe에 다른 column 값의 평균 column을 추가하기

# 라이브러리 불러오기
import pandas as pd

# sample 데이터셋 만들기
sample_df = pd.DataFrame(data={'col1':[0, 1, 2, 3, 4],
                                'col2':[10, 11, 12, 13, 14],
                                'col3':[20, 21, 22, 23, 24]})

# 평균 column 만들기
COL = sample_df.loc[:, 'col':]
sample_df['average'] = COL.mean(axis=1)
