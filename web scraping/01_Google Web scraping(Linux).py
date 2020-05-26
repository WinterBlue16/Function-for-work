# 구글 웹 크롤러 만들기(Linux)
# 통상적으로 웹 크롤링을 할 때는 Chromedriver를 쓰지만 AWS는 기반이 linux인 데다 Chrome 브라우저가 설치되어 있지 않아 브라우저 설치부터 헤야 한다.
# 그런 번거로움을 덜기 위해 다음과 같이 PhantomJS를 사용하여 크롤링을 진행할 수 있다.

# PhantomJS는 이곳(https://phantomjs.org/download.html)에서 받을 수 있다.
# 여기서 가장 중요한 라이브러리는 PhantomJS(version 2.1.1)와 selenium(version 3.11.0)이다. PhantomJS는 더 이상 개발이 진행되지 않고, selenium은 높은 버전의 경우 PhantomJS를 지원하지 않으므로 버전을 주의 깊게 확인한다!


# 0. PhantomJS 파일 압축 풀기
tar -jxvf phantomjs-2.1.1-linux-x86_64.tar.bz2

# 0. 라이브러리 불러오기
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import phantomjs

# 1. 검색할 단어 설정
search_keyword = '코로나 바이러스 확진 현황'

# 2. 드라이버 설정
driver = webdriver.PhantomJS('phantomjs-2.1.1-linux-x86_64/bin/phantomjs')
# driver.set_window_size(1120, 550)
driver.get('https://google.com')

# 제대로 url이 들어왔는지 확인
print(driver.current_url)

search = driver.find_element_by_name("q") # class_name이나 xpath를 넣으면 에러가 터지거나 제대로 값이 나오지 않는다
# 태그는 사이트에 따라 변경 가능

time.sleep(5)

# 3. 검색어 입력 + 엔터키 누르기
search.send_keys(search_keyword)
search.send_keys(Keys.ENTER)

time.sleep(10)

# 4. BeautifulSoup으로 텍스트 꺼내기
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
# print(soup)

time.sleep(5)

search_li = []
for text in soup.find_all('div', {'class' : 'dsgSw'}):
    t = text.get_text()
    search_li.append(t)

driver.close()
 
