# 리스트의 모든 값을 대상으로 조건을 주고 싶을 때, for문 외에 all이나 any도 이용할 수 있다
x=[0,1,2,3,4,5,6,7,8,9]

# x의 모든 값이 10보다 작은지 확인(all)
print(all(i < 10 for i in x))

>> True

# x의 값 중 9 이상인 값이 하나라도 있는지 확인(any)
print(any(i >= 9 for i in x))

>> True
