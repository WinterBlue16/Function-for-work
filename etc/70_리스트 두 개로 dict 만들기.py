# 두 개의 리스트를 각각 key, value로 하여 dict를 생성
dessert = ['쿠키', '마들렌', '마카롱', '케이크']
num = [1,2,3,4]

dessert_dic = { name: value for name, value in zip(dessert, num) }
print(dessert_dic)