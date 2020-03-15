
# 빠르게 ML model(classification)을 구현하기 위한 준비 코드

# 0. 라이브러리 불러오기
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report


# 1. 데이터 읽어들이기
df = pd.read_csv(, encoding='utf-8', thousands=',') # excel, json


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

# 4. 모델 선택하기
# 4-1. classifier 알고리즘 전부 추출
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


# 5. 모델 훈련시키기
model.fit(x_train, y_train)


# 6. 평가 검증하기
score = model.score(y_pred, y_test) 
print("score : %.2f"% score)

y_pred = model.predict(x_test)
print("Accuracy : %.2f" % accuracy_score(y_pred, y_test)) 


# 7. classification report
print(classification_report(y_test, y_pred))