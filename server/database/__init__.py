from iotdb.Session import Session
from iotdb.utils.IoTDBConstants import TSDataType, TSEncoding, Compressor
from enum import Enum


SESSION_IP = "127.0.0.1"
SESSION_PORT = "6667"
SESSION_USERNAME = "root"
SESSION_PASSWORD = "root"


class Device(Enum):
    HCSR04 = "HCSR04"
    MPU6050 = "MPU6050"


def new_session() -> Session:
    session = Session(SESSION_IP, SESSION_PORT, SESSION_USERNAME, SESSION_PASSWORD)
    session.open(False)
    return session
