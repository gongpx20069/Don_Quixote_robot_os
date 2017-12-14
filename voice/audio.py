#-*-coding:utf-8-*-

#引入库
import pyaudio
import wave
import sys
import numpy as np
import time

# 定义数据流块
CHUNK = 1024
CHANNELS = 2
RATE = 8000 #44100
RECORD_SECONDS = 5
def playaudio(filename='temp.wav'):
    wf = wave.open(filename, 'rb')
    p = pyaudio.PyAudio()
    # 打开数据流
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)
    # 读取数据
    data = wf.readframes(CHUNK)
    # 播放
    while data != '':
        stream.write(data)
        data = wf.readframes(CHUNK)
    # 停止数据流
    stream.stop_stream()
    stream.close()
    # 关闭 PyAudio
    p.terminate()

def getvoice():
    FORMAT = pyaudio.paInt16
    WAVE_OUTPUT_FILENAME = "output.wav"
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)
    print("* recording")
    frames = []
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("* done recording")
    stream.stop_stream()
    stream.close()
    p.terminate()
    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

def waitRecord(threshold, timer):
    FORMAT = pyaudio.paInt16
    WAVE_OUTPUT_FILENAME = "temp1.wav"
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)
    print("开始监听")
    temp = 0
    frames = []
    time1=time.time()
    Flag = False
    while True:
     #   print '等待录制',temp
        data = stream.read(CHUNK)
        frames.append(data)
        audio_data = np.fromstring(data, dtype=np.short)
        temp = np.max(audio_data)
        while temp > threshold :
            Flag = True
        #    print '录制中，当前阈值：',temp
            data = stream.read(CHUNK)
            frames.append(data)
            audio_data = np.fromstring(data, dtype=np.short)
            temp = np.max(audio_data)
            time1 = time.time()
        if Flag:
            if time.time()-time1>timer:
                break
        else:
            frames.pop()
    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    stream.stop_stream()
    stream.close()
    p.terminate()
    print '录制结束'
