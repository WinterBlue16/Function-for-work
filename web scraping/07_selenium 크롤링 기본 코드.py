# selenium을 활용한 웹 크롤링 기본 코드
# 코드 실행을 위해서는 크롬 브라우저 드라이버가 필요하다.

# 라이브러리 불러오기
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select # dropdown 선택을 위해 필수!
import time

# 검색어 설정
search_keyword='검색하고 싶은 단어'
url = '검색하고 싶은 사이트의 주소' + search_keyword # 사이트마다 검색 url 형식이 다르므로 주의한다!

# 드라이버 설정
driver=webdriver.Chrome('chromedriver.exe') # chrome X Chrome O
driver.get(url)

time.sleep(2)

driver.quit() # driver.close()
