# 데이터 전처리 작업 시 필요없는 행만 날리고 싶을 때
# 1. 결측치가 있는 행만 제거 
df = df.dropna()
df.dropna(inplace=True) # 변수 선언 없이 바로 반영해줌

# 2. 한 컬럼에서 결측치가 있는 행만 제거
df.loc[df.isnull()['column']] # 해당 컬럼에서 NaN값을 갖는 행들만 뽑아내기 # 행 INDEX 체크
df = df.drop(['INDEX name_1', 'INDEX name_2']) # 해당 인덱스를 가진 행만 골라 제거