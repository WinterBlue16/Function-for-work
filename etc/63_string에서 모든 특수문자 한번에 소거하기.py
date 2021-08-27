# 특수문자가 섞여 있는 문자열에서 한 번에 모든 특수문자를 소거하고 싶을 때 사용
import re
import string

sample_string = '@@#$g5a%^anslhlk2*(^*(*))(!'


def punctuation_marks_filter(text):
    punctuation_marks_filter = re.compile(
        '[%s]' % re.escape(string.punctuation))
    filter_string = punctuation_marks_filter.sub('', text)

    return filter_string


print(punctuation_marks_filter(sample_string))
