# 변수가 내가 작성한 코드 내에 존재하는지 확인하고 싶을 때
my_variable = 'my variable'

# in local
if 'my_variable' in locals():
    print(True)

# in global
if 'my_variable' in globals():
    print(True)

# catch nameerror
try:
    my_variable
    print(my_variable)
except NameError as e:
    my_variable = None
