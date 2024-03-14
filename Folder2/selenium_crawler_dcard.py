from selenium import webdriver
from selenium. webdriver.common.by import By #這樣才能用find_element
from selenium. webdriver.common.keys import Keys
from selenium. webdriver.chrome.options import Options
# explicit wait 會等到網站有東西才做動作
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#設定Chrome Driver的執行路徑
options = Options()
options.chrome_executable_path = "/Users/nickchen/Desktop/python/python-basic/Selenium/chromedriver-mac-x64/chromedriver"
options.add_experimental_option("detach", True) #讓他不要打開就跳掉

#建立Driver物件實體 用程式操作瀏覽器運作
# 點選連結標籤
driver = webdriver.Chrome(options=options)
driver.get("https://www.dcard.tw/f")

# 在dcard上搜尋比特幣 並且把標題印出  現在 用爬蟲程式跑 dcard 它好像會自動把你視為機器人...
search = driver.find_element(By.NAME, "query")
search.clear() # 將搜尋欄位清空
search.send_keys("比特幣")
time.sleep(5)
search.send_keys(Keys.RETURN)
# 讓他可以等到網頁有我們要的東西在往下run程式 最多等20s
WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, "atm_mk_stnw88"))
    )

# 印出標題
titles = driver.find_elements(By.CLASS_NAME, "atm_cs_1hcvtr6")
for title in titles:
    print(title.text)

#根據標題裡的a tag文字來點擊他
link = driver.find_element(By.LINK_TEXT, "為什麼小孩被虐死是社工該死？")
link.click()
driver.back() #回到上一頁
driver.forward(); # 回到下一頁