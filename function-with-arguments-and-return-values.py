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
times_pressed = 0


button_A = digitalio.DigitalInOut(board.BUTTON_A)
button_A.switch_to_input(digitalio.Pull.DOWN)


button_B = digitalio.DigitalInOut(board.BUTTON_B)
button_B.switch_to_input(digitalio.Pull.DOWN)

def play_sound(filename, press_count):
        press_count += 1
        print(f"Press total: {press_count}")
        with open(path + filename, "rb") as wave_file:
                wave = WaveFile(wave_file)
                audio.play(wave)
                while audio.playing:
                        pass
        return press_count

while True:
        if button_A.value:
                print("A Pressed")
                times_pressed = play_sound("drum_cowbell.wav", times_pressed)
        elif button_B.value:
                print("B pressed")
                play_sound("B", "scratch.wav")




