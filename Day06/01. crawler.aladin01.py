

from selenium import webdriver
import time
#뷰티풀수프 임포트 (bs4)
from bs4 import BeautifulSoup


# 웹 드라이버 활성화
driver = webdriver.Chrome(r'C:\Users\minho\Desktop\crawling\chromedriver_win32\chromedriver.exe')

# 알라딘 홈페이지 이동
driver.get('https://www.aladin.co.kr')
time.sleep(1.5)

# 베스트셀러 탭 클릭
driver.find_element_by_xpath('//*[@id="re_mallmenu"]/ul/li[3]/div/a/img').click()

# selenium으로 현재 페이지의 html소스코드를 전부 불러오기.
src = driver.page_source
# print(src) 모든 html 소스를 가지고 온 것을 확인.


# 뷰티풀수프 객체 생성.
# 뷰티풀수프 객체를 생성하면서, 셀레늄이 가지고 온 html 소스를
# 제공하고, 해당 소스를 html문법으로 변환하라는 주문.
soup = BeautifulSoup(src, 'html.parser')

'''
- 뷰티풀수프를 사용하여 수집하고 싶은 데이터가 들어있는 태그를 부분추출할 수 있습니다.

- find_all() 메서드는 인수값으로 추출하고자 하는 태그의 이름을 적으면 해당 태그만 전부 추출하여 리스트에 담아 대입합니다.

'''


