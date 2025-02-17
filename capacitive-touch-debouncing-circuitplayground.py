import board, neopixel, time, digitalio
import touchio
from adafruit_debouncer import Button
from adafruit_led_animation.color import (RED, YELLOW,\
    ORANGE, GREEN, TEAL, CYAN, BLUE, PURPLE, MAGENTA, GOLD, \
    PINK, AQUA, JADE, AMBER, OLD_LACE, WHITE, BLACK)
from audiocore import WaveFile
from adafruit_debouncer import Button

try:
    from audioio import AudioOut
except ImportError:
    try:
        from audiopwmio import PWMAudioOut as AudioOut
    except ImportError:
        print("This board does not support audio")


speaker = digitalio.DigitalInOut(board.SPEAKER_ENABLE)
speaker.direction = digitalio.Direction.OUTPUT
speaker.value = True

audio = AudioOut(board.SPEAKER)

path = "drumSounds/"

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10)


touchpad_A1_input = touchio.TouchIn(board.A1)
touchpad_A1 = Button(touchpad_A1_input, value_when_pressed=True)
touchpad_A2_input = touchio.TouchIn(board.A2)
touchpad_A2 = Button(touchpad_A2_input, value_when_pressed=True)
touchpad_A3_input = touchio.TouchIn(board.A3)
touchpad_A3 = Button(touchpad_A3_input, value_when_pressed=True)

def play_sound(filename):
    with open(path + filename, "rb") as wave_file:
        wave = WaveFile(wave_file)
        audio.play(wave)
        while audio.playing:
            pass

while True:
    touchpad_A1.update()
    touchpad_A2.update()
    touchpad_A3.update()
    if touchpad_A1.pressed:
        pixels.fill(RED)
        play_sound("drum_cowbell.wav")
        pixels.fill(BLACK)
    if touchpad_A2.pressed:
        pixels.fill(ORANGE)
        play_sound("bd_zome.wav")
        pixels.fill(BLACK)
    if touchpad_A3.pressed:
        pixels.fill(YELLOW)
        play_sound("elec_hi_snare.wav")
        pixels.fill(BLACK)