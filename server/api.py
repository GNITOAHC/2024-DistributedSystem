from fastapi import FastAPI
from database import new_session
from database.query import get_time_zone

app = FastAPI()

session = new_session()

class ReadDataType:
    def __init__(self, start_time, end_time, device):
        self.start_time = start_time
        self.end_time = end_time
        self.device = device

def read_data(data: ReadDataType):
    q_string = f"select * from root.{data.device}* where time >= {data.start_time} and time <= {data.end_time}"
    result = session.execute_query_statement(q_string)
    df = result.todf()
    
    return df


@app.get("/")
def root_test():
    return get_time_zone(session)

@app.get("/MPU6050")
def get_items(start:int, end:int):
    ''' data syntax
        "0": {
            "Time": 1718442994480.0,
            "root.MPU6050.pitch_rate": -0.03999999910593033,
            "root.MPU6050.yaw_angle": -2.5199999809265137,
            "root.MPU6050.roll_angle": -0.019999999552965164,
            "root.MPU6050.pitch_angle": 0.7300000190734863,
            "root.MPU6050.roll_rate": 0.05000000074505806,
            "root.MPU6050.yaw_rate": -0.07000000029802322
        },
    '''
    if(start and end):
        query = ReadDataType(int(start), int(end), "MPU6050")
        rd = read_data(query).transpose().to_dict()
        
        return rd
    else:
        return {"message":"failed"}

@app.get("/HCSR04")
def get_items(start, end):
    ''' data syntax
        "0": {
            "Time": 1718442994141.0,
            "root.HCSR04.value": 118.9000015258789
        },
    '''
    if(start and end):
        query = ReadDataType(int(start), int(end), "HCSR04")
        rd = read_data(query).transpose().to_dict()
        
        return rd
    else:
        return {"message":"failed"}
