import board, time, busio, adafruit_lis3dh

i2c = busio.I2C(board.ACCELEROMETER_SCL, board.ACCELEROMETER_SDA)
accelerometer = adafruit_lis3dh.LIS3DH_I2C(i2c,address=0x19)

accelerometer.range = adafruit_lis3dh.RANGE_2_G

while True:
    x, y, z = accelerometer.acceleration
    print((x, y, z))
    print(f"x:{x:6.2f}, y:{y:6.2f}, z:{z:6.2f}")
    time.sleep(0.1)
