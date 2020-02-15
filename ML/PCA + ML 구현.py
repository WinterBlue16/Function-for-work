#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# PCA(차원축소)가 포함된 ML 기본 코드

# 0. 라이브러리 불러오기
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report


# 1. 데이터 읽어들이기
df = pd.read_csv(, encoding='utf-8', thousands=',') # excel, json  # encoding='cp949'


# 2. 데이터 전처리하기
y = df['']
x = df.drop('', axis=1)


# 3. 데이터 나누기(train, test)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

'''
# 3-1. 다중 분류 시 One-hot Encoding
# sklearn
from sklearn.preprocessing import OneHotEncoder

onehot_encoder = OneHotEncoder()
y_train = y_train.reshape(len(y_train), -1) 
y_test = y_test.reshape(len(y_test), -1)

y_train = onehot_encoder.fit_transform(y_train)
y_test = onehot_encoder.fit_transform(y_test)

# keras == 1.14
from keras.utils import np_utils
y_train = np_utils.to_categorical(y_train)
y_val = np_utils.to_categorical(y_val)

# keras == 2.0
from tensorflow.keras.utils import to_categorical

y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

'''

# 4. Scaler 적용
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
scaler.fit(x_train)
x_train_scaled = scaler.transform(x_train)

from sklearn.decomposition import PCA
pca = PCA(n_components=) # 축소해 새로 만들 column 수 # 여러 숫자를 대입하며 acc 비교할 것
pca.fit(x_train_scaled)

x_pca = pca.transform(x_train_scaled)
# print("원본 데이터 형태 :", x_train_scaled.shape)
# print("축소된 데이터 형태 :", x_pca.shape)


# 5. 모델 선택하기
# 5-1. classifier 알고리즘 전부 추출
warnings.filterwarnings('ignore')
allAlgorithms = all_estimators(type_filter='classifier') 

print(allAlgorithms)
print(len(allAlgorithms))
print(type(allAlgorithms))

for (name, algorithm) in allAlgorithms:
    # 각 알고리즘 객체 생성하기-------------(*2)
    model = algorithm()
    
    # 학습하고 평가하기---------------------(*3)
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)
    print(name, "의 정답률 = ", accuracy_score(y_test, y_pred))


from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier()


# 6. 모델 훈련시키기
model.fit(x_train, y_train)


# 7. 평가 검증하기
score = model.score(x_test, y_test) 
print("score : %.2f"% score)

y_pred = model.predict(x_test)
print("Accuracy : %.2f" % accuracy_score(y_pred, y_test)) 


# 8. classification report
print(classification_report(y_test, y_pred))

