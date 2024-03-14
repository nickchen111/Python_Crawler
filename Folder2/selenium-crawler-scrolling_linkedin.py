#載入Selenium模組
from selenium import webdriver
from selenium. webdriver.common.by import By 
from selenium. webdriver.chrome.options import Options

#設定Chrome Driver的執行路徑
options = Options()
options.chrome_executable_path = "/Users/nickchen/Desktop/python/python-basic/Selenium/chromedriver-mac-x64/chromedriver"

#建立Driver物件實體 用程式操作瀏覽器運作
driver = webdriver.Chrome()
#連線到Linkedin的職缺頁面
driver.get("https://www.linkedin.com/jobs/search?trk=guest_homepage-basic_guest_nav_menu_jobs&position=1&pageNum=0")

#捲動視窗並等待瀏覽器載入更多內容
n = 0
while n <= 3:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") #捲動視窗到底部
    import time
    time.sleep(3) #等待3s
    n += 1

#取得網頁中的工作標題
tags = driver.find_elements(By.CLASS_NAME, "base-search-card__title")
for tag in tags:
    print(tag.text)
driver.close()