# Data processing(전처리)를 위한 함수 모음
df = dataframe

# 1. 데이터 읽어오기

# 2. 데이터 살펴보기
df.head()
df.tail()
df.describe()

# 3. Null 값 확인
df.info()

# 4. 데이터 분포 확인(이상치 여부 판단)
df.hist(bin=, figsize=( , ))

# 5. 열별 분석
df[].value_counts()

# 6. Null값 채우기

# 7. 필요없는 열, 행 제거하기
del df[]

# 8. 문자(str)를 숫자(int, float)로 전환
int()

# 9. 이상치 제거하고 확인하기


# 10. (DNN)np.array 자료형으로 변환하기
df = df.values