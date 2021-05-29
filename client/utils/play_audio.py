import sounddevice as sd
import soundfile as sf


# requires python-sounddevice, numpy, and soundfile to be installed

def play_audio(filepath):
    data, fs = sf.read(filepath, dtype='float32')
    print(data)
    sd.play(data, fs)
    sd.wait()  # Wait until file is done playing
