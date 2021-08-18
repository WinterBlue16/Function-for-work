# 변수가 내가 작성한 코드 내에 존재하는지 확인하고 싶을 때
# 변수 생성
my_variable = 'my variable'

# 함수 생성


def function():
    global y
    y = 1
    # if 'y' in locals():
    #     print(True)
    return y


function()

# in local
if 'my_variable' in locals():
    print(True)

if 'y' in locals():
    print(True)

# in global
if 'my_variable' in globals():
    print(True)

if 'y' in globals():
    print(True)

# catch nameerror
try:
    my_variable
    print(my_variable)
except NameError as e:
    my_variable = None


# 함수 내부에서 global로 정의했을 경우 locals()에서는 False가 나온다. 하지만 함수 바깥에서는 locals(), globals() 전부 True값이다.
