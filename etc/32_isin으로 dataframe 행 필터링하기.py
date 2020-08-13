# dataframe을 다룰 때면 필터링을 해야 하는 경우가 많이, 아니 거의 항상 생긴다.
# 필요한 데이터가 들어있는 행만을 남기고 싶은데, 막상 그렇게 하려니 쉽지가 않다.

# 여러가지 방법이 있지만 그 중 가장 간편한 방법은 isin을 이용하는 것이다.
# 특히 따로 list가 존재하고, 그 list에 포함된 요소가 들어있는 행만을 남겨두고 싶을 때 유용한 방법이다.

# 라이브러리 불러오기
import pandas as pd
import itertools

# sample data 만들기
sample_df = pd.DataFrame(data={'positive':['웃음', '신남', '감격', '희열'], 'neutral':['무덤덤', '지침', '아무 생각 없음', '공허'], 'negative' : ['슬픔', '분노', '역겨움', '혐오']})
sample_df # 데이터 확인

# 웃음이 있는 행만 남기기
smile_df = sample_df[sample_df['positive'].isin(['웃음'])]
smile_df

# 웃음, 감격이 있는 행만 남기기
smile_delight_df = sample_df[sample_df['positive'].isin(['웃음', '감격'])]
smile_delight_df
