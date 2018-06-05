# _*_ coding:utf-8 _*_

import urllib2

import random

url = "http://www.baidu.com/"

# 常用的user agent
ua_list = [
	"Mozilla/5.0(Windows;U;WindowsNT6.1;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50",
	"Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0",
	"Mozilla/5.0(WindowsNT6.1;rv:2.0.1)Gecko/20100101Firefox/4.0.1"
]

#随机选择一个报头
user_agent = random.choice(ua_list)

#构造一个请求
request = urllib2.Request(url)

request.add_header("User-Agent" , user_agent)

print request.get_header("User-agent")

