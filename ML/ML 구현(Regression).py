
# 빠르게 ML model(Regression)을 구현하기 위한 준비 코드

# 0. 라이브러리 불러오기
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

# 1. 데이터 읽어들이기
df = pd.read_csv(, encoding='utf-8', thousands=',') # excel, json

# 2. 데이터 전처리하기
y = df['']
x = df.drop('', axis=1)
 
# 3. 데이터 나누기(train, test)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

# 4. 모델 선택하기
# 4-1. regressor 알고리즘 전부 추출
from sklearn.utils.testing import all_estimators

allAlgorithms = all_estimators(type_filter='regressor') 

print(allAlgorithms)
print(len(allAlgorithms))
print(type(allAlgorithms))

for (name, algorithm) in allAlgorithms:

    model = algorithm()
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)
    print(name, "의 loss = ", r2_score(y_test, y_pred))

# 5. 모델 훈련시키기
model.fit(x_train, y_train)

# 6. 평가 검증하기
loss = r2_score(y_pred, y_test) 
print("loss : %.2f"% loss)

y_pred = model.predict(x_test)
print("loss : %.2f" % r2_score(y_pred, y_test)) 


