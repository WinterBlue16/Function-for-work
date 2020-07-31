# dataframe을 다룰 시 int인 줄 알았던 series의 type이 str이라 당황하는 경우가 생긴다.
# 이런 경우 자칫하다 시간을 버릴 수 있으므로 전체/일부 열을 합을 구하기 전에 확인해보는 것이 좋다.

# 라이브러리 불러오기
import pandas as pd

# 데이터 만들기
sample_df = pd.DataFrame(data={'int':[1, 2, 3, 4], 'str':['1', '2', '3', '4'], 'float' : [1.0, 2.0, 3.0, 4.0]})
# 데이터 확인
sample_df

# 열별 type 확인하기
sample_df['int'].dtype
>> dtype('int64')
sample_df['str'].dtype
>> dtype('0')
sample_df['float'].dtype
>> dtype('float64')
