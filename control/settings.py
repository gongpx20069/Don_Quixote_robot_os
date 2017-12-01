# -*- coding: utf-8 -*-
import json
import urllib2
class BaiduVoiceFather(object):
    appkey = u''#百度appkey
    secretkey = u''#百度secretkey
    appid = u''#百度appid
    tokenurl=u'https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id=%s&client_secret=%s'%(appkey, secretkey)#获取百度语音token的网址
    voiceurl = u'http://tsn.baidu.com/text2audio?lan=zh&ctp=1&cuid=%s&tok=%s&tex=%s&vol=9'#获取语音识别的API
    cuid=''#获取语音识别的cuid，是唯一标识符，可以用机器的MAC，或者自己写一个不会重复的id
    #获取token
    def gettoken(self):
        re_dict = json.loads(urllib2.urlopen(self.tokenurl).read())
        return re_dict['access_token']

class ChatFather(object):
    key = ""  # turing123网站的key
    apiurl = "http://www.tuling123.com/openapi/api?"
