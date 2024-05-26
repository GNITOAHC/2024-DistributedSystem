require("dotenv").config();
const { Board, Proximity, IMU } = require("johnny-five");

const board = new Board({
  port: process.env.COM_NUM,
  repl: false
});

board.on("ready", () => {
  // HC-SR04
  const hcsr04 = new Proximity({
    controller: "HCSR04",
    pin: "A0",
    freq: 333 // ms per data
  });

  // MPU-6050
  const mpu6050 = new IMU({
    controller: "MPU6050",
    freq: 1000 // ms per data
  });

  hcsr04.on("data", () => {
    const { centimeters } = hcsr04;
    console.log("  cm  : ", centimeters);
  });

  mpu6050.on("data", () => {
    const { roll, yaw, pitch } = mpu6050.gyro;
    console.log("  pitch  : ", pitch);
    console.log("  roll   : ", roll);
    console.log("  yaw    : ", yaw);
  });
});