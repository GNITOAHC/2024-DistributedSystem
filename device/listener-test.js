const mqtt = require('mqtt')
const client_hcsr04 = mqtt.connect()
const client_mpu6050 = mqtt.connect()

client_hcsr04.subscribe('HCSR04')
client_mpu6050.subscribe('MPU6050')

client_hcsr04.on('message', (topic, payload, _packet) => {
  console.log("hcsr04:", topic)
  console.log("hcsr04:", payload.toString())
})

client_mpu6050.on('message', (topic, payload, _packet) => {
  console.log("mpu6050:", topic)
  console.log("mpu6050:", payload.toString())
})
