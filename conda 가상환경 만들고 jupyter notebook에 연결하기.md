# conda 가상환경 생성 및 jupyter notebook에 연결하기

> 코딩할 때 사용하는 라이브러리의 버전은 매우 중요하다. 함수 형태가 바뀔 가능성이 있는 것은 물론 이전 버전에서 멀쩡히 존재하던 함수가 최근 업데이트 된 버전에서 없어지는 일도 있다. 이런 예시로는 `tensorflow`가 있다. 딥러닝에서 자주 사용되는 라이브러리 중 하나인 `keras`는 `tensorflow 2.0`이 나오면서 아예 그 안에 포함된 상태(tf. keras)가 되었다. 
>
> 단순하게 보면 가장 최근에 나온 버전의 라이브러리를 쓰는 것이 좋아보일지 모르지만, 과거에 작성한 코드를 참고해야 하거나 아직 해당 버전의 라이브러리가 보편적으로 쓰이지 않아 구글링이 용이하지 않을 때, 혹은(이게 가장 큰 이유일지도 모른다) 내게 예전 버전의 라이브러리가 더 쓰기 편할 때는 과거에 나온 버전을 더 선호하게 된다. 
>
> 결국 케바케라는 것인데, 여기서 고민이라고 할까 어떤 욕심이 슬그머니 생긴다. 과거 버전의 라이브러리, 최근에 나온 라이브러리가 설치된 환경을 만들어 놓고, 필요한 상황에 따라 바로바로 바꿔서 써볼 순 없을까? 있다. 없으면 이 문서를 만들지도 않았을 것이다. 지금부터 작업 효율을 올려줄, 원래 개발환경과 다른 별도의 가상환경을 만들어보자. 



## 1. cmd에서 가상환경 만들기

> 이하 코드는 Anaconda prompt가 아닌 cmd를 기준으로 한다.

```shell
$ cd / # C 드라이브로 이동
$ cd Users #사용자 폴더로 이동
$ cd "사용자 id" 
```



```shell
$ conda create -n "가상환경 이름" "설치하고 싶은 라이브러리" 
# ex) conda create -n gpu_env python==3.7.3
$ conda info --env # 설치된 가상환경 확인
```



```shell
$ conda activate "가상환경 이름" # 가상환경 실행
# ex) conda activate gpu_env
$ conda install "가상환경에 설치할 라이브러리 이름" # 라이브러리 설치 코드 1
$ pip install "가상환경에 설치할 라이브러리 이름" # 라이브러리 설치 코드 2

$ conda deactivate # 가상환경 실행 종료
```

```shell
# 가상환경을 삭제하고 싶을 때
$ conda remove -n "가상환경 이름" --all
# ex) conda remove -n gpu_env --all 
# 완전히 가상환경을 삭제하기 위해서는 anaconda/env 경로 안의 해당 가상환경 폴더까지 제거해야 함
```



## 2. jupyter notebook에 kernel 추가하기
> jupyter notebook에서 바로 새로운 가상환경에 접속할 수 있도록 별도의 커널을 추가한다. 
원래 위처럼 만든 가상환경에 접속하기 위해서는 `cmd`를 통해 가상환경을 만들어둔 위치로 이동하고, `conda activate` 명령어를 이용해야 활성화할 수 있다. 하지만 그 방법 대신 jupyter notebook에 커널을 추가하는 것으로 손쉽게 가상환경을 활성화시킬 수 있다. 


```shell
# jupyter notebook 설치
$ conda install jupyter notebook # kernel 추가를 위한 라이브러리 ipykernel 포함
$ python -m ipykernel install --user --name "가상환경 이름" --display-name "[jupyter notebook에서 표시될 이름]"
# ex) python -m ipykernel install --user --name gpu_env --display-name "[tensorflow-gpu:2.1.0]"
```

```shell
# 추가한 kernel을 삭제하고 싶을 때
$ jupyter kernelspec uninstall "가상환경 이름"
# ex) jupyter kernelspec uninstall gpu_env
```



