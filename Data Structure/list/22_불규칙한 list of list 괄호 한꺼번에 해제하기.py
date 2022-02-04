"""
리스트 자료형을 다루다 보면 규칙적인 list of list(리스트 안의 리스트)도 존재하지만(ex. [[2,3], [5,6]]), 
불규칙한 경우도 존재할 수 있다.(ex. [1, [2], [3, [4]]])
이 경우 중첩된 리스트의 괄호들을 모두 제거하여 깨끗한 하나의 리스트로 만들 때 쓰이는 함수이다. 
"""

from collections.abc import Iterable


def flatten_irregular_list(lst):
    for el in lst:
        if isinstance(el, Iterable) and not isinstance(el, (str, bytes)):
            yield from flatten_irregular_list(el)
        else:
            yield el

# print(list(flatten_irregular_list([1, [2], [[3]]])))
