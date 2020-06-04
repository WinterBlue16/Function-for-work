# 여러 개의 함수를 정의하고 중첩하여 활용하여야 할 때, 연산에 필요한 변수를 재정의하기 번거로울 때가 있다.
# 앞에서 정의했던 함수 안에 정의를 해 놨었는데 이걸 또 복붙해야 하나 싶을 때,
# global 함수를 활용하면 다른 함수 정의 시 사용했던 변수를 그대로 가져와 편하게 사용할 수 있다.

# 전역 변수 설정
global test_title

# 함수 1 정의
def function1(title_1):
    global test_title
    test_title = title_1
    print(test_title)

# 함수 2 정의
def function2(title_2):
    global test_title
    if test_title != title_2:
        print('test_title은 그대로입니다.')
        print(test_title)

# 변수 시험해보기
function1('제목 1')
>>> 제목 1

function2('제목 3')
>>> test_title은 그대로입니다
    제목 1
