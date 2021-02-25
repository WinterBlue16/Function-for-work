# y 값(target, label)이 편중되어 있을 경우 사용
# wine data 예시(https://github.com/WinterBlue16/Function-for-work/blob/master/Bad%20example%20of%20y_data.png?raw=true)
import pandas as pd
import numpy as np

# 데이터 읽어들이기
wine = pd.read_csv("./data/winequality-white.csv", 
                   sep=";", encoding='utf-8', header=0)

# Input 데이터, Output 데이터로 분리
y = wine['quality']
x = wine.drop('quality', axis=1)

y = y.values
x = x.values

# y 값(=output) 변경
newlist = []
for v in list(y):
    if v <= 4:
        newlist += [0]
    elif v <= 7:
        newlist += [1]
    else:
        newlist += [2]
y = newlist

# y의 column이 더 많은 경우 범주를 더 나눌 필요 있음
# 이 뒤로는 sklearn을 이용해 train, test set으로 나눠주면 ok