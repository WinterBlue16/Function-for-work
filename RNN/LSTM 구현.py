# 빠르게 RNN(LSTM)을 구현하기 위한 준비 코드

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

# 4. 모델 생성하기
from keras.models import Model
from keras.layers import Input, LSTM, Dense, BatchNormalization, Dropout

input1 = Input(shape=())
dense1 = LSTM(256, activation='relu', return_sequences=True)(input1) 
dense1 = LSTM(256, activation='relu', return_sequences=False)(danse1) 
dense1 = Dense(256)(dense1) 
dense1 = Dense(256)(dense1) 
output1 = Dense(1)(dense1)

model = Model(inputs=, outputs=)

# 5. 모델 훈련시키기 
model.compile(loss='mse', 
              optimizer='adam',
              metrics=['mae'])
model.fit(,epochs=,batch_size=, validation_split=)

# 6. 평가 검증하기
loss, mae = model.evaluate()
print('loss :', loss)
print('mae :', mae)

from sklearn.metrics import mean_squared_error, r2_score
y_pred = model.predict(x_test, batch_size=)

def RMSE(i, j):
    rmse = np.sqrt(mean_squared_error(i, j))
    return rmse
print("RMSE :", RMSE(y_test, y_pred)) 


R2 = r2_score(y_test, y_pred)
print("R2 :", R2)


# 7. 모델 저장하기
model.save('./save/DNN_model01.h5') # 경로 수정
print('저장 완료')

