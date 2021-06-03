import sounddevice as sd
import soundfile as sf

# depending on machine/setup
sd.default.device = 3
sd.default.channels = 2

def play_audio(filepath):
    data, fs = sf.read(filepath, dtype='float32')
    sd.play(data, fs)
    sd.wait()  # Wait until file is done playing
