# 다중 분류 기준

# colab에서 압축파일 해제하는 코드 
!unzip -uq "압축파일 위치 경로" -d "압축 해제 후 파일들을 저장할 폴더 경로" 

# 라이브러리 불러오기
import sys
import tensorflow as tf
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten,  GlobalAveragePooling2D
from keras.layers.convolutional import Conv2D, MaxPooling2D
import numpy as np

import cv2
import os
import glob

# 경로 설정
path_plus='첫 번째 분류 이미지 폴더 위치 경로' # 폴더명 변경 가능
path_zero='두 번째 분류 이미지 폴더 위치 경로'
path_minus='세 번째 분류 이미지 폴더 위치 경로'
# path_unkno='image/unknown'

la=len(os.listdir(path_zero))
lb=len(os.listdir(path_plus))
lc=len(os.listdir(path_minus))
# lc=len(os.listdir(path_unkno)) 

print('zero 경로에 저장된 파일의 개수:'+str(la))
print('plue 경로에 저장된 파일의 개수:'+str(lb))
print('minus 경로에 저장된 파일의 개수:'+str(lc))

# image 사이즈 설정
xsize=200
ysize=200

# image 전처리 함수 생성
x=[]
y=[]

from keras.preprocessing import image
import numpy as np

def read_dir(path, label):
    
    files = glob.glob(path + "/*.jpg")
    if bool(files) == False:
        files = glob.glob(path + "/*.png") 
     
    for f in files:

        try:
            img = image.load_img(f, target_size=(xsize,ysize))
            img_tr= image.img_to_array(img)        
            img_tr /= 255.
            
            y.append(label)
            x.append(img_tr)
        except:
            pass

# 함수 적용
read_dir(path_plus, 0) # 경로, 정답(숫자)
read_dir(path_zero, 1) 
read_dir(path_minus, 2) 

# numpy.array 자료형으로 변환
x=np.array(x)
y=np.array(y)


