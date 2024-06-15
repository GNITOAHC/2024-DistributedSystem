from fastapi import FastAPI
from database import new_session
from database.query import get_time_zone

app = FastAPI()

session = new_session()

# @app.get("/HCSR04")



@app.get("/")
def root_test():
    return get_time_zone(session)
