import ssl 
# 忽略 SSL 憑證驗證錯誤 因為是mac所以比較麻煩 直接問GPT
context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

#抓取PTT八卦版網頁原始碼HTML
import urllib.request as req
def getData(url):
    #建立一個request物件 附加Request header資訊 讓自己看起來是正常的request 才能access
    request = req.Request(url, headers={
        "cookie" : "over18=1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
    })

    with req.urlopen(request, context=context) as response:
        data = response.read().decode("utf-8")
    

    #解析原始碼 取得每篇文章的標題 讓beautifulsoup協助我們解析HTML格式文件
    import bs4
    root = bs4.BeautifulSoup(data, "html.parser")
    print(root.title.string) #加上string可以純抓文字

    titles = root.find("div", class_= "title") #尋找class= title 的標籤div 
    if titles != None: print(titles.a.string) #只找到一個

    #一次找所有的
    all_title = root.find_all("div", class_ = "title")
    print(all_title)

    for tit in all_title:
        if(tit.a != None):
            print(tit.a.string)

    #瘋狂找上一頁 抓取上一頁的連結
    next_link = root.find("a", string="‹ 上頁") #找到內文是 ‹ 上頁 的 a tag
    return next_link["href"]

#抓取一個頁面的標題
pageURL = "https://www.ptt.cc/bbs/Gossiping/index.html"
count = 0
while count < 5:
    pageURL = "https://www.ptt.cc" + getData(pageURL)
    count += 1