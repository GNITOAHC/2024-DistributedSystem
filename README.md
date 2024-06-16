# 2024-DistributedSystem

## Overall usage

1. Start mosquitto and IoTDB server.
2. Link the device and run `node device.js`
3. Run both server and api endpoint. `python server.py` & `fastapi dev api.py`
4. Start the client. `go run cmd/app/main.go`

## Device

Link the device and write into Arduino.

```
cd ./device/
npm install
node device.js
```

## Server

- `server.py` is the server
- `api.py` is the api entry point.

### Server - server

```
cd server
pip install apache-iotdb paho-mqtt python-dotenv
python server.py
```

### Server - api

```
cd server
pip install fastapi
fastapi dev api.py
```

## Client

```
cd client
go run ./cmd/app/main.go
```
