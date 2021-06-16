# 리스트에 중복된 item이 존재해서 제거하고 싶을 때

sentence = 'The scientist does not study nature because it is useful, he studies it because he delights in it, and he delights in it because it is beautiful. If nature were not beautiful, it would not be worth knowing, and if nature were not worth knowing, life would not be worth living.'
sample_li = sentence.split() # 문장을 단어로 잘라 list로 만들어 줌

print(len(sample_li)) # 51

# 리스트(list) → 집합(set) → 리스트(list)
sample_li = set(sample_li) # 집합은 중복을 허용하지 않으므로 중복 item 자동 제거
sample_li = list(sample_li) # 다시 리스트로 변환

print(len(sample_li)) # 27

 