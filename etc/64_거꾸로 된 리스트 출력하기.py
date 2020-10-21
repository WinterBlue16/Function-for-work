
# 리스트의 순서를 오름차순이나 내림차순이 아니라, 거꾸로 뒤집는 게 편리한 경우도 있다. 
# 그럴 때 reversed(), reverse() 함수를 활용한다. 

sample_li=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 리스트를 뒤집어 출력
sample_li.reverse()
sample_li

# 리스트를 뒤집어 출력 2
print(list(reversed(sample_li)))
