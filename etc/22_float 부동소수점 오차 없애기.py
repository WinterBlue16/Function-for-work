'''
float 연산에서 발생하는 부동소수점 오차를 없애는 라이브러리와 그 활용법
'''
import decimal

a = 0.12
b = 1.78

# 통상적인 연산(오차 위험 있음)
normal = b-a
print(normal)

# decimal 활용
different = float(decimal.Decimal(b)-decimal.Decimal(a))
print(different)
