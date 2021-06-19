# 2차원 배열을 입력으로 받는 코드
# 행과 열을 지정
n, m = map(int, input().split())

# 1
mylist = [0 for _ in range(n)]

for i in range(n):
    mylist[i]=list(map(int, input().split()))


# 2
mylist=[]
for i in range(n):
    mylist.append(list(map(int, input().split())))


# 3
mylist=[list(map(int, input().split()) for _ in range(n))]