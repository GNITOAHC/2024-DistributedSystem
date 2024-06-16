from iotdb.Session import Session


class ReadDataType:
    def __init__(self, start_time, end_time, device):
        self.start_time = start_time
        self.end_time = end_time
        self.device = device


def read_data(session: Session, data: ReadDataType):
    q_string = f"select * from root.{data.device}* where time >= {data.start_time} and time <= {data.end_time}"
    result = session.execute_query_statement(q_string)

    df = result.todf()
    print(df)

    # for i in range(len(df)):
    #     print(df.loc[i, "Time"], df.loc[i, "root.MPU6050.pitch_rate"])

    return


from iotdb.Session import Session

SESSION_IP = "127.0.0.1"
SESSION_PORT = "6667"
SESSION_USERNAME = "root"
SESSION_PASSWORD = "root"


def new_session() -> Session:
    session = Session(SESSION_IP, SESSION_PORT, SESSION_USERNAME, SESSION_PASSWORD)
    session.open(False)
    return session


def main():
    session = new_session()
    query = ReadDataType(1718442994141, 1718457853140, "MPU6050")
    read_data(session, query)


if __name__ == "__main__":
    main()
