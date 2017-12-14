#!/usr/bin/python
# -*- coding: utf8 -*-
'''
使用百度语音合成将文字转化为mp3
'''
import urllib2
import sys
import io
import wave
from pydub import AudioSegment
import audio
import re
reload(sys)
sys.setdefaultencoding('utf-8')
from control.settings import BaiduVoiceFather
class word2voice(BaiduVoiceFather):
    #调用getvoice可将语音文件放在项目路径下
    def getvoice(self,word):
        url = self.voiceurl%(self.appid,self.gettoken(),word)
        self.mp32wav(data = urllib2.urlopen(url).read(),filename = 'temp.wav')

    def mp32wav(self, data,filename):
        aud = io.BytesIO(data)
        sound=AudioSegment.from_file(aud,format='mp3')
        raw_data = sound._data
        #写入到文件，验证结果是否正确。
        l=len(raw_data)
        f=wave.open(filename,'wb')
        f.setnchannels(1)
        f.setsampwidth(2)
        f.setframerate(16000)
        f.setnframes(l)
        f.writeframes(raw_data)
        f.close()

temp = word2voice()
def playword(word):
    word = re.sub('\s', '', word)
    temp.getvoice(word)
    audio.playaudio()
