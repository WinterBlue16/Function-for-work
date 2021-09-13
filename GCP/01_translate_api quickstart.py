"""
Google Cloud Platform의 translate api를 빠르게 사용, 시험해볼 수 있는 예시입니다. 
해당 api를 사용하기 위해서는 다음의 조건을 충족해야 합니다.

1. google 계정이 존재한다.
2. project가 존재한다. 
3. project에서 translate api 사용 설정이 되어있다.(결제 계정이 존재해야 한다.)
4. 사용자 인증 정보에서 서비스 계정을 생성하고, 서비스 키를 json으로 다운받았다.
5. (mac 기준).bashrc/.bash_profile에서 export하거나 코드를 입력하는 방법을 통해 위의 서비스 키로 google credential 인증을 완료하였다.
6. google.cloud가 설치되어 있다. 

"""
from google.cloud
