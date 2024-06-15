from iotdb.Session import Session
from iotdb.utils.IoTDBConstants import Compressor, TSDataType, TSEncoding

ip = "127.0.0.1"
port_ = "6667"
username_ = "root"
password_ = "root"

session = Session(ip, port_, username_, password_)
session.open(False)

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

# zone = session.get_time_zone()
# print("zone: ", zone)

# session.create_time_series("root.abc", TSDataType.BOOLEAN, TSEncoding.PLAIN, Compressor.SNAPPY)
# session.set_storage_group("cool")

# has = session.check_time_series_exists("root.ln.tt")
# print("has ts root: ", has)

session.close()
