import board, neopixel, time, digitalio
import touchio

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
colors = [RED, YELLOW,ORANGE, GREEN, TEAL, CYAN, BLUE, PURPLE]

drumsamples = ["bass_hit_c.wav", "bd_tek.wav", "bd_zome.wav",  "drum_cowbell.wav", \
               "elec_cymbal.wav",  "elec_hi_snare.wav", "scratch.wav", "splat.wav"]

pads = [board.A1, board.A2, board.A3, board.A4, board.A5, board.A6, board.TX]

touchpads = []

for pad in pads:
    touchpads.append(touchio.TouchIn(pad))

def play_sound(filename):
    with open(path + filename, "rb") as wave_file:
        wave = WaveFile(wave_file)
        audio.play(wave)
        while audio.playing:
            pass

while True:
    for i in range(len(touchpads)):
        if touchpads[i].value:
            pixels.fill(colors[i])
            play_sound(drumsamples[i])
            pixels.fill(BLACK)