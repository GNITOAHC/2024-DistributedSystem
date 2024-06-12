# publisher.py

import paho.mqtt.client as mqtt
import json
import time

HOST = "127.0.0.1"
PORT = 1883
TOPIC1 = "HCSR04"
TOPIC2 = "MPU6050"

topics = ["HCSR04", "MPU6050"]
messages = [{
    "value": 455.1,
    "time": 1718037202913
}, 
{
    "time": 1718037056800,
    "pitch": {
        "rate": 0.29,
        "angle": 0.01
    },
    "roll": {
        "rate": -0.29,
        "angle": -0.01
    },
    "yaw": {
        "rate": 0.09,
        "angle": 0.01
    }
}]


# while True:
client = mqtt.Client() # 連線設定 # 初始化地端程式

# 設定連線資訊(IP, Port, 連線時間)
client.connect(host=HOST, port=PORT, keepalive=60)

for i in range(len(topics)):
    client.publish(topics[i], json.dumps(messages[i]))
    print(f"Published '{messages[i]}' to '{topics[i]}'")
    time.sleep(2)  # Wait for 2 seconds before sending the next message