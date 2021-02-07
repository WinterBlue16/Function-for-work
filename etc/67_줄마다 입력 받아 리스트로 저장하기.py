# 여러 줄에 걸쳐 input이 들어올 경우 이를 모두 받아 list로 만든다

x = list(input() for _ in range(5)) # 5줄에 걸쳐 입력된 input을 모두 list로 만듦
print(x)

x = [input() for _ in range(5)]
print(x)