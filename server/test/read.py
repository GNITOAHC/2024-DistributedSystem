from iotdb.Session import Session
from iotdb.utils.IoTDBConstants import TSDataType, TSEncoding, Compressor


class ReadDataType:
    def __init__(self, start_time, end_time, device):
        self.start_time = start_time
        self.end_time = end_time
        self.device = device


def read_data(session: Session, data: ReadDataType):
    
    result = session.execute_query_statement(
        f"select * from root.{data.device} WHERE datatime >= {data.start_time} AND time <= {data.end_time}"
        )

    df = result.todf()
    print(df)

    data_list = []
    for row in df:
        time, pitch_rate, pitch_angle, roll_rate, roll_angle, yaw_rate, yaw_angle = row
        data_dict = {
            "time": time,
            "pitch": {"rate": pitch_rate, "angle": pitch_angle},
            "roll": {"rate": roll_rate, "angle": roll_angle},
            "yaw": {"rate": yaw_rate, "angle": yaw_angle}
        }
        data_list.append(data_dict)

    result_dict = {"data": data_list}
    print(result_dict)
    
    pass
