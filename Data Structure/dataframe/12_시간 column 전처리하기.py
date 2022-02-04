# 시간 column 전처리하기
# datetime 형식의 column을 그대로 머신러닝이나 딥러닝에 input할 수는 없다.
# 열을 쪼개 새로운 column을 생성하는 코드

# 라이브러리 불러오기
import pandas as pd

# column 쪼개기
sample_df['년']=sample_df['일시'].dt.year
sample_df['월']=sample_df['일시'].dt.month
sample_df['일자']=sample_df['일시'].dt.day
sample_df['시']=sample_df['일시'].dt.hour
sample_df['분']=sample_df['일시'].dt.minute
sample_df['초']=sample_df['일시'].dt.second
