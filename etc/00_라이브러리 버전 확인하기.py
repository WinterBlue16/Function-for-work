# 설치된 라이브러리의 버전을 확인하고 싶을 때
# 방법 1 
pip freeze 

# 방법 2 
# 확인하고 싶은 라이브러리를 import한 후 실행
import urllib.request 
import keras as k
import tensorflow as tf
import pandas as pd
import numpy as np
import cv2

print('request 버전 :' + urllib.request.__version__)
print('keras 버전 :' + k.__version__)
print('tensorflow 버전 :' + tf.__version__)
print('pandas 버전 :' + pd.__version__)
print('numpy 버전 :' + np.__version__)
print('OpenCV 버전 :' + cv2.__version__)

