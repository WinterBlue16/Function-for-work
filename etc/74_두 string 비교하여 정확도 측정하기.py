from difflib import SequenceMatcher

str_1 = "안녕하세요?"
str_2 = "안녕하세요."
str_3 = "안녕하십니까?"

print(round(SequenceMatcher(None, str_1, str_2).ratio(), 2))
print(round(SequenceMatcher(None, str_1, str_3).ratio(), 2))
