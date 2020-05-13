# CNN 모델을 구현할 때 image데이터의 크기가 커, 데이터 전체를 메모리에 업로드하려 하면 Memoryerror가 발생한다.
# 이는 ImageDataGenerator를 활용하여 데이터를 조금씩 메모리에 업로드하는 방법으로 해결할 수 있다.
# 전체적인 CNN 모델 구현 방법은 Image 폴더에서 불러오기 문서에 있으므로 생략

# 1. 데이터셋 불러오기, 라벨링
from keras.preprocessing.image import ImageDataGenerator

train_data = ImageDataGenerator(rescale=1./255) # 모든 픽셀을 0~1 사이의 숫자로 변환
val_data = ImageDataGenerator(rescale=1./255)
test_data = ImageDataGenerator(rescale=1./255)

train_set = train_data.flow_from_directory('C:/Users/User/Desktop/dataset/train', # train set 저장 경로
                                           target_size=(1024,1024), # image 크기 재설정 # 고화질 이미지를 학습시켜야 할 경우 이 숫자가 원본과 동일할 때도 있다
                                           batch_size=1, # 이미지를 몇 개씩 가져와 처리할지 설정 # target_size가 클수록 데이터 하나당 용량이 커져 batch_size를 줄여야 한다
                                           class_mode='categorical') # 다중분류 시 자동으로 라벨링

val_set = test_data.flow_from_directory('C:/Users/User/Desktop/dataset/test', # validation set 저장 경로
                                           target_size=(1024,1024),
                                           batch_size=1,
                                           class_mode='categorical')


test_set = test_data.flow_from_directory('C:/Users/User/Desktop/dataset/test', # test set 저장 경로
                                           target_size=(1024,1024),
                                           batch_size=1,
                                           class_mode='categorical')

# 2. model fit
history = model.fit_generator(train_set, # 모델은 위에서 미리 선언
                    steps_per_epoch=30,
                    epochs=30,
                    validation_data=val_set,
                   validation_steps=50)
