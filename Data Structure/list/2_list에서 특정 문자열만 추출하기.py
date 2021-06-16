# list에서 특정 문자열이 포함된 item만 추출하고 싶을 때
# 예시로 사용한 문장은 푸앵카레의 명언

sentence = 'The scientist does not study nature because it is useful, he studies it because he delights in it, and he delights in it because it is beautiful. If nature were not beautiful, it would not be worth knowing, and if nature were not worth knowing, life would not be worth living.'
sample_li = sentence.split() # 문장을 단어로 잘라 list로 만들어 줌

# 'a'와 'ing'가 포함된 item 추출 → 리스트로 만들기
# 방법 1
a_li = []
for word in sample_li:
    if 'a' in word:
        a_li.append(word)
print(a_li)

# 방법 2        
ing_li = [word for word in sample_li if 'ing' in word] 
print(ing_li)