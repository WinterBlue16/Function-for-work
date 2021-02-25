# 데이터프레임을 다룰 때 series의 type을 int,float 혹은 str로 바꿔야 하는 일이 생길 때 사용한다.

# 라이브러리 불러오기
import pandas as pd

# 데이터프레임 만들기
sample_df = pd.DataFrame(data={'float':['1', '2', '3'], 'int': ['1', '2', '3'], 'str':['1', '2', '3']})
sample_df # 데이터 확인

# str => int로 series type 변환
# pd.to_numeric
sample_df['int'] = pd.to_numeric(sample_df['int'])
sample_df[['int']] = sample_df[['int']].apply(pd.to_numeric)

# astype
sample_df['int'] = sample_df['int'].astype(int)
sample_df = sample_df.astype({'int' : int})


# str => float로 series type 변환
sample_df = sample_df.astype({'float' : np.float})
sample_df = sample_df.astype(float)
