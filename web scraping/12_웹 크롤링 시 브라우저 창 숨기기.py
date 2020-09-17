# 웹크롤링 코드를 django 등에서 사용할 때, 가상 브라우저 창이 뜨는 것을 숨겨준다.

# 라이브러리 불러오기
from selenium import webdriver

# Headless 옵션 지정
options = webdriver.ChromeOptions()
options.add_argument('headless')

# chromedriver 위치 지정
driver = webdriver.Chrome("chromedriver.exe의 절대 경로", chrome_options=options)
url = '크롤링할 사이트 주소'

# 가상 브라우저 종료
driver.quit()
