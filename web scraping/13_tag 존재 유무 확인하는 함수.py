# 웹 크롤링 시 특정 tag 안에 담겨있는 text를 크롤링해야 하는데, 해당 tag가 존재하는지를 확인하고 싶을 떄 사용한다

from selenium.common.exceptions import NoSuchElementException

def check_exist_by_xpath(xpath): # xpath 외에도 class, name 등으로 변환해 체크해볼 수 있다
    try:
        webdriver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True