# _*_ coding=utf-8 _*_

import urllib
import urllib2

# 通过抓包的方式获取的url，不是浏览器的显示的url
url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc"

# 完整的headers
headers = {

"Accept":"application/json, text/javascript, */*; q=0.01",
"X-Requested-With":"XMLHttpRequest",
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"
}

key = raw_input("请输入需要翻译的文字：")

# 发送到服务器的表单数据
formdata = {
        "type" : "AUTO",
        "i" : key,
        "doctype" : "json",
        "xmlVersion" : "1.8",
        "keyfrom" : "fanyi.web",
        "ue" : "UTF-8",
        "action" : "FY_BY_CLICKBUTTON",
        "typoResult" : "true"
}

data = urllib.urlencode(formdata)
print data
request = urllib2.Request(url,data=data,headers= headers)

print urllib2.urlopen(request).read()