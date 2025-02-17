import board, busio, adafruit_lis3dh, neopixel, time, digitalio
from neopixel import NeoPixel
from audiocore import WaveFile
from adafruit_debouncer import Button

try:
    from audioio import AudioOut
except ImportError:
    try:
        from audiopwmio import PWMAudioOut as AudioOut
    except ImportError:
        print("This board does not support audio")

i2c = busio.I2C(board.ACCELEROMETER_SCL, board.ACCELEROMETER_SDA)
accelerometer = adafruit_lis3dh.LIS3DH_I2C(i2c, address=0x19)
accelerometer.range = adafruit_lis3dh.RANGE_2_G

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.3, auto_write=True)

speaker = digitalio.DigitalInOut(board.SPEAKER_ENABLE)
speaker.direction = digitalio.Direction.OUTPUT
speaker.value = True
audio = AudioOut(board.SPEAKER)

button_A_input = digitalio.DigitalInOut(board.BUTTON_A)
button_A_input.switch_to_input(digitalio.Pull.DOWN)
button_A = Button(button_A_input, value_when_pressed=True)

button_B_input = digitalio.DigitalInOut(board.BUTTON_B)
button_B_input.switch_to_input(digitalio.Pull.DOWN)
button_B = Button(button_B_input, value_when_pressed=True)

sound = ("alarm/siren.wav")

armed = False

def play_sound(filename):
    with open(filename, "rb") as wave_file:
        wave = WaveFile(wave_file)
        audio.play(wave)
        while audio.playing:
            pass

def detect_movement():
    global last_position
    x, y, z = accelerometer.acceleration

    if last_position is not None:
        if abs(x - last_position[0]) > 1.0 or abs(y - last_position[1]) > 1.0 or abs(z - last_position[2]) > 1.0:
            return True

    last_position = (x, y, z)
    return False

def activate_alarm():
    pixels.fill((255, 0, 0))
    play_sound(sound)

def disarm_alarm():
    global armed
    armed = False
    pixels.fill((0, 0, 0))

while True:
    button_A.update()
    button_B.update()
    if button_A.pressed:
        print("Resetting in 5 secs")
        time.sleep(5)
        armed = True
        last_position = accelerometer.acceleration
        print("Alarm!")

    if armed and detect_movement():
        print("Movement detected!")
        activate_alarm()

    if button_B.pressed:
        print("Hold Button B for 5 seconds to disarm...")
        hold_time = 0

        while button_B.pressed:
            time.sleep(1)
            hold_time += 1
            print(f"Held for {hold_time} seconds...")

            if hold_time >= 5:
                print("Alarm disarmed!")
                disarm_alarm()
                break

