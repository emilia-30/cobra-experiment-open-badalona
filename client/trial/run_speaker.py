import time
import tkinter
# import simpleaudio as sa
from utils import play_audio, prepare_out
from gui import gui
from duck import *
from const import *

path_to_audio_dir = "static/audio/"


def run_speaker(stim: Stim, send):
    # prime - sentence or beep
    time.sleep(DURATIONS["PAUSE_BEFORE_PRIME"])
    print(stim)

    if stim.get("prime") == PRIME_TYPES['beep']:
        filename = path_to_audio_dir + stim.get("prime") + '.wav'
    else:
        filename = path_to_audio_dir + stim.get("prime") + '/' + stim.get("stim") + '.wav'

    print(filename)
    play_audio(filename)

    # image
    time.sleep(DURATIONS["PAUSE_BEFORE_IMAGE"])

    gui.show_image(stim.get("stim"))

    send(
        prepare_out(
            "prime and image shown"
        )
    )

    time.sleep(DURATIONS['DISPLAY_IMAGE_TIME'])
    gui.remove_image()
