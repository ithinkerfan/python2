# _*_ coding=utf-8 _*_

import urllib
import urllib2
import random

def loadPage(url,filename):
    """
    作用：根据url发送请求，获取服务器响应文件
    :param url: 需要爬去的url地址
    :param filename: 处理的文件名
    :return: 返回服务器响应的文件
    """
    print "loading......" + filename

    ua_list = [
        "Mozilla/5.0(Windows;U;WindowsNT6.1;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50",
        "Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0",
        "Mozilla/5.0(WindowsNT6.1;rv:2.0.1)Gecko/20100101Firefox/4.0.1"
    ]

    # 随机选择一个报头
    user_agent = random.choice(ua_list)
    request = urllib2.Request(url)
    request.add_header("User-agent", user_agent)

    return urllib2.urlopen(request).read()


def writePage(html,filename):
    """
    作用：将html写入本地
    :param html: 服务器响应的文件内容
    :param filename: 文件名
    :return: 写入文件内容
    """
    print "saving......" + filename

    #文件写入
    with open(filename, "w") as file:
        file.write(html)

    print "-" * 30

def tiebaSpider(url, beginPage, endPage):
    """
    作用：贴吧爬虫调度器，负责组合处理每个页面的url
    :param url: 贴吧url的前部分
    :param beginPage: 起始页
    :param endPage: 结束页
    :return:
    """
    for page in range(beginPage,endPage + 1):
        pn = (page - 1)*50
        filename = "NO." + str(page) + "_page.html"
        fullurl = url + "&pn=" + str(pn)

        html = loadPage(fullurl,filename)

        writePage(html,filename)

        print "that is all,thanks!"

if __name__ == "__main__":
    kw = raw_input("please input spider tieba name:")
    beginPage = int(raw_input("please input begin page number:"))
    endPage = int(raw_input("please input end page number:"))

    url = "http://tieba.baidu.com/f?"
    key = urllib.urlencode({"kw": kw})
    fullurl = url + key

    tiebaSpider(fullurl, beginPage ,endPage)
