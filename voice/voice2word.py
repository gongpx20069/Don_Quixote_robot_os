# -*- coding: utf-8 -*-
import json
import urllib2
import base64
from control.settings import BaiduVoiceFather
class voice2word(BaiduVoiceFather):
    def getText(self):
        d = open('temp.wav','rb').read()
        data={
            "format": "wav",
            "rate": 16000,
            "channel": 1,
            "token":self.gettoken(),
            "cuid": '303648105471511959505',
            "len": len(d),
            "speech": base64.encodestring(d).replace('\n', '')
        }
        request = urllib2.Request(self.texturl, data=json.dumps(data),
                               headers={'Content-Type': 'application/json'})
        result = json.loads(urllib2.urlopen(request).read())
        return result['result'][0]
v = voice2word()
def getvoiceText():
    return v.getText()
