# dict를 정렬시키려고 sorted를 사용한 것까지는 좋았는데 자료형이 tuple로 바뀌었다. 
# 하지만 아래에 작성할 코드를 생각하면 dict 자료형이 더 수월할 경우 tuple을 dict로 변환

# sample tuple
pie_tuple=[('몽쉘', 4780), ('초코파이', 3840), ('빅파이', 3830)]

# tuple을 dict로 변환하기
pie_dict=dict(pie_tuple)
print(pie_dict)

# tuple을 dict로 변환하기 2(key ↔ value)
pie_dict2=dict(map(reversed, pie_tuple))
print(pie_dict2)