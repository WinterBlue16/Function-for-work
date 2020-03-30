# 이진분류 기준
from keras.preprocessing.image import ImageDataGenerator

train_data = ImageDataGenerator(rescale=1./255, # 모든 픽셀을 0~1 사이의 숫자로 변환
                                shear_range=0.2,
                                zoom_range=0.2,
                                horizontal_flip=True)
test_data = ImageDataGenerator(rescale=1./255)
train_set = train_data.flow_from_directory('C:/Users/User/Desktop/dataset/train', # train image 폴더 저장 경로
                                           target_size=(100,100), # image 크기 재설정
                                           batch_size=1,
                                           class_mode='binary') # 이진분류 시

test_set = test_data.flow_from_directory('C:/Users/User/Desktop/dataset/test', # test image 폴더 저장 경로
                                           target_size=(100,100), # image 크기 재설정
                                           batch_size=1,
                                           class_mode='binary') # 이진분류 시

model.fit_generator(train_set, # 모델은 위에서 미리 선언해둠
                    steps_per_epoch=30,
                    epochs=30,
                    validation_data=test_set,
                   validation_steps=50)