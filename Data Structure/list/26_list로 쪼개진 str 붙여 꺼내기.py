# python에서 string을 list로 만들 경우 한 자 한 자가 다른 item이 되곤 한다.
# 그렇게 따로따로 떨어진 글자들을 모아 원래 형태로 만들고, list에서도 빼내고 싶을 때 사용한다.


# str
example_str = 'melancholy'

# list로 만들기
example_li = list(example_str)
print(example_li)

# list에서 빼내기
back_str = ''.join(example_li)
print(back_str)

# 문장 str
example_sentence = 'Am I blue?'

# list로 만들기
example_li2 = list(example_sentence)
print(example_li2)

# list에서 빼내기(공백 고려하지 않음)
back_sentence = ''.join(example_li2)
print(back_sentence)

# list에서 빼내기(공백 고려)
back_sentence = ' '.join(example_li2)
print(back_sentence)
