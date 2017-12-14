# -*- coding: utf-8 -*-
import urllib2
import urllib
import base64
from control import settings
import cv2
import time
import json
import threading
# 二进制方式打开图片文件
class BFR(settings.BFRFather):
    message={
            'location':{'left':0,'top':0,'height':0,'width':0},
            'name':'null',
            'age':'null',
            'beauty':'null',
            'gender':'null'
        }
    def getBFR(self):
        img = base64.b64encode(open('temp.jpg', 'rb').read())
        request_url = "https://aip.baidubce.com/rest/2.0/face/v1/detect"
        params = {"face_fields": "age,beauty,expression,faceshape,gender,glasses,landmark,race,qualities", "image": img,
                  "max_face_num": 5}
        params = urllib.urlencode(params)
        request_url = request_url + "?access_token=" + self.access_token
        try:
            request = urllib2.Request(url=request_url, data=params)
            request.add_header('Content-Type', 'application/x-www-form-urlencoded')
            response = urllib2.urlopen(request)
            content = json.loads(response.read())
            temp = {}
            if content:
                for i in content['result']:
                    if 'location' in i:
                        temp['location'] = i['location']
                    if 'age' in i:
                        temp['age'] = i['age']
                        temp['beauty'] = i['beauty']
                        temp['gender'] = i['gender']
                        self.message = temp
            print temp
        except Exception,e:
            print 'Error:',e


    def video(self, settime):
        self.access_token = self.gettoken()
        cap = cv2.VideoCapture(0)  # 打开0号摄像头
        success = True
        time0= time.time()
        font = cv2.FONT_HERSHEY_SIMPLEX
        thread1 = threading.Thread(target=self.getBFR, args=())
        while success:
            success, frame = cap.read()
            if time.time() - time0 > settime:
                time0 = time.time()
                cv2.imwrite('temp.jpg',frame)
                if not thread1.is_alive():
                    thread1 = threading.Thread(target=self.getBFR, args=())
                    thread1.setDaemon(True)
                    thread1.start()
            cv2.rectangle(frame,(self.message['location']['left'],self.message['location']['top']+self.message['location']['height']), (self.message['location']['left']+self.message['location']['width'],self.message['location']['top']), (0,255,0), 4)
            cv2.putText(frame,str(self.message['beauty']), (self.message['location']['left'],self.message['location']['top']),font,1, (0,0,255),5)
            cv2.imshow("test", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()

BFR().video(2)
