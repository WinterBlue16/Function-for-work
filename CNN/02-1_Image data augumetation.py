# ImageDataGenerator로 데이터를 증식하는 방법과 함수 내 중요 parametor를 설명
# 전체 CNN 모델 구성 과정은 이전 문서에 있으므로 생략

# 0. 라이브러리 불러오기
from keras.preprocessing.image import ImageDataGenerator

# 1-1. 이진 분류(binary classification)
train_data = ImageDataGenerator(rescale=1./255, # 모든 픽셀을 0~1 사이의 숫자로 변환
                                rotation_range = 90, # 지정된 각도(0。~ 90。) 내에서 임의로 원본 이미지 회전
                                width_shift_range = 0.1, # 수평 방향(가로)로 전체 픽셀의 0.1만큼 임의로 원본 이미지 이동
                                height_shift_range = 0.1, # 위와 같은 원리로 수직 방향으로 이동
                                shear_range = 0.2,  # 지정한 강도 내에서 시계 반대방향으로 원본 이미지 변형
                                zoom_range = 0.2, # 지정한 범위 내에서 임의로 원본 이미지 확대(1+0.2=1.2)/축소(1-0.2=0.8)
                                horizontal_flip = True, # 수평 방향으로 뒤집기
                                vertical_flip = True, # 수직 방향으로 뒤집기
                                fill_mode = 'nearest') # 이미지를 회전, 변형했을 때 셍기는 공간을 채우는 방식
test_data = ImageDataGenerator(rescale=1./255)
train_set = train_data.flow_from_directory('C:/Users/User/Desktop/dataset/train', # train image 폴더 저장 경로
                                           target_size=(100,100), # image 크기 재설정
                                           batch_size=1,
                                           class_mode='binary')

test_set = test_data.flow_from_directory('C:/Users/User/Desktop/dataset/test', # test image 폴더 저장 경로
                                           target_size=(100,100),
                                           batch_size=1,
                                           class_mode='binary')

model.fit_generator(train_set, # 모델은 위에서 미리 선언해둠
                    steps_per_epoch=30,
                    epochs=30,
                    validation_data=test_set,
                   validation_steps=50)


# 다중 분류(Multiple classification)
from keras.preprocessing.image import ImageDataGenerator

train_data = ImageDataGenerator(rescale=1./255, # 모든 픽셀을 0~1 사이의 숫자로 변환
                                rotation_range = 90, # 지정된 각도(0。~ 90。) 내에서 임의로 원본 이미지 회전
                                width_shift_range = 0.1, # 수평 방향(가로)로 전체 픽셀의 0.1만큼 임의로 원본 이미지 이동
                                height_shift_range = 0.1, # 위와 같은 원리로 수직 방향으로 이동
                                shear_range = 0.2,  # 지정한 강도 내에서 시계 반대방향으로 원본 이미지 변형
                                zoom_range = 0.2, # 지정한 범위 내에서 임의로 원본 이미지 확대(1+0.2=1.2)/축소(1-0.2=0.8)
                                horizontal_flip = True, # 수평 방향으로 뒤집기
                                vertical_flip = True, # 수직 방향으로 뒤집기
                                fill_mode = 'nearest') # 이미지를 회전, 변형했을 때 셍기는 공간을 채우는 방식
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


# 2. 참고 사이트
# https://tykimos.github.io/2017/06/10/CNN_Data_Augmentation/
# https://keraskorea.github.io/posts/2018-10-24-little_data_powerful_model/
