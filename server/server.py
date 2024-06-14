import paho.mqtt.client as mqtt
from dotenv import load_dotenv
from database import Device, new_session
from database.query import get_time_zone, write_data
from database.parse import parse_hcsr04, parse_mpu6050

load_dotenv()

HOST = "127.0.0.1"
PORT = 1883


def on_connect(client, _userdata, _flags, _rc):
    print("on_connect")
    # print(Device.HCSR04.value, Device.MPU6050.value)
    client.subscribe(Device.HCSR04.value)
    client.subscribe(Device.MPU6050.value)
    return


def on_message(client, userdata, msg):
    match msg.topic:
        case Device.MPU6050.value:
            parsed_data = parse_mpu6050(msg)
            write_data(userdata, parsed_data) # userdata was set to iotdb_session
            # print(parsed_data)
            pass
        case Device.HCSR04.value:
            parsed_data = parse_hcsr04(msg)
            write_data(userdata, parsed_data) # userdata was set to iotdb_session
            # print(parsed_data)
            pass


def main():
    client = mqtt.Client()  # 連線設定 # 初始化地端程式

    client.on_connect = on_connect  # 設定連線的動作
    client.on_message = on_message  # 設定接收訊息的動作
    iotdb_session = new_session()
    client.user_data_set(iotdb_session)

    # 設定連線資訊(IP, Port, 連線時間)
    client.connect(host=HOST, port=PORT, keepalive=60)

    # 開始連線，執行設定的動作和處理重新連線問題
    client.loop_forever()
    pass


if __name__ == "__main__":
    main()
