import board
import neopixel, time
from board import NEOPIXEL
from neopixel import NeoPixel
from adafruit_led_animation.color import RED, YELLOW, ORANGE, \
        GREEN, TEAL, CYAN, BLUE, PURPLE, MAGENTA, GOLD, PINK, AQUA, \
        JADE, AMBER, OLD_LACE, WHITE, BLACK

# Set up our 10 NeoPixels on our board and call them "pixels"
pixels: NeoPixel = neopixel.NeoPixel(board.NEOPIXEL, 10)
strip = neopixel.NeoPixel(board.A1, 30, brightness=0.5)

colors = [RED, YELLOW, ORANGE, GREEN, TEAL, CYAN, BLUE, PURPLE, MAGENTA, GOLD, PINK, AQUA,
        JADE, AMBER, OLD_LACE, WHITE, BLACK]

time_interval = 0.2

while True:
        for color in colors:
                pixels.fill(color)
                time.sleep(time_interval)


















