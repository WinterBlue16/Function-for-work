# 한 column 내에 몇 종류의 값들이 얼마나 존재하는지 알아보기 위한 함수
# 보통 column 내의 값들이 string일 때 사용한다.

# 라이브러리 불러오기
import pandas as pd

# 샘플 데이터프레임 만들기
sample_df = pd.DataFrame(data={'케이크':['시폰', '파운드', '롤', '크레이프'], '그 외': '마카롱', '에클레어', '마들렌', '슈크림'})

# 각 column 값들 조회하기
sample_df['케이크'].value_counts()
sample_df['그 외'].value_counts()
