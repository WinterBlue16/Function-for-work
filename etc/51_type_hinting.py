# arguements에 type을 추가할 수 있다
# 다만 output type이 다르다고 해서 error가 발생하지는 않는다

def sayHello(name: str) -> str :
    print('{}님이 입장하셨습니다.'.format(name))
    return 'Hello' + name

def sperateSentence(sentence: str) -> list :
    return sentence.split()

def listToStr(strList: list) -> str:
    return ' '.join(strList)
