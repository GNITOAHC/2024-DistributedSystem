import json
from iotdb.Session import Session
from iotdb.utils.IoTDBConstants import TSDataType, TSEncoding, Compressor
from datetime import datetime

# 寫入檔案
def Read_Write_Data(data) -> str:
    time = data["time"]
    print(data)
    if len(data) == 2:
        device = "HCSR04"
        value = data["value"]
        print(time, device, value)
        write_Data(time, device, value)

    elif len(data) == 4:
        device = "MPU6050"
        value = [data["pitch"]["rate"], data["pitch"]["angle"],
                 data["roll"]["rate"], data["roll"]["angle"],
                 data["yaw"]["rate"], data["yaw"]["angle"],]
        print(time, device, value)
        write_Data(time, device, value)

    return "Succefully!!"

# 資料寫入
def write_Data(time, device, value):
    ip = "127.0.0.1"
    port_ = "6667"
    username_ = "root"
    password_ = "root"
    session = Session(ip, port_, username_, password_)
    session.open(False)

    sg_lst = ["root." + device]

    if device == "HCSR04":
        ts_path_lst_ = [
            "root.HCSR04.value",
        ]
        data_types = [
            TSDataType.FLOAT,
        ]
        measurements = [
            "value"
        ]
    
    elif device == "MPU6050":
        ts_path_lst_ = [
            "root.MPU6050.pitch_rate",
            "root.MPU6050.pitch_angle",
            "root.MPU6050.roll_rate",
            "root.MPU6050.roll_angle",
            "root.MPU6050.yaw_rate",
            "root.MPU6050.yaw_angle",
        ]
        data_types = [
            TSDataType.FLOAT,
            TSDataType.FLOAT,
            TSDataType.FLOAT,
            TSDataType.FLOAT,
            TSDataType.FLOAT,
            TSDataType.FLOAT,
        ]
        measurements = [
            "pitch_ rate",
            "pitch_angle",
            "roll_rate",
            "roll_angle",
            "yaw_rate",
            "yaw_angle",
        ]
    else: print(f"Don't have this device!!")


    for ts in ts_path_lst_:
        if(session.check_time_series_exists(ts) == False):
            session.create_time_series(ts, TSDataType.FLOAT, TSEncoding.PLAIN, Compressor.SNAPPY)

    session.insert_aligned_record("root." + device, time, measurements, data_types, value)

    with session.execute_query_statement(
        "select * from root.MPU6050*"
    ) as session_data_base:
        while(session_data_base.has_next()):
            print(session_data_base.next())

    session.delete_time_series(ts_path_lst_)
    session.delete_storage_groups(sg_lst)
    session.close()


result = Read_Write_Data({
    "time": 1718037056800,
    "pitch":{
            "rate": 0.29,
            "angle": 0.01
        },
    "roll": {
            "rate": -0.29,
            "angle": -0.01
        },
    "yaw":  {
            "rate": 0.09,
            "angle": 0.01
        }
    })