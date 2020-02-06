
# 빠르게 Ensamble model을 구현하기 위한 준비 코드

# 0. 기본 라이브러리 불러오기
import numpy as np
import pandas as pd

# 1. 데이터 읽어들이기
df1 = pd.read_csv(, encoding='utf-8', thousands=',')
df2 = pd.read_csv(, encoding='utf-8', thousands=',')

# 2. 데이터 전처리하기
x = df['']
y = df['']

x = x.values
y = y.values

# 3. 데이터 나누기(trian, test)
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, shuffle=True)

# 4. 모델 생성하기
from keras.models import Sequential, Model
from keras.layers import Input, LSTM, Dense, BatchNormalization, Dropout

# Sequential 
model = Sequential()

model.add(Dense(256, input_shape=())) # input_dim=
model.add(Dense(256))
model.add(Dense(256))
model.add(Dense(1))

# Function model 1
input1 = Input(shape=())
dense1 = Dense(256)(input1) 
dense1 = Dense(256)(dense1) 
dense1 = Dense(256)(dense1) 
output1 = Dense(1)(dense1)

# Function model 2
input2 = Input(shape=())
dense2 = Dense(256)(input2) 
dense2 = Dense(256)(dense2) 
dense2 = Dense(256)(dense2) 
output2 = Dense(1)(dense2)

# Concatenate
from keras.layers.merge import concatenate
merge1 = concatenate([output1,output2])

# ensamble model 1
dense3 = Dense(256)(merge1) 
dense3 = Dense(256)(dense3) 
dense3 = Dense(256)(dense3) 
output3 = Dense(1)(dense3)

# ensamble model 2
dense4 = Dense(256)(merge1) 
dense4 = Dense(256)(dense4) 
dense4 = Dense(256)(dense4) 
output4 = Dense(1)(dense4)


model = Model(inputs=[,], outputs=[,])

# 5. 모델 훈련시키기 
model.compile(loss='mse', 
              optimizer='adam',
              metrics=['mae'])
model.fit(,epochs=,batch_size=, validation_split=)

# 6. 평가 검증하기
result = model.evaluate([],[], batch_size=) # y값의 갯수에 따라 변수가 다수가 될 수 있음
print(result)

from sklearn.metrics import mean_squared_error, r2_score
y_pred = model.predict([], batch_size=)

def RMSE(i, j):
    rmse = np.sqrt(mean_squared_error(i, j))
    return rmse
rmse_list = [RMSE(,[0]), RMSE(,[1])] # x값(input)이 여러 개일 경우
rmse = np.mean(rmse)
print("RMSE :", rmse) 

R2_list = [r2_score(,[0]), r2_score(,[1])]
R2 = np.mean(R2_list)
print("R2 :", R2)


# 7. 모델 저장하기
model.save('./save/ensamble_model01.h5') # 경로 수정
print('저장 완료')

