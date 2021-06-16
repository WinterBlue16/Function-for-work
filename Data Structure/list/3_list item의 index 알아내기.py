# 리스트 item의 index가 헷갈리거나 기억나지 않을 때

sentence = 'The scientist does not study nature because it is useful, he studies it because he delights in it, and he delights in it because it is beautiful. If nature were not beautiful, it would not be worth knowing, and if nature were not worth knowing, life would not be worth living.'
sample_li = sentence.split() # 문장을 단어로 잘라 list로 만들어 줌

print(sample_li.index('nature')) # list 내에서 단어가 중복될 경우, 가장 앞에 있는 index만 보여줌