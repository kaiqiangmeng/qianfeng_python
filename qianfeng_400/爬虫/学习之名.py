#
import re
import os
import urllib.request
import time

def getHTML(url):
    headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:73.0) Gecko/20100101 Firefox/73.0"
        }
    req = urllib.request.Request(url, headers=headers)
    resp = urllib.request.urlopen(req)
    htmlInfo = resp.read().decode("utf-8")
    return htmlInfo
def getHTML_1(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:73.0) Gecko/20100101 Firefox/73.0"
    }
    req = urllib.request.Request(url, headers=headers)
    resp = urllib.request.urlopen(req)
    htmlInfo = resp.read()
    return htmlInfo
# 分离链接url的re语句
count = 4500
for k in range(44,50):
    rootSite = r"http://xxee11.com/htm/Picture8/"+str(k)+".htm"
    rootInfo = getHTML(rootSite)
    siteUrl_re =re.compile(r"<a href=\"(.*?)\" title")
    jpgUrlList = siteUrl_re.findall(rootInfo)
    print(jpgUrlList)

    for i in jpgUrlList:
        realUrl = "http://xxee11.com"+i
        print(realUrl)
        jpgInfo = getHTML(realUrl)

        three_re = re.compile(r"\);\" src=\"(.*?)\">")
        jpgUrl = three_re.findall(jpgInfo)
        print(jpgUrl)
        for n in jpgUrl:
            print(n)
            jpgtopath = getHTML_1(n)
            time.sleep(0.1)
            toPath = r"/media/jixy2/528589bc-ea5a-4464-961c-8465fdc30e80/Python文档/123"
            absPath = os.path.join(toPath, str(count)+".jpg")
            count += 1
            with open(absPath,"wb") as f:
                f.write(jpgtopath)