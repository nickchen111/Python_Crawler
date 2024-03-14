#載入Selenium模組
from selenium import webdriver
from selenium. webdriver.common.by import By 
from selenium. webdriver.common.keys import Keys
from selenium. webdriver.chrome.options import Options

import time
#設定Chrome Driver的執行路徑
options = Options()
options.chrome_executable_path = "/Users/nickchen/Desktop/python/python-basic/Selenium/chromedriver-mac-x64/chromedriver"
options.add_experimental_option("detach", True)
#建立Driver物件實體 用程式操作瀏覽器運作
driver=webdriver.Chrome(options=options)

#連線到Leetcode登入頁面 fail
driver.get("https://leetcode.com/accounts/login/?next=%2Fproblemset%2F%3Fpage%3D2%26sorting%3DW3sic29ydE9yZGVyIjoiQVNDRU5ESU5HIiwib3JkZXJCeSI6IkZST05URU5EX0lEIn1d")
#輸入帳號密碼 按下登入按鈕
usernameInput = driver.find_element(By.ID,"id_login")
passwordInput = driver.find_element(By.ID,"id_password")
time.sleep(15)
usernameInput.send_keys("chen_111")
passwordInput.send_keys("nickboy1994")
time.sleep(10)

 #多了驗證不是機器人的地方就失敗了
verify = driver.find_element(By.CSS_SELECTOR, "[type=checkbox]") #可以抓取任意格式
verify.click()
# verify.send_keys(Keys.ENTER) fail

signinBtn = driver.find_element(By.ID, "signin_btn")
signinBtn.send_keys(Keys.ENTER)

#等待登入完成
time.sleep(5)
#連線到登入後才能取得資料的頁面 並取得想要的資料
driver.get("https://leetcode.com/problemset/")
time.sleep(3)
stateElement = driver.find_element(By.CSS_SELECTOR, "[data-difficulty=TOTAL]")
print(stateElement.text)
columns = stateElement.text.split("\n")
print("已完成刷題數量",columns[1])
driver.close()