import requests

# 기본 코드
response = requests.get('요청을 보낼 웹 주소(url)').json()
print(response)

# 만약 이 응답을 전역 변수로 사용하고 싶다면 아래와 같이 진행하면 된다.


def response_to_global_var(url):
    global response
    response = requests.get(url).json()
    return response
