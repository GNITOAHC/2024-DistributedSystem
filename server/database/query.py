from iotdb.Session import Session
from iotdb.utils.IoTDBConstants import TSDataType, TSEncoding, Compressor


def get_time_zone(session: Session):
    return session.get_time_zone()


class WriteDataType:
    def __init__(self, device, time, ts_paths, types, measurements, values):
        self.device = device
        self.time = time
        self.ts_paths = ts_paths
        self.types = types
        self.measurements = measurements
        self.values = values

    def __str__(self) -> str:
        return f"[{self.time}] {self.device}: {self.ts_paths} || {self.types} || {self.measurements} || {self.values}"


def write_data(session: Session, data: WriteDataType):
    print(get_time_zone(session))

    for ts in data.ts_paths:
        if session.check_time_series_exists(ts) == False:
            session.create_time_series(
                ts, TSDataType.FLOAT, TSEncoding.PLAIN, Compressor.SNAPPY
            )

    session.insert_aligned_record(
        "root." + data.device, data.time, data.measurements, data.types, data.values
    )

    with session.execute_query_statement(
        "select * from root.MPU6050*"
    ) as session_data_base:
        while session_data_base.has_next():
            print(session_data_base.next())

    with session.execute_query_statement(
        "select * from root.HCSR04*"
    ) as session_data_base:
        while session_data_base.has_next():
            print(session_data_base.next())

