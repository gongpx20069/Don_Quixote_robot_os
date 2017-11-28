# -*- coding: utf-8 -*-
from voice import word_robot
from voice import word2voice

def robot(word):
    print '>',word
    re_word = word_robot.robot(word)
    print '#',re_word
    word2voice.playword(re_word)

while True:
    robot(raw_input())
