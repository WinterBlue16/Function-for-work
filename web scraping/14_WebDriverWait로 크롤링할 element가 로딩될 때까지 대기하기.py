# 크롤링할 내용이 많아질 경우, 파싱을 하기 전에 코드가 실행되는 경우가 생긴다.
# 이럴 경우 찾고자 하는 element가 다 로딩될 때까지 대기하고 코드를 실행하는 방법이다.
# 아래 코드는 Google Chrome을 기준으로 한다

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome(executable_path="chromedriver.exe 경로")
driver.get("URL 주소")

try:
    # class가 desc_txt인 element가 로딩될 때까지 10초 대기
    element=WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "desc_text"))
    )
except TimeoutException:
    # 실패 시에는 에러 메시지로 Time out 출력
    print('Time Out')

finally:
    driver.quit()

