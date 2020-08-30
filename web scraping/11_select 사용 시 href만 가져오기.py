# BeautifulSoup 크롤링 시 select로 데이터 가져오는 방법을 정리한다
# select로 크롤링하였을 때, 그 안의 href만 가져오는 방법을 알아본다

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

# select로 부모 자식 지정하기
crawling_ex = soup.select('.부모 태그_class > #자식 태그_id > .자식의 자식 태그_class > a') # 태그 이름은 #이나 .을 찍을 필요 없이 그냥 적으면 된다.

# href 가져오기
url_li=[]
for t in crawling_ex:
    url=t['href']
    url_li.append(url)

url_li
