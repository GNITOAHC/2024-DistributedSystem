# subscriber.py

import paho.mqtt.client as mqtt
import json

HOST = "127.0.0.1"
PORT = 1883
TOPIC1 = "HCSR04"
TOPIC2 = "MPU6050"

# 當連線到伺服器時，要做的動作
def on_connect(client, userdata, flags, rc):
    print(f"HCSR04已連線, Host: {HOST}:{PORT}")
    # 當失去連線，或重新連線，重新訂閱 TOPIC
    client.subscribe(TOPIC1)
    client.subscribe(TOPIC2)
    
def topic1Func(msg):
    # HCSR04
    print(f"action of HCSR04, msg = {msg}")

def topic2Func(msg):
    # MPU6050
    print(f"action of MPU6050, msg = {msg}")

# 當接收到pubisher訊息時，要做的動作
def on_message(client, userdata, _msg):
    msg = json.loads(_msg.payload)
    
    if _msg.topic == TOPIC1:
        topic1Func(msg)
    if _msg.topic == TOPIC2:
        topic2Func(msg)
        
if __name__ == '__main__':
    client = mqtt.Client() # 連線設定 # 初始化地端程式
    client.on_connect = on_connect # 設定連線的動作
    client.on_message = on_message # 設定接收訊息的動作
    
    # 設定連線資訊(IP, Port, 連線時間)
    client.connect(host=HOST, port=PORT, keepalive=60)
    
    # 開始連線，執行設定的動作和處理重新連線問題
    client.loop_forever()