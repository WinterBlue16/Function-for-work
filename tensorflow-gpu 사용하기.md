#  tensorflow-gpu 사용하기

> tensorflow-gpu의 설치 과정을 기록한 문서이다. (`window 10`, `gpu NVIDIA Geforce GTX 1650`)

이하의 설치 및 진행과정은 노트북의 사양에 따라 달라질 수 있다. 다만 순서는 달라지지 않으므로 유의해야 한다.
사실 tensorflow-gpu의 경우 명령어 한 줄이면 설치할 수 있지만, 성공적인 설치 및 진행을 위한 준비과정이 조금 까다로운 편이다. 가장 먼저 필요한 것은 본인 컴퓨터의 GPU 버전과 회사를 확인하는 것이다. 

## 0. NVIDIA GPU 버전 확인 

> '작업 관리자' > '성능' 탭에서 조회 가능

노트북의 외장 그래픽은 `NVIDIA GeForce GTX 1650`로, CUDA 홈페이지의 지원 가능 목록에 추가되어있지는 않으나 사용이 가능하다. [NVIDIA 질의응답 페이지](https://forums.developer.nvidia.com/t/cuda-enabled-geforce-1650/81010/2)에 따르면 2008년 이후 출시된 모든 GPU 버전은 CUDA의 지원을 받는다고 한다. 
버전을 확인했다면 그 다음은 본격적으로 준비를 할 차례다. tensorflow-gpu를 설치하기 위해 준비해야 하는 파일은 세 가지이다. 첫 번째는 **visual studio code**, 두 번째가 **CUDA**, 세 번째가 **cuDNN**이다. 


## 1. VisualStudio2019 다운로드 및 설치
> 반드시 CUDA 전에 설치를 완료해 놓을 것! 

VisualStudio는 [공식 링크](https://visualstudio.microsoft.com/ko/vs/)를 통해 다운로드할 수 있으며, 설치 시간이 20분~30분 정도 걸릴 수 있다. 옵션의 설치는 사용자의 편의에 따르며 옵션에 따라 파일의 크기가 달라질 수 있다. 



## 2. CUDA 다운로드 및 설치

> window 10 운영체제를 사용할 경우 통상적으로 CUDA 10 이상의 버전을 설치하게 된다. 하지만 똑같은 10 이상 버전이라도 컴퓨터에 따라 후에 실행 시 오류가 발생할 수 있으므로 주의한다.

CUDA 10.2

CUDA 10.1 update2(설치 버전)

CUDA 10.1 update1

CUDA 10.1

## 3. cuDNN 다운로드 및 설치

cuDNN 8.0.3

cuDNN 7.6.5(설치 버전)

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

jupyter notebook screen shot