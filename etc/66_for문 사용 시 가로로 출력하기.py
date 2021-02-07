# for문 사용 시 가로로 출력하기
# 예시
for i in range(10):
    print(i, end='')

# 리스트를 출력하기
import string

sample_li = [i for i in string.ascii_lowercase] # 영소문자 모음
for i in sample_li:
    print(i) # 줄마다 하나씩 출력

for i in sample_li:
    print(i, end=' ') # 한 줄에 모두 출력