# 코드 실행 시 시간 복잡도를 최소화하기 위해서 연산 수행 시간을 측정할 때
# 아래의 예시는 같은 작업을 수행하는 서로 다른 코드의 연산 시간을 비교한 것이다.

import time

x=[]

start_time1=time.time()
for i in range(10000):
    x.append(i)
# print(x)
end_time1=time.time()

print('연산에 걸린 시간(append):', end_time1-start_time1)

start_time2=time.time()
for i in range(10000):
    x+=[i]
# print(x)
end_time2=time.time()

print('연산에 걸린 시간(use list):', end_time2-start_time2)