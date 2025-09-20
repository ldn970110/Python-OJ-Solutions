import urllib.request as req
def getdata(url):
    request=req.Request(url,headers={
        "cookie":"over18=1",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    })
    with req.urlopen(request)as response:
        data=response.read().decode("utf-8")
    import bs4
    root=bs4.BeautifulSoup(data,"html.parser")
    titles=root.find_all("div",class_='title')

    for title in titles:
        if title.a !=None:
            print(title.a.text)
    nextlink=root.find("a", string="‹ 上頁")
    c=nextlink
    return c
pageURL='https://www.ptt.cc/bbs/Gossiping/index.html'
n=0
while n<3:
    pageURL='https://www.ptt.cc'+ getdata(pageURL)
    n=n+1


