a = [1, 2, 3]
b = a
c = [1, 2, 3]
d = [4, 5]

# is(값이 동일한 같은 'object'일 때 True)
print(a is b)  # True
print(a is c)  # False # 값은 같지만 다른 객체이므로 False
print(a is d)  # False # 값도 다르고 다른 객체이므로 False

# =
print(a == b)  # True
print(a == c)  # True
print(a == d)  # False

# is not
print(a is not b)
print(a is not c)
print(a is not d)

# !=
print(a != b)
print(a != c)
print(a != d)
