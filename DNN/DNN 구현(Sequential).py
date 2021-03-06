
# 빠르게 DeepLearning을 구현하기 위한 준비 코드

# 0. 기본 라이브러리 불러오기
import numpy as np
import pandas as pd

# 1. 데이터 읽어들이기
df = pd.read_csv(, encoding='utf-8', thousands=',')

# 2. 데이터 전처리하기
x = df['']
y = df['']

x = x.values
y = y.values

# 3. 데이터 나누기(trian, test)
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, shuffle=True)

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

# 4. 모델 생성하기
from keras.models import Sequential
from keras.layers import Dense, BatchNormalization, Dropout

model = Sequential()

model.add(Dense(256, input_shape=())) # input_dim=
model.add(Dense(256))
model.add(Dense(256))
model.add(Dense(1))


# 5. 모델 훈련시키기 
model.compile(loss='mse', 
              optimizer='adam',
              metrics=['mae'])
hist = model.fit(,epochs=,batch_size=, validation_split=)

# 6. 평가 검증하기
loss, mae = model.evaluate()
print('loss :', loss)
print('mae :', mae)

# 7. matplotlib으로 시각화
import matplotlib.pyplot as plt

plt.plot(hist.history['loss'])
plt.plot(hist.history['val_loss'])
plt.plot(hist.history['acc'])
plt.plot(hist.history['val_acc'])
plt.title('DACON DNN loss, acc')
plt.xlabel('epoch')
plt.ylabel('loss, acc')
plt.legend(['train loss', 'test loss', 'train acc', 'test acc'])
plt.show()


# 8. R2, RMSE로 모델 평가하기
from sklearn.metrics import mean_squared_error, r2_score
y_pred = model.predict(x_test, batch_size=)

def RMSE(i, j):
    rmse = np.sqrt(mean_squared_error(i, j))
    return rmse
print("RMSE :", RMSE(y_test, y_pred)) 


R2 = r2_score(y_test, y_pred)
print("R2 :", R2)


# 9. 모델 저장하기
model.save('./save/DNN_model01.h5') # 경로 수정
print('저장 완료')

