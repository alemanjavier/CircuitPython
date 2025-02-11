import board, time, neopixel, digitalio
from audiocore import WaveFile
try:
        from audiopwmio import PWMAudioOut as AudioOut
except ImportError:
        try:
                from audiopwmio import PWMAudioOut as AudioOut
        except ImportError:
                print("This board does not support audio")

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
pixels.fill(RED)

speaker = digitalio.DigitalInOut(board.SPEAKER_ENABLE)
speaker.direction = digitalio.Direction.OUTPUT
speaker.value = True

audio = AudioOut(board.SPEAKER)

path = "alarm/"

button_A = digitalio.DigitalInOut(board.BUTTON_A)
button_A.switch_to_input(digitalio.Pull.DOWN)
button_B = digitalio.DigitalInOut(board.BUTTON_B)
button_B.switch_to_input(digitalio.Pull.DOWN)

def play_sound(filename):
    with open(path + filename, "rb") as wave_file:
         wave = WaveFile(wave_file)
         audio.play(wave)
         while audio.playing:
              keep_playing = pulse()
              if keep_playing == False:
                  pixels.brightness = 0.0
                  audio.stop()
         return keep_playing

def pulse():
        for i in range (101):
                pixels.brightness = i/100
                if button_B.value:
                        return False
        for i in range (100, -1, -1):
                pixels.brightness = i/100
                if button_B.value:
                        return False
        return True

start_playing = False
pixels.brightness = 0.0
print(light_sensor.value,)


print("Program is running!")
while True:
        if light_sensor.value > 100:
                start_playing = True
        if start_playing:
                start_playing = play_sound("siren.wav")
