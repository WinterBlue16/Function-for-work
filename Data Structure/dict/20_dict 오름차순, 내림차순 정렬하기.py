# dict 자료형을 key, 혹은 value 기준으로 오름차순, 내림차순 정렬할 때 
# 파이 과자 dict 만들기
snack_pie=['빅파이', '초코파이', '몽쉘']
price=[3830, 3840, 4780]
pie_dict= dict(zip(snack_pie, price))
print(pie_dict)

# key 기준으로 오름차순 정렬
pie_dict1=sorted(pie_dict.items(), key=lambda x:x[0])
print(pie_dict1)

# key 기준으로 내림차순 정렬
pie_dict2=sorted(pie_dict.items(), key=lambda x:x[0], reverse=True)
print(pie_dict2)

# value 기준으로 오름차순 정렬
pie_dict3=sorted(pie_dict.items(), key=lambda x:x[1])
print(pie_dict3)

# value 기준으로 내림차순 정렬
pie_dict4=sorted(pie_dict.items(), key=lambda x:x[1], reverse=True)
print(pie_dict4)

# 오름차순, 내림차순 정렬은 가능하나, 정렬되며 자료형이 dict → tuple로 자동 변환된다는 점에 주의

