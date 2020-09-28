#  tensorflow-gpu 사용하기

> tensorflow-gpu의 설치 과정을 기록한 문서이다. 



## 0. NVIDIA GPU 버전 확인 

> '작업 관리자' > '성능' 탭에서 조회 가능

NVIDIA GeForce GTX 1650 



## 1. VisualStudio2019 다운로드 및 설치



## 2. CUDA 다운로드 및 설치

CUDA 10.2

CUDA 10.1 update2

CUDA 10.1 update1

CUDA 10.1

## 3. cuDNN 다운로드 및 설치

cuDNN 8.0.3

cuDNN 7.6.5

## 4. cuDNN 세팅

cuDNN zip 압축 풀고 CUDA toolkit 내 cuda 폴더 안에 붙여넣기

## 5. 가상환경 생성 및 tensorflow-gpu 설치

```shell
# tensorflow-gpu 설치
$ conda install tensorflow-gpu
$ pip install tensorflow-gpu

# cmd에서 라이브러리와 gpu가 제대로 세팅되었는지 확인
$ python 
```

```python
import tensorflow as tf
tf.__version__ # 버전 확인, '2.1.0'

from tensorflow.python.client import device_lib
device_lib.list_local_devices()

tf.test.is_gpu_available()
# cmd와 jupyter notebook cell에서 모두 True값이 나와야 함
```



## 6. 결과