"""
특수문자가 섞여 있는 문자열에서 한 번에 모든 특수문자를 소거하고 싶을 때 사용

"""
import re
import string


sample_string = '@@#$g5a%^anslhlk2*(^*(*))(!'


# 방법 1
def punctuation_marks_filter(text):
    punctuation_marks_filter = re.compile(
        '[%s]' % re.escape(string.punctuation))
    filter_string = punctuation_marks_filter.sub('', text)

    return filter_string


print(punctuation_marks_filter(sample_string))


# 방법 2
def remove_punctuation_marks(text):
    for p in sample_string:
        if p in text:
            text = text.replace(p, '')

    return text


# 방법 3
punctuation_marks = ['~', '@', '#', '$', '%', '^', '&',
                     '*', '(', ')', '+', '-', ';', ':', '/', ',', '.']


def filter_punctuation_marks(text, punctuation_marks=punctuation_marks):
    punctuation_marks = ''.join(punctuation_marks)
    filtered_text = re.sub('['+punctuation_marks+']', '', text)
    print(filtered_text)
    return filtered_text
