# server

1. Start mosquitto server. [Download](https://mosquitto.org/download/)
2. Start IotDB server. [Download](https://iotdb.apache.org/Download/)
3. Start `device.js` at [device directory](../device/README.md)
   ```
   npm install
   node device.js
   ```
4. Start server.
    ```
    pip install apache-iotdb paho-mqtt python-dotenv
    python server.py
    ```

## device name   
- HCSR04: 超音波 cm 
- MPU6050: 陀螺儀 yaw, roll, pitch