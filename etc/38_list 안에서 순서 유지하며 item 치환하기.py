# 엑셀로 데이터를 한땀 한땀 입력하다 보면 간혹 그냥 쳤을 때는 인식되지 않는 기호가 있어 사람을 빡치게 하는데,
# 시간이 없을 때면 급한 대로 ''(작은따옴표)나 ""(큰따옴표)로 묶곤 한다.
# 하지만 후에 이 데이터에서 필요한 값을 꺼낼 때 문제가 발생하는데, 특히 리스트 안에서 깂을 서치할 때 귀찮은 상황이 된다.
# 다음은 리스트 안의 item 중 일부를 치환하고 싶을 때 유용하다.

# 리스트 만들기
text_li = ['"멍멍"', '왈왈', '"으르렁"']

# 새로운 리스트 만들기
new_li = []

# 기존 리스트에서 따옴표들이 들어간 부분만 치환
for i in text_li:

        word_box = i.replace("'", '').replace('"', '')
        new_li.append(word_box)

# 값이 치환된 리스트 출력(순서 유지)
print(new_li)

# 위 방법의 장점은 item들의 순서가 그대로 유지된다는 점이다.
# 딱히 순서가 바뀌어도 상관없다면 이런 방법도 있다.

text_li = ['"멍멍"', '왈왈', '"으르렁"']
for t in text_li:
    if "'" in t:
        r_text = t.replace("'", "")
        text_li.remove(t)
        text_li.append(r_text)

    elif '"' in t:
        r_text = t.replace('"', '')
        text_li.remove(t)
        text_li.append(r_text)

print(text_li)
