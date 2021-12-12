# 가상 브라우저를 활용해 자동검색기를 만들 때

# 라이브러리 불러오기
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

input_keywords = ['입력창에 입력할 내용 1', '입력창에 입력할 내용 2'...]

driver = webdriver.Chrome("chrome 드라이버 위치 경로") # 파일 확장자까지 제대로 쓸 것
driver.get("가상 브라우저로 접속할 주소 입력") # https://google.com

search = driver.find_element_by_xpath('개발자도구에서 copy한 입력창 xpath 입력')

for keywords in input_keywords:
    search.send_keys(input_keywords) # 백종원 파스타집 위치
    search.send_keys(Keys.ENTER) # 가상 브라우저에서 엔터키 치는 코드

    time.sleep(5) # 5초 쉬고 다음 코드 실행
