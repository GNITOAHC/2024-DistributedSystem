# server

1. Start mosquitto server. [Download](https://mosquitto.org/download/)
2. Start IotDB server. [Download](https://iotdb.apache.org/Download/)
3. Start `device.js` at [device directory](../device/README.md)

   ```
   npm install
   node device.js
   ```

4. Start server.

   ```
   pip install apache-iotdb paho-mqtt python-dotenv
   python server.py
   ```

# api

Device name:

- HCSR04: 超音波 cm
- MPU6050: 陀螺儀 yaw, roll, pitch

## `/mpu6050`

<code>GET</code> <code><b>/</b></code> <code>(Get data)</code>

##### Query Parameters

> | key   | required | data type | description |
> | ----- | -------- | --------- | ----------- |
> | start | true     | string    | Start time  |
> | end   | true     | string    | End time    |

##### Responses

```ts
type Res = {
  time: string;
  pitch: { rate: float; angle: float };
  roll: { rate: float; angle: float };
  yaw: { rate: float; angle: float };
};
```

```json
{
  "list": [
    {
      "time": 1718384500469,
      "pitch": { "rate": -0.01, "angle": -16.99 },
      "yaw": { "rate": 0.05, "angle": 14.21 },
      "roll": { "rate": 0.0, "angle": -23.1 }
    },
    {
      "time": 1718384500469,
      "pitch": { "rate": -0.01, "angle": -16.99 },
      "yaw": { "rate": 0.05, "angle": 14.21 },
      "roll": { "rate": 0.0, "angle": -23.1 }
    }
  ]
}
```

> | http code | content-type       | response        |
> | --------- | ------------------ | --------------- |
> | `200`     | `application/json` | `Res[]`         |
> | `400`     | `text/plain`       | `error message` |

## `/hcsr04`

<code>GET</code> <code><b>/</b></code> <code>(Get data)</code>

##### Query Parameters

> | key   | required | data type | description |
> | ----- | -------- | --------- | ----------- |
> | start | true     | string    | Start time  |
> | end   | true     | string    | End time    |

##### Responses

```ts
type Res = {
  time: string;
  value: string;
};
```

```json
{
  "list": [
    {
      "time": 1718384500469,
      "value": 7.0
    },
    {
      "time": 1718384500469,
      "value": 8.2
    }
  ]
}
```

> | http code | content-type       | response        |
> | --------- | ------------------ | --------------- |
> | `200`     | `application/json` | `Res[]`         |
> | `400`     | `text/plain`       | `error message` |
