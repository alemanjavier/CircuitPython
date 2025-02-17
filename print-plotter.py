import board
import analogio
import time

light_sensor = analogio.AnalogIn(board.LIGHT)
SENSOR_MAX = 65535
LINE_LENGTH = 90
value_length = len(f"{SENSOR_MAX:,}")

plot_length = LINE_LENGTH - value_length - 1

def print_plot(sensor_value):
    spaces = " " * (int(sensor_value * (plot_length / SENSOR_MAX)-1) )
    print(f"{sensor_value:{value_length},}" + " " + spaces + "Physi Comp is Fun")

while True:
    print_plot(light_sensor.value)
    time.sleep(0.05)

















