# _*_ coding:utf-8 _*_

import urllib2
import ssl

# 忽略ssl安全认证
context = ssl._create_unverified_context()

# url = "https://www.12306.cn/mormhweb/"
url = "https://www.baidu.com/"


headers = {
"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
}

request = urllib2.Request(url,headers=headers)

response = urllib2.urlopen(request,context=context)

print response.read()