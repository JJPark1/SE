from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#step2.검색할 키워드 입력
query = input('검색할 키워드를 입력하세요: ')

#step3.크롬드라이버로 원하는 url로 접속
url = 'https://map.naver.com/v5/?c=14134688.3376756,4518373.6724403,15,0,0,0,dh'
driver = webdriver.Chrome('/Users/jungmin/Downloads/chromedriver')
driver.get(url)
time.sleep(3)

#step4.검색창에 키워드 입력 후 엔터
search_box = driver.find_element_by_css_selector("input#query")
search_box.send_keys(query)
search_box.send_keys(Keys.RETURN)
time.sleep(2)

#step5.뉴스 탭 클릭
driver.find_element_by_xpath('//*[@id="lnb"]/div[1]/div/ul/li[2]/a').click()

time.sleep(2)



blog_titles = driver.find_elements_by_css_selector(".total_tit")

for i in blog_titles:
    title = i.text
    print(title)