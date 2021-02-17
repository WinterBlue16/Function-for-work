# 주어진 리스트 안의 item들이 나열될 수 있는 경우의 수를 구한다
# 서로 다른 리스트를 혼합하여 경우의 수를 구하고 싶은 경우 커다란 리스트 안에 대상 리스트들을 포함시켜야 한다.
from itertools import permutations, combinations, combinations_with_replacement, product

li_1=['사과', '배', '바나나']
li_2=['식빵', '소보루빵', '크림빵']
li_3=['주스', '맥주', '요거트']

# 각 리스트 나열 시 모든 경우의 수 출력(순서 고려, 중복 허용 X)
per_1=list(permutations(li_1)) # li_2, li_3
# print(per_1)

# 각 리스트에서 N개만큼 뽑아 나열할 경우(순서 고려, 중복 허용 X)
per_2=list(permutations(li_1, 2)) # N=2
# print(per_2)

# 각 리스트 나열 시 N개만큼 뽑아 나열하는 모든 경우의 수 출력(중복 허용)
per_3=list(product(li_1, repeat=2)) # li_2, li_3
# print(per_3)

# 각 리스트 나열 시 N개만큼 뽑아 나열할 경우 출력(순서 고려하지 않음)
con_1=list(combinations(li_1, 2)) # li_2, li_3
# print(con_1)

# 각 리스트 나열 시 N개만큼 뽑아 나열할 경우 출력(순서 고려하지 않음, 중복 허용)
con_2=list(combinations_with_replacement(li_1, 2)) # li_2, li_3
# print(con_2)

# 3개의 리스트에서 각 리스트 값들을 나열할 때의 모든 경우의 수
all_li=[li_1,li_2,li_3]
all_per=list(product(*all_li))
# print(all_per)

# 2개의 리스트로 모든 경우의 수
two_li=[li_1,li_2]
two_per=list(product(*two_li))
print(two_per)
