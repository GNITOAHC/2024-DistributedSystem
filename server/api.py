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
    
    if(start and end):
        # print(int(start))
        # print(int(end))
        query = ReadDataType(int(start), int(end), "MPU6050")
        rd = read_data(query).transpose().to_dict()
        
        return rd
    else:
        return {"message":"failed"}

@app.get("/HCSR04")
def get_items(start, end):
    if(start and end):
        # print(int(start))
        # print(int(end))
        query = ReadDataType(int(start), int(end), "HCSR04")
        rd = read_data(query).transpose().to_dict()
        
        return rd
    else:
        return {"message":"failed"}
