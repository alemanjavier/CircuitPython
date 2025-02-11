import board
import neopixel, time
from board import NEOPIXEL
from neopixel import NeoPixel

# Set up our 10 NeoPixels on our board and call them "pixels"
pixels: NeoPixel = neopixel.NeoPixel(board.NEOPIXEL, 10)
strip = neopixel.NeoPixel(board.A1, 30, brightness=0.5)

RED = (255, 0, 0)
ORANGE = (255, 40, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
INDIGO = (75, 0, 130)
VIOLET = (180, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
CYAN = (0, 255, 255)

time_interval = 0.1

rainbow_colors = [RED, ORANGE, YELLOW, GREEN, BLUE, INDIGO, VIOLET]
rainbow_colors.append(CYAN)

while True:
        for rainbow_color in rainbow_colors:
                for i in range(len(pixels)):
                        pixels[i] = rainbow_color
                        time.sleep(time_interval)


















