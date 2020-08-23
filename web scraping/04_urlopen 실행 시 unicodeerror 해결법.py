# AWS 또는 타 환경에서 웹 크롤링 시(urlopen 실행 시) unicodeerror가 발생할 때가 있다.
# 파이썬 2.x 버전에서 주로 난다고 하지만 3.x 버전에서도 출몰할 때가 있으므로 대처법을 알아둔다.

# 간단한 크롤링 코드
from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen
from urllib.parse import quote # 요게 핵심!
import time

query = quote('프로그래머') # query가 한글일 경우 quote로 감싸주면 에러가 발생하지 않는다
url = "https://ko.wikipedia.org/wiki/" + query

html = urlopen(url) # html = requests.get(url).content로 하는 방법도 있다.
soup = BeautifulSoup(html, 'html.parser')

time.sleep(3)
