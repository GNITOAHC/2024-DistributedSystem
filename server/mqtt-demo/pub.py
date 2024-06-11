# publisher.py

import paho.mqtt.client as mqtt
import json
import time

HOST = "127.0.0.1"
PORT = 1883
TOPIC1 = "HCSR04"
TOPIC2 = "MPU6050"

topics = ["HCSR04", "MPU6050"]
messages = [{'messages':'Message for HCSR04'}, {'messages':'Message for MPU6050'}]


while True:
    client = mqtt.Client() # 連線設定 # 初始化地端程式
    
    # 設定連線資訊(IP, Port, 連線時間)
    client.connect(host=HOST, port=PORT, keepalive=60)
    
    for i in range(len(topics)):
        client.publish(topics[i], json.dumps(messages[i]))
        print(f"Published '{messages[i]}' to '{topics[i]}'")
        time.sleep(2)  # Wait for 2 seconds before sending the next message