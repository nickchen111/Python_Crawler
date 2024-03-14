# Python_Crawler

# 資料夾說明
* 第一個資料夾:
  * ptt電影版文章標題
    * 基本的user-agent來發送請求爬取
    * beautifulsoup 解析 HTML格式
  * ptt八卦版文章標題
    * user-agent 與 cookie 來發送請求爬取
    * beautifulsoup 解析 HTML格式
  * KKDAY 文章標題
    * user-agent 與 cookie 來發送請求爬取
    * Json模組 解析 Json 格式
  * Medium文章標題
    * user-agent 與 cookie 與 context - type 來發送請求爬取
    * Json模組 解析 Json 格式  
 
 * 第二個資料夾：
   * ptt股票版文章標題
     * Selenium模組爬取文章標題
   * Linkedin
     * Selenium模組 並且使用Scroll到底的方式爬取所有職缺
   * Dcard
     * Selunium 模組 模擬使用者實際操作,輸入比特幣並且搜尋後爬取比特幣相關文章標題
     * Explict Wait技術
 * 第三個資料夾:
   * Leetcode
     * Selenium模組 爬取已經寫過的題數
     * 帳號密碼登入系統模擬 -> 模擬使用者輸入帳號密碼 但最近多了我不是機器人的認證系統..(TBD)
  * Instagram
    * Selenium模組 登入IG帳戶將跟#cat有關的照片抓取到桌面資料夾內
    * Explict Wait技術
    * 帳號密碼登入系統模擬 -> 模擬使用者輸入帳號密碼 

# English Version
* First folder:
  * PTT movie board
    * Sending requests with basic user-agent for crawling
    * Parsing HTML format with BeautifulSoup
  * PTT gossip board
    * Sending requests with user-agent and cookie for crawling
    * Parsing HTML format with BeautifulSoup
  * KKDAY
    * Sending requests with user-agent and cookie for crawling
    * Parsing JSON format with the Json module
  * Medium
    * Sending requests with user-agent, cookie, and context-type for crawling
    * Parsing JSON format with the Json module

* Second folder:
  * PTT stock board
    * Crawling article titles with the Selenium module
  * LinkedIn
    * Crawling all job vacancies by scrolling to the bottom with the Selenium module
  * Dcard
    * Crawling titles of articles related to Bitcoin by simulating user interaction, inputting Bitcoin, and searching
    * Using Explicit Wait skill
* Third folder:
  * Leetcode
    * Crawling the number of problems already solved with the Selenium module
    * Simulating account login system -> Simulating user inputting account password but recently added the "I am not a robot" verification system.. (TBD)
  * Instagram
    * Logging into the IG account and fetching photos related to #cat to the desktop folder
    * Using Explicit Wait skill
    * Simulating account login system -> Simulating user inputting account password
