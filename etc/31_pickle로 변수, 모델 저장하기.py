# python으로 작업하다 보면, 데이터를 저장하고 로드해 와야 하는 경우가 많이 생긴다.
# 한번 파일을 저장해두고 나면 번거로운 작업이 줄어들고 속도도 빨라지지만, 유감스럽게도 python에서는 저장 형식이 정해져 있는 경우가 대부분
# model이나 pandas의 pd.to_csv 등이 대표적인 예이다. 그럼 일반 변수나 리스트, dict 등을 저장하여 활용할 방법은 없는 것일까?

# 다행스럽게도 이런 경우 pickle이라는 라이브러리를 활용하여 도움을 받을 수 있다.

# 라이브러리 불러오기
import pickle

# sample data 생성
int_li = [1, 2, 3, 4, 5, 6]
str_li = ['대너리스', '존', '아리아', '산사', '티리온']

# 저장하기
with open('./int_li.pkl', 'wb') as f:
    pickle.dump(int_li, f)

with open('./str_li.pkl', 'wb') as f:
    pickle.dump(str_li, f)

# 로드하기
with open('./int_li.pkl', 'rb') as f:
    load_data = pickle.load(f)

with open('./str_li.pkl', 'rb') as f:
    load_data = pickle.load(f)
