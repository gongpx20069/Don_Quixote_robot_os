#!/usr/bin/python
# -*- coding: utf8 -*-
'''
使用百度语音合成将文字转化为mp3
'''
import urllib2
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
class word2voice(object):
    appkey = u''#百度appkey
    secretkey = u''#百度secretkey
    appid = u''#百度appid
    tokenurl=u'https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id=%s&client_secret=%s'%(appkey, secretkey)
    voiceurl = u'http://tsn.baidu.com/text2audio?lan=zh&ctp=1&cuid=%s&tok=%s&tex=%s&vol=9'
    def gettoken(self):
        re_dict = json.loads(urllib2.urlopen(self.tokenurl).read())
        return re_dict['access_token']
    #调用getvoice可将语音文件放在项目路径下
    def getvoice(self,word):
        url = self.voiceurl%(self.appid,self.gettoken(),word)
        with open('temp.mp3','wb') as f:
            f.write(urllib2.urlopen(url).read())
            
