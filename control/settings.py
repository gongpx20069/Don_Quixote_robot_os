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

class BFRFather(object):
    access_key = ''#access_token为官网获取的AK
    secret_key = ''#secret_key为官网获取的secret_key
     # client_id 为官网获取的AK， client_secret 为官网获取的SK
    def gettoken(self):
        host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=%s&client_secret=%s'%(self.access_key,self.secret_key)
        request = urllib2.Request(host)
        request.add_header('Content-Type', 'application/json; charset=UTF-8')
        response = urllib2.urlopen(request)
        content = json.loads(response.read())
        return content['access_token']
