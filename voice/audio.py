#-*-coding:utf-8-*-

#引入库
import pyaudio
import wave
import sys

# 定义数据流块
CHUNK = 1024
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 5
def playaudio():
    wf = wave.open(r'temp.wav', 'rb')
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
