# BeautifulSoup 크롤링 시 select로 데이터 가져오는 방법을 정리한다
# 부모 자식을 지정하여 크롤링하는 방식으로 불필요한 연산을 줄이도록 한다

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
crawling_ex1 = soup.select('#부모 태그_id > #자식 태그_id > #자식의 자식 태그_id')
crawling_ex2 = soup.select('.부모 태그_class > .자식 태그_class > .자식의 자식 태그_class')
crawling_mix = soup.select('.부모 태그_class > #자식 태그_id > .자식의 자식 태그_class')

# select_one으로 element 지정하기
crawling_text = soup.select_one('태그') # 'span'
crawling_text2 = soup.select_one('.클래스명') # '.num_txt'
crawling_text3 = soup.select_one('태그.클래스명') # 'span.num_txt'
crawling_text4 = soup.select_one('#id') # '#reply'
crawling_text5 = soup.select_one('태그#id') # 'span#reply'
crawling_text6 = soup.select_one('태그.클래스명#id') # 'span.num_txt#reply'


# 참고 사이트 : https://desarraigado.tistory.com/14
