# 날짜 열의 형식이 제각각일 때 각 연도 순으로 분류, 묶어주는 함수
# 예시> 2001~2020

df1 = df[df['열 이름'].str.contains('2001')==True] # 년도를 포함한 행을 전부 꺼내 데이터프레임화한다.
df1['열 이름'] = 2001 # 인자를 모두 해당 연도로 바꿔준다.

def changedate(df, num): # 데이터프레임, 숫자를 넣어주면 해당 숫자의 str이 포함된 행만을 꺼내 데이터 프레임화
    temp_df = df[df['열 이름'].str.contains(str(num))==True] 
    return temp_df

for i in range(2002, 2021): 
    sub_df = changedate(df, i) # 연도별 숫자가 포함된 행을 각각 모아
    sub_df['열 이름']=i # 선택된 행의 인자를 모두 해당 연도로 바꿔준다.
    temp_df = pd.concat([temp_df, sub_df]) # 처리가 끝난 열들을 순서대로 합쳐 준다.
    
temp_df