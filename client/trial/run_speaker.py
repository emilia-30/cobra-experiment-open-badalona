import time

from const import *
from duck import *
from gui import gui
from utils import play_audio, prepare_out

path_to_audio_dir = "static/audio/"


def run_speaker(stim: Stim, send):
    # prime - sentence or beep
    print(stim)

    if stim.get("prime") == PRIME_TYPES['beep']:
        filename = path_to_audio_dir + stim.get("prime") + '.wav'
    else:
        filename = path_to_audio_dir + stim.get("prime") + '/' + stim.get("stim") + '.wav'

    play_audio(filename)

    # image
    gui.show_image(stim.get("stim"))

    send(
        prepare_out(
            "prime and image shown"
        )
    )

    time.sleep(DURATIONS['DISPLAY_IMAGE_TIME'])
    gui.remove_image()
