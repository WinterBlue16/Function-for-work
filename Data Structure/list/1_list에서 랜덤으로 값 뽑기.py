# 리스트에서 랜덤으로 값 뽑아내고 싶을 때 사용
import random 

# 하나의 값 뽑기
sample_li = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(random.choice(sample_li))

# 여러 개 값 뽑기(중복 허용 X)
print(random.sample(sample_li, 2)) # 2개 값 
print(random.sample(sample_li, 3)) # 3개 값 

# 값이 다수일 경우 자동으로 list가 됨
# len(sample_li)보다 숫자가 클 경우 컴파일 에러 발생

# 여러 개 값 뽑기(중복 허용)
print([random.choice(sample_li) for i in range(2)]) # 2개 값 # 대괄호를 넣지 않으면 값 자체가 뽑히지 않음
