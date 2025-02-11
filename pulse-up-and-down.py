import board, time, neopixel

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
pixels.fill(RED)

def pulse():
        for i in range (101):
                pixels.brightness = i/100
        for i in range (100, -1, -1):
                pixels.brightness = i/100

print("Program is running!")
while True:
        pulse()
