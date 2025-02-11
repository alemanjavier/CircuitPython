import board
import neopixel, time, digitalio
from board import NEOPIXEL
from neopixel import NeoPixel
from adafruit_led_animation.color import RED, YELLOW, ORANGE, \
        GREEN, TEAL, CYAN, BLUE, PURPLE, MAGENTA, GOLD, PINK, AQUA, \
        JADE, AMBER, OLD_LACE, WHITE, BLACK
from adafruit_debouncer import Button

# Set up our 10 NeoPixels on our board and call them "pixels"
pixels: NeoPixel = neopixel.NeoPixel(board.NEOPIXEL, 10)
strip = neopixel.NeoPixel(board.A1, 30, brightness=0.5)

colors = [RED, YELLOW, ORANGE, GREEN, TEAL, CYAN, BLUE, PURPLE, MAGENTA, GOLD, PINK, AQUA,
        JADE, AMBER, OLD_LACE, WHITE, BLACK]

button_A_input = digitalio.DigitalInOut(board.BUTTON_A)
button_A_input.switch_to_input(digitalio.Pull.DOWN)
button_A = Button(button_A_input, value_when_pressed=True)

button_B_input = digitalio.DigitalInOut(board.BUTTON_B)
button_B_input.switch_to_input(digitalio.Pull.DOWN)
button_B = Button(button_B_input, value_when_pressed=True)

press_count_A = 0
press_count_B = 0


while True:
        button_A.update()
        button_B.update()
        if button_A.pressed:
                pixels.fill(RED)
                press_count_A += 1
                print(f"Press count A: {press_count_A}")
        elif button_A.released:
                pixels.fill(BLACK)
        elif button_B.pressed:
                pixels.fill(RED)
                press_count_B += 1
                print(f"Press count B: {press_count_B}")
        elif button_B.released:
                pixels.fill(BLACK)








