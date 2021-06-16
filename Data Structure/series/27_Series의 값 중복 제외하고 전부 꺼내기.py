# 데이터프레임을 다룰 때, 한 열(column)에서 중복을 제외한 값들을 모두 알고 싶을 때 사용한다.

# 라이브러리 불러오기
import pandas as pd
import array

# 데이터 만들기
sample_df = pd.DataFrame(data={'positive':['웃음', '신남', '감격', '희열'], 'neutral':['무덤덤', '지침', '아무 생각 없음', '공허'], 'negative' : ['슬픔', '분노', '역겨움', '혐오']})
sample_df # 데이터 확인

# positive열 값들 보기
sample_df['positive'].unique() # 중복을 뺀 모든 값들이 포함된 array 생성
