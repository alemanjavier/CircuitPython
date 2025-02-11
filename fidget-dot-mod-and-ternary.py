import board
import neopixel, time, digitalio
from neopixel import NeoPixel
from adafruit_led_animation.color import RED, YELLOW, ORANGE, \
        GREEN, TEAL, CYAN, BLUE, PURPLE, MAGENTA, GOLD, PINK, AQUA, \
        JADE, AMBER, OLD_LACE, WHITE, BLACK
from audiocore import WaveFile
from adafruit_debouncer import Button

try:
        from audioio import AudioOut
except ImportError:
        try:
                from audiopwmio import PWMAudioOut as AudioOut
        except ImportError:
                print("This board does not support audio")


# Set up our 10 NeoPixels on our board and call them "pixels"
pixels: NeoPixel = neopixel.NeoPixel(board.NEOPIXEL, 10)

colors = [RED, YELLOW, ORANGE, GREEN, TEAL, CYAN, BLUE, PURPLE, MAGENTA, GOLD, PINK, AQUA,
        JADE, AMBER, OLD_LACE, WHITE, BLACK]

speaker = digitalio.DigitalInOut(board.SPEAKER_ENABLE)
speaker.direction = digitalio.Direction.OUTPUT
speaker.value = True

audio = AudioOut(board.SPEAKER)

path = "drumSounds/"
light_position = -1


button_A_input = digitalio.DigitalInOut(board.BUTTON_A)
button_A_input.switch_to_input(digitalio.Pull.DOWN)
button_A = Button(button_A_input, value_when_pressed=True)


button_B_input = digitalio.DigitalInOut(board.BUTTON_B)
button_B_input.switch_to_input(digitalio.Pull.DOWN)
button_B = Button(button_B_input, value_when_pressed=True)

def play_sound(filename):
        with open(path + filename, "rb") as wave_file:
                wave = WaveFile(wave_file)
                audio.play(wave)
                while audio.playing:
                        pass

def move_dot(position, direction, color):
        play_sound("splat.wav")
        pixels[position] = BLACK
        position = position + direction
        position = position % 10
        position = 9 if position < 0 else position
        # if position < 0:
        #         position = 9
        # if position > 9:
        #         position = 0
        # elif position < 0:
        #         position = 9
        pixels[position] = color
        return position
while True:
        button_A.update()
        button_B.update()
        if button_A.pressed:
                light_position = move_dot(light_position, 1, RED)
        elif button_B.value:
                light_position = move_dot(light_position, -1, BLUE)



