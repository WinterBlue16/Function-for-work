# 이진분류(binary classification) 기준
# ImageDataGenerator를 사용해 CNN을 구동할 때의 code를 설명한다

# 0. 라이브러리 불러오기(ImageDataGenerator 제외)
import numpy as np
from keras.models import Sequential, Model
from keras.layers import Dense, Conv2D, MaxPooling2D, Flatten, Dropout, BatchNormalization, Activation
from keras.optimizers import Adam


# 1. 모델링
nb_classes = 2 # 분류할 클래스 수

model = Sequential()
model.add(Conv2D(64, (2, 2), padding='same',
                 input_shape=(10, 10, 1), strides=2))
model.add(BatchNormalization())
model.add(Activation('relu'))

model.add(Conv2D(128, (2, 2), padding='same'))
model.add(BatchNormalization())
model.add(Activation('relu'))
model.add(MaxPooling2D(2, 2)))

model.add(Conv2D(256, (2, 2), padding='same'))
model.add(BatchNormalization())
model.add(Activation('relu'))
model.add(Dropout(0.3))

model.add(Flatten())
model.add(Dense(nb_classes, activation='softmax'))
# model.add(Dense(nb_classes, activation='sigmoid'))


opt = Adam(lr=0.0001) # learning rate 조정
model.complie(optimizer=opt, loss='binary_crossentropy', metrics=['accuracy'])


# 2. 데이터셋 불러오기, 라벨링
from keras.preprocessing.image import ImageDataGenerator

train_data = ImageDataGenerator(rescale=1./255) # 모든 픽셀을 0~1 사이의 숫자로 변환
val_data = ImageDataGenerator(rescale=1./255)
test_data = ImageDataGenerator(rescale=1./255)

train_set = train_data.flow_from_directory('C:/Users/User/Desktop/dataset/train', # train set 저장 경로
                                           target_size=(100,100), # image 크기 재설정
                                           batch_size=1, # 이미지를 몇 개씩 가져와 처리할지 설정
                                           class_mode='binary') # 다중분류 시 자동으로 라벨링

val_set = test_data.flow_from_directory('C:/Users/User/Desktop/dataset/test', # validation set 저장 경로
                                           target_size=(100,100),
                                           batch_size=1,
                                           class_mode='binary')


test_set = test_data.flow_from_directory('C:/Users/User/Desktop/dataset/test', # test set 저장 경로
                                           target_size=(100,100),
                                           batch_size=1,
                                           class_mode='binary')

# 3. model fit
history = model.fit_generator(train_set, # 모델은 위에서 미리 선언
                    steps_per_epoch=30,
                    epochs=30,
                    validation_data=test_set,
                   validation_steps=50)

# 4. 시각화
import matplotlib.pyplot as plt

plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])

plt.title('CNN model loss, acc')
plt.xlabel('epoch')
plt.ylabel('loss, acc')
plt.legend(['train loss', 'test loss', 'train acc', 'test acc'])
plt.show()

# 5. predict
pred = model.predict_generator(test_set)

# 6. model 저장
model.save('C:/Users/User/Desktop/save/CNN_example(binary).h5')
print('모델 저장이 완료되었습니다.')
