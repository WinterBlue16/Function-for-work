# NaN값이 들어간 행들을 확인하고 싶을 때 
df.loc[df.isnull()] # 데이터 프레임 전체 대상
df.loc[df.isnull()['column']] # 해당 컬럼 내 NaN값이 들어간 경우 그 행만 추출