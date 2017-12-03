# -*- coding: utf-8 -*-
from voice import word_robot
from voice import word2voice
from voice import voice2word
from voice import audio
def interactive():
    audio.waitRecord(8000,1)
    inputword = voice2word.getvoiceText()
    print '>',inputword
    outputword = word_robot.robot(inputword)
    word2voice.playword(outputword)
    print '#',outputword

while True:
    interactive()
