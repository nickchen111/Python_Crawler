import ssl 
# 忽略 SSL 憑證驗證錯誤 因為是mac所以比較麻煩 直接問GPT
context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

#抓取KKDAY 的文章資料 Json格式
import urllib.request as req
#改成直接找有文章標題的網址
url = "https://www.kkday.com/zh-tw?cid=7725&ud1=SEM&ud2=brand&gad_source=1&gclid=Cj0KCQiAxOauBhCaARIsAEbUSQQjpW_88uhMifLUeYE6lgRUccDWwpPXuWPlotSDrAO8upYAEC3ypVwaAmHFEALw_wcB"

#建立一個request物件 附加Request header資訊 讓自己看起來是正常的request 才能access
request = req.Request(url, headers={
    "Content-Type" : "text/html; charset=UTF-8",
    "cookie" : "country_lang=zh-tw; currency=TWD; KKUD=7b48eb52f93657e16fdcfac297277440; _gcl_au=1.1.461771489.1708797945; __lt__cid=fbccdb71-6255-4307-b593-ee05f704d41a; _fbp=fb.1.1708797964895.897269397; rskxRunCookie=0; rCookie=otk6tkilzwrzykj7c9xs2blt0cgu3a; CookieConsent={stamp:%27AcOFf+t+3xIHn/JK0oopBthjK5JCz/wVHUdqVH1H47Bcj9gXKzk6LQ==%27%2Cnecessary:true%2Cpreferences:true%2Cstatistics:true%2Cmarketing:true%2Cmethod:%27explicit%27%2Cver:1%2Cutc:1708797967686%2Cregion:%27tw%27}; _hjSessionUser_628088=eyJpZCI6ImRmMThlYzY5LTcwZWMtNWJiYS1iYmU2LTA5YWYxY2ViYTFjMCIsImNyZWF0ZWQiOjE3MDg3OTc5NjU0MTUsImV4aXN0aW5nIjp0cnVlfQ==; CID=7725; UD1=SEM; UD2=brand; cto_bundle=RR3m0V9ocmdjJTJCaDZFWWVMcEV5eHFMSjBFTnRDUXRpRlJldFpiTjU5cnRab3cwWTU0cUhhTGZQRDNBJTJGN2QxUHpwOFclMkZHTWlVMUM3N21hVSUyQlRLc0p3UVlTakpvdVN3U2E1S1J3YlYzaThQSUx3aU42ZXBCTUZrU00zMklrd0lXY3dYS3NTckc4R1J2SURHT0lUN1c5dFNMS29FbUQ2U1lPJTJGVHpoamx0S2NnaGI0aUR0aGNSSlFSZDRHNlAzdWJsTmVWUHZMalRkemVrbGc1UHpVaGUyY0ZhS09meWRsY3ZTaEc0bDh4RkVDZyUyRnhNQm9oNWhPcTJWRGNCSXJzTUs3Tzl5bUJv; csrf_cookie_name=cefe1902159cf92d7c4a06526fa1668a; KKWEB=a%3A4%3A%7Bs%3A10%3A%22session_id%22%3Bs%3A32%3A%22d4e6e55fc835ec373b047629d2d38034%22%3Bs%3A7%3A%22channel%22%3Bs%3A5%3A%22GUEST%22%3Bs%3A13%3A%22last_activity%22%3Bi%3A1709028789%3Bs%3A9%3A%22user_data%22%3Bs%3A0%3A%22%22%3B%7Db7657c894e98e45a0a985aa7483fe356; _gcl_aw=GCL.1709028796.Cj0KCQiAxOauBhCaARIsAEbUSQQjpW_88uhMifLUeYE6lgRUccDWwpPXuWPlotSDrAO8upYAEC3ypVwaAmHFEALw_wcB; __lt__sid=30a428e0-734fcd95; _ga_RJJY5WQFKP=GS1.1.1709028795.2.1.1709028795.60.0.0; _ga=GA1.2.1670096094.1708797959; _gid=GA1.2.247848523.1709028796; _gac_UA-49763723-1=1.1709028796.Cj0KCQiAxOauBhCaARIsAEbUSQQjpW_88uhMifLUeYE6lgRUccDWwpPXuWPlotSDrAO8upYAEC3ypVwaAmHFEALw_wcB; _dc_gtm_UA-49763723-1=1; _gac_UA-117438867-1=1.1709028796.Cj0KCQiAxOauBhCaARIsAEbUSQQjpW_88uhMifLUeYE6lgRUccDWwpPXuWPlotSDrAO8upYAEC3ypVwaAmHFEALw_wcB; _dc_gtm_UA-117438867-1=1; _hjSession_628088=eyJpZCI6IjhmMzVlMTYyLWMzYTItNDQ3Ny1iZWIzLWMyODI4NmJhZTMyMCIsImMiOjE3MDkwMjg3OTYxMTEsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MX0=; _uetsid=d315d750d55811ee93389f0b701f7144; _uetvid=1b0f8f20a96411edb0ee35743afee70d; lastRskxRun=1709028797628; datadome=mwGbxLb0Mc4Ovhj1A7vvJ8UbOXg1pa_~MRoR2QL2U4MSiFGxq4RFSGH7nxlKT3TUPGsfPo7Kvj2qt2MvJWAj0dAqsH73dkoMXGOxme3c94Rru3ymFa0aG9mKWsjTDLSR",    
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
}) #根據觀察 取得的資料是Json格式

with req.urlopen(request, context=context) as response:
    data = response.read().decode("utf-8")
#print(data)

#解析JSon格式
import json
data = json.loads(data) #把原始json資料解析成JSON格式的字典/列表表示形式 loads輸入的是串流 load輸入的是字串 
print(data)

#取得JSON資料中的文章標題列表
posts = data["data"]["homepage_product_group"] #這個相當於列表
for key in posts:
    print(key["title"]) #此為字典