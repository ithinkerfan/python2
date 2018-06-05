# _*_ coding=utf-8 _*_

import urllib
#使用url访问的时候，显示中文字符其实是经过url编码，所以用urlencode进行编码
wd = {"wd" : "中国"}

print urllib.urlencode(wd)

#解码的时候，使用urllib.unquote()

a = urllib.urlencode(wd)

print urllib.unquote(a).decode("utf-8")


