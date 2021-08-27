

'''
- 네이버로 접속해서 뉴스스탠드 쪽 파란 '네이버뉴스' 클릭 -> 

정치, 경제, 사회, 생활/문화, 세계, IT/과학 탭을 돌아다니면서 헤드라인 뉴스 4개씩 클릭해 주시면 됩니다,
뒤로가기는 driver.back() 메서드로 뒤로가기 가능.

XPATH를 따다보면 규칙을 발견할 수 있을겁니다.
반복분 이용해서 클릭 명령을 내려주시면 됩니다.
24개의 명령 일일이 쓰기 X, 규칙을 찾아보세요.
'''

from selenium import webdriver
import time

# 다운로드 받은 크롬 물리 드라이버 가동 명령
driver = webdriver.Chrome(r'C:\Users\minho\Desktop\crawling\chromedriver_win32\chromedriver.exe')

# 물리 드라이버로 사이트 이동 명령
driver.get('https://www.naver.com')
time.sleep(1)

# 네이버 뉴스 진입
naver_news_btn = driver.find_element_by_xpath('//*[@id="NM_NEWSSTAND_HEADER"]/div[2]/a[1]').click()
time.sleep(1)


'''
# 정치
politics_btn = driver.find_element_by_xpath('//*[@id="lnb"]/ul/li[3]/a/span').click()
time.sleep(1)

for num in range(1,4):
    politics = driver.find_element_by_xpath(f'//*[@id="main_content"]/div/div[2]/div[1]/div[{num}]/div[1]/ul/li[1]/div[2]/a')
    politics_id = f'//*[@id="main_content"]/div/div[2]/div[1]/div[{num}]/div[1]/ul/li[1]/div[2]/a'
    if politics_id.find('[2]', )
    politics.click()
    time.sleep(1)
    driver.back()
    time.sleep(1)

driver.back()


# 경제 
economy_btn = driver.find_element_by_xpath('//*[@id="lnb"]/ul/li[4]/a/span').click()
time.sleep(1)

for num in range(1,4):
    economy = driver.find_element_by_xpath(f'//*[@id="main_content"]/div/div[2]/div[1]/div[{num}]/div[1]/ul/li[1]/div[2]/a')
    economy_id = f'//*[@id="main_content"]/div/div[2]/div[1]/div[{num}]/div[1]/ul/li[1]/div[2]/a'

    economy.click()
    time.sleep(1)
    driver.back()
    time.sleep(1)

driver.back()
'''


    


