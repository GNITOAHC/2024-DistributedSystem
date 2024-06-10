const mqtt = require('mqtt')
require('dotenv').config()
const { Board, Proximity, IMU } = require('johnny-five')
const client = mqtt.connect()

const board = new Board({
  port: process.env.COM_NUM,
  repl: false,
})

function HCSR04_data(cm, time) {
  return {
    value: cm,
    time: time,
  }
}

function MPU6050_data(pitch, roll, yaw, time) {
  return {
    time: time,
    pitch: { rate: pitch.rate, angle: pitch.angle },
    roll: { rate: roll.rate, angle: roll.angle },
    yaw: { rate: yaw.rate, angle: yaw.angle },
  }
}

board.on('ready', () => {
  // HC-SR04
  const hcsr04 = new Proximity({
    controller: 'HCSR04',
    pin: 'A0',
    freq: 333, // ms per data
  })

  // MPU-6050
  const mpu6050 = new IMU({
    controller: 'MPU6050',
    freq: 1000, // ms per data
  })

  hcsr04.on('data', () => {
    const { centimeters } = hcsr04
    console.log('  cm  : ', centimeters)
    client.publish(
      'HCSR04',
      JSON.stringify(HCSR04_data(centimeters, Date.now()))
    )
  })

  mpu6050.on('data', () => {
    const { roll, yaw, pitch } = mpu6050.gyro
    console.log('  pitch  : ', pitch)
    console.log('  roll   : ', roll)
    console.log('  yaw    : ', yaw)
    client.publish(
      'MPU6050',
      JSON.stringify(MPU6050_data(pitch, roll, yaw, Date.now()))
    )
  })
})
