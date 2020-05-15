import sys
import os
import glob
import cv2, numpy as np

path = glob.glob('C:/Users/user/Desktop/dataset_imageprocessing/train/E03/*.jpg') # 해당 경로 내 모든 이미지 불러오기

i = 0
for img in path: # 경로 내에 있는 이미지를 하나씩 꺼냄
    src = cv2.imread(img) # 이미지 numpy 배열로 불러옴
    cascade_file = 'haarcascade_frontface.xml' # 얼굴 검출 파일 가져오기
    cascade = cv2.CascadeClassifier(cascade_file)

    face_list = cascade.detectMultiScale(src) # 여기서는 컬러 이미지 그대로 넣었지만 BGR2GRAY로 그레이스케일해서 넣는 것도 가능

    for (x,y,w,h) in face_list: # 얼굴 좌표가 검출된 모든 이미지
        print('얼굴 검출에 성공했습니다.') # 검출 성공 메시지 출력
        roi = src[y:y+h, x:x+w] # 얼굴 좌표 부분만 선택
        if roi.shape[0] < 150 or roi.shape[1] < 150 : # 만약 얼굴이 아닌 다른 물체가 검출되었을 경우를 방지
            pass
#       imagex = cv2.resize(roi, (400, 400)) # resize도 가능
        else:
            print(roi.shape)
            cv2.imwrite(f'C:/Users/user/Desktop/roi/train/E03/{i * 1}.jpg', roi) # 파일 경로 지정, 파일명 지정
            print('사진을 저장했습니다.') # 저장 완료 메시지 출력
            i += 1
