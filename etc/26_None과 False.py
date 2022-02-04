# None과 False의 차이점에 대해 정리한다.

# None과 False를 한 번에 걸러내는 방법
a = None
b = False

if a:
    print('a')

if b:
    print('b')

# a, b 모두 출력되지 않는 것을 볼 수 있다.

# None
try:
    if a > 0:
        print('a')
except TypeError as e:
    print('None은 부등호를 사용해 숫자와 비교할 수 없습니다.')

# None은 부등호로 숫자(int, float)와 비교할 수 없으며 typeerror가 발생한다.
# ==, !=는 사용할 수 있다.

# False
if b > 0:
    print('b')
else:
    print('False는 부등호를 사용해 숫자와 비교할 수 있습니다.')

if b == 0:
    print('False는 0과 같은 값으로 볼 수 있습니다.')

if b > -1 and b < 1:
    print('False는 음수보다 크고, 양수보다 작습니다.')
