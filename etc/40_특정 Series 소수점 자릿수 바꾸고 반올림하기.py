# dataframe 내 특정 column의 소수점 자리를 바꾸고 싶을 때 사용하는 코드

# 라이브러리 불러오기
import pandas as pd
import numpy as np

# 샘플 데이터 만들기
sample_df=pd.DataFrame(data={'A' : [1, 2, 3, 4, 5], 'B': [1.00000, 1.99999, 2.99871, 3.99902, 5.00000]})
sample_df

# 'B' column 소수점 2번째 자리까지 반올림하여 표시하도록 변경
sample_df['B']=np.round(sample_df['B'], 2)
sample_df
