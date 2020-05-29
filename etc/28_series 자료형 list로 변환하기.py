
# pandas에서 자주 쓰이는 자료형인 series(보통 column만 꺼낼 경우)는 인덱싱이 잘 되지 않는다.
# 원하는 값을 찾아내고 보다 자유롭게 활용하기 위해 list 자료형으로 변환하고 싶을 때, 또 웹페이지 제작 시 render로 넘기고 싶을 때 사용한다.

# 라이브러리 불러오기
import pandas as pd

# 데이터프레임 만들기
sample_df = pd.DataFrame(data={'positive':['웃음', '신남', '감격'], 'neutral':['무덤덤', '지침', '아무 생각 없음'], 'negative' : ['슬픔', '분노', '역겨움']})
sample_df # 데이터 프레임 형성 확인

# 자료형 확인
print(type(sample_df['positive']))
>> <class 'pandas.core.series.Series'>

# list로 변환
seriestolist = sample_df['positive'].tolist()
>> ['웃음', '신남', '감격']

# 자료형 확인
print(type(seriestolist))
>> <class 'list'>
