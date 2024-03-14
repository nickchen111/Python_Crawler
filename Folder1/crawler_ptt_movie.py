import ssl 
# 忽略 SSL 憑證驗證錯誤 因為是mac所以比較麻煩 直接問GPT
context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

#抓取PTT電影版網頁原始碼HTML
import urllib.request as req
url = "https://www.ptt.cc/bbs/movie/index.html"

#建立一個request物件 附加Request header資訊 讓自己看起來是正常的request 才能access
request = req.Request(url, headers={
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
})

with req.urlopen(request, context=context) as response:
    data = response.read().decode("utf-8")
#print(data)

#解析原始碼 取得每篇文章的標題 讓beautifulsoup協助我們解析HTML格式文件
import bs4
root = bs4.BeautifulSoup(data, "html.parser")
print(root.title.string) #加上string可以純抓文字

titles = root.find("div", class_= "title") #尋找class= title 的標籤div 
print(titles.a.string) #只找到一個

#一次找所有的
all_title = root.find_all("div", class_ = "title")
print(all_title)

for tit in all_title:
    if(tit.a != None):
        print(tit.a.string)  #不印出本文已被刪除的