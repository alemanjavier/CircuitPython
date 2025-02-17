import board, digitalio
from audiomp3 import MP3Decoder

try:
    from audioio import AudioOut
except ImportError:
    try:
        from audiopwmio import PWMAudioOut as AudioOut
    except ImportError:
        print("This board does not support audio out")

speaker = digitalio.DigitalInOut(board.SPEAKER_ENABLE)
speaker.direction = digitalio.Direction.OUTPUT
speaker.value = True

audio = AudioOut(board.SPEAKER)

path = "sounds/"

filename = "encouragement1.mp3"
mp3_file = open(path +filename, "rb")
decoder = MP3Decoder(mp3_file)

def play_mp3(filename):
    decoder.file = open(path + filename, "rb")
    audio.play(decoder)
    while audio.playing:
        pass

play_mp3("encouragement1.mp3")
play_mp3("encouragement2.mp3")
play_mp3("nice-work.mp3")