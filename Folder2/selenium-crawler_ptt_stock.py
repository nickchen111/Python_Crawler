#載入Selenium模組
from selenium import webdriver
from selenium. webdriver.common.by import By #這樣才能用find_element
from selenium. webdriver.chrome.options import Options

#下載Chrome Driver的執行相關路徑
options = Options()
options.chrome_executable_path = "/Users/nickchen/Desktop/python/python-basic/Selenium/chromedriver-mac-x64/chromedriver"

#建立Driver物件實體 用程式操作瀏覽器運作
#新的selenium 版本已經不要設定driver的路徑,系統會自動detect, 所以在driver的設定可以改成以下:
driver = webdriver.Chrome()
driver.get("https://www.ptt.cc/bbs/Stock/index.html")
#print(driver.page_source) #取得網頁原始碼

#抓取股票版網頁中的文章標題
element = driver.find_elements(By.CLASS_NAME, "title") #find_elements可以取得多個 find_element只取一個 搜尋class name 是title的標籤
#print(element)
for e in element :
    print(e.text) # .text可取得內部文字

#取得上一頁的文章標題
lastPage = driver.find_element(By.LINK_TEXT, "‹ 上頁")
lastPage.click() #模擬使用者的點擊連結標籤
element = driver.find_elements(By.CLASS_NAME, "title")
for e in element :
    print(e.text) # .text可取得內部文字
driver.close()