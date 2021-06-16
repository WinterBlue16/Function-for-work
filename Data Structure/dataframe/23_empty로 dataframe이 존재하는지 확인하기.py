# 데이터 처리 시 데이터 프레임이 비어 있는지 아닌지 확인하고 싶을 때가 있다.
# 그 때는 empty를 이용하여 간편하게 확인해 볼 수 있다.
# 이는 데이터 처리뿐 아니라 if 조건문을 만들 때도 유용하게 쓰인다!

# 라이브러리 불러오기
import pandas as pd
import itertools

# sample data 만들기
sample_df = pd.DataFrame(data={'positive':['웃음', '신남', '감격', '희열'], 'neutral':['무덤덤', '지침', '아무 생각 없음', '공허'], 'negative' : ['슬픔', '분노', '역겨움', '혐오']})
sample_df # 데이터 확인

# 데이터프레임이 비었는지 확인
if sample_df.empty:
    print('데이터프레임이 비었습니다.')

# 데이터프레임이 비지 않았는지 확인
if not sample_df.empty:
    print('데이터프레임이 존재합니다.')


# 참고 링크 : https://stackoverflow.com/questions/36543606/python-pandas-check-if-dataframe-is-not-empty/36543629
