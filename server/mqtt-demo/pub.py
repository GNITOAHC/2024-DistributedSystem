# publisher.py

import paho.mqtt.client as mqtt
import json

HOST = "127.0.0.1"
PORT = 1883
TOPIC = "TEST"

testdata = {'messages': 'Git'}

if __name__ == '__main__':
    
    client = mqtt.Client() # 連線設定 # 初始化地端程式
    
    # 設定連線資訊(IP, Port, 連線時間)
    client.connect(host=HOST, port=PORT, keepalive=60)
    
    print (f"send: msg = {testdata}")
    #要發布的主題和內容
    client.publish(topic=TOPIC, payload=json.dumps(testdata))