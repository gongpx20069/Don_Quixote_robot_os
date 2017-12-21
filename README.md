# Don_Quixote_robot_os(堂吉诃德智能家居系统)
计划在linux(Python)上编写一个智能家居开发平台，可以进行正常聊天，旅行规划、日程安排、天气咨询; 可以通过语音对家电进行控制;
我们的目标是让所有对Python有所了解的人，都可以用最廉价的方式定制家居机器人系统。
所有代码开源，所用第三方API以及包都属于免费或者开源；打造一个免费的机器人管家；可以运行在旧手机、老电脑、树莓派上，不需要太大的运行空间和内存；
只要有想法就会上传

目前需要的网络API：

图灵机器人API；

百度语音API;

百度人脸识别API;


目前需要依赖包：

PyAudio：用于语音交互；

Opencv2：用于人脸识别，图像处理；

jeiba：用于NLP分词等；

pydub:用于mp3转换wav，PyAudio不能播放mp3；


注意：项目在下载后主要改动control文件夹中的settings.py和control_robot.py
settings.py:配置文件，里面有提示的所有需要的百度语音API的key和图灵机器人API；
control_robot:关于所有机器人的控制文件可以在里面编写，包括对语音、人脸等的识别；

# 开源许可证：

The MIT License (MIT)

Copyright (c) 2017 Peixian Gong

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
