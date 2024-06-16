# 2024-DistributedSystem

## Overall usage

1. Start mosquitto. `mosquitto.exe -c mosquitto.conf -v`
2. Start IoTDB server. `.\start-standalone.bat` or `sh ./start-standalone.sh`
3. Link the device and run `node device.js`
4. Run both server and api endpoint. `python server.py` & `fastapi dev api.py`
5. Start the client. `go run cmd/app/main.go`
6. Start the airplane simulator. `npm run dev`

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

## Airplane

This simulator required mosquitto which supports web socket.

```
# mosquitto.conf
allow_anonymous true

# Listen on http port 1883
listener 1883

# Listen on websocket port 9001
listener 9001
protocol websockets
socket_domain ipv4
```

```
mosquitto.exe -c mosquitto.conf -v
```

```
npm install
npm run dev
```
