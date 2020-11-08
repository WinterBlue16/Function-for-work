# tensorflow-gpu 설치 중 발생 에러 보고

> 설치 중 발생한 에러들에 대해 정리한 문서이다. 

![밑줄](https://user-images.githubusercontent.com/58945760/95451120-49a78780-09a2-11eb-8159-cd7d4daf1a68.jpg)

## tf.test.is_gpu_available() = False

> 설치 중 발생했던 에러들은 모두 `cuDNN`과 `CUDA`의 버전이 맞지 않아 발생한 것들이었다.

### 1. cudart64_101.dll not found

원인 :  `CUDA`의 버전이 맞지 않아 생기는 오류이다.  `CUDA 10.2` 버전을 설치했을 때 발생하였다.  

해결 방법 : 설치한 `CUDA`를 삭제하고,  `CUDA` 웹페이지에서 `CUDA 10.1 Update 2` 버전을 다시 다운로드하여 설치하였다. 

### 2. cudnn64_7.dll not found

원인 : `cuDNN`의 버전이 맞지 않아 생기는 오류이다. `cuDNN 8.0.3` 버전을 설치하였을 때 발생하였다. 

해결 방법 : `cuDNN` 파일을 모두 삭제한 후, `cuDNN 7.6.5 버전`을 다시 다운로드한 후 다시 설치한 `CUDA` 폴더에 덮어씌워 해결하였다. 

해결 후의 정상적인 설치 진행에 대해서는 [이 문서](https://github.com/WinterBlue16/Function-for-work/blob/master/tensorflow-gpu%20%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0.md#tensorflow-gpu-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0)에서 확인할 수 있다. 

