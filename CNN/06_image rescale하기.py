# imagegenerator를 써서 모델링을 잘 했는데도 predict를 하면 그 결과가 나오지 않을 때가 있다.
# 그럴 때는 반드시 rescale 여부를 확인하자.

from keras.models import load_model
import numpy as np
import cv2

model = load_model('./cnn0515(imagegenerator, 200, haar cascade).h5') # 예시 코드

sample_image = cv2.imread("./photo.PNG") # 예시 png 파일
image_rescale = sample_image.astype('float32')/255
image_resize =  cv2.resize(image_rescale, (200, 200)) # resize 순서는 바뀌어도 상관없다!

pred = model.predict(image_resize)
print(pred)
