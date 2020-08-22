# BeautifulSoup을 이용한 크롤링 기본 코드

# 라이브러리 불러오기
from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen
import pandas as pd

# url 설정
url = '크롤링하고 싶은 주소'

html=requests.get(url).content
soup=BeautifulSoup(html, 'html.parser')
# print(soup)

# 이 다음부터는 find_all이나 find, get_text 등을 활용하여 웹페이지 내 텍스트를 크롤링할 수 있다.
