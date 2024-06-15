import json
from .query import WriteDataType
from iotdb.utils.IoTDBConstants import TSDataType, TSEncoding, Compressor


def parse_hcsr04(raw) -> WriteDataType:
    data = json.loads(raw.payload)
    write_data = WriteDataType(
        "HCSR04",
        data["time"],
        ["root.HCSR04.value"],
        [TSDataType.FLOAT],
        ["value"],
        [data["value"]],
    )
    # print(write_data)
    return write_data


def parse_mpu6050(raw) -> WriteDataType:
    data = json.loads(raw.payload)
    dd_list = [
        "pitch_rate",
        "pitch_angle",
        "roll_rate",
        "roll_angle",
        "yaw_rate",
        "yaw_angle",
    ]
    paths = [f"root.MPU6050.{x}" for x in dd_list]
    types = [TSDataType.FLOAT for _ in range(0, 6)]  # All float type
    measurements = dd_list
    value = [
        data["pitch"]["rate"],
        data["pitch"]["angle"],
        data["roll"]["rate"],
        data["roll"]["angle"],
        data["yaw"]["rate"],
        data["yaw"]["angle"],
    ]
    write_data = WriteDataType(
        "MPU6050", data["time"], paths, types, measurements, value
    )
    return write_data
