# device

## JSON Schema

### JSON Schema of HCSR04

```json
{
  "value": "value",
  "time": "time"
}
```

For example:

```json
{
  "value": 455.1,
  "time": 1718037202913
}
```

### JSON Schema of MPU6050

```json
{
  "measurement": {
    "rate": "rate value",
    "angle": "angle value",
    "time": "time"
  }
}
```

For example:

```json
{
  "time": 1718037056800,
  "pitch": {
    "rate": 0.29,
    "angle": 0.01
  },
  "roll": {
    "rate": -0.29,
    "angle": -0.01
  },
  "yaw": {
    "rate": 0.09,
    "angle": 0.01
  }
}
```

### Timestamps

The timestamps are can be convert back to readable format by `datetime.fromtimestamp()` method in Python.

```python
from datetime import datetime
tt = 1718037202913
print(datetime.fromtimestamp(tt/1000)) # Output: 2024-06-11 00:33:22.913000
```
