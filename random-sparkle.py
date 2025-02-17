import board, random, neopixel, NEOPIXEL, time

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

last_light = -1

while True:
    random_lights = random.randrange(len(pixels))
    while last_light == random_lights:
        random_lights = random.randrange(len(pixels))
    pixels[random_lights] = WHITE
    time.sleep(0.1)
    pixels[random_lights] = BLACK
    last_light = random_lights


