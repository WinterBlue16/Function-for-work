# 코딩 테스트 등에서 대문자/소문자 알파벳 리스트가 필요할 때 사용할 수 있다
import string

# 소문자 리스트
lower = [i for i in string.ascii_lowercase]
print(lower)

# 대문자 리스트
upper = [i for i in string.ascii_uppercase]
print(upper)

# 대문자+소문자 전체 리스트
lowup = [i for i in string.ascii_letters]
print(lower)

# (번외)숫자
digit = [i for i in string.digits]
print(digit)