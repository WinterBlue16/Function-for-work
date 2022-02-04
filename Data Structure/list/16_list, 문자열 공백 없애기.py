# list의 item, 크롤링 후 문자열에서 공백을 없애고 싶을 때

sample = '      boring      ' # '  bo    r in    g  '
sample_li = ['    fly ', '   to    ', 'the     ', '      sky']

# 문자열에서 공백 없애기
print(sample.strip())

# list item별 공백 없애기
strip_li = []
for i in sample_li:
    i = i.strip()
    strip_li.append(i)
print(strip_li)