# Data processing(전처리)를 위한 함수 모음
# 0. 라이브러리 불러오기
import pandas as pd
import numpy as np
import datetime


# 1. 데이터 읽어오기
df = pd.read_csv('csv파일이 위치한 경로', index_col=0, encoding='utf-8') 
# 파일 경로는 Shift+마우스 오른쪽 버튼으로 경로 복사 가능. 단, '\'를 '/'로 바꿔주어야 한다! 


# 2. 데이터 살펴보기
df.head() # 가장 윗 행 5개
df.tail() # 가장 아래 행 5개
df.describe() # 최솟값, 최댓값

df.sort_values(by='정렬 기준으로 삼고 싶은 column명', ascending='False', inplace=True) # 날짜순으로 내림차순 정렬

# 3. Null 값 확인
df.info()

def changedatetype(column):
    for i in range(len(column)):
        column[i] = datetime.datetime.strptime(column[i], '%B %d, %Y') # str을 날짜로 바꿔주는 함수(참고: https://brownbears.tistory.com/432)

# 문자열에 대한 함수 목록(https://m.blog.naver.com/PostView.nhn?blogId=wideeyed&logNo=221603778414&proxyReferer=https%3A%2F%2Fwww.google.com%2F)



# 4. 데이터 분포 확인(이상치 여부 판단)
df.hist(bin=, figsize=( , ))

# 5. 열별 분석
df['열 이름'].value_counts()

# 6. Null값 채우기
df.loc[df.isnull()['열 이름']] # NaN값이 있는 행들만 뽑아내 확인
df['열 이름'].replace({'바꾸고 싶은 내용 1': 바꿀 내용 1, '바꾸고 싶은 내용 2': 바꿀 내용 2}) # 특정한 값 골라내어 다른 값으로 바꾸기
df['열 이름'].replace(np.nan, 바꿀 내용) # 결측치 부분 대체하기
df['열 이름'].astype(int) # 정수형으로 변경
df['열 이름'].astype(float) # 실수형으로 변경 # df.astype으로 전체 데이터 프레임에도 적용 가능

# 7. 필요없는 열, 행 제거하기
del df['열 이름']
df.rename(columns={"원래 열 이름":"바꿀 열 이름"}, inplace=True)
df.dropna() # 결측치가 존재하는 모든 행을 제거

# 8. 문자(str)를 숫자(int, float)로 전환
int()

# 9. 이상치 제거하고 확인하기


# 10. (DNN)np.array 자료형으로 변환하기
df = df.values