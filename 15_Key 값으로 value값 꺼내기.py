# 지역-지역번호, 성-이름처럼 dict 자료형을 만들었을 때, key값만 가지고 value값을 꺼내고 싶을 경우
# 예시 1
text_dict = {'저기':'응?', '뭐해' : '그냥 있어', '볼래?' : '어디서?', '갈까?':'내가 갈게'}

key =  input()
print(text_dict.get(key)) # get(key, 디폴트값) # 해당 key에 value가 없을 경우 디폴트값이 출력

# 예시 2
heroine_dict = {'제인 에어':'제인 에어', '광막한 사르가소 바다':'앙투아네트 메이슨', 
               '폭풍의 언덕':'캐서린 언쇼' , '오만과 편견':'엘리자베스 베넷', '안네의 일기':'안네 프랑크'}
key = input()
print(heroine_dict.get(key))