#  tensorflow-gpu 사용하기

> tensorflow-gpu의 설치 과정을 기록한 문서이다. (`window 10`, `gpu NVIDIA Geforce GTX 1650`)

이하의 설치 및 진행과정은 노트북의 사양에 따라 달라질 수 있다. 다만 순서는 달라지지 않으므로 유의해야 한다.
사실 tensorflow-gpu의 경우 명령어 한 줄이면 설치할 수 있지만, 성공적인 설치 및 진행을 위한 준비과정이 조금 까다로운 편이다. 가장 먼저 필요한 것은 본인 컴퓨터의 GPU 버전과 회사를 확인하는 것이다. 

## 0. NVIDIA GPU 버전 확인 

> 작업 표시줄에서 마우스 오른쪽 클릭 > '작업 관리자' > '성능' 탭에서 조회 가능

노트북의 외장 그래픽은 `NVIDIA GeForce GTX 1650`로, CUDA 홈페이지의 지원 가능 목록에 추가되어있지는 않으나 사용이 가능하다. [NVIDIA 질의응답 페이지](https://forums.developer.nvidia.com/t/cuda-enabled-geforce-1650/81010/2)에 따르면 2008년 이후 출시된 모든 GPU 버전은 CUDA의 지원을 받는다고 한다. 
버전을 확인했다면 그 다음은 본격적으로 준비를 할 차례다. tensorflow-gpu를 설치하기 위해 준비해야 하는 파일은 세 가지이다. 첫 번째는 **visual studio code**, 두 번째가 **CUDA**, 세 번째가 **cuDNN**이다. 


## 1. VisualStudio2019 다운로드 및 설치
> 반드시 CUDA 전에 설치를 완료해 놓을 것! 

VisualStudio는 [공식 링크](https://visualstudio.microsoft.com/ko/vs/)를 통해 다운로드할 수 있으며, 설치 시간이 20분~30분 정도 걸릴 수 있다. 옵션의 설치는 사용자의 편의에 따르며 옵션에 따라 파일의 크기가 달라질 수 있다. 

![visualstudio](https://user-images.githubusercontent.com/58945760/95453765-69d94580-09a6-11eb-866d-50ab270d1c7f.PNG)



## 2. CUDA Toolkit 다운로드 및 설치

> window 10 운영체제를 사용할 경우 통상적으로 CUDA 10 이상의 버전을 설치하게 된다. 하지만 똑같은 10 이상 버전이라도 컴퓨터에 따라 후에 실행 시 오류가 발생할 수 있으므로 주의한다.

CUDA는 [NVIDIA 공식 웹페이지](https://developer.nvidia.com/cuda-toolkit-archive)에서 다운로드 할 수 있다. 

![cuda](https://user-images.githubusercontent.com/58945760/95452756-b885e000-09a4-11eb-8660-1a053891e9fd.PNG)



원래는 `CUDA 10.2`  버전을 설치하였으나 에러가 발생하여 `CUDA 10.1 update2` 버전을 설치하였다. `CUDA 10.1 update1`나 `CUDA 10.1`를 설치해도 에러는 발생하지 않을 것으로 보이나 업데이트를 거친 버전이 성능 면에서 더 나을 것 같아 설치했다.

## 3. cuDNN 다운로드 및 설치

`CUDA`는 파일을 받는 데 로그인이 따로 필요없었지만, `cuDNN`을 다운받으려면 NVIDIA 회원가입이 필요하다. 페이스북이나 Google 아이디로 가입할 수 있다. 여기서 끝나면 좋은데, 로그인 후 추가 설문 과정을 또(.....) 거쳐야 한다. 생각보다 번거로운 과정을 마치고 나면 아래와 같은 화면이 뜰 것이다. 

![cudnn](https://user-images.githubusercontent.com/58945760/95453330-9b9ddc80-09a5-11eb-8c5d-117539d1556f.PNG)

Archived cuDNN Releases를 클릭하면 8.0.4 이하 버전도 모두 볼 수 있다. 물론 다운로드도 가능하다. `cuDNN` 버전마다 옆에 호환되는 `CUDA` 버전을 확인할 수 있으니 참고하면 된다. 원래는 `cuDNN 8.0.3` 버전을 받아 설치 시도해보았으나 에러가 발생하여 `cuDNN 7.6.5` 버전을 내려받아 다시 설치를 진행하였다. 

## 4. cuDNN 세팅

`cuDNN`을 다운로드하면 zip파일 하나가 다운로드된다. 이후의 과정은 다음을 따르면 된다. 

- `cuDNN` zip 파일의 압축을 풀어준다.  

- **"C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v10.1\"** 경로를 따라 아래의 화면이 보이도록 한다. 아래 화면은 cuDNN이 설치된 상태이므로 설치되기 전과는 달라 보일 수 있다. 하지만 가장 위에 있는 폴더가 bin이라면 제대로 온 것이다!

  ![cudnn 덮어씌우기](https://user-images.githubusercontent.com/58945760/95454339-495dbb00-09a7-11eb-988c-b7b36d16c84e.PNG)

- 압축을 푼 cudnn 파일 안에는 cuda 폴더가 있다. 해당 폴더 안의 모든 파일을 복사하여 위의 위치(**"C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v10.1\"**)에 붙여넣는다.



이걸로 cuDNN 설치도 완료되었다. 이제 cmd를 열어 본격적으로 tensorflow-gpu를 설치해보자.

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

설치가 완료되었을 때의 cmd 화면은 다음과 같다. 메시지 밑에 name: [GPU 모델명]이 제대로 나오는지 확인해야 한다.

![gpu 설치 완료](https://user-images.githubusercontent.com/58945760/95454969-1ec03200-09a8-11eb-8e7a-b68db37341dc.PNG)



jupyter notebook에서의 GPU 실행 확인 화면은 다음과 같다. 

![gpu 사용 확인](https://user-images.githubusercontent.com/58945760/95454942-12d47000-09a8-11eb-9010-81cb52ef5472.PNG)

True가 나온다면 마침내 tensorflow-gpu가 제대로 설치된 것이다! 이제 MNIST 예제 등을 사용하여 CPU일 때와 속도를 비교해보자. 한참 빨라진 속도에 놀랄 것이다!