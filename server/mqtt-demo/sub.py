# subscriber.py

import paho.mqtt.client as mqtt
import json

HOST = "127.0.0.1"
PORT = 1883
TOPIC = "TEST"

# 當地端程式連線伺服器得到回應時，要做的動作
def on_connect(client, userdata, flags, rc):
    # print("Connected with result code "+str(rc))
    print(f"Mqtt已連線, Host: {HOST}:{PORT}, TOPIC: {TOPIC}")
    # 如果我們失去連線或重新連線時 # 地端程式將會重新訂閱 TOPIC
    client.subscribe(TOPIC)

# 當接收到從伺服器發送的訊息時要進行的動作
def on_message(client, userdata, _msg):
    msg = json.loads(_msg.payload)
    # print(f"received: msg = {messages}")

if __name__ == '__main__':
    
    client = mqtt.Client() # 連線設定 # 初始化地端程式
    client.on_connect = on_connect # 設定連線的動作
    client.on_message = on_message # 設定接收訊息的動作
    
    # 設定連線資訊(IP, Port, 連線時間)
    client.connect(host=HOST, port=PORT, keepalive=60)
    
    # 開始連線，執行設定的動作和處理重新連線問題
    client.loop_forever()