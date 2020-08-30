# BeautifulSoup 크롤링 시 select로 데이터 가져오는 방법을 정리한다
# 여기서는 class명을 사용해 크롤링한다
# 크롤링된 데이터는 list 형식으로 저장된다

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

# select로 크롤링하기(class명)
crawling_class = soup.select('.class_이름')
# crawling_class
