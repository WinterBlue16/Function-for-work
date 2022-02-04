# dict 혹은 counter 자료형에서 key만 꺼내어 사용하고 싶을 때가 있다.
# 그럴 때는 keys() 함수를 활용하여 간편하게 꺼낼 수 있다.
# 덤으로 counter 자료형을 다루는 방법에 대해서도 알아본다.

# sample 만들기
heroes = Counter({'이순신': 1598,
                 '김시민': 1592,
                 '권율': 1599,
                 '김완': 1546,
                 '류성룡': 1607})

# type 확인
print(type(heroes))
>>> <class 'collections.Counter'>

# 인덱싱 시도
print(heroes[0])
>>> 0
# 엇, 인덱싱이 되지 않는다. 그렇다면 이건 어떨까?

# 인덱싱 시도 2차
print(heroes[0][0])
>>> TypeError: 'int' object is not subscriptable
# 이것도 안 된다. 첫 value를 문자형으로 바꿔도 마찬가지.
# 그렇다면 delete 어떨까?

# delete 시도
del heroes['류성룡']
heroes
>>> Counter({'이순신': 1598, '김시민': 1592, '권율': 1599, '김완': 1546})
# 엇, del은 먹힌다! 지우는 것은 가능하다는 말이다. 그렇다면?

# insert 시도
heroes.insert({'이순신': 1598}, {'정운' : 1592})
>>> AttributeError: 'Counter' object has no attribute 'insert'
# 지우는 건 되는데 추가가 안된다. 다른 시도를 해보자.

# append 시도
heroes.append({'정운' : 1592})
>>> AttributeError: 'Counter' object has no attribute 'append'
# 역시 안된다. 왜 지우는 건 되는데 추가는 안되는지 모를 일이다.
# list에 주로 쓰는 방식이어서일까. 그렇다면 모양이 비슷한 dict를 다루듯이 해보자.

# dict 형식으로 쌍 추가하기
heroes['정운'] = 1592
>>> Counter({'이순신': '1598', '김시민': 1592, '권율': 1599, '김완': 1546, '정운': 1592})
# 된다!! 이 예에서 볼 수 있듯이, Counter 자료형은 dict와 거의 비슷하다고 생각하면 될 것 같다.

# key만 꺼내 리스트로 만들기
heroes.keys()
>>> dict_keys(['이순신', '김시민', '권율', '김완', '정운'])
list(heroes.keys())
['이순신', '김시민', '권율', '김완', '정운']


# 보다시피 깔끔하게 list 형식으로 변환할 수 있다!

# 카운터 자료형들 사이에 뺄셈도 가능하다! 
heroes_1 =  Counter({'이순신': 1598, '김시민': 1592, '권율': 1599, '김완': 1546})
heroes_2 = Counter({'김시민': 1592, '권율': 1599})

heroes_3 = heroes1 - heroes_2
heroes_3 # Counter({'이순신': 1598, '김완': 1546})



