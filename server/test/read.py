from iotdb.Session import Session
from iotdb.utils.IoTDBConstants import TSDataType, TSEncoding, Compressor


class ReadDaaType:
    def __init__(self, start_time, end_time, device):
        self.start_time = start_time
        self.end_time = end_time
        self.device = device


def read_data(session: Session, data: ReadDaaType):
    pass
