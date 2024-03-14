from selenium import webdriver
from selenium. webdriver.common.by import By #這樣才能用find_element
from selenium. webdriver.common.keys import Keys
from selenium. webdriver.chrome.options import Options
# explicit wait 會等到網站有東西才做動作
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
#下載圖片需要的模組
import os
import wget
#設定Chrome Driver的執行路徑
options = Options()
options.chrome_executable_path = "/Users/nickchen/Desktop/python/python-basic/Selenium/chromedriver-mac-x64/chromedriver"
options.add_experimental_option("detach", True) #讓他不要打開就跳掉

#建立Driver物件實體 用程式操作瀏覽器運作
#爬取ig關鍵字圖片
driver = webdriver.Chrome(options=options)
driver.get("https://www.instagram.com/")

username = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )
password = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "password"))
    )

username.clear()
password.clear()
username.send_keys("s27206383@yahoo.com.tw")
time.sleep(7)
password.send_keys("xxxx")
time.sleep(8)
login = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
login.click()

#將問你是否開啟通知視窗關閉
obs = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, '_a9_1'))
    )
obs.click()

time.sleep(6)

# 點選搜尋圖示
search = driver.find_element((By.XPATH, '//*[@id="mount_0_0_gm"]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/span/div/a/div/div[2]/div/div/span/span'))
    
search.click()
search.click()
search2 = driver.find_element(By.XPATH, '//*[@id="mount_0_0_If"]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/input')
keyword = "#cat"
search2.send_keys(keyword)
time.sleep(1)
search2.send_keys(Keys.RETURN)
time.sleep(1)
search2.send_keys(Keys.RETURN)


WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'FFVAD'))
    )

#滑到底五次 
for i in range(5):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)

imgs = driver.find_elements(By.CLASS_NAME, "FFVAD")

# 建立資料夾與路徑
path = os.path.join(keyword)
os.mkdir(path)
count = 0
for img in imgs:
    save_as = os.path.join(path, keyword + str(count) + ".jpg")
    count += 1
    wget.download(img.get_attribute("src"), save_as)



